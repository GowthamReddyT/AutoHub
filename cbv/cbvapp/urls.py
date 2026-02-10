from django.urls import path
from cbvapp import views

urlpatterns = [

    # HOME – Company list
    path('', views.AllCompanies.as_view(), name='list'),

    # EMI (MUST be above <int:pk>/)
    path('emi/<int:pk>/', views.EmiCalculator.as_view(), name='emi_calculator'),

    # PRODUCT DETAIL (optional, if you use it)
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # COMPANY CRUD
    path('create/', views.AddNewCompany.as_view(), name='create'),
    path('add/', views.AddNewCompany.as_view(), name='add'),

    path('<int:pk>/edit/', views.EditCompany.as_view(), name='edit_company'),
    path('<int:pk>/delete/', views.DeleteCompany.as_view(), name='delete_company'),

    # COMPANY DETAIL (KEEP THIS LAST)
    path('<int:pk>/', views.CompanyDetails.as_view(), name='detail'),
]
