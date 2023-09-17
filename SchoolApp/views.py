from openpyxl import Workbook
from SchoolApp.pdf import render_to_pdf
from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from SchoolApp.models import Student, StudentFamily, Contacts
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from xhtml2pdf import pisa
import datetime
from SchoolApp.resources import Studentresource



# Create your views here.


def home(request):
    return render(request, 'Home.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fphonenumber = request.POST.get("num")
        fdescription = request.POST.get("Description")

        print(fname, femail, fphonenumber, fdescription)
        messages.info(
            request, f'The name is {fname},email is {femail},Phonenumber is{fphonenumber}&your query is{fdescription}')

        query = Contacts(name=fname, email=femail,
                         phonenumber=fphonenumber, description=fdescription)
        query.save()
        messages.success(request, "Thanks For Contating us")
    return render(request, 'Contact.html')


def index(request):
    try:
        if 'q' in request.GET:
            q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q))
        data = Student.objects.filter(multiple_q)
        if not data:
            messages.warning(request, "No data found")
        else:
            pass
    except:
        pass
        data = Student.objects.all()
    page = Paginator(data, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {'page': page}
    return render(request, 'StudentsAdd.html', context)


def insertedData(request):

    if request.method == "POST":
        RollNumber = request.POST.get('roll')
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Age = request.POST.get('age')
        Gender = request.POST.get('gender')
    try:
        if Student.objects.get(email=Email):
            messages.warning(request, "Email is Already Taken")
            return redirect("/StudentAdd")
    except:
        pass
    try:
        if Student.objects.get(name=Name):
            messages.warning(request, "Name is Already Taken")
            return redirect("/StudentAdd")
    except:
        pass
    try:
        if Student.objects.get(rollnumber=RollNumber):
            messages.warning(request, "RollNumber is Already Taken")
            return redirect("/StudentAdd")
    except:
        pass
        query = Student(rollnumber=RollNumber, name=Name,
                        email=Email, age=Age, gender=Gender)
    messages.success(request, 'Student Details Added Successfully')
    query.save()
    return redirect("/StudentAdd")
    return render(request, 'StudentsAdd.html')


def update(request, id):
    if request.method == "POST":
        RollNumber = request.POST['roll']
        Name = request.POST['name']
        Email = request.POST['email']
        Age = request.POST['age']
        Gender = request.POST['gender']
    
        edit = Student.objects.get(id=id)
        edit.rollnumber = RollNumber
        edit.name = Name
        edit.email = Email
        edit.age = Age
        edit.gender = Gender
        edit.save()
    
        messages.success(request, "Student Details successfully Updated..")
        return redirect("/StudentAdd")
    d = Student.objects.get(id=id)
    context = {'d': d}
    return render(request, 'Student_Edit.html', context)


def delete(request,pk):
    d = Student.objects.get(id=pk)
    if request.method == 'POST':
        d.delete()
        messages.success(request, "Student Details Successfully deleted..")
        return redirect("/StudentAdd")
    return render(request, 'delete_invoice.html')


def StudentEdit(request):
    return render(request, 'Student_Edit.html')


# Student Family Details
def Family(request):

    family = StudentFamily.objects.all()
    try:
        if request.method == "GET":
            st = request.GET.get('q')
        if st != None:
            multiple_q = Q(Q(father_name__icontains=st))
            # family=StudentFamily.objects.filter(father_name__icontains=st)
            family = StudentFamily.objects.filter(multiple_q)
        if not family:
            messages.warning(request, "No data found")
    except:
        pass
    context = {'family': family}
    return render(request, 'StudentDetails.html', context)


def familyinsertedData(request):
    SF=Student.objects.all()
    print(SF)
    
    if request.method=="POST":
        
        name_id=request.POST.get('name')
        try:
            Name = Student.objects.get(name=name_id)
        except Student.DoesNotExist:
            Name=None
        try:
            if StudentFamily.objects.get(name=Name,father_name=FatherName):
                messages.warning(request,"Name is Already Taken")
            return redirect("/StudentDetails")
        except:
            pass
       
            
        
        FatherName=request.POST.get('father_name')
        MotherName=request.POST.get('mother_name')
        EmergencyContact=request.POST.get('emergency')
        Address=request.POST.get('address')
        try:
            if StudentFamily.objects.get(father_name=FatherName):
                messages.warning(request,"Father Name is Already Taken")
            return redirect("/StudentDetails")
        except:
            pass
    
        query1=StudentFamily(name=Name,father_name=FatherName,mother_name=MotherName,emergency=EmergencyContact,address=Address)
        messages.success(request,'Student Details Added Successfully')
        query1.save()
        return redirect("/StudentDetails")
    try:
        if not query1:
            messages.info(request,"narendra")
            return redirect("/StudentDetails")
    except:
        pass
    return render(request,'Student_Details.html')
    


def StudentDetailsUpdate(request, id):
    if request.method == "POST":
        name_id = request.POST.get('name')
        print(name_id)
        Name = Student.objects.get(name=name_id)
        FatherName = request.POST['father_name']
        MotherName = request.POST['mother_name']
        EmergencyContact = request.POST['emergency']
        Address = request.POST['address']

        SDU = StudentFamily.objects.get(id=id)

        SDU.name = Name
        SDU.father_name = FatherName
        SDU.mother_name = MotherName
        SDU.emergency = EmergencyContact
        SDU.address = Address
        
        SDU.save()
        messages.success(request, "Student Details successfully Updated..")
        return redirect("/StudentDetails")
    category = StudentFamily.objects.get(id=id)
    context = {'category': category}
    return render(request, 'StudentDetailsEdit.html', context)


def StudentDetailsDelete(request, id):
    d = StudentFamily.objects.get(id=id)
    d.delete()
    messages.success(request, "Student Details Successfully deleted..")
    return redirect("/StudentDetails")


def captcha(request):
    return render(request, 'captcha.html')


def StudentDetailsResultList(request):
    template_name = "StudentDetailsPdf.html"
    family = StudentFamily.objects.all().order_by("id")

    return render_to_pdf(
        template_name,
        {
            "family": family,
        },
    )

def StudentResultList(request):
    template_name = "StudentsPdf.html"
    family = Student.objects.all().order_by("id")

    return render_to_pdf(
        template_name,
        {
            "family": family,
        },
    )

