from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

#函数视图
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User


@csrf_exempt
def user(request):
    if request.method == 'GET':
        print("GET 查询操作")
        return HttpResponse("GET SUCCESS")
    elif request.method == 'POST':
        print("POST 添加操作")
        return HttpResponse("POST SUCCESS")
    elif request.method == 'PUT':
        print("PUT 修改操作")
        return HttpResponse("PUT SUCCESS")
    elif request.method == 'DELETE':
        print("DELETE 删除操作")
        return HttpResponse("DELETE SUCCESS")

#类视图
@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            user_val = User.objects.filter(pk = user_id).values("username","password","sex").first()
            if user_val:
                return JsonResponse({
                    "status":200,
                    "message":"单个用户查询成功",
                    "results":user_val
                })
        else:
            user_list = User.objects.all().values("username","password","sex")
            if user_list:
                return JsonResponse({
                    "status":200,
                    "message":"所有用户查询成功",
                    "results":list(user_list)
                })
        return JsonResponse({
            "status":500,
            "message":"用户信息查询失败"
        })

    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        sex = request.POST.get("sex")
        try:
            user_obj = User.objects.create(username=username,password=pwd,sex=sex)
            return JsonResponse({
                "status":200,
                "message":"添加用户成功",
                "results":{"username":user_obj.username,
                           "password":user_obj.password,
                           "sex":user_obj.sex}
            })
        except:
            return JsonResponse({
                "status":500,
                "message":"添加用户失败"
            })


    def put(self,request,*args,**kwargs):
        print("PUT 修改操作")
        return HttpResponse("PUT SUCCESS")
    def delete(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            User.objects.filter(pk=user_id).first().delete()
            return JsonResponse({
                "status":200,
                "message":"删除用户成功"
            })
        return JsonResponse({
            "status": 500,
            "message": "删除用户失败"
        })

#drf类视图
class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            user_val = User.objects.filter(pk = user_id).values("username","password","sex").first()
            if user_val:
                return Response({
                    "status":200,
                    "message":"查询单个成功",
                    "results":user_val
                })
        else:
            user_list = User.objects.all().values("username","password","sex")
            if user_list:
                return Response({
                    "status":200,
                    "message":"查询所有成功",
                    "results":list(user_list)
                })
        return Response({
            "status": 500,
            "message": "查询失败",
        })

    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        sex = request.POST.get("sex")
        try:
            user_obj = User.objects.create(username=username,password=password,sex=sex)
            if user_obj:
                return Response({
                    "status":200,
                    "message":"drf添加用户成功",
                    "results":{
                        "username":user_obj.username,
                        "password":user_obj.password,
                        "sex":user_obj.sex
                    }
                })
        except:
            return Response({
                "status":500,
                "message":"drf添加用户失败"
            })

    def put(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            user_obj = User.objects.filter(pk=user_id).first()
            print(user_obj)

    def delete(self,request,*args,**kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            User.objects.filter(pk=user_id).first().delete()
            return Response({
                "status": 200,
                "message": "删除用户成功"
            })
        return Response({
            "status": 500,
            "message": "删除用户失败"
        })
