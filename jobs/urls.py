from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/add/', views.add_job, name='add-job'),
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit-job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete-job'),
]
