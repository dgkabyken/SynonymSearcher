from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import DocumentForm


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_webform:model_form_upload'))
    else:
        form = DocumentForm()
    return render(request, 'main_webform/model_form_upload.html', {
        'form': form
    })

def read_file(request):
    f = open('media/media/README.txt', 'r')
    file_contents = f.read()
    f.close()
    return render(request, "main_webform/text.html", {
        'file_contents': file_contents
    })


