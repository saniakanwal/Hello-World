from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import pandas as pd 
class homeView(TemplateView):
	template_name = 'home.html'
class LoginView(TemplateView):
	template_name = 'login.html'
class scholarLink(TemplateView):
        var1 = ""
        template_name='displayscholar.html'
        data = pd.read_csv('links.csv',encoding = "ISO-8859-1", header = None)
        data_list = list(data[0])
        data = list(data[1])
        def get_context_data(self, **kwargs):
                context = super(scholarLink, self).get_context_data(**kwargs)
                context.update({'var1': self.data_list})
                context.update({'var2': self.data})
                return context
       
        
       
        

