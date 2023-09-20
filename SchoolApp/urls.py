from django.urls import path
from SchoolApp import views
from SchoolApp import excel
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('StudentAdd/',views.index,name="StudentAdd"),
    path('StudentInsert/',views.insertedData,name="StudentInsert"),
    path('StudentUpdate/<id>',views.update,name="StudentUpdate"),
    path('StudentDelete/<str:pk>/',views.delete,name="StudentDelete"),
    path('StudentDetails/',views.Family,name="StudentDetails"),
    path('StudentDetailsInsert/',views.familyinsertedData,name="StudentDetailsInsert"),
    path('StudentDetailsEdit/<id>',views.StudentDetailsUpdate,name="StudentDetailsEdit"),
    path('StudentDetailsDelete/<id>',views.StudentDetailsDelete,name="StudentDetailsDelete"),

    #Excel
    path('UploadStudents/',excel.Student_upload,name="UploadStudents"),
    path('StudentExcelDownload/', excel.Student_Download_File,name="StudentExcelDownload"),

    #Export Urls
    path('StudentExport/',excel.Student_Export_Data_To_Excel,name="StudentExport"),
    path('StudentFamilyExport/',excel.StudentFamily_Export_Data_To_Excel,name="StudentFamiltExportdata"),

    #PDF URLS
    path('StudentDataPdf/',views.StudentDtaPdf,name="StudentDataPdf"),
    path('StudentDetailsDataPdf/',views.StudentDetailsDataPdf,name="StudentDetailsDataPdf"),

    #View Page Functionality Urls
    path('<int:id>', views.view_student, name='view_student'),
    path('<int:id>', views.view_studentdetails, name='view_studentdetails'),
    

   

]