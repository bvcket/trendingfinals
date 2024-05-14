from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    themecolor = models.CharField(max_length=100)
    logoUrl = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    estimated_tuition_minimum = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    estimated_tuition_maximum = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    board_passing_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return f"{self.university.name} - {self.course.name}"

class Schedule(models.Model):
    university = models.OneToOneField(University, on_delete=models.CASCADE)
    application_start = models.DateField(blank=True, null=True)
    application_end = models.DateField(blank=True, null=True)
    entrance_exam_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.university.name} Schedule"

class Requirement(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

