from django.urls import path
from courses.views import list_all_courses, list_courses_details

urlpatterns = [
    path('',list_all_courses),
    path('<int:id>',list_courses_details)
]