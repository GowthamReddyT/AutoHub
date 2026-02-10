from urllib import request
import django
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvapp.models import Company


# Create your views here..
# class Myclass(View):
#     def get(self,request):
#         return HttpResponse("<h1> This is the Class Based View</h1>")

class Myclass(TemplateView):
    template_name="index.html"

class AllCompanies(ListView):
    model = Company
    context_object_name = "companies"

class CompanyDetails(DetailView):
    model = Company
    context_object_name = "company_details"

class AddNewCompany(CreateView):
    model = Company
    fields = '__all__'
    success_url = '/company/'

