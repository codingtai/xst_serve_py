from django.shortcuts import HttpResponse
from web_serve.forms.account import SendSmsForm, RegisterForm, LoginForm
from django.http import JsonResponse
from web_serve import models
import json
from django.core import serializers


def reg_login(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        data = form.cleaned_data
        data.pop('code')
        instance = models.UserInfo.objects.create(**data)
        print(instance)
        user_object = form.cleaned_data['mobile_phone']
        print(user_object)
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})


def send_sms(request):
    # 发送短信
    form = SendSmsForm(request, data=request.GET)
    # 校验手机号不能为空，格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phonenum = form.cleaned_data['phonenum']
            password = form.cleaned_data['password']
            user = models.UserInfo.objects.filter(mobile_phone=phonenum, password=password)
            detail = models.Detail.objects.filter(user_id_id=user.first().pk)
            if user.first():
                request.session['user_id'] = user.first().pk
            user_data = json.loads(serializers.serialize("json", user))
            detail_data = json.loads(serializers.serialize("json", detail))
            return JsonResponse({'status': True, 'user': user_data, 'detail': detail_data})

        return JsonResponse({'status': False, 'error': form.errors})


def login_out(request):
    if request.method == "GET":
        request.session.flush()
        return HttpResponse('登出成功')
