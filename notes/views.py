from django.shortcuts import render
from django.http import HttpResponse

from.models import Note, Tag

# Create your views here.
def notes(request):
    notes = Note.objects.all()

    result = ""
    
    for note in notes:
        result += "{}\n".format(note.html_view())
    return HttpResponse(result)