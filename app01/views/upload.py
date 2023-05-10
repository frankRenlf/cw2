from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from app01.modelForms.UploadModelForm import UploadForm
from django.shortcuts import render, redirect, HttpResponse


def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')
    file_obj = request.FILES.get("file")
    f = open('./app01/files/' + file_obj.name, mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    return render(request, 'upload_list.html')


def upload_form(request):
    if request.method == "GET":
        form = UploadForm()
        return render(request, 'upload_form.html', {"form": form, "title": "upload"})
    form = UploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse('success')
    return render(request, 'upload_form.html', {"form": form, "title": "upload"})