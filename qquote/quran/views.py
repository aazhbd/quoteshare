from django.shortcuts import render
from django.db.models import Q, Count, Min, Max, Sum
from quran.models import *

from django.views import generic

class HomeView(generic.ListView):
    model = Chapter
    context_object_name = 'chapters'
    template_name = 'home.html'


class ChapterView(generic.TemplateView):
    template_name = "chapter.html"

    def get(self, request, *args, **kwagrs):
        self.chapter_number = kwagrs['chapter']
        self.author_ids = [5]
        authors = request.GET.get("t", None)
        if(authors):
            author_ids = authors.split(',')
            self.author_ids = self.author_ids + author_ids
            self.selected_authors = Author.objects.filter(pk__in=self.author_ids)
        else:
            self.selected_authors = Author.objects.filter(pk=5)

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_authors'] = self.selected_authors

        total_verses = Verse.objects.filter(Q(author__name='Original Text') & Q(chapter=self.chapter_number)).count()
        translations = []
        for verse_num in range(1, total_verses):
            translation = Verse.objects.filter(Q(author__id__in=self.author_ids) & Q(chapter=self.chapter_number) & Q(number=verse_num))
            translations.append(translation)
        data['translations'] = translations

        chapter_info = Chapter.objects.filter(number=self.chapter_number)
        for ci in chapter_info:
            data['chapter_info'] = ci

        data['author_info'] = Author.objects.all()
        data['language_info'] = Language.objects.all()
        return data




class ChapterListView(generic.ListView):
    model = Verse
    context_object_name = 'chapter'
    template_name = 'chapter.html'

    def get(self, request, *args, **kwagrs):
        self.object_list = self.get_queryset()
        author_ids = request.GET['t'].split(',')
        self.selected_authors = Author.objects.filter(pk__in=author_ids)

        self.chapter_number = kwagrs['chapter']

        v = Q(author__name='Original Text')
        for author in self.selected_authors:
            v |= Q(author__name=author.name)

        v = Q(v) & Q(chapter=self.chapter_number)

        self.object_list = self.object_list.filter(v)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_authors'] = self.selected_authors

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

