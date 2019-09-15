from django.contrib import admin

# Register your models here.
from ormdemo.models import AddressInfo, Student, Teacher, TeacherAssistant, Course

# admin.site.register(AddressInfo)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeacherAssistant)
admin.site.register(Course)
