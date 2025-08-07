from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('services/',views.ServicesView.as_view(),name='services'),
    path('contact/',views.ContactView,name='contact'),
    path('team/',views.TeamView,name='team'),
    path('properties/',views.PropertyView,name='properties'),
    path('properties/<str:city>/', views.PropertyView, name='properties_by_city'),
    path('detail/<int:id>',views.DetailPropertyView,name='detail'),
]
