from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import DocumentForm
from . import functions


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['text']
            word = form.cleaned_data['word_to_search']

            if subject == '':
                file = functions.read_file(form.cleaned_data['document'])

                return render(request, 'main_webform/text.html', {'subject': file,
                                                                  'word': word
                                                                  })
            else:
                return render(request, 'main_webform/text.html', {'subject': subject,
                                                                  'word': word
                                                                  })
            #return HttpResponseRedirect(reverse('main_webform:model_form_upload'))

    else:
        form = DocumentForm()
    context = {'form': form}

    return render(request, 'main_webform/model_form_upload.html', context)


def test_model_form(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('main_webform:test_model_form')
    else:
        form = DocumentForm()
    text = form
    #text = 'Привет Молдир. Че не степ?'
    context = {'form': form,
               'result': text}

    return render(request, 'main_webform/test_model_form.html', context)
