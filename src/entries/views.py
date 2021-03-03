from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Entry


def index(request):
    entries = Entry.objects.all()
    paginator = Paginator(entries, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'entries/index.html', context)


def new_entry(request):
    return render(request, 'entries/form.html')
