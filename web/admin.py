from django.contrib import admin
from web.models import Plot,Crop,Tool

# Register your models here.

class PlotAdmin(admin.ModelAdmin):
    list_display = ('DateTime','Location','Farm','Plot','Plants')

admin.site.register(Plot, PlotAdmin)


class CropAdmin(admin.ModelAdmin):
    list_display = ('DateTime','Location','Crop_Id','Crop_Type','Crop_variaty','Crop_name','ExYielPHec','Plant_hei', 'CropPeriod')

admin.site.register(Crop, CropAdmin)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('Tool_Id','Tool_Name','ToolRate','Phone_no')

admin.site.register(Tool, ToolAdmin)