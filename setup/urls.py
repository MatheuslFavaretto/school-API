from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationViewSet, ListOfRegistrationsStudent, ListStudentRegistrations
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Student')
router.register('courses', CoursesViewSet, basename='Course')
router.register('registrations', RegistrationViewSet, basename='Registration')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls) ),
    path('students/<int:pk>/registrations/', ListOfRegistrationsStudent.as_view()),
    path('course/<int:pk>/registrations/', ListStudentRegistrations.as_view())
]
