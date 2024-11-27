from django.shortcuts import render
from .models import Application
from django.views import generic

# Create your views here.
def index(request):
    applications_done = Application.objects.filter(status__exact='d')[:4]
    num_applications_accepted = Application.objects.filter(status__exact='a').count()

    return render(
        request, 'index.html', {'applications_done': applications_done,
                                'num_applications_accepted': num_applications_accepted})

class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4

    def get_queryset(self):
        return Application.objects.filter(status__incontains='d')

class ApplicationDetailView(generic.DetailView):
    model = Application
    def get_queryset(self):
        return Application.objects.filter(status__incontains='d')
