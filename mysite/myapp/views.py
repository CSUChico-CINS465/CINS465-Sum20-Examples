from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout


from . import models
from . import forms

# Create your views here.
def index(request,page=0):
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    # numperpage=5
    # li = models.SuggestionModel.objects.all()[page*numperpage:page*numperpage+numperpage]
    li = models.SuggestionModel.objects.all()
    context = {
        "variable":"Suggestion List",
        "my_list":li,
        "title": "My Title",
        "form":form_instance,
    }
    return render(request, "index.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")


def view_two(request):
    context = {
        "variable":"Second",
        "title": "Second",
    }
    return render(request, "second.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)