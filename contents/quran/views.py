from django.shortcuts import render
from django.db.models import Q, Count, Min, Max, Sum
from quran.models import *
from django.core.paginator import Paginator
from django.views import generic

from django.views.generic import TemplateView
from wagtail.models import Site


class ChapterView(generic.ListView):
    model = Verse
    context_object_name = 'translations'
    template_name = "chapter.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.chapter_number = kwargs.get('chapter', 1)

        original_text = Author.objects.filter(name='Original Text')
        self.author_ids = [original_text[0].id]
        authors = request.GET.get("t", None)
        if authors:
            author_ids = authors.split(',')
            self.author_ids = self.author_ids + author_ids
            self.selected_authors = Author.objects.filter(pk__in=self.author_ids)
        else:
            self.selected_authors = Author.objects.filter(pk=original_text[0].id)

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

        return data


class SearchView(generic.ListView):
    model = Verse
    template_name = 'search.html'
    context_object_name = 'results'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        search_key = request.GET.get("q", "**")
        search_lang = request.GET.get("lang", None)

        v = Q(vtext__icontains=search_key)
        if search_lang:
            v &= Q(vlang__iso_code=search_lang)
        self.object_list = self.object_list.filter(v)
        data = self.get_context_data()
        data['result_count'] = self.object_list.count()
        data['result_keyword'] = search_key if search_key != "**" else "empty"
        data['result_lang'] = search_lang
        return self.render_to_response(data)


class CrawlerView(TemplateView):
    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context


