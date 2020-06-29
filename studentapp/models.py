from django.db import models

# Create your models here.
class Student(models.Model):
    gender_choices = (
        (0,"女"),
        (1,"男"),
        (2,"未知"),
    )
    stu_name = models.CharField(max_length=32)
    stu_age = models.IntegerField()
    gender = models.SmallIntegerField(choices=gender_choices,default=1)
    stu_img = models.ImageField(upload_to="pic",default="pic/1.jpg")
    class Meta:
        db_table = "drf_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stu_name