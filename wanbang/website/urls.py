"""
URL configuration for wanbang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name = "home"),
    path('about.html', views.about, name = "about"),
    path('contact.html', views.contact, name = "contact"),
    path('expert.html', views.expert, name = "expert"),
    path('interior.html', views.interior, name = "interior"),
    path('exterior.html', views.exterior, name = "exterior"),
    path('aboutu.html', views.aboutu, name = "aboutu"),
    path('insight.html', views.insight, name = "insight"),
    path('blog_template.html', views.blog_template, name = "blog_template"),
    
    # Blog URLs - removed duplicate with consistent naming
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/<slug:slug>.html', views.blog_detail, name='blog_detail'),
    
    # Make sure hardcoded paths like 'blog/contact.html' don't exist
    
    # Special case for the Sandy Springs blog
    path('blog/blog_interior_sandy_springs.html', views.blog_detail, 
         {'slug': 'blog_interior_sandy_springs'}, name='blog_interior_sandy_springs'),
    
    # Redirect any attempts to access /blog/contact.html to the contact page
    path('blog/contact.html', RedirectView.as_view(pattern_name='contact', permanent=True)),
    path('contact/', views.contact, name='contact'),
]

