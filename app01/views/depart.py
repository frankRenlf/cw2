from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from rest_framework.views import APIView

""" create depart operations """


def depart_list(request):
    depart_union = models.Department.objects.all()
    pagination = Pagination(request, depart_union)
    return render(request, 'depart_list.html',
                  {"depart_union": pagination.number_list, "page_list": pagination.page_list})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')

    depart_title = request.POST.get("title")
    models.Department.objects.create(title=depart_title)
    return redirect('/depart/list')


def depart_delete(request):
    # print(request.method)
    depart_id = request.GET.get("id")
    models.Department.objects.filter(id=depart_id).delete()
    return redirect('/depart/list')


def depart_edit(request, did):
    if request.method == "GET":
        title = models.Department.objects.filter(id=did).all()[0].title
        return render(request, 'depart_edit.html', {"title": title})
    title = request.POST.get("title")
    models.Department.objects.filter(id=did).update(title=title)
    return redirect('/depart/list')



