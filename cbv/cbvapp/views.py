from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from cbvapp.models import Company, Product


class Myclass(TemplateView):
    template_name = "index.html"


class AllCompanies(ListView):
    model = Company
    template_name = "cbvapp/company_list.html"
    context_object_name = "companies"


class CompanyDetails(DetailView):
    model = Company
    template_name = "cbvapp/company_detail.html"
    context_object_name = "company_details"


class AddNewCompany(CreateView):
    model = Company
    fields = "__all__"
    template_name = "cbvapp/add_company.html"
    success_url = reverse_lazy("list")


class EditCompany(UpdateView):
    model = Company
    fields = ["name", "ceo", "est_year", "origin", "image"]
    template_name = "cbvapp/company_Edit.html"
    success_url = reverse_lazy("list")


class DeleteCompany(DeleteView):
    model = Company
    template_name = "cbvapp/company_confirm_delete.html"
    success_url = reverse_lazy("list")


class EmiCalculator(DetailView):
    model = Product
    template_name = "cbvapp/emi_calculator.html"
    context_object_name = "product"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        tenure = int(request.POST.get("tenure"))
        loan_amount = float(request.POST.get("loan_amount"))

        rate = 12
        P = loan_amount
        R = (rate / 12) / 100
        N = tenure * 12

        emi = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

        context = self.get_context_data(
            emi=round(emi, 2),
            tenure=tenure,
            loan_amount=loan_amount
        )
        return self.render_to_response(context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "cbvapp/products_details.html"
    context_object_name = "product"
