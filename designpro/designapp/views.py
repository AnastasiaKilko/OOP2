from django.shortcuts import render
from .models import Application

# Create your views here.
def index(request):

    num_applications_accepted = Application.objects.filter(status__exact='a').count()

    return render(
        request, 'index.html', {'num_applications_accepted': num_applications_accepted})