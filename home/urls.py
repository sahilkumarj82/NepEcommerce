from tkinter.tix import Form
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<slug>', ProductDetaileView.as_view(), name='detail'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),

]