from django.contrib import admin

from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result', views.results),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
