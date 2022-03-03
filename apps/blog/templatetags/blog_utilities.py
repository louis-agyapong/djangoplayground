from django import template

register = template.Library()


@register.filter(name="to_int")
def to_int(value) -> int:
    return int(value)
