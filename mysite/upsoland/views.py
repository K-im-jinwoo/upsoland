from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'upsoland/index.html',
    )

def about_me(request):
    return render(
        request, 
        'upsoland/about_me.html',
    )