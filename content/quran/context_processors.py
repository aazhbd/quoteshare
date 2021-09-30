from quran.models import *


def chapter_processor(request):
    return {'chapters': Chapter.objects.all()}


def menu_processor(request):
    data = {}
    distincts = Verse.objects.values('author').distinct()
    data['author_info'] = Author.objects.filter(id__in=[dauthor.author.id for dauthor in distincts]).order_by('name')
    data['language_info'] = Language.objects.filter(id__in=[dauthor.author.alang.id for dauthor in distincts]).order_by('name')
    return data
