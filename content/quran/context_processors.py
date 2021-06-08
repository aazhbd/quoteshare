from quran.models import *

def chapter_processor(request):
    data = {}
    data['chapters'] = Chapter.objects.all()
    return data


def menu_processor(request):
    data = {}
    dista = Verse.objects.raw('SELECT id, author_id FROM quran_verse GROUP BY author_id')
    distinct_authors = [dauthor.author.id for dauthor in dista]
    distinct_langauges = [dauthor.author.alang.id for dauthor in dista]

    data['author_info'] = Author.objects.filter(id__in=distinct_authors).order_by('name')
    data['language_info'] = Language.objects.filter(id__in=distinct_langauges).order_by('name')
    return data


