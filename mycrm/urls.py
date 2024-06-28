from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name= 'home'),
    path('login/', login_user, name= 'loginpage'),
    path('logout/', logout_user, name= 'logout'),

]
