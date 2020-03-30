from django.shortcuts import render

from quran.models import Chapter

from django.views import generic

class HomeView(generic.ListView):
    model = Chapter
    context_object_name = 'chapters'
    template_name = 'home.html'

