
from .models import Student
from import_export import resources

class StudentFamilyesource(resources.ModelResource):
    class meta:
        model=Student