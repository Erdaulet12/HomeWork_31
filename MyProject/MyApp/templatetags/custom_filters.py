from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def to_uppercase(value):
    return value.upper() if isinstance(value, str) else value


@register.filter
def round_value(value):
    try:
        return round(float(value))
    except (ValueError, TypeError):
        return value


@register.simple_tag
def create_list(*args):
    return mark_safe('<ul>' + ''.join(f'<li>{arg}</li>' for arg in args) + '</ul>')


@register.inclusion_tag('current_date.html')
def show_current_date():
    from datetime import datetime
    return {'current_date': datetime.now()}
