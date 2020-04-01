from django.shortcuts import render
from django.db.models import Q, Count, Min, Max, Sum
from quran.models import *

from django.views import generic

class HomeView(generic.ListView):
    model = Chapter
    context_object_name = 'chapters'
    template_name = 'home.html'


class ChapterView(generic.ListView):
    model = Verse
    context_object_name = 'chapter'
    template_name = 'chapter.html'

    def get(self, request, *args, **kwagrs):
        self.object_list = self.get_queryset()
        self.chapter_number = kwagrs['chapter']
        v = Q(chapter=self.chapter_number) & Q(author__name='Original Text')
        self.object_list = self.object_list.filter(v)
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        data['author_info'] = Author.objects.all()
        data['language_info'] = Language.objects.all()
        return data


class VerseView(generic.ListView):
    model = Verse
    context_object_name = 'verse'
    template_name = 'verse.html'

    def get(self, request, *args, **kwagrs):
        self.object_list = self.get_queryset()
        self.chapter_number = kwagrs['chapter']
        self.verse_number = kwagrs['verse']
        v = Q(chapter=self.chapter_number) & Q(number=self.verse_number) & Q(author__name='Original Text')
        self.object_list = self.object_list.filter(v)
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        data['author_info'] = Author.objects.all()
        data['language_info'] = Language.objects.all()
        return data

