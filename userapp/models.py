from django.db import models

# Create your models here.
class User(models.Model):
    sex_choice = (
        (0,"female"),
        (1,"male"),
        (2,"unknown"),
    )
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    sex = models.SmallIntegerField(choices=sex_choice,default=1)

    class Meta:
        db_table = "drf_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username