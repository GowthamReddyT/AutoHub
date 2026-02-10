from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from cbvapp.models import Company, Product, Interior, Exterior


# ---------------- HOME ----------------
class Myclass(TemplateView):
    template_name = "index.html"


# ---------------- COMPANY ----------------
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
    template_name = "cbvapp/delete_confirm.html"
    success_url = reverse_lazy("list")


# ---------------- PRODUCT ----------------
class ProductDetailView(DetailView):
    model = Product
    template_name = "cbvapp/products_details.html"
    context_object_name = "product"


# ---------------- EMI ----------------
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


# ---------------- INTERIOR ----------------
class AddInterior(CreateView):
    model = Interior
    fields = ["image"]
    template_name = "cbvapp/add_interior.html"

    def form_valid(self, form):
        form.instance.product_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.object.product.id})


class DeleteInterior(DeleteView):
    model = Interior
    template_name = "cbvapp/delete_confirm.html"

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.object.product.id})


# ---------------- EXTERIOR ----------------
class AddExterior(CreateView):
    model = Exterior
    fields = ["image"]
    template_name = "cbvapp/add_exterior.html"

    def form_valid(self, form):
        form.instance.product_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.object.product.id})


class DeleteInterior(View):
    def get(self, request, pk):
        interior = get_object_or_404(Interior, pk=pk)
        product_id = interior.product.id
        interior.delete()
        return redirect("product_detail", pk=product_id)


class DeleteExterior(View):
    def get(self, request, pk):
        exterior = get_object_or_404(Exterior, pk=pk)
        product_id = exterior.product.id
        exterior.delete()
        return redirect("product_detail", pk=product_id)