import json
import random

from django.shortcuts import render, redirect
from rest_framework import generics

from app01 import models
from app01.models import Order
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime


def order_list(request):
    form = OrderModelForm()
    # return render(request, "order_list.html", {"form": form})
    search_txt = request.GET.get("flight_id")
    page_size = 3
    data_dict = {}
    search = "flight"
    if search_txt:
        data_dict[search + "__contains"] = search_txt
    if search_txt is None or search_txt is '':
        data_list = models.Order.objects.filter().order_by("-id")
    else:
        data_list = models.Order.objects.filter(flight_id=int(search_txt, base=10)).order_by("-id")

    sub = 2
    pagination = Pagination(request, data_list, search, page_size, "index", sub)
    print(pagination.number_list[0].__dict__)
    return render(request, 'order_list.html',
                  {"number_list": pagination.number_list, "page_list": pagination.page_list,
                   "search": "" if pagination.search_query is None else pagination.search_query,
                   "form": form})


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.admin_id = request.session.get("info")["id"]
        form.instance.number = datetime.now().strftime("%Y%m%d%H%S") + "_" + str(
            random.randint(1000, 9999))
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    oid = request.GET.get("oid")
    exist = models.Order.objects.filter(id=oid).exists()
    if not exist:
        return JsonResponse({"status": False, "error": "not found"})
    models.Order.objects.filter(id=oid).first().delete()
    return JsonResponse({"status": True})


def order_edit(request, oid):
    order = models.Order.objects.filter(id=oid).values("id", "flight_id", "passenger_id", "price", "create_time",
                                                       "status").first()
    if not order:
        return JsonResponse({"status": False, "error": "not found"})
    return JsonResponse({"status": True, "data": order})


@csrf_exempt
def order_edit_save(request, oid):
    order = models.Order.objects.filter(id=oid).first()
    if not order:
        return JsonResponse({"status": False, "error": "not found"})
    form = OrderModelForm(data=request.POST, instance=order)
    if form.is_valid():
        form.instance.admin_id = request.session.get("info")["id"]
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


class OrderEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Order):
            return {"order_id": obj.id,
                    "number": obj.number,
                    "flight_id": obj.flight_id,
                    "passenger_id": obj.passenger_id,
                    "price": obj.price,
                    "create_time": obj.create_time.isoformat(),
                    "status": obj.status,
                    "payment_platform": obj.payment_platform_id}
        return super().default(obj)


class OrderData(generics.RetrieveUpdateDestroyAPIView):
    @csrf_exempt  # add
    def get(self, request, *args, **kwargs):
        flight_union = models.Flight.objects.all()
        pagination = Pagination(request, flight_union)
        data = {'flight_union': pagination.number_list, "page_list": pagination.page_list}
        fu = {}
        i = 0
        print("get")
        for d in list(flight_union):
            fu[i] = json.dumps(d, cls=OrderEncoder)
            i += 1
        return JsonResponse({'flight_union': fu})


class OrderList(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request, *args, **kwargs):
        form = OrderModelForm()
        # return render(request, "order_list.html", {"form": form})
        search_txt = request.GET.get("flight_id")
        page_size = 3
        data_dict = {}
        search = "flight"
        if search_txt:
            data_dict[search + "__contains"] = search_txt
        if search_txt is None or search_txt is '':
            data_list = models.Order.objects.filter().order_by("-id")
        else:
            data_list = models.Order.objects.filter(flight_id=int(search_txt, base=10)).order_by("-id")

        sub = 2
        pagination = Pagination(request, data_list, search, page_size, "index", sub)
        print(pagination.number_list[0].__dict__)
        return render(request, 'order_list.html',
                      {"number_list": pagination.number_list, "page_list": pagination.page_list,
                       "search": "" if pagination.search_query is None else pagination.search_query,
                       "form": form})

    # edit
    def post(self, request, *args, **kwargs):
        form = OrderModelForm(data=request.POST)
        if form.is_valid():
            form.instance.admin_id = request.session.get("info")["id"]
            form.instance.number = datetime.now().strftime("%Y%m%d%H%S") + "_" + str(
                random.randint(1000, 9999))
            form.save()
            return JsonResponse({"status": True})
        return JsonResponse({"status": False, "error": form.errors})

    def patch(self, request, *args, **kwargs):
        oid = request.GET.get('oid')
        order = models.Order.objects.filter(id=oid).first()
        if not order:
            return JsonResponse({"status": False, "error": "not found"})
        form = OrderModelForm(data=request.POST, instance=order)
        if form.is_valid():
            form.instance.admin_id = request.session.get("info")["id"]
            form.save()
            return JsonResponse({"status": True})
        return JsonResponse({"status": False, "error": form.errors})

    def delete(self, request, *args, **kwargs):
        oid = request.GET.get("oid")
        exist = models.Order.objects.filter(id=oid).exists()
        if not exist:
            return JsonResponse({"status": False, "error": "not found"})
        models.Order.objects.filter(id=oid).first().delete()
        return JsonResponse({"status": True})
