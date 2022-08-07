from django.contrib import admin
from .models import QrcodeApi, TestModel

# Register your models here.

class QrcodeApi_gen(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']

admin.site.register(QrcodeApi, QrcodeApi_gen)

# api generator
class Api_gen(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']

admin.site.register(TestModel, Api_gen)