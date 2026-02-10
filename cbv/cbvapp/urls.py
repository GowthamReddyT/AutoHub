from django.urls import path
from cbvapp import views

urlpatterns = [
    path('',views.AllCompanies.as_view(),name = 'list'),
    path('<int:pk>/',views.CompanyDetails.as_view(),name = 'detail'),
     path('create/', views.AddNewCompany.as_view(), name='create'),
]