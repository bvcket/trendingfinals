from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import *

# Create your views here.
def homepage(request):
        return render(request,'home/homepage.html')

def dynamicDD(request):
        filtereduniversity = University.objects.all()
        courses = Course.objects.all()
        locations = University.objects.values_list('location', flat=True).distinct()

        coursefilter = request.GET.get('selected_course')
        locationfilter = request.GET.get('selected_location')
        tuitionfilter = request.GET.get('selected_tuition')
        passingratefilter = request.GET.get('selected_passingrate')
        searchquery = request.GET.get('searchquery')

        if searchquery != '' and searchquery is not None:
                filtereduniversity = filtereduniversity.filter(name__icontains=searchquery)

        if coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(universitycourse__course__name=coursefilter)
                

        if locationfilter != 'None' and locationfilter is not None:
                filtereduniversity = filtereduniversity.filter(location=locationfilter)

        if tuitionfilter != '' and tuitionfilter is not None and coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(
                        universitycourse__course__name=coursefilter,
                        universitycourse__estimated_tuition_minimum__lte=tuitionfilter,
                        universitycourse__estimated_tuition_maximum__gte=tuitionfilter
                )

        if passingratefilter != '' and passingratefilter is not None and coursefilter != 'None' and coursefilter is not None:
                filtereduniversity = filtereduniversity.filter(
                        universitycourse__course__name=coursefilter,
                        universitycourse__board_passing_rate__gte=passingratefilter
                ).distinct() 

        if tuitionfilter == '' and coursefilter == 'None' and locationfilter == 'None' and passingratefilter == '':
                filtereduniversity = None


        context = {"universities" : filtereduniversity, "coursefilter":coursefilter, "passingratefilter":passingratefilter , "courses":courses, "locations":locations}
        return render(request,'home/dynamicDD.html',context)


def courseView(request, UniversityCourse_id):
        universitycourse = get_object_or_404(UniversityCourse, id=UniversityCourse_id)
        universitys = universitycourse.university
        requirements = Requirement.objects.filter(university__id = universitys.id)
        course = universitycourse.course
        university_name = universitys.name
        university_description = universitys.description
        estimated_tuition_minimum = str(universitycourse.estimated_tuition_minimum)
        estimated_tuition_maximum = str(universitycourse.estimated_tuition_maximum)
        location = universitys.location
        board_passing_rate = str(universitycourse.board_passing_rate)
        logoUrl = universitys.logoUrl
        schedules = get_object_or_404(Schedule, university=universitys)
        application_start = schedules.application_start
        application_end = schedules.application_end
        entrance_exam_date = schedules.entrance_exam_date

        context = {
                'university_name': university_name,
                'requirements': requirements,
                'university_description': university_description,
                'course': course,
                'estimated_tuition_minimum': estimated_tuition_minimum,
                'estimated_tuition_maximum': estimated_tuition_maximum,
                'location': location,
                'board_passing_rate': board_passing_rate,
                'logoUrl': logoUrl,
                'application_start': application_start,
                'application_end': application_end,
                'entrance_exam_date': entrance_exam_date,
                

        }
        return render(request, 'home/courses.html', context)

def uniView(request, University_id):
        universitys = get_object_or_404(University, id=University_id)
        university_name = universitys.name
        requirements = Requirement.objects.filter(university__id=University_id)
        university_description = universitys.description
        logoUrl = universitys.logoUrl
        schedules = get_object_or_404(Schedule, university=universitys)
        application_start = schedules.application_start
        application_end = schedules.application_end
        entrance_exam_date = schedules.entrance_exam_date

        context = {
                'university_name': university_name,
                'requirements': requirements,
                'university_description': university_description,
                'logoUrl': logoUrl,
                'application_start': application_start,
                'application_end': application_end,
                'entrance_exam_date': entrance_exam_date,
        }

        return render(request, 'home/universities.html', context)

