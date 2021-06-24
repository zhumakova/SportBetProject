from django.contrib import admin
from .models import *

class BetAdmin(admin.ModelAdmin):
    list_display = ['profile','match','amount','result']
    readonly_fields = ['match','result']

admin.site.register(Bet,BetAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['amount']


admin.site.register(Transaction,TransactionAdmin)

