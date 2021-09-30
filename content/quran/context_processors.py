from quran.models import *

def chapter_processor(request):
    data = {}
    data['chapters'] = Chapter.objects.all()
    return data


def menu_processor(request):
    data = {}
    distincts = Verse.objects.values('author').distinct()
    distinct_langauges = [dauthor.author.alang.id for dauthor in distincts]

    data['author_info'] = Author.objects.filter(id__in=[dauthor.author.id for dauthor in distincts]).order_by('name')
    data['language_info'] = Language.objects.filter(id__in=distinct_langauges).order_by('name')
    return data


