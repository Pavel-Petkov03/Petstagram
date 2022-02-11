from django import template

from Petstagram.main.models import ProfileModel

register = template.Library()


@register.simple_tag()
def is_authenticated():
    return ProfileModel.objects.exists()
