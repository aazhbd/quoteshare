from quran.models import *


def chapter_processor(request):
    return {'chapters': Chapter.objects.all()}


def menu_processor(request):
    info = {}
    distincts = Verse.objects.values('author').distinct()
    info['author_info'] = Author.objects.filter(id__in=list(distincts.values_list('author', flat=True))).order_by('name')
    info['language_info'] = Language.objects.filter(id__in=list(info['author_info'].values_list('alang', flat=True))).order_by('name')
    return info
