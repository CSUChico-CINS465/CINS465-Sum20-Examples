from datetime import datetime, timezone
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if request.user.is_authenticated:
            if form_instance.is_valid():
                form_instance.save(request)
                form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    suggestion_list = models.SuggestionModel.objects.all()
    context = {
        "variable":"Suggestion List",
        "my_list":suggestion_list,
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

def add_comment(request, sugg_id):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                form.save(request, sugg_id)
                return redirect("/")
        else:
            return redirect("/")
    else:
        form = forms.CommentForm()
    context = {
        "title":"Comment",
        "sugg_id": sugg_id,
        "form":form
    }
    return render(request, "comment.html", context=context)

def add_suggestion(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.SuggestionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(request)
                return redirect("/")
        else:
            return redirect("/")
    else:
        form = forms.SuggestionForm()
    context = {
        "title":"Suggestion",
        "form":form
    }
    return render(request, "suggestion.html", context=context)

def get_suggestions(request):
    suggestion_objects = models.SuggestionModel.objects.all().order_by(
        '-published_on'
    )
    suggestion_list = {}
    suggestion_list["suggestions"] = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(
            suggestion=sugg
        ).order_by(
            '-published_on'
        )
        temp_sugg = {}
        temp_sugg["id"] = sugg.id
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["author"] = sugg.author.username
        temp_sugg["date"] = sugg.published_on.strftime("%Y-%m-%d %H:%M:%S")
        temp_sugg["comments"] = []
        try:
            temp_sugg["image"] = sugg.image.url
            temp_sugg["image_desc"] = sugg.image_description
        except ValueError:
            temp_sugg["image"] = ""
            temp_sugg["image_desc"] = "" 
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
