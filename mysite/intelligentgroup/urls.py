from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^search_action_analysis/$', views.search_action_analysis, name='search_action_analysis')
]