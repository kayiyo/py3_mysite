from django.db import models
from django.utils.html import format_html


# Create your models here.
class OrderNew(models.Model):

    name = models.CharField(max_length=150, null=True)                   # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)                    # 类型
    xpath = models.CharField(max_length=150, null=True)                  # 定位信息
    search_area = models.CharField(max_length=150, null=True)            # 搜索区域
    move_point = models.CharField(max_length=150, null=True)             # 移动位置

    class Meta:
        verbose_name = 'OrderNew'
        verbose_name_plural = '[01]新建订单OrderNew'


class ProjectManager(models.Model):

    name = models.CharField(max_length=150, null=True)                   # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)                    # 类型
    xpath = models.CharField(max_length=150, null=True)                  # 定位信息
    search_area = models.CharField(max_length=150, null=True)            # 搜索区域
    move_point = models.CharField(max_length=150, null=True)             # 移动位置

    class Meta:
        verbose_name = 'ProjectManager'
        verbose_name_plural = '[02]项目管理ProjectManager'


class ProjectExecute(models.Model):

    name = models.CharField(max_length=150, null=True)                   # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)                    # 类型
    xpath = models.CharField(max_length=150, null=True)                  # 定位信息
    search_area = models.CharField(max_length=150, null=True)            # 搜索区域
    move_point = models.CharField(max_length=150, null=True)             # 移动位置

    class Meta:
        verbose_name = 'ProjectExecute'
        verbose_name_plural = '[03]项目执行ProjectExecute'


class ExportNotice(models.Model):

    name = models.CharField(max_length=150, null=True)                   # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)                    # 类型
    xpath = models.CharField(max_length=150, null=True)                  # 定位信息
    search_area = models.CharField(max_length=150, null=True)            # 搜索区域
    move_point = models.CharField(max_length=150, null=True)             # 移动位置

    class Meta:
        verbose_name = 'ExportNotice'
        verbose_name_plural = '[04]出口通知ExportNotice'


class PurchaseRequest(models.Model):

    name = models.CharField(max_length=150, null=True)                   # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)                    # 类型
    xpath = models.CharField(max_length=150, null=True)                  # 定位信息
    search_area = models.CharField(max_length=150, null=True)            # 搜索区域
    move_point = models.CharField(max_length=150, null=True)             # 移动位置

    class Meta:
        verbose_name = 'PurchaseRequest'
        verbose_name_plural = '[05]采购申请PurchaseRequest'


class PurchaseOrder(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'PurchaseOrder'
        verbose_name_plural = '[06]采购订单PurchaseOrder'


class DeclarationNew(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'DeclarationNew'
        verbose_name_plural = '[07]新增报检DeclarationNew'


class CheckIn(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'CheckIn'
        verbose_name_plural = '[08]入库质检CheckIn'


class OperationIn(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'OperationIn'
        verbose_name_plural = '[09]办理入库OperationIn'


class ShipmentNotice(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'ShipmentNotice'
        verbose_name_plural = '[10]看货通知ShipmentNotice'


class CheckSubmit(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'CheckSubmit'
        verbose_name_plural = '[11]提交质检CheckSubmit'


class CheckOut(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'CheckOut'
        verbose_name_plural = '[12]出库质检CheckOut'


class OperationOut(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'OperationOut'
        verbose_name_plural = '[13]办理出库OperationOut'


class LogisticsTrack(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'LogisticsTrack'
        verbose_name_plural = '[14]物流跟踪LogisticsTrack'


class FinancialPayment(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'FinancialPayment'
        verbose_name_plural = '[15]财务收款FinancialPayment'


class RegisterWeb(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'RegisterWeb'
        verbose_name_plural = '[16]门户注册RegisterWeb'


class LoginWeb(models.Model):
    name = models.CharField(max_length=150, null=True)  # 名称
    type = models.ForeignKey('ProcessType', max_length=150, null=True, on_delete=models.SET_NULL)  # 类型
    key = models.CharField(max_length=150, null=True)  # 类型
    xpath = models.CharField(max_length=150, null=True)  # 定位信息
    search_area = models.CharField(max_length=150, null=True)  # 搜索区域
    move_point = models.CharField(max_length=150, null=True)  # 移动位置

    class Meta:
        verbose_name = 'LoginWeb'
        verbose_name_plural = '[17]门户登录LoginWeb'


class ProcessType(models.Model):
    process = models.CharField(max_length=150, primary_key=True)
    description = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name = 'ProcessType'
        verbose_name_plural = '执行类型维护'

    def __str__(self):
        return self.description


class OrderTestReport(models.Model):
    RESULT_TYPE_LIST = (
        ('Failed', '失败'),
        ('Passed', '通过'),
    )
    title = models.CharField(max_length=150)      # 报告标题
    location = models.CharField(max_length=150)        # 报告地址
    result = models.CharField(max_length=150, choices=RESULT_TYPE_LIST)     # 报告结果
    timestamp = models.DateTimeField()            # 创建时间
    # color_code = models.CharField(max_length=6, default='green')
    # exclude = ('color_code',)

    def colored_result(self):
        if self.result == 'Passed':
            color_code = 'green'
            self.result = '通过'
        elif self.result == 'Failed':
            color_code = 'red'
            self.result = '失败'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.result,
        )
    colored_result.short_description = '结果'
    colored_result.allow_tags = True

    class Meta:
        verbose_name = 'OrderTestReport'
        verbose_name_plural = '测试报告'

    def __str__(self):
        return self.location
