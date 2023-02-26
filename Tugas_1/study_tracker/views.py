from django.shortcuts import render
from study_tracker.models import TransactionRecord


# Create your views here.
def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': 'Ardian'
    }
    return render(request, "tracker.html", context)
