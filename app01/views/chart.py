from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime


def chart_list(request):
    return render(request, "chat_list.html")


def chart_bar(request):
    legend = ['1', '2']
    title = "Bar"
    series = [{
        'name': '1',
        'type': 'bar',
        'data': [5, 20, 36, 10, 10, 20, 60]},
        {'name': '2',
         'type': 'bar',
         'data': [20, 60, 5, 20, 36, 10, 10]
         }]
    xAxis = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    result = {
        "status": True,
        "data": {
            "title": title,
            "legend": legend,
            "series": series,
            "xAxis": xAxis
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    title = "Pie"
    series = [{'value': 1048, 'name': 'Search Engine'},
              {'value': 735, 'name': 'Direct'},
              {'value': 580, 'name': 'Email'},
              {'value': 484, 'name': 'Union Ads'},
              {'value': 300, 'name': 'Video Ads'}]
    result = {
        "status": True,
        "data": {
            "title": title,
            "series": series,
        }
    }
    return JsonResponse(result)


def chart_line(request):
    legend = ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
    title = "Line"
    series = [
        {
            'name': 'Email',
            'type': 'line',
            'stack': 'Total',
            'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
            'name': 'Union Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [220, 182, 191, 234, 290, 330, 310]
        },
        {
            'name': 'Video Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [150, 232, 201, 154, 190, 330, 410]
        },
        {
            'name': 'Direct',
            'type': 'line',
            'stack': 'Total',
            'data': [320, 332, 301, 334, 390, 330, 320]
        },
        {
            'name': 'Search Engine',
            'type': 'line',
            'stack': 'Total',
            'data': [820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
    xAxis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    result = {
        "status": True,
        "data": {
            "title": title,
            "legend": legend,
            "series": series,
            "xAxis": xAxis
        }
    }
    return JsonResponse(result)
