from django.contrib import admin

# Register your models here.
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )

admin.site.register(Phone, PhoneAdmin)