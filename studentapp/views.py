from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from studentapp.models import Student
from .serializers import StudentSerializer,StudentDeSerializer

class StudentAPIView(APIView):
    def get(self,request,*args,**kwargs):
        stu_id = kwargs.get("pk")
        if stu_id:
            stu_obj = Student.objects.filter(pk=stu_id).first()
            stu_ser = StudentSerializer(stu_obj).data
            return Response({
                "status":200,
                "message":"查询单个学生信息",
                "results":stu_ser
            })
        else:
            stu_list = Student.objects.all()
            stu_list_ser = StudentSerializer(stu_list,many=True).data
            return Response({
                "status": 200,
                "message": "查询所有学生信息",
                "results": stu_list_ser
            })

    def post(self,request,*args,**kwargs):
        stu_data = request.data
        if not isinstance(stu_data,dict) or stu_data == {}:
            return Response({
                "status":404,
                "msg":"数据信息不正确",
            })
        stu_obj = StudentDeSerializer(data=stu_data)
        if stu_obj.is_valid():
            stu = stu_obj.save()
            return Response({
                "status": 200,
                "msg": "添加成功",
                "results":StudentSerializer(stu).data
            })
        else:
            return Response({
                "status": 500,
                "msg": "添加失败",
                "results": stu_obj.errors
            })