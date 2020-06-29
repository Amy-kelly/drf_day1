from django.db import models

# Create your models here.
class Employee(models.Model):
    gender_choices = (
        (0,"female"),
        (1,"male"),
        (2,"unknown"),
    )
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=gender_choices,default=1)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pic = models.ImageField(upload_to="pic",default="pic/1.jpg")

    class Meta:
        db_table = "drf_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username