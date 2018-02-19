from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import random


# Data Elements

# Skills

SEEKING = "SE"
NOVICE = "NO"
TRAINED = "TR"
EXPERT = "EX"
MASTER = "MA"

SKILL_LEVELS = (
    ("SEEKING", "Seeking"),
    ('NOVICE', "Novice"),
    ('TRAINED', "Trained"),
    ("EXPERT", "Expert"),
    ("MASTER", "Master")
)

# Requirement Types

QUESTION = "QE"
DEMOGRAPHIC = "DE"
EDUCATION = "ED"
CERTIFICATION = "CE"
TRAINING = "TR"
EXPERIENCE = "EX"
BEHAVIOR = "BE"

REQUIREMENT_CHOICES = (
    ("QUESTION", "Question"),
    ("DEMOGRAPHIC", "Demographic"),
    ("EDUCATION", "Education"),
    ("CERTIFICATION", "Certification"),
    ("TRAINING", "Training"),
    ("EXPERIENCE", "Experience"),
    ("BEHAVIOR", "Behavior")
)

# Assessments

MEETS = "ME"
FAILS = "FL"
EXCEEDS = "EX"

ASSESSMENT_CHOICES = (
    ("MEETS", "Meets requirement"),
    ("FAILS", "Does not meet requirement"),
    ("EXCEEDS", "Exceeds requirement")
)

# Applications

APPLIED = "AP"
SCREENED_IN = "SC"
SCREENED_OUT = "SO"
REVIEW = "RE"
ASSESSED = "AS"
RETAINED = "RT"
INTERVIEW = "IN"
OFFERED = "OF"
REFUSED = "RF"
ACCEPTED = "AC"

APPLICATION_STATUS_TYPES = (
    ("APPLIED", "Applied"),
    ("SCREENED_IN", "Screened In"),
    ("SCREENED_OUT", "Screened Out"),
    ("REVIEW", "Under Review"),
    ("ASSESSED", "Assessment Completed"),
    ("RETAINED", "Application Retained"),
    ("INTERVIEW", "Interview Requested"),
    ("OFFERED", "Job Offered"),
    ("REFUSED", "Job Refused"),
    ("ACCEPTED", "Job Accepted"),
)

# Models

class Member(models.Model):

    AC = "Active"
    IN = "Inactive"

    STATUS = (
        (AC, "Active"),
        (IN, "Inactive"),
        )

    name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hr_practitioner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    status = models.CharField(max_length=64, choices=STATUS, default="Active")
    email = models.EmailField(max_length=128, blank=True, null=True) # validate email
    phone = models.CharField(max_length=10, blank=True, null=True) # validate numbers only
    profile = models.URLField(max_length=128, blank=True, null=True) # validate GCconnex profile
    image = models.ImageField(
        upload_to='opportunities/static/opportunities/images/user_images/%Y/%m/%d/%H_%M_%S', default='images/user_images/nothing.jpg')
    bio = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True, default=54.16045)
    longitude = models.FloatField(blank=True, null=True, default=-92.01873)
    zoom = models.IntegerField(default=6, blank=True, null=True, help_text="Sets the default zoom")
    salary = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Member, self).save(*args, **kwargs)


class Opportunity(models.Model):
    """Core model for jobs, mentoring and other professional opportunities
    to connect with other people

    Opportunities have the following related models:

    creator -> Member
    skills -> Skill - abilities needed for the opportunity
    tags -> Tag - metadata associated with the opportunity

    """

    title = models.CharField(max_length=256)
    image = models.ImageField(
        upload_to='opportunities/static/opportunities/images/opportunity_images/%Y/%m/%d/%H_%M_%S',
        default='opportunities/static/opportunities/images/opportunity_images/nothing.jpg')
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='creator',
    )
    slug = models.SlugField(unique=True, max_length=255)

    # Location fields
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    province = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=6)

    # Date and time fields
    pub_date = models.DateTimeField('date published', auto_now=True)
    apply_date = models.DateTimeField('apply by')
    start_date = models.DateTimeField('starting date')
    end_date = models.DateTimeField('ending date')
    permanent_opportunity = models.BooleanField(default=False)

    # Related Models
    elements = models.ManyToManyField(
        "Element",
        through='Requirement',
        through_fields=('opportunity', 'element'),
        related_name='elements',
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.creator.name}-{self.title}")
        super(Opportunity, self).save(*args, **kwargs)


