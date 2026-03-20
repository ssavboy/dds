from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_date

from .forms import CashFlowRecordForm
from .models import CashFlowRecord, Category, OperationType, Status, SubCategory


def records_list(request):
    records = CashFlowRecord.objects.select_related(
        "status", "operation_type", "category", "subcategory"
    ).all()

    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    status_id = request.GET.get("status")
    operation_type_id = request.GET.get("operation_type")
    category_id = request.GET.get("category")
    subcategory_id = request.GET.get("subcategory")

    if date_from:
        records = records.filter(created_at__gte=parse_date(date_from))
    if date_to:
        records = records.filter(created_at__lte=parse_date(date_to))
    if status_id:
        records = records.filter(status_id=status_id)
    if operation_type_id:
        records = records.filter(operation_type_id=operation_type_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)

    context = {
        "records": records,
        "statuses": Status.objects.all(),
        "operation_types": OperationType.objects.all(),
        "categories": Category.objects.all(),
        "subcategories": SubCategory.objects.all(),
        "params": request.GET,
    }
    return render(request, "app/records_list.html", context)


def record_create(request):
    if request.method == "POST":
        form = CashFlowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("records_list")
    else:
        form = CashFlowRecordForm()
    return render(request, "app/record_form.html", {"form": form})


def record_update(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == "POST":
        form = CashFlowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("records_list")
    else:
        form = CashFlowRecordForm(instance=record)
    return render(request, "app/record_form.html", {"form": form, "record": record})


def record_delete(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("records_list")
    return render(request, "app/record_confirm_delete.html", {"record": record})
