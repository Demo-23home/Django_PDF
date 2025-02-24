from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Customer(models.Model): 
    name = models.CharField(_(""), max_length=50)
    logo = models.ImageField(_(""), upload_to="customer/images")
    description = models.TextField(_(""))
    created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_(""), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name