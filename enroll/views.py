from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'enroll/home.html', {'studata':stu_data})

class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'enroll/add-student.html', {'form':fm})

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'enroll/add-student.html', {'form':fm})

class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')

class EditStudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'enroll/edit-student.html', {'form':fm})    

    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()    
            return redirect('/')


