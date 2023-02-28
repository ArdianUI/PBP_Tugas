from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse



# Create your views here.
def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
    'list_of_assignments': assignment_data,
    'name': 'Ardian'
    }
    return render(request, "tracker.html", context)

def create_assignment(request):
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:study_tracker'))

    context = {'form': form}
    return render(request, "create_assignment.html", context)
