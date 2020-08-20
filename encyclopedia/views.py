from django.shortcuts import render
from django.http import HttpResponse

from . import util

import markdown as md


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()   
    })

def search(request, entry):
    value = util.get_entry(entry)
    if value is None:
        return render(request, None)
    html = md.markdown(value, extensions=['markdown.extensions.fenced_code'])
    return render(request, "encyclopedia/markdown.html", {
        "entry": entry,
        "body": html
    })