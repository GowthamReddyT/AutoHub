from django.urls import path
from cbvapp import views

urlpatterns = [

    # ---------------- HOME (Company List) ----------------
    path('', views.AllCompanies.as_view(), name='companies'),

    # ---------------- EMI ----------------
    # Keep this above <int:pk>/ pattern
    path('emi/<int:pk>/', views.EmiCalculator.as_view(), name='emi_calculator'),

    # ---------------- PRODUCT DETAIL ----------------
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # ---------------- COMPANY CRUD ----------------
    path('add/', views.AddNewCompany.as_view(), name='add_company'),
    path('<int:pk>/edit/', views.EditCompany.as_view(), name='edit_company'),
    path('<int:pk>/delete/', views.DeleteCompany.as_view(), name='delete_company'),

    # ---------------- COMPANY DETAIL (KEEP LAST) ----------------
    path('<int:pk>/', views.CompanyDetails.as_view(), name='detail'),
]
