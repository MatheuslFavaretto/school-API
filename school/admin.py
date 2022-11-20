from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'Code_course', 'description',)
    list_display_links = ('id', 'Code_course',)
    search_fields = ('Code_course',)

admin.site.register(Course, Courses)
