import json

from web_serve import models
from django.http import JsonResponse
from django.core import serializers


# def get_local(request):
#     if request.method == "GET":
#         local_list = models.Detail.objects.filter(kind_id=2)
#         data = json.loads(serializers.serialize("json", local_list))
#         return JsonResponse({'status': True, 'local': data})
#
#     return JsonResponse({'status': False})
