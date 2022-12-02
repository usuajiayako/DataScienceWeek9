from django.shortcuts import render
from .models import Visitor
from django.http import HttpResponse
# Create your views here.

def visitors(request):
    visitors = Visitor.objects.all().order_by('date')
    return render(request, 'visitors/visitors.html', {'visitors':visitors})

def visitor_detail(request, id):
    return HttpResponse(id)