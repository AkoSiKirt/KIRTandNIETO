from django.contrib import admin
from django.urls import path
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('submit_report/', views.submit_report, name='submit_report'),
]
