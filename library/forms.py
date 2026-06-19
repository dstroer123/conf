from django.forms import inlineformset_factory

from .models import Author, Book


BookFormSet = inlineformset_factory(
    Author,
    Book,
    fields=('title', 'pages'),
    extra=3,
    can_delete=True
)