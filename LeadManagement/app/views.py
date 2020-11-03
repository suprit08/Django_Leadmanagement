from django.shortcuts import render, redirect
from .models import Lead
from .import forms

# Create your views here.
def showHome(request):
    form = forms.LeadForm
    if request.method=='POST':
        form=forms.LeadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect('display')
    return render(request, 'home.html', {'form':form})

def showDisplay(request):
    qs = Lead.objects.all()
    return render(request, 'display.html', {'qs':qs})