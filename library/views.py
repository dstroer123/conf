from django.shortcuts import render, redirect

from .models import Author
from .forms import BookFormSet


def create_author(request):
    author = Author()

    if request.method == 'POST':
        author.name = request.POST.get('name')

        formset = BookFormSet(request.POST, instance=author)

        if author.name and formset.is_valid():
            author.save()
            formset.instance = author
            formset.save()

            return redirect('/')

    else:
        formset = BookFormSet(instance=author)

    return render(
        request,
        'library/index.html',
        {'formset': formset}
    )