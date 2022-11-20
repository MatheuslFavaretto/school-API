from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )
    Code_course = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description

class Registration(models.Model):
        PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Nightly')
        )
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='A')

