from rest_framework import generics
from app01.models import Department
from app01.serializers import MyModelSerializer
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.utils.Pagination import Pagination


class MyModelList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs):
        depart_union = models.Department.objects.all()
        pagination = Pagination(request, depart_union)
        return render(request, 'depart_list.html',
                      {"depart_union": pagination.number_list, "page_list": pagination.page_list})

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')

