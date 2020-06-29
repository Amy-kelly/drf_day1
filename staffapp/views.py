from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from staffapp.models import Employee
from .serializers import EmployeeSerializer,EmployeeDeSerializer


class EmployeeAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        #传id查询单个，不传查所有，否则提示错误信息
        if user_id:
            emp_obj = Employee.objects.filter(pk=user_id).first()
            emp_ser = EmployeeSerializer(emp_obj).data
            return Response({
                "status":200,
                "message":"查询单个员工信息",
                "results":emp_ser
            })
        else:
            emp_list = Employee.objects.all()
            emp_list_ser = EmployeeSerializer(emp_list,many=True).data
            return Response({
                "status": 200,
                "message": "查询所有员工信息",
                "results": emp_list_ser
            })

    def post(self,request,*args,**kwargs):
        user_data = request.data
        #入库前对数据判断
        if not isinstance(user_data,dict) or user_data == {}:
            return Response({
                "status":404,
                "message":"数据不符合要求哦~",
            })
        emp_ser = EmployeeDeSerializer(data=user_data)
        if emp_ser.is_valid():
            emp_obj = emp_ser.save()
            return Response({
                "status":200,
                "message":"添加用户成功",
                "results":EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status":500,
                "message":"添加用户失败",
                "results":emp_ser.errors
            })
