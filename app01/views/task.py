from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def task_list(request):
    return render(request, 'task_list.html')


@csrf_exempt
def task_ajax(request):
    obj1 = request.POST
    obj2 = request.GET
    print(obj1)
    print(obj2)
    return JsonResponse({"success": "1"})
