from django.shortcuts import render
from django.http import HttpResponse

items = [['Sample Item', '02/25/21']]

# Create your views here.

def index(request):
    return render(request, 'pantry/index.html', {
        "items": items
    })