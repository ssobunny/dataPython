from django.shortcuts import render
from .models import Cafe

def index(request):
  return render(request, 'main/index.html')

def cafelist(request):
  cafelistobj = Cafe.objects.all()
  return render(request, 'main/cafelist.html',
                {'cafelistobj': cafelistobj})

def cafedetails(request, pk):
  cafeobj = Cafe.objects.get(pk=pk)
  return render(request, 'main/cafedetails.html',
                {'cafeobj': cafeobj})

def sample(request):
  value = 2
  return render(request, 'main/sample.html',
                {'value': value})