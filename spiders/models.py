from django.db import models
# Create your models here.
from django.db import models

class NewHouse(models.Model):
    name = models.CharField("项目名称", max_length=255, blank=True)
    supervision_bank = models.CharField("资金监管银行", max_length=255, blank=True)
    supervision_acount = models.CharField("监管帐号", max_length=255, blank=True)
    project_state = models.CharField("项目状态", max_length=255, blank=True)
    address = models.CharField("项目地址", max_length=255, blank=True)
    dev_company = models.CharField("开发公司", max_length=255, blank=True)
    license_authority = models.CharField("发证机关", max_length=255, blank=True)
    sale_permit = models.CharField("预(现)售证名称", max_length=255, blank=True)
    license_key = models.CharField("预(现)售许可证号", max_length=255, blank=True)
    online_saleable_area = models.DecimalField("纳入网上可售面积", max_digits=10, decimal_places=2, blank=True, default=0)
    online_saleable_flats = models.DecimalField("纳入网上可售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    saleable_area = models.DecimalField("当前可售面积", max_digits=10, decimal_places=2, blank=True, default=0)
    saleable_flats = models.DecimalField("当前可售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    sold_area = models.DecimalField("已售面积", max_digits=10, decimal_places=2, blank=True, default=0)
    sold_flats = models.DecimalField("已售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    residential_area = models.DecimalField("当前(住宅)可售面积", max_digits=10, decimal_places=2, blank=True, default=0)
    residential_flats = models.DecimalField("当前(住宅)可售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    sold_residential_area = models.DecimalField("已售(住宅)面积", max_digits=10, decimal_places=2, blank=True, default=0)
    sold_residential_flats = models.DecimalField("已售(住宅)套数", max_digits=10, decimal_places=2, blank=True, default=0)
    reserve_area = models.DecimalField("预定面积", max_digits=10, decimal_places=2, blank=True, default=0)
    reserve_flats = models.DecimalField("预定套数", max_digits=10, decimal_places=2, blank=True, default=0)
    saleable_parking_amount = models.DecimalField("车位可售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    saleable_garage_amount = models.DecimalField("车库可售套数", max_digits=10, decimal_places=2, blank=True, default=0)
    sold_avg_price = models.DecimalField("已售(住宅)平均价", max_digits=10, decimal_places=2, blank=True, default=0)
    districts = models.CharField("所在区县", max_length=255, blank=True)
    contact_phone = models.CharField("售楼电话", max_length=255, blank=True)
    high_price = models.DecimalField("最高单价(住宅)", max_digits=10, decimal_places=2, blank=True, default=0)
    low_price = models.DecimalField("最低单价(住宅)", max_digits=10, decimal_places=2, blank=True, default=0)
    remark = models.CharField("备注", max_length=255, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        ordering = ('created',)
        db_table = 'new_house'

class ProxyIp(models.Model):
    ip = models.CharField("ip地址", max_length=50)
    port = models.CharField("端口号", max_length=10)
    speed = models.IntegerField("网速")
    proxy_type = models.CharField("代理类型", max_length=10, default='HTTP')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        ordering = ('created',)
        db_table = 'proxy_ip'


class AdministrativeCoding(models.Model):
    coding = models.CharField("行政编码", max_length=15)
    name = models.CharField("行政名称", max_length=50)
    pid = models.CharField("上级行政编码", max_length=15)
    level = models.IntegerField("行政等级")
    classification_code = models.CharField("城乡分类代码", max_length=5, default="")
    created = models.DateTimeField("创建时间",auto_now_add=True)
    class Meta:
        managed = True
        ordering = ('coding',)
        db_table = 'administrative_coding'
