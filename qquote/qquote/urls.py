from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from quran import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('info', TemplateView.as_view(template_name='info.html'), name='info'),
    path('<int:chapter>/', views.ChapterView.as_view(), name='chapter'),
    path('<int:chapter>/<int:verse>/', views.VerseView.as_view(), name='verse'),
    path('<int:chapter>/<int:verse>-<int:toverse>/', views.VerseView.as_view(), name='verse'),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
]
