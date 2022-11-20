from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Student')
router.register('courses', CoursesViewSet, basename='Course')
router.register('resgistrations', RegistrationViewSet, basename='Registration')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls) )
]
