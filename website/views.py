from django.shortcuts import render, redirect

# import authentication methods
from django.contrib.auth import authenticate, login, logout
# import flashing messages
from django.contrib import messages
from .forms import SignUpForm, Add_Record_Form
from django.contrib.auth.models import User
from . models import Record


# Create your views here.


def home(request):
    
    records = Record.objects.all()
    # return render(request, 'view_records.html', )
    return render (request, 'home.html', {'records': records})


def view_record(request, pk):
    
    record = Record.objects.get(id=pk)
    return render (request, 'view_record.html', {'record': record})

# login users
def login_user(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {user.first_name}")
            return redirect ('home')
        else:
            messages.error(request, "username or password is incorrect")
    
    return render (request, 'home.html')
# logout users
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You Have Been Logged out")
        return redirect ('home')
    return render (request, 'logout.html')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Verify if the user exists, then return the form with same data and error msg
        # note: is_valid() check if the user is exist, but it doesn't return error, 
        # if User.objects.filter(username=request.POST['username']).exists():
        #     messages.error(request, "username already exists")
        #     return render(request, 'register.html', {'form': form})
        
        # if the user doesn't exist, proceed with form
        if form.is_valid():
            # Authenticate and login  
            username= form.cleaned_data['username'] # when the form data is valid, the valid data the form will return a dict called cleaned_data
            password= form.cleaned_data["password1"]
            fname = form.cleaned_data['first_name']
            # save the data
            form.save()

            # Authenticate the new user and log him in and direct him to home
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcom {fname}")
            return redirect ('home')
    
    return render(request, 'register.html', {'form': form})


def add_record(request):
    form = Add_Record_Form()
    if request.method == 'POST':
        form = Add_Record_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'add_record.html', {'form': form})


def delete_record(request, pk):

    
    record = Record.objects.get(id=pk)
    if request.method == 'POST':

        record_name = record # save the record's name in this var before deleting so we can show it in the success msg 
        record.delete()
        messages.success(request, f" {record_name} record has been deleted")

        return redirect('home')
    return render(request, 'delete_record.html', {'record': record})

def edit_record(request, pk):

    record = Record.objects.get(id=pk)
    form = Add_Record_Form(instance = record)
    if request.method == 'POST':
        form = Add_Record_Form(request.POST) # we have to specify the instance, otherwise Django will add it as a new record
        if form.is_valid():
           
            form.save()
        return redirect('home')
    return render(request, 'edit_record.html', {'record': form})