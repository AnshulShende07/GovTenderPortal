
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("signup",views.handlesignup, name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('feedback',views.feedback, name='feedback'),
    path('company',views.company,name='company'),
    path('c_profile',views.c_profile,name='c_profile'),
    path('govlogin',views.govlogin,name='govlogin'),
    path('managet',views.managet,name='managet'),
    path('addtender',views.addtender,name='addtender'),
    path('viewtender',views.viewtender,name='viewtender'),
    path('tenders',views.handletender,name='handletender'),
    path('create_progress',views.create_progress,name='progress'),
    path('application',views.application,name='application'),
    path('comp_apply',views.comp_apply,name='comp_apply'),
    path('deltender',views.deltender,name='deltender'),
    path('mail',views.mail,name='mail'),
    path('chat',views.chat, name = 'chat')
    # path('vtenders',views.companyviewtender,name='viewtendercompany')
 
    
]
