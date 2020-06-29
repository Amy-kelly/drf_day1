from rest_framework import serializers


from drf_day1 import settings

#序列化器
from staffapp.models import Employee


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    #自定义字段
    #处理数据库中不存在的自定义字段
    salt = serializers.SerializerMethodField()
    def get_salt(self,obj):
        print(self) #QuerySet 参与序列化的模型
        print("*******")
        print(obj) #model对象
        return "salt" #所有均返回salt

    #对数据库中已存在的字段自定义处理
    #修改性别以0 1呈现的方式
    gender = serializers.SerializerMethodField()
    def get_gender(self,obj):
        # if obj.gender == 0:
        #     return "女"
        # elif obj.gender == 1:
        #     return "男"
        # else:
        #     return "未知"
        # return ("男" if (obj.gender == 1) else "女")
        return obj.get_gender_display()

    #自定义图片信息使其显示完整的路径
    pic = serializers.SerializerMethodField()
    def get_pic(self,obj):
        return "%s%s%s" % ("http://127.0.0.1:8000",settings.MEDIA_URL,str(obj.pic))

#反序列化器
class EmployeeDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=8,
        min_length=2,
        error_messages={
            "max_length":"用户名超过最大限度",
            "min_length":"用户名低于最小限度"
        }
    )
    password = serializers.CharField(required=True)
    phone = serializers.CharField()
    #重写create方法完成新增
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)