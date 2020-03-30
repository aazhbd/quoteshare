from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from quran import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    # path('', TemplateView.as_view(template_name='main.html')),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('accounts/', include('allauth.urls')),
]
