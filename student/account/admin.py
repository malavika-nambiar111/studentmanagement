from django.contrib import admin

from .models import Courses,Contact,Staff
# Register your models here.

admin.site.register(Courses)

class customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,customerdetails)

admin.site.register(Staff)
