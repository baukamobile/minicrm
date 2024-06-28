from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
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
        return render(request, 'home.html')

# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logging out...')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')