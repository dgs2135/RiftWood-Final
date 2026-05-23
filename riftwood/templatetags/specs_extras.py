from django import template

register = template.Library()

@register.filter
def split_specs(value, delimiter=';'):
    return [s.strip() for s in value.split(delimiter) if s.strip()]