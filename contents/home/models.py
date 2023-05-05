from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField


class HomePage(Page):
    home_title = models.CharField(max_length=600, blank=True)
    body = MarkdownField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='home_image')

    content_panels = Page.content_panels + [
        FieldPanel("home_title", classname="Home title"),
        MarkdownPanel("body"),
        FieldPanel('image', classname="Home image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]
