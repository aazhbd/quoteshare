from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import *

class LanguageAdmin(ModelAdmin):
    model = Language
    menu_label = 'Language'
    menu_icon = 'snippet'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'iso_code')
    list_filter = ('name',)
    search_fields = ('name')

class AuthorAdmin(ModelAdmin):
    model = Author
    menu_label = 'Author'
    menu_icon = 'view'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'alang')
    list_filter = ('name',)
    search_fields = ('name')

class ChapterAdmin(ModelAdmin):
    model = Chapter
    menu_label = 'Chapter'
    menu_icon = 'doc-full'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('number', 'english_name')
    list_filter = ('number',)
    search_fields = ('number', 'english_name')

class VerseAdmin(ModelAdmin):
    model = Verse
    menu_label = 'Verse'
    menu_icon = 'doc-full'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('number', 'vlang')
    list_filter = ('number',)
    search_fields = ('number', 'vtext')


modeladmin_register(LanguageAdmin)

modeladmin_register(AuthorAdmin)

modeladmin_register(ChapterAdmin)

modeladmin_register(VerseAdmin)

