from django.shortcuts import render
from django.http import HttpResponse
from .models import table
# Create your views here.
def home(request):
  tabs = table.objects.all()
  return render(request,'index.html', {'tabs': tabs})