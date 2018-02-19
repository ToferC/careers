from django.contrib import admin
from .models import Opportunity, Element, Response, Application, Member
from .models import Requirement, ApplicationStatus, Assessment, Skill
from .models import MemberSkillLink, OpenRecommendation, SkillRecommendation
from .models import Tag, File

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Element)
admin.site.register(Response)
admin.site.register(Application)
admin.site.register(Member)
admin.site.register(Requirement)
admin.site.register(ApplicationStatus)
admin.site.register(Assessment)
admin.site.register(Skill)
admin.site.register(MemberSkillLink)
admin.site.register(OpenRecommendation)
admin.site.register(SkillRecommendation)
admin.site.register(Tag)
admin.site.register(File)

