from django.shortcuts import render,redirect
from django.contrib import messages
from SchoolApp.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
def home(request):
    return render(request,'Home.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphonenumber=request.POST.get("num")
        fdescription=request.POST.get("Description")

        print(fname,femail,fphonenumber,fdescription)
        messages.info(request,f'The name is {fname},email is {femail},Phonenumber is{fphonenumber}&your query is{fdescription}')

        query=Contacts(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks For Contating us")
    return render(request,'Contact.html')




def index(request):
    try:
        if 'q' in request.GET:
            q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q))
        data = Student.objects.filter(multiple_q) 
        if not data:
            messages.warning(request,"No data found")
        else:
            pass
    except:
        pass
        data=Student.objects.all()
    page=Paginator(data,10)
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
    context={'page':page}
    return render(request,'StudentsAdd.html',context)



def insertedData(request):
   
    if request.method=="POST":
        RollNumber=request.POST.get('roll')
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        Artist=request.POST.get('artist')
    try:
        if Student.objects.get(email=Email):
            messages.warning(request,"Email is Already Taken")
            return redirect("/StudentAdd")
    except:
        pass
        query=Student(rollnumber=RollNumber,name=Name,email=Email,age=Age,gender=Gender)
    messages.success(request,'Student Details Added Successfully')
    query.save()
    return redirect("/StudentAdd")
    return render(request,'StudentsAdd.html')
    

def update(request,id):
    if request.method=="POST":
        RollNumber=request.POST['roll']
        Name=request.POST['name']
        Email=request.POST['email']
        Age=request.POST['age']
        Gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.rollnumber=RollNumber
        edit.name=Name
        edit.email=Email
        edit.age=Age
        edit.gender=Gender
        #try:
            #if Student.objects.get(email=edit.email):
                #messages.warning(request,"Already mail exists. Enter New mail")
                #return redirect("/")
        #except:
            #pass
        edit.save()
        messages.success(request,"Student Details successfully Updated..")
        return redirect("/StudentAdd")
    d=Student.objects.get(id=id)
    context={'d':d}
    return render(request,'Student_Edit.html',context)

def delete(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.success(request,"Student Details Successfully deleted..")
    return redirect("/StudentAdd")

def StudentEdit(request):
    return render(request,'Student_Edit.html')




##Student Family Details
def Family(request):
    try:
        if 'q' in request.GET:
            q = request.GET['q']
        #data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(father_name__icontains=q))
        family = StudentFamily.objects.filter(multiple_q) 
        if not family:
           messages.warning(request,"No data found")
        else:
            pass
    except:
        pass

        family=StudentFamily.objects.all()
        SF=Student.objects.all()
        #page1=Paginator(family,10)
        #page_list1=request.GET.get('page1')
        #page1=page1.get_page(page_list1)
        #context={'page1':page1,'SF':SF}
        context={'SF':SF,'family':family}
       
        return render(request,'StudentDetails.html',context)

def familyinsertedData(request):
    SF=Student.objects.all()
    print(SF)
    
    if request.method=="POST":
        
        name_id=request.POST.get('name')
        Name=Student.objects.get(name=name_id)
        try:
            if StudentFamily.objects.get(name=Name):
                messages.warning(request,"Name is Already Taken")
            return redirect("/StudentDetails")
        except:
            pass
            
        
        FatherName=request.POST.get('father_name')
        MotherName=request.POST.get('mother_name')
        EmergencyContact=request.POST.get('emergency')
        Address=request.POST.get('address')
    
        query1=StudentFamily(name=Name,father_name=FatherName,mother_name=MotherName,emergency=EmergencyContact,address=Address)
    messages.success(request,'Student Details Added Successfully')
    query1.save()
    return redirect("/StudentDetails")
    return render(request,'Student_Details.html')

def StudentDetailsUpdate(request,id):
    if request.method=="POST":
        name_id=request.POST.get('name')
        Name=Student.objects.get(name=name_id)
        FatherName=request.POST['father_name']
        MotherName=request.POST['mother_name']
        EmergencyContact=request.POST['emergency']
        Address=request.POST['address']

        SDU=StudentFamily.objects.get(id=id)
        
        SDU.name=Name
        SDU.father_name=FatherName
        SDU.mother_name=MotherName
        SDU.emergencycontact=EmergencyContact
        SDU.address=Address
        #try:
            #if Student.objects.get(email=edit.email):
                #messages.warning(request,"Already mail exists. Enter New mail")
                #return redirect("/")
        #except:
            #pass
        SDU.save()
        messages.success(request,"Student Details successfully Updated..")
        return redirect("/StudentDetails")
    category=StudentFamily.objects.get(id=id)
    context={'category':category}
    return render(request,'StudentDetailsEdit.html',context)

def StudentDetailsDelete(request,id):
    d=StudentFamily.objects.get(id=id)
    d.delete()
    messages.success(request,"Student Details Successfully deleted..")
    return redirect("/StudentDetails")


def pdf(request):
    d=Student.objects.all()
    template_path ='StudentsAdd.html'
    context = {'d': d}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Student.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response) 
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
