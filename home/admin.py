from django.contrib import admin

# Register your models here.
from .models import Product, ResearchPaper, Design, Requirement

admin.site.register(Product)
admin.site.register(ResearchPaper)
admin.site.register(Design)
admin.site.register(Requirement)
