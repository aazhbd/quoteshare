from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.sitemap_generator import Sitemap

from search import views as search_views

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap as django_sitemap
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page

from django.views.generic import TemplateView
from quran import views
from quran.models import Chapter, Verse

info_dict = {
    'queryset': Chapter.objects.all(),
}

sitemapset = {
    'chapters': GenericSitemap(info_dict, priority=0.8),

    'discuss': Sitemap,

    'verses': GenericSitemap({
        'queryset': Verse.objects.filter(author__name="Original Text").order_by('id'),
    }, priority=0.8),
}

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='index'),

    path(
        "sitemap.xml",
        cache_page(86400)(sitemap_views.index),
        {"sitemaps": sitemapset},
        name="django.contrib.sitemaps.views.index",
    ),

    path(
        "sitemap-<section>.xml",
        cache_page(86400)(sitemap_views.sitemap),
        {"sitemaps": sitemapset},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    # path('sitemap.xml', django_sitemap,
    #      {'sitemaps': sitemapset},
    #      name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt', views.CrawlerView.as_view()),

    path('qsearch/', views.SearchView.as_view(), name='qsearch'),

    path('<int:chapter>/', views.ChapterView.as_view(), name='chapter'),
    path('<int:chapter>/<int:verse>/', views.ChapterView.as_view(), name='verse'),
    path('<int:chapter>/<int:verse>-<int:toverse>/', views.ChapterView.as_view(), name='verse-range'),

    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
