from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Persons
from .forms import PersonForm
# Create your views here.
def index(request):
    form = PersonForm()
    context = {'db': Persons.objects.all(), 'form': form}
    return render(request, 'cr/index.html', context=context)
def add(request):
    if not request.GET:
        form = PersonForm()
        return render(request, 'cr/add.html', context={'form': form})
    else:
        form = PersonForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return HttpResponseRedirect('/')