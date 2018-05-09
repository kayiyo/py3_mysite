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
    # list_editable = ('key', 'xpath',)

    # option = forms.ModelChoiceField(label=u'下拉框', queryset=mysql.objects.all())

admin.site.register([OrderNew, ProjectManager, ProjectExecute,
                     ExportNotice, PurchaseRequest, PurchaseOrder,
                     DeclarationNew, CheckIn, OperationIn,
                     ShipmentNotice, CheckSubmit, CheckOut,
                     OperationOut, LogisticsTrack, FinancialPayment,
                     ], OrderAdmin)


class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'process', 'description']
    search_fields = ('type',)                               # 搜索字段
    # ordering = ('id',)                                    # 排序 “-”为倒序
    list_display_links = ('id', 'process', 'description',)   # 点击该字段可编辑
    # list_editable = ('process', 'description',)

admin.site.register(ProcessType, ProcessTypeAdmin)


# class OrderTestReportAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'location', 'result', 'timestamp']
#     search_fields = ('result', 'timestamp')                                 # 搜索字段
#     # ordering = ('id',)                                                    # 排序 “-”为倒序
#     list_filter = ('result', 'timestamp')  # 过滤器
#     readonly_fields = ('id', 'title', 'location', 'result', 'timestamp')        # 点击该字段可编辑
#     date_hierarchy = 'timestamp'
#
# admin.site.register(OrderTestReport, OrderTestReportAdmin)


class OrderTestReportAdmin(admin.ModelAdmin):
    # def color_result(self, obj):
    #     if obj.result == 'Passed':
    #         return "<font color=\"red\">%s</font>" % ("通过",)
    #     elif obj.result == 'Failed':
    #         return "<font color=\"red\">%s</font>" % ("失败",)
    # color_result.short_description = '结果'
    # color_result.allow_tags = True
    list_display = ['id', 'title', 'location', 'colored_result', 'timestamp']
    search_fields = ('result', 'timestamp')                                 # 搜索字段
    # ordering = ('id',)                                                    # 排序 “-”为倒序
    list_filter = ('result', 'timestamp')  # 过滤器
    # readonly_fields = ('id', 'title', 'location', 'result', 'timestamp')        # 该字段只读
    date_hierarchy = 'timestamp'

admin.site.register(OrderTestReport, OrderTestReportAdmin)