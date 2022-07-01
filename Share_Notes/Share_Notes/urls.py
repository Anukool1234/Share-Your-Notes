"""Share_Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from notes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about,name='about'),
    path('contact', contact,name='contact'),
    path('login', userlogin,name='login'),
    path('Logout', Logout,name='Logout'),
    path('signup', signup1,name='signup'),
    path('profile', profile,name='profile'),
    path('admin_home', admin_home,name='admin_home'),
    path('login_admin', login_admin,name='login_admin'),
    path('', index,name='index'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('changepassword', changepassword,name='changepassword'),
    path('upload_notes', upload_notes,name='upload_notes'),
    path('pending_notes', pending_notes,name='pending_notes'),
    path('accepted_notes', accepted_notes,name='accepted_notes'),
    path('rejected_notes', rejected_notes,name='rejected_notes'),
    path('all_notes', all_notes,name='all_notes'),
    path('view_mynotes', view_mynotes,name='view_mynotes'),
    path('view_users', view_users,name='view_users'),
    path('viewallnotes', viewallnotes,name='viewallnotes'),
    path('delete_mynotes/<int:pid>', delete_mynotes,name='delete_mynotes'),
    path('delete_notes/<int:pid>', delete_notes,name='delete_notes'),
    path('assign_status/<int:pid>', assign_status,name='assign_status'),
    path('delete_users/<int:pid>', delete_users,name='delete_users')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
