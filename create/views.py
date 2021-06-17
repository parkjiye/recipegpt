from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html', {})


@csrf_exempt
def page2(request):
    return render(request, 'page2.html', {})
