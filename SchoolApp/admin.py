from django.contrib import admin

from .models import Student,StudentFamily,Contacts
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("rollnumber","name", "email", "age","gender",)
admin.site.register(Student,ImportExportModelAdmin)
class StudentDetailPdf(ImportExportModelAdmin):
  list_display =("rollnumber","name", "email", "age","gender",)
class StudentDetailsAdmin(admin.ModelAdmin):
  list_display = ("name","father_name","mother_name","emergency")


 
admin.site.register(StudentFamily,StudentDetailsAdmin)
admin.site.register(Contacts)


  
