from django.shortcuts import render
from study_tracker.models import StudyRecord


# Create your views here.
def show_tracker(request):
    transaction_data = StudyRecord.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': 'Ardian'
    }
    return render(request, "tracker.html", context)
