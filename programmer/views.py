from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from .models import Programmer, Language
from .forms import LanguageForm


# Create your views here.

# def index(request, programmer_id):
#     """
#     programmer = Programmer.objects.get(pk=programmer_id)
#
#     languageFormset = modelformset_factory(Language, fields=('name',))
#     if request.POST == 'POST':
#         formset = languageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer_id))
#         if formset.is_valid():
#             instances = formset.save(commit=False)
#             for instance in instances:
#                 instance.programmer_id = programmer.id
#                 instance.save()
#
#             return redirect('index', programmer_id=programmer.id)
#         else:
#             raise ValueError
#     formset = languageFormset(queryset=Language.objects.filter(programmer__id=programmer_id))
#     return render(request, 'index.html', {'formset': formset})
#     """
#     programmer = Programmer.objects.get(pk=programmer_id)
#     # LanguageFormset = modelformset_factory(Language, fields=('name',))
#     LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name', 'image',))
#
#     if request.method == 'POST':
#         # formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
#         formset = LanguageFormset(request.POST, request.FILES, instance=programmer)
#         if formset.is_valid():
#             formset.save()
#             # instances = formset.save(commit=False)
#             # for instance in instances:
#             #    instance.programmer_id = programmer.id
#             #    instance.save()
#
#             return redirect('index', programmer_id=programmer.id)
#         else:
#             raise Exception
#     # formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
#     formset = LanguageFormset()
#
#     return render(request, 'index.html', {'formset': formset})


def create(request):
    programmer = Programmer.objects.all()
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name', 'image',))

    if request.method == 'POST':
        form = LanguageForm(request.POST)
        # formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = LanguageFormset(request.POST, request.FILES)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save(commit=False)
            formset.programmer = form
            formset.save()
        else:
            raise Exception
    else:
        form = LanguageForm()
        formset = LanguageFormset()
        return render(request, 'index.html', {'formset': formset, 'form':form})



def about(request):
    language = Language.objects.all()
    return render(request, 'detail.html', {'formset': language})
