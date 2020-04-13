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
    context_object_name = 'translations'
    template_name = "chapter.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.chapter_number = kwargs.get('chapter', 1)

        self.author_ids = [1]
        authors = request.GET.get("t", None)
        if authors:
            author_ids = authors.split(',')
            self.author_ids = self.author_ids + author_ids
            self.selected_authors = Author.objects.filter(pk__in=self.author_ids)
        else:
            self.selected_authors = Author.objects.filter(pk=1)

        self.verse_number = kwargs.get('verse', 0)
        self.to_verse = kwargs.get('toverse', 0)
        self.to_verse = self.verse_number if self.to_verse < self.verse_number else self.to_verse

        if self.to_verse > 0 and self.verse_number > 0:
            v = Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number) & Q(number__gte=self.verse_number) & Q(number__lte=self.to_verse)
        elif self.verse_number > 0:
            v = Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number) & Q(number=self.verse_number)
        else:
            v = Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number)

        self.object_list = self.object_list.filter(v).order_by("number", 'author')
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_authors'] = self.selected_authors

        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        dista = Verse.objects.raw('SELECT id, author_id FROM quran_verse GROUP BY author_id')
        distinct_authors = [dauthor.author.id for dauthor in dista]
        distinct_langauges = [dauthor.author.alang.id for dauthor in dista]

        data['author_info'] = Author.objects.filter(id__in=distinct_authors).order_by('name')
        data['language_info'] = Language.objects.filter(id__in=distinct_langauges).order_by('name')
        return data


