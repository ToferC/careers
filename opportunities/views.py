from django.shortcuts import render
from django.http import HttpResponse
from .models import Opportunity, Element, Response, Application, Member
from .models import Requirement, ApplicationStatus, GenericSkill, RequiredSkill
from .models import LinkedSkill, OpenRecommendation, SkillRecommendation
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

    required_skills = RequiredSkill.objects.filter(
        opportunity=opportunity
    )

    context['opportunity'] = opportunity
    context['requirements'] = requirements
    context['applications'] = applications
    context['required_skills'] = required_skills

    return render(request, 'opportunities/view_opportunity.html', context)


def review_applicants(request, opportunity_slug):

    context = {}

    opportunity = Opportunity.objects.get(
        slug=opportunity_slug
    )

    requirements = Requirement.objects.filter(
        opportunity=opportunity)

    applications = Application.objects.filter(
        opportunity=opportunity
    )

    required_skills = RequiredSkill.objects.filter(
        opportunity=opportunity
    )

    responses = Response.objects.filter(
        application__opportunity=opportunity
    )

    context['opportunity'] = opportunity
    context['requirements'] = requirements
    context['applications'] = applications
    context['required_skills'] = required_skills
    context['responses'] = responses

    return render(request, 'opportunities/review_applicants.html', context)



def view_member(request, member_slug):

    context = {}

    member = Member.objects.get(
        slug=member_slug
    )

    skill_links = LinkedSkill.objects.filter(
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

    responses = Response.objects.filter(
        application=application
    )

    context['application'] = application
    context['status'] = status
    context['requirements'] = requirements
    context['responses'] = responses

    return render(request, 'opportunities/view_application.html', context)
