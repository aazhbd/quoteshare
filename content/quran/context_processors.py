from quran.models import *


def chapter_processor(request):
    return {'chapters': Chapter.objects.all()}


def menu_processor(request):
    data = {}
    distincts = Verse.objects.values('author').distinct()
    data['author_info'] = Author.objects.filter(id__in=list(distincts.values_list('author', flat=True))).order_by('name')
    data['language_info'] = Language.objects.filter(id__in=list(data['author_info'].values_list('alang', flat=True))).order_by('name')
    return data
