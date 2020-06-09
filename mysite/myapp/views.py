from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from datetime import datetime, timezone


from . import models
from . import forms

# Create your views here.
def index(request,page=0):
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if request.user.is_authenticated:
            if form_instance.is_valid():
                form_instance.save(request)
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

@login_required()
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

def get_suggestions(request):
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = {}
    suggestion_list["suggestions"] = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["id"] = sugg.id
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["author"] = sugg.author.username
        temp_sugg["date"] = sugg.published_on.strftime("%Y-%m-%d %H:%M:%S")
        temp_sugg["comments"] = []
        for comm in comment_objects:
            temp_comm = {}
            temp_comm["id"] = comm.id
            temp_comm["comment"] = comm.comment
            temp_comm["author"] = comm.author.username
            temp_comm["date"] = (datetime.now(timezone.utc) - comm.published_on)
            temp_sugg["comments"].append(temp_comm)
        suggestion_list["suggestions"].append(temp_sugg)
    # print(suggestion_list)
    return JsonResponse(suggestion_list)
