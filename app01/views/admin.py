from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.AdminModelForm import AdminModelForm, AdminResetModelForm


def admin_list(request):
    search = "name"
    name_txt = request.GET.get(search)
    name_txt = name_txt if name_txt is not None else ''
    page_size = 3
    data_dict = {}
    if name_txt:
        data_dict[search + "__contains"] = name_txt
    data_list = models.Admin.objects.filter(**data_dict)
    sub = 2
    pagination = Pagination(request, data_list, search, page_size, "index", sub)

    return render(request, 'admin_list.html',
                  {"number_list": pagination.number_list, "page_list": pagination.page_list,
                   search: "" if pagination.search_query is None else pagination.search_query})


def admin_add(request):
    if request.method == "GET":
        admin_null = AdminModelForm()
        return render(request, 'template.html', {"form": admin_null, "title": "create admin"})
    admin_form = AdminModelForm(data=request.POST)
    if admin_form.is_valid():
        admin_form.save()
        return redirect('/admin/list')
    return render(request, 'template.html', {"form": admin_form, "title": "create admin"})


def admin_edit(request, aid):
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        return redirect('/admin/list')
    if request.method == "GET":
        admin_null = AdminModelForm(instance=admin)
        return render(request, 'template.html', {"form": admin_null, "title": "edit admin"})
    admin_form = AdminModelForm(data=request.POST, instance=admin)
    if admin_form.is_valid():
        admin_form.save()
        return redirect('/admin/list')
    return render(request, 'template.html', {"form": admin_form, "title": "edit admin"})


def admin_delete(request, aid):
    models.Admin.objects.filter(id=aid).first().delete()
    return redirect('/admin/list')


def admin_reset(request, aid):
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        return redirect('/admin/list')
    if request.method == "GET":
        admin_null = AdminResetModelForm(instance=admin)
        return render(request, 'template.html', {"form": admin_null, "title": "reset " + admin.name})
    admin_form = AdminResetModelForm(data=request.POST, instance=admin)
    if admin_form.is_valid():
        admin_form.save()
        return redirect('/admin/list')
    return render(request, 'template.html', {"form": admin_form, "title": "reset " + admin.name})
