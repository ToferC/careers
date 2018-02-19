from django.shortcuts import render
from django.http import HttpResponse
from .models import Opportunity, Element, Response, Application, Member
from .models import Requirement, ApplicationStatus, Assessment, Skill
from .models import MemberSkillLink, OpenRecommendation, SkillRecommendation
from .models import Tag, File


# Create your views here.

def index(request):

    context = {}

    opportunities = Opportunity.objects.all()

    context['opportunities'] = opportunities

    return render(request, 'opportunities/index.html', context)


def view_opportunity(request, opportunity_slug):

    context = {}

    opportunity = Opportunity.objects.get(
        slug=opportunity_slug
    )

    requirements = Requirement.objects.filter(
        opportunity=opportunity)

    applications = Application.objects.filter(
        opportunity=opportunity
    )

    context['opportunity'] = opportunity
    context['requirements'] = requirements
    context['applications'] = applications

    return render(request, 'opportunities/view_opportunity.html', context)


def view_member(request, member_slug):

    context = {}

    member = Member.objects.get(
        slug=member_slug
    )

    skill_links = MemberSkillLink.objects.filter(
        member=member)

    applications = Application.objects.filter(
        applicant=member
    )

    context['member'] = member
    context['skill_links'] = skill_links
    context['applications'] = applications

    return render(request, 'opportunities/view_member.html', context)


def view_application(request, application_slug):

    context = {}

    application = Application.objects.get(
        slug=application_slug
    )

    status = ApplicationStatus.objects.get(
        application=application)

    requirements = Requirement.objects.filter(
        opportunity=application.opportunity
    )

    context['application'] = application
    context['status'] = status
    context['requirements'] = requirements

    return render(request, 'opportunities/view_application.html', context)
