from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.search import index

from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField


class BlogIndexPage(Page):
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


class BlogPage(Page):
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