class Element(models.Model):
    """
    Model representing a generic or specific requirement or question
    for an opportunity. Accessed via the Requirement foreign key.
    """

    title = models.CharField(max_length=64)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=32,
                                choices=REQUIREMENT_CHOICES,
                                default=EXPERIENCE
                                )
    description = models.TextField(max_length=250, blank=True)
    weight = models.FloatField(default=1)
    mandatory = models.BooleanField(default=False)
    generic = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Requirement(models.Model):
    """
    Model connecting Elements and Opportunities.
    """

    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.opportunity.title}-{self.element.title}"


class Response(models.Model):
    """
    Model representing an applicant's response to opportunity
    requirements and their assessment.
    """

    applicant = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='applying_member'
    )
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    evidence = models.TextField(max_length=500)
    file = models.ForeignKey("File", blank=True, null=True,
                             on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    submitted_date = models.DateTimeField(auto_now=True)
    edited_date = models.DateTimeField(auto_now=True)

    # Assessing fields
    assessor = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='assessing_member'
    )
    assessment = models.CharField(max_length=32,
                                  choices=ASSESSMENT_CHOICES,
                                  default=MEETS)
    rationale = models.TextField(max_length=500)
    assessed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.name}-{self.requirement}"


class Application(models.Model):
    """
    Model representing a user's application to an opportunity
    """

    applicant = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='applicant'
    )
    opportunity = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
        related_name='applied_to_opportunity'
    )
    apply_date = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.applicant.name}-{self.opportunity.title}")
        super(Application, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.applicant.name}-{self.opportunity.title}"


class ApplicationStatus(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=APPLICATION_STATUS_TYPES,
        default=APPLIED)
    status_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()

    def set_status_to_screened_out(self):
        self.status = "Screened Out"

    def __str__(self):
        return f"{self.application}-{self.status}"


class GenericSkill(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    image = models.ImageField(
            upload_to='opportunities/static/opportunities/images/skill_images/%Y/%m/%d/%H_%M_%S',
            default='opportunities/static/opportunities/images/skill_images/nothing.jpg',
            null=True,
            blank=True
        )

    def __str__(self):
        return f"{self.title}"


class LinkedSkill(models.Model):
    """
    Model that initially connects a generic skill
    with a Member and sets level.
    """

    skill = models.ForeignKey(GenericSkill,
                              on_delete=models.CASCADE,
                              related_name="linked_skill")

    level = models.CharField(max_length=15,
                             choices=SKILL_LEVELS,
                             default=NOVICE)
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               related_name="linked_member"
                               )
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.member.name}-{self.skill.title}-{self.level}"


class RequiredSkill(models.Model):
    """
    Model that initially connects a generic skill
    with an Opportunity and sets the required level.
    """

    skill = models.ForeignKey(GenericSkill,
                              on_delete=models.CASCADE,
                              related_name="required_skill")

    required_level = models.CharField(max_length=15,
                             choices=SKILL_LEVELS,
                             default=NOVICE)
    opportunity = models.ForeignKey(Opportunity,
                               on_delete=models.CASCADE,
                               related_name="linked_opportunity"
                               )
    description = models.TextField(
        max_length=250,
        blank=True,
        default="Enter description here"
    )
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.opportunity.title}-{self.skill.title}-{self.required_level}"


class OpenRecommendation(models.Model):
    """
        Model for users to provide personal recommendations for
        other users.
    """

    creator = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='recommendation_creator'
    )
    subject = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='subject'
    )
    text = models.TextField(max_length=250, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"REC-{self.creator.name}->{self.subject.name}"


class SkillRecommendation(models.Model):
    creator = models.ForeignKey(Member, on_delete=models.CASCADE)
    skill = models.ForeignKey(LinkedSkill, on_delete=models.CASCADE)
    level = models.CharField(max_length=15, choices=SKILL_LEVELS,
                             default=NOVICE)
    text = models.TextField(max_length=250, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"SK_REC-{self.creator.name}-{self.skill.member.name}"


class Tag(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    image = models.ImageField(
        upload_to='opportunities/static/opportunities/images/tag_images/%Y/%m/%d/%H_%M_%S',
        default='opportunities/static/opportunities/images/tag_images/nothing.jpg',
        null=True,
        blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title


def user_directory_path(instance, filename):
    return f'opportunities/static/files/response_{instance.creator.id}/{filename}'


class File(models.Model):
    creator = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    file = models.FileField(upload_to=user_directory_path)
    upload_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}-{self.upload_date}"

