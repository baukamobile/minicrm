from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.



# def home(request):
#     if request.method == 'POST':
#         username = request.POST.['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have been login! ')
#             return redirect('home')
#         else:
#             messages(request, 'There was an error with login')
#             return redirect('home')
#     else:
#         return render(request, 'home.html')

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error with your login')
            return redirect('home')
    else:
        return render(request, 'home.html', context={'records':records})

# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logging out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have succesfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', context={
        'form': form,
    })
    return render(request, 'register.html', context={
        'form': form,
    })


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', context={'customer_record':customer_record})
    else:
        messages.success(request, 'something wrong')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_rd = Record.objects.get(id=pk)
        delete_rd.delete()
        messages.success(request, 'Deleted...')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged to do that')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added...')
                return redirect('home')
        return render(request, 'add_record.html', context={'form':form})
    else:
        messages.success(request, 'Record Added...')
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')
        return render(request, 'update_record.html', context={'form':form, 'current_record': current_record})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')
