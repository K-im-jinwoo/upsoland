from django.shortcuts import render

# Create your views here.

def consulting(request):
  return render (
    request,
    'counsel/consulting.html',
  )