from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class OperationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.PROTECT,
        related_name="categories",
    )

    class Meta:
        unique_together = ("name", "operation_type")

    def __str__(self):
        return f"{self.name} ({self.operation_type})"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="subcategories",
    )

    class Meta:
        unique_together = ("name", "category")

    def __str__(self):
        return f"{self.name} ({self.category})"


class CashFlowRecord(models.Model):
    created_at = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="records")
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.PROTECT,
        related_name="records",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="records",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        related_name="records",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)

    def clean(self):
        if (
            self.category
            and self.operation_type
            and self.category.operation_type != self.operation_type
        ):
            raise ValidationError("Категория не относится к выбранному типу.")

        if (
            self.subcategory
            and self.category
            and self.subcategory.category != self.category
        ):
            raise ValidationError("Подкатегория не относится к выбранной категории.")

    def __str__(self):
        return f"{self.created_at} {self.operation_type} {self.amount}"
