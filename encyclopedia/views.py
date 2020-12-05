from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SearchForm
import random

from . import util

import markdown as md


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()   
    })

def search(request, entry):
    value = util.get_entry(entry)
    if value is None:
        matches = util.match_title(entry)
        if not matches:
            return render(request, "encyclopedia/404.html", {
            "entry": entry,   
            })
        return render(request, "encyclopedia/matches.html", {
            "entries": matches,
            "requestedpage": entry,
        })
    html = md.markdown(value, extensions=['markdown.extensions.fenced_code'])
    return render(request, "encyclopedia/markdown.html", {
        "entry": entry,
        "body": html,
    })

def query(request):
    if request.method == "POST":
        return search(request, request.POST['q'])

def createpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/createpage.html")
    elif request.method == "POST":
        title = request.POST['title']
        if util.check_title(title):
            util.save_entry(title, request.POST['body'])
            return search(request, title)
        match = util.match_title(title).pop(0)
        return render(request, "encyclopedia/titleerror.html", {
            "title": match
        })

def editpage(request):
    if request.method == "GET":
        title = request.GET['q']
        body = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
        "body": body,
        "title": title,
        })
    elif request.method == "POST":
        print(request)
        title = request.POST['title']
        util.save_entry(title, request.POST['body'])
        return redirect('/wiki/' + title)

def randompage(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('/wiki/' + random_entry)