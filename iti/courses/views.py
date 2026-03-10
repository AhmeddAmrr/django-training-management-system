from django.shortcuts import render,get_object_or_404
from courses.models import Courses
from django.http import HttpResponse
# Create your views here.
def list_all_courses(request):
    courses_list = Courses.objects.all()
    context={
        'courses_list' : courses_list
    }
    return render (request,"courses/index.html", context)
def list_courses_details(request, id):
    # return HttpResponse(f"Course {id}")
    course = get_object_or_404(Courses,pk=id)
    #  Courses.objects.filter(id=id)[0]
    context={
        'course' : course
    }
    return render (request,"courses/course_details.html", context) 