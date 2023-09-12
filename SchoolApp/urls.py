from django.urls import path
from SchoolApp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('StudentAdd/',views.index,name="StudentAdd"),
    path('StudentInsert/',views.insertedData,name="StudentInsert"),
    path('StudentUpdate/<id>',views.update,name="StudentUpdate"),
    path('StudentEdit/',views.StudentEdit,name="studentedit"),
    path('StudentDelete/<id>',views.delete,name="StudentDelete"),
    path('StudentDetails/',views.Family,name="StudentDetails"),
    path('StudentDetailsInsert/',views.familyinsertedData,name="StudentDetailsInsert"),
    path('StudentDetailsEdit/<id>',views.StudentDetailsUpdate,name="StudentDetailsEdit"),
    path('StudentDetailsDelete/<id>',views.StudentDetailsDelete,name="StudentDetailsDelete"),
    path('pdf/',views.pdf),
    
]