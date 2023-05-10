from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.PrettyModelForm import PrettyModelForm

""" create prettyNumber operations """


def pretty_list(request):
    mobile_txt = request.GET.get("mobile")
    mobile_txt = mobile_txt if mobile_txt is not None else ''
    page_size = 3
    data_dict = {}
    search = "mobile"
    if mobile_txt:
        data_dict[search + "__contains"] = mobile_txt
    data_list = models.PrettyNumber.objects.filter(**data_dict).order_by("-level")
    print(data_dict)
    sub = 2
    pagination = Pagination(request, data_list, search, page_size, "index", sub)

    return render(request, 'pretty_list.html',
                  {"number_list": pagination.number_list, "page_list": pagination.page_list,
                   "mobile": "" if pagination.search_query is None else pagination.search_query})


def pretty_add(request):
    if request.method == "GET":
        pretty_null = PrettyModelForm()
        return render(request, 'prettyForm_add.html', {"prettyForm": pretty_null})
    pretty_form = PrettyModelForm(data=request.POST)
    if pretty_form.is_valid():
        pretty_form.save()
        return redirect('/pretty/list')
    return render(request, 'prettyForm_add.html', {"prettyForm": pretty_form})


def pretty_delete(request, pid):
    models.PrettyNumber.objects.filter(id=pid).first().delete()
    return redirect('/pretty/list')


def pretty_edit(request, pid):
    pretty = models.PrettyNumber.objects.filter(id=pid).first()
    if request.method == "GET":
        pretty_null = PrettyModelForm(instance=pretty)
        return render(request, 'prettyForm_edit.html', {"prettyForm": pretty_null})
    pretty_form = PrettyModelForm(data=request.POST, instance=pretty)
    if pretty_form.is_valid():
        pretty_form.save()
        return redirect('/pretty/list')
    return render(request, 'prettyForm_edit.html', {"prettyForm": pretty_form})
