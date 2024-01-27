from django.urls import path

from django_templates_static_files.employees.views import index


urlpatterns = (
    path('', index, name='index'),
)

