from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','age','wallet','promo_code']
    readonly_fields = ['wallet','promo_code']

admin.site.register(Profile,ProfileAdmin)