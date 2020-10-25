from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import complaintMessageForm

# Create your views here.

def index(request):
    return render(request, 'complaint/foo.html')

def confirmMessage(request):
    if request.method == 'POST':
        form = complaintMessageForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('POST success')
    else:
        form = complaintMessageForm()
    
    return render(request, 'complaint/message.html', {'form':form})
