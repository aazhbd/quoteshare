from django.shortcuts import render
from django.db.models import Q, Count, Min, Max, Sum
from quran.models import *

from django.db.models.query import QuerySet

from django.views import generic

class HomeView(generic.ListView):
    model = Chapter
    context_object_name = 'chapters'
    template_name = 'home.html'


class ChapterView(generic.TemplateView):
    template_name = "chapter.html"

    def get(self, request, *args, **kwagrs):
        self.chapter_number = kwagrs['chapter']
        self.author_ids = [1]
        authors = request.GET.get("t", None)
        if authors:
            author_ids = authors.split(',')
            self.author_ids = self.author_ids + author_ids
            self.selected_authors = Author.objects.filter(pk__in=self.author_ids)
        else:
            self.selected_authors = Author.objects.filter(pk=1)

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_authors'] = self.selected_authors

        data['translations'] = Verse.objects.filter(Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number)).order_by('number', 'author')

        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        dista = Verse.objects.raw('SELECT id, author_id FROM quran_verse GROUP BY author_id')
        distinct_authors = [dauthor.author.id for dauthor in dista]
        distinct_langauges = [dauthor.author.alang.id for dauthor in dista]

        data['author_info'] = Author.objects.filter(id__in=distinct_authors)
        data['language_info'] = Language.objects.filter(id__in=distinct_langauges)
        return data


class VerseView(generic.ListView):
    model = Verse
    context_object_name = 'verse'
    template_name = 'verse.html'

    def get(self, request, *args, **kwagrs):
        self.object_list = self.get_queryset()
        self.chapter_number = kwagrs['chapter']
        self.verse_number = kwagrs['verse']

        self.author_ids = [1]
        authors = request.GET.get("t", None)
        if authors:
            author_ids = authors.split(',')
            self.author_ids = self.author_ids + author_ids
            self.selected_authors = Author.objects.filter(pk__in=self.author_ids)
        else:
            self.selected_authors = Author.objects.filter(pk=1)

        v = Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number) & Q(number=self.verse_number)
        self.object_list = self.object_list.filter(v).order_by('number', 'author')
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_authors'] = self.selected_authors

        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        dista = Verse.objects.raw('SELECT id, author_id FROM quran_verse GROUP BY author_id')
        distinct_authors = [dauthor.author.id for dauthor in dista]
        distinct_langauges = [dauthor.author.alang.id for dauthor in dista]

        data['author_info'] = Author.objects.filter(id__in=distinct_authors)
        data['language_info'] = Language.objects.filter(id__in=distinct_langauges)
        return data

