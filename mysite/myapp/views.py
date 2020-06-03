from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, page=0):
    li = list(range(page*20,page*20+20))
    context = {
        "variable":"Hello World",
        "my_list":li,
        "title": "My Title",
        "page": page
    }
    return render(request,"index.html", context=context)

def view_two(request):
    context = {
        "variable":"Second",
        "title": "Second",
    }
    return render(request,"second.html", context=context)