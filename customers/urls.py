from django.urls import path
from .views import render_pdf_view

urlpatterns = [
    path("invoice/<int:customer_id>/", render_pdf_view, name="customer_invoice"),
]
