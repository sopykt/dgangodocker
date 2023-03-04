from django import template
from datetime import date

register = template.Library()

@register.filter
def age(birthdate):
    today = date.today()
    age_in_days = (today - birthdate).days
    age_in_months = int(age_in_days / 30.436875)
    years, months = divmod(age_in_months, 12)
    # days = today.day - birthdate.day
    if years == 0 and months != 0:
        return f"{months} m"
    elif years == 0 and months == 0:
        return f"{age_in_days} days"
    else:
        return f"{years} yrs, {months} m"
