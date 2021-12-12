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
    return unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode("utf-8").replace('\'', '').replace('`',
                                                                                                                   '')
