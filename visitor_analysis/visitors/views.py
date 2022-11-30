from django.shortcuts import render
from .models import Visitor
# Create your views here.

def visitors(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitors.html', {'visitors':visitors})
