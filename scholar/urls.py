from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns=[
	path('', TemplateView.as_view(template_name="home.html"),name='home'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
	path('list/',views.scholarLink.as_view(),name='list'),
]
