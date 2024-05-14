from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dynamic/",views.dynamicDD, name="dynamicDD"),
    path('dynamic/courses/<int:UniversityCourse_id>/', views.courseView, name="courseView"),
    path('dynamic/universities/<int:University_id>/', views.uniView, name="uniView"),
]