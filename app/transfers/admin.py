from django.contrib import admin

from .models import Transfer


class TransferAdmin(admin.ModelAdmin):
    model = Transfer

admin.site.register(Transfer, TransferAdmin)