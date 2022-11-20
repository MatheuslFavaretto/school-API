from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListOfRegistrationsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    """Showing all Registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListOfRegistrationsStudent(generics.ListAPIView):
    """Showing all Registrations of Studentes"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset 
    serializer_class = ListOfRegistrationsSerializer