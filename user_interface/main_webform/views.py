from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DocumentForm
from .functions import read_file
from .functions import get_syn_pos
from django.urls import reverse

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['text']
            word = form.cleaned_data['word_to_search']

            if subject == '':
                try:
                    file = read_file(form.cleaned_data['document'])
                    result = get_syn_pos(word, file)
                    return render(request, 'main_webform/text.html', {'result': result,
                                                                      'word': word
                                                                      })
                except:
                    return HttpResponseRedirect(reverse('main_webform:model_form_upload'))

            else:
                result = get_syn_pos(word, subject)
                return render(request, 'main_webform/text.html', {'result': result,
                                                                  'word': word
                                                                  })


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
    context = {'form': form,
               'result': text}

    return render(request, 'main_webform/test_model_form.html', context)
