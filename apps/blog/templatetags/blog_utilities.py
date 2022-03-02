from atexit import register
from django import template

register = template.Library()


@register.filter()
def to_int(value) -> int:
    """convert value to int"""
    return int(value)
