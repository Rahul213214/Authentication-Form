from django.db import models

# Create your models here.
class Plot(models.Model):
    DateTime =models.DateTimeField(auto_now_add=True)
    
    Location =models.CharField(max_length=50)
    Farm =models.CharField(max_length=50)
    Plot =models.CharField(max_length=50)
    Plants =models.CharField(max_length=50)


class Crop(models.Model):
    DateTime =models.DateTimeField(auto_now_add=True)
    
    Location =models.CharField(max_length=50)
    Crop_Id =models.CharField(max_length=50)
    Crop_Type =models.CharField(max_length=50)
    Crop_variaty =models.CharField(max_length=50)
    Crop_name =models.CharField(max_length=50)
    ExYielPHec =models.CharField(max_length=50)
    Plant_hei =models.CharField(max_length=50)
    CropPeriod =models.CharField(max_length=50)

    

class Tool(models.Model):
    Tool_Id =models.CharField(max_length=50)
    Tool_Name =models.CharField(max_length=50)
    ToolRate =models.CharField(max_length=50)
    Phone_no =models.CharField(max_length=50)



