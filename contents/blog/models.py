from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from wagtailmetadata.models import MetadataPageMixin

from quran.models import Chapter


class BlogIndexPage(MetadataPageMixin, Page):
    sub_title = models.CharField(max_length=600, blank=True)
    body = MarkdownField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='blog_index_image')

    content_panels = Page.content_panels + [
        FieldPanel("sub_title", classname="blog index title"),
        MarkdownPanel("body"),
        FieldPanel('image', classname="blog index image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('sub_title'),
        index.SearchField('body'),
    ]


class BlogPage(MetadataPageMixin, Page):
    sub_title = models.CharField(max_length=600, blank=True)
    body = MarkdownField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='blog_image')

    content_panels = Page.content_panels + [
        FieldPanel("sub_title", classname="blog title"),
        MarkdownPanel("body"),
        FieldPanel('image', classname="blog image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('sub_title'),
        index.SearchField('body'),
    ]

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        context['recommended'] = BlogPage.objects.live().exclude(id=self.id).order_by('?')[:5]
        context['surah'] = Chapter.objects.order_by('?')[:10]
        return context
