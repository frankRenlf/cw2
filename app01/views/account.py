from django.shortcuts import render, redirect, HttpResponse

from io import BytesIO

from app01 import models
from app01.modelForms.LoginModelForm import LoginModelForm
from app01.utils.generatePillow import check_code


def login(request):
    if request.method == "GET":
        form = LoginModelForm()
        return render(request, 'login.html', {"form": form})
    admin = models.Admin.objects.filter(name=request.POST.get("name")).first()
    form = LoginModelForm(data=request.POST, instance=admin)
    if form.is_valid():
        code = request.session.get("img_code")
        if code != form.cleaned_data.pop("code"):
            form.add_error("code", "invalid code")
            return render(request, 'login.html', {"form": form})
        request.session.clear()
        request.session["info"] = {"id": admin.id, "name": admin.name}
        request.session.set_expiry(60 * 60 * 24)
        return redirect('/admin/list')
    return render(request, 'login.html', {"form": form})


def logout(request):
    request.session.clear()
    return redirect('/login')


def img_code(request):
    img, code_str = check_code()

    request.session['img_code'] = code_str
    request.session.set_expiry(60)
    stream = BytesIO()

    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
