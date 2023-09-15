
from .models import Student,StudentFamily
from import_export import resources

class Studentresource(resources.ModelResource):
    class meta:
        model=Student
        #import_id_fields =["rollnumber","name", "email", "age","gender"]
        #skip_unchanged = True
        #use_bulk = True