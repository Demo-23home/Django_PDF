from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import os

from django.conf import settings
from .models import Customer


def render_pdf_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    template_path = "customers/invoice_template.html"
    context = {"customer": customer}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_{customer.name}.pdf"'

    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    
    return response


def link_callback(uri, rel):
    """
    Convert HTML media URLs to absolute paths for PDF rendering.
    """
    if uri.startswith(settings.MEDIA_URL):
        return os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    if uri.startswith(settings.STATIC_URL):
        return os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return uri
