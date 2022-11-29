from django.shortcuts import render

# Create your views here.

def visitors(request):
    return render(request, 'visitors/visitors.html' )
