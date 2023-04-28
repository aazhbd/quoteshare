from quran.models import *


def chapter_processor(request):
    return {'chapters': Chapter.objects.all()}


def menu_processor(request):
    info = {}
    #distincts = Verse.objects.values('author').distinct()
    # distinct_authors = [5, 8, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    #                     38, 39, 41, 42, 43, 44, 45, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65,
    #                     66, 67, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]
    #.filter(id__in=distinct_authors).order_by('name')
    # distinct authors 31.12.2021
    info['author_info'] = Author.objects.order_by('name')
    info['language_info'] = Language.objects.filter(id__in=list(info['author_info'].values_list('alang', flat=True))).order_by('name')
    return info
