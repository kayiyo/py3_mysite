from django.contrib import admin
from django import forms
from mysql.models import *


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'key', 'xpath', 'search_area', 'move_point']
    search_fields = ('name', 'type',)           # 搜索字段
    list_filter = ('type',)                     # 过滤器
    ordering = ('id',)                          # 排序 “-”为倒序
    list_display_links = ('name',)              # 点击该字段可编辑

    # option = forms.ModelChoiceField(label=u'下拉框', queryset=mysql.objects.all())

admin.site.register([OrderNew, ProjectManager, ProjectExecute,
                     ExportNotice, PurchaseRequest, PurchaseOrder,
                     DeclarationNew, CheckIn, OperationIn,
                     ShipmentNotice, CheckSubmit, CheckOut,
                     OperationOut, LogisticsTrack, FinancialPayment,
                     ], OrderAdmin)
