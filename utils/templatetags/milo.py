import datetime
from django.template import Library

register = Library()


@register.simple_tag
def is_age_enough(value):
    if not value:
        return value

    now = datetime.date.today()
    if now.year - value.year < 14:
        return "blocked"
    return "allowed"


@register.simple_tag
def biz_faz(value):
    if not value:
        return value

    if value % 5 == 0 and value % 3 == 0:
        return "BizzFuzz"

    if value % 5 == 0:
        return "Fuzz"

    if value % 3 == 0:
        return "Bizz"

    return value
