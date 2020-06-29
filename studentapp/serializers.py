from rest_framework import serializers


from drf_day1 import settings

#序列化器
from studentapp.models import Student


class StudentSerializer(serializers.Serializer):
    stu_name = serializers.CharField()
    stu_age = serializers.IntegerField()
    # gender = serializers.IntegerField()
    # stu_img = serializers.ImageField()
    #对相关字段进行自定义处理
    gender = serializers.SerializerMethodField()
    def get_gender(self,obj):
        return obj.get_gender_display()

    stu_img = serializers.SerializerMethodField()
    def get_stu_img(self,obj):
        return "%s%s%s" %("http://127.0.0.1:8000",settings.MEDIA_URL,obj.stu_img)

#反序列化器
class StudentDeSerializer(serializers.Serializer):
    stu_name = serializers.CharField(
        max_length=6,
        min_length=2,
    )
    stu_age = serializers.IntegerField()
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

