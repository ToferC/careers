from django.contrib import admin
from .models import Opportunity, Element, Response, Application, Member
from .models import Requirement, ApplicationStatus, GenericSkill, RequiredSkill
from .models import LinkedSkill, OpenRecommendation, SkillRecommendation
from .models import Tag, File

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Element)
admin.site.register(Response)
admin.site.register(Application)
admin.site.register(Member)
admin.site.register(Requirement)
admin.site.register(ApplicationStatus)
admin.site.register(GenericSkill)
admin.site.register(LinkedSkill)
admin.site.register(RequiredSkill)
admin.site.register(OpenRecommendation)
admin.site.register(SkillRecommendation)
admin.site.register(Tag)
admin.site.register(File)

