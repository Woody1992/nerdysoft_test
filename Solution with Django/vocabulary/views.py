from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View
from django.db.utils import IntegrityError
from .models import Word


class HonePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

    def post(self, request):
        search = request.POST['searchText']
        words = Word.objects.filter(name__contains=search).order_by('name')
        context = {
            'words': words,
            'search': search if len(words) > 0 else f'No words found for {search}'
        }
        return render(request, 'base.html', context)


class AddWordView(View):
    def post(self, request):
        word = request.POST['addWord'].lower().capitalize()
        try:
            Word.objects.create(name=word)
            messages.success(request, f'Word {word} has been added!')
        except IntegrityError:
            messages.error(request, f'Word {word} already in vocabulary')
        return render(request, 'base.html')


class DeleteWordView(View):
    def post(self, request):
        word = request.POST['deleteWord'].lower().capitalize()
        try:
            Word.objects.get(name=word).delete()
            messages.success(request, f'Word {word} has been deleted!')
        except ObjectDoesNotExist:
            messages.error(request, f'Word {word} doesnt exist')
        return render(request, 'base.html')
