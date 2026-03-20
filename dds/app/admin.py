from django.contrib import admin

from .models import CashFlowRecord, Category, OperationType, Status, SubCategory

admin.site.register(Status)
admin.site.register(OperationType)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CashFlowRecord)
