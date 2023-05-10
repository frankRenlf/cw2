"""EmployeeManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from app01 import viewsHome
from app01.views import depart, user, pretty, admin, account, task, order, chart, upload, flight
from app01.rest_frame import MyModelList
from app01.views.flight import FlightList, FlightData
from app01.views.order import OrderList, OrderData
urlpatterns = [
    # path('admin/', admin.site.urls),
    # home
    path('', viewsHome.home),
    # depart
    path('depart/list', depart.depart_list),
    path('depart/add', depart.depart_add),
    path('depart/delete', depart.depart_delete),
    path('depart/<int:did>/edit', depart.depart_edit),
    path('knowledge', MyModelList.MyModelList.as_view()),
    # user
    path('user/list', user.user_list),
    path('user/add', user.user_add),
    path('user/modelForm/add', user.user_modelform_add),
    path('user/delete', user.user_delete),
    path('user/<int:uid>/edit', user.user_modelform_edit),
    path('user/upload', user.user_upload),
    # pretty
    path('pretty/list', pretty.pretty_list),
    path('pretty/add', pretty.pretty_add),
    path('pretty/<int:pid>/delete', pretty.pretty_delete),
    path('pretty/<int:pid>/edit', pretty.pretty_edit),
    # admin
    path('admin/list', admin.admin_list),
    path('admin/add', admin.admin_add),
    path('admin/<int:aid>/edit', admin.admin_edit),
    path('admin/<int:aid>/delete', admin.admin_delete),
    path('admin/<int:aid>/reset', admin.admin_reset),
    # account
    path('login', account.login),
    path('logout', account.logout),
    # code picture
    path('image/code', account.img_code),
    # task
    path('task/ajax', task.task_ajax),
    path('task/list', task.task_list),

    # chart
    path('chart/list', chart.chart_list),
    path('chart/bar', chart.chart_bar),
    path('chart/pie', chart.chart_pie),
    path('chart/line', chart.chart_line),
    # upload
    path('upload/list', upload.upload_list),
    path('upload/form', upload.upload_form),

    # flight
    # path('flight/list', flight.flight_list),
    # path('flight/modelForm/add', flight.flight_modelform_add),
    # path('flight/<int:fid>/delete', flight.flight_delete),
    # path('flight/<int:fid>/edit', flight.flight_modelform_edit),
    path('flight/', FlightList.as_view()),
    path('flight_data/', FlightData.as_view()),

    # order
    # path('order/list', order.order_list),
    # path('order/add', order.order_add),
    # path('order/delete', order.order_delete),
    path('order/<int:oid>/edit', order.order_edit),
    # path('order/edit/<int:oid>', order.order_edit_save),

    path('order/', OrderList.as_view()),
    # new app knowledge

]
