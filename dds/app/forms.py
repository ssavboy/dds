from django import forms

from .models import CashFlowRecord, Category, OperationType, SubCategory


class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = [
            "created_at",
            "status",
            "operation_type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["amount"].required = True
        self.fields["operation_type"].required = True
        self.fields["category"].required = True
        self.fields["subcategory"].required = True

        # по умолчанию — все варианты доступны
        self.fields["operation_type"].queryset = OperationType.objects.all()
        self.fields["category"].queryset = Category.objects.all()
        self.fields["subcategory"].queryset = SubCategory.objects.all()

        data = self.data or None
        instance = self.instance

        # 1. operation_type_id
        operation_type_id = None
        if data:
            operation_type_id = data.get("operation_type")
        elif instance and getattr(instance, "operation_type", None):
            operation_type_id = instance.operation_type.pk

        if operation_type_id:
            self.fields["category"].queryset = Category.objects.filter(
                operation_type_id=operation_type_id
            )

        # 2. category_id
        category_id = None
        if data:
            category_id = data.get("category")
        elif instance and getattr(instance, "category", None):
            category_id = instance.category.pk

        if category_id:
            self.fields["subcategory"].queryset = SubCategory.objects.filter(
                category_id=category_id
            )
