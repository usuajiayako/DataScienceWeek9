from django.shortcuts import render, redirect
from .models import Visitor
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from . import report
from . import analysis

from django.http import JsonResponse
from django.core import serializers
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

# Report
@login_required(login_url="/accounts/login/")
def visitor_report(request):
    if request.method == 'POST':
        date = request.POST.get("date")
        selected_date = Visitor.objects.filter(date=date)
        df, df_csv = report.data_to_df(selected_date) # visitor table
        visitor_num = Visitor.objects.filter(date=date).count() # total number of visitor
        gender = analysis.gender_analysis(df_csv) # gender ratio pie chart
        return render(request, 'visitors/report_detail.html', {'df': df, 'visitor_number':visitor_num, 'gender':gender})
    return render(request, 'visitors/report.html') 

# Dashboard
def dashboard_with_pivot(request):
    return render(request, 'visitors/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Visitor.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)