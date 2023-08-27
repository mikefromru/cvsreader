from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import Client

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(Client, ClientAdmin)