import json

from web_serve import models
from django.http import JsonResponse
from django.core import serializers
# from django.shortcuts import HttpResponse


def get_banner(request):
    if request.method == "GET":
        banner_list = models.HomeBanner.objects.all().order_by('index')
        data = json.loads(serializers.serialize("json", banner_list))
        return JsonResponse({'status': True, 'banner': data})

    return JsonResponse({'status': False})


def get_category(request):
    if request.method == "GET":
        category_list = models.DetailKind.objects.all().order_by('pk')
        data = json.loads(serializers.serialize("json", category_list))
        return JsonResponse({'status': True, 'category': data})

    return JsonResponse({'status': False})


def get_rank(request):
    if request.method == "GET":
        rank_list = models.Detail.objects.all().order_by('pk')
        data = json.loads(serializers.serialize("json", rank_list))
        return JsonResponse({'status': True, 'rank': data})

    return JsonResponse({'status': False})


def get_serve(request):
    if request.method == "GET":
        serve_list = models.Detail.objects.filter(kind_id=8)
        data = json.loads(serializers.serialize("json", serve_list))
        return JsonResponse({'status': True, 'serve': data})

    return JsonResponse({'status': False})


def get_land(request):
    if request.method == "GET":
        land_list = models.Detail.objects.filter(kind_id=3)
        data = json.loads(serializers.serialize("json", land_list))
        return JsonResponse({'status': True, 'land': data})

    return JsonResponse({'status': False})


def get_local(request):
    if request.method == "GET":
        local_list = models.Detail.objects.filter(kind_id=2)
        data = json.loads(serializers.serialize("json", local_list))
        return JsonResponse({'status': True, 'local': data})

    return JsonResponse({'status': False})


def get_water(request):
    if request.method == "GET":
        water_list = models.Detail.objects.filter(kind_id=6)
        data = json.loads(serializers.serialize("json", water_list))
        return JsonResponse({'status': True, 'water': data})

    return JsonResponse({'status': False})


def get_sea(request):
    if request.method == "GET":
        sea_list = models.Detail.objects.filter(kind_id=4)
        data = json.loads(serializers.serialize("json", sea_list))
        return JsonResponse({'status': True, 'sea': data})

    return JsonResponse({'status': False})


def get_detail(request):
    if request.method == "GET":
        pk = request.GET.get('id')
        detail = models.Detail.objects.filter(pk=pk)
        # print(detail)
        user_id = detail.first().user_id_id
        user = models.UserInfo.objects.filter(pk=user_id)
        data_id = user.first().data_id_id
        personal = models.PersonalData.objects.filter(pk=data_id)
        # print(user)
        detail_data = json.loads(serializers.serialize("json", detail))
        user_data = json.loads(serializers.serialize("json", user))
        personal_data = json.loads(serializers.serialize("json", personal))
        return JsonResponse({'status': True, 'detail': detail_data, 'user': user_data, 'personalData': personal_data})
