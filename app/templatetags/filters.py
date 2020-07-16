from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name="set_rows")
def set_rows(value, arg):
    return value.as_widget(attrs={'rows': arg})


@register.filter(name="add_input_attrs")
def add_input_attrs(value, args):
    print(args)
    return value.as_widget(attrs={'class': args.style_classes, 'placeholder': args.placeholder})
