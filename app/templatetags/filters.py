from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name="set_rows")
def set_rows(value, arg):
    return value.as_widget(attrs={'rows': arg})


@register.filter(name="limit_characters")
def limit_characters(string, limit):
    if len(string) > limit:
        limit += 3
        return string[0:-3] + "..."
    else:
        return string
