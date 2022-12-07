from django.shortcuts import render, redirect
from .models import Visitor
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def visitors(request):
    visitors = Visitor.objects.all().order_by('date')
    return render(request, 'visitors/visitors.html', {'visitors':visitors})

def visitor_detail(request, id):
    visitor = Visitor.objects.get(id=id)
    return render(request, 'visitors/visitor_detail.html', {'visitor':visitor})

@login_required(login_url="/accounts/login/")
def visitor_register(request):
    if request.method == 'POST':
        form = forms.RegisterVisitor(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("visitors:register")
    else:
        form = forms.RegisterVisitor()
    return render(request, 'visitors/visitor_register.html', {'form':form})