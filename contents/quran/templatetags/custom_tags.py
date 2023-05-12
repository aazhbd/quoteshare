from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.filter
def simplify(value):
    import unicodedata
    return unicodedata.normalize('NFC', value).replace('\'', '').replace('`', '').replace('\n', '').rstrip()


@register.filter
def uninormal(value):
    import unicodedata
    return unicodedata.normalize('NFC', value).replace('\n', '').rstrip()

