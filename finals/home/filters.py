import django_filters
from .models import *

class FilterCourse(django_filters.FilterSet):
    class Meta:
        model = University
        fields = ['name','location']

        exclude = ['description','themecolor','logoURl']