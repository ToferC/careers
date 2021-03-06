from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('opportunity/<str:opportunity_slug>/', views.view_opportunity,
         name='view_opportunity'),
    path('review_applicants/<str:opportunity_slug>/', views.review_applicants,
         name='review_applicants'),
    path('member/<str:member_slug>/', views.view_member,
         name='view_member'),
    path('application/<str:application_slug>/', views.view_application,
         name='view_application'),

]