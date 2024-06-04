from django.shortcuts import render,redirect
from  .models import Students
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    students = Students.objects.all()  # Fetch the students data
    return render(request, 'students.html', {'students': students})

def view_student(request, id):
    students= Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data ['student_number']
            new_first_name = form.cleaned_data ['first_name']
            new_last_name = form.cleaned_data ['last_name']
            new_email = form.cleaned_data ['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data ['gpa']

            new_student=Students(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            new_student.save()
            return render (request, 'add.html', {
            'form': StudentsForm(),
            'success': True,
            }
            )
    else:
        form=StudentsForm()
        return render (request, 'add.html', {
            'form': StudentsForm()
            }
        )
            
def edit(request, id):
    student = get_object_or_404(Students, pk=id)
    
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
        else:
            return render(request, 'edit.html', {
                'form': form
            })
    else:
        form = StudentsForm(instance=student)
        return render(request, 'edit.html', {
            'form': form
        })
        


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'login.html')

def delete(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Students, pk=id)
        student.delete()
        return HttpResponseRedirect( reverse('index'))
     
