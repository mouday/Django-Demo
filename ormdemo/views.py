from django.shortcuts import render

# Create your views here.
from django.views import View

from ormdemo.models import AddressInfo, Course, GroupConcat
from django.http import JsonResponse, HttpResponse


class Index(View):
    def get(self, request):
        print(Course.objects.values("teacher").annotate(
            title=GroupConcat(
                "title",
                distinct=True,
                ordering="title ASC",
                separator="-")).query)
        Course.objects.raw()
        return HttpResponse("hi")


class AddressAPI(View):
    """
    http://127.0.0.1:8000/ormdemo/address/0
    """

    def get(self, request, address_id=0):
        if int(address_id) == 0:  # 为0表示查询省
            address_list = AddressInfo.objects.filter(pid__isnull=True).values("id", "address")

        else:  # 查询市
            address_list = AddressInfo.objects.filter(pid_id=int(address_id)).values("id", "address")
        return JsonResponse(list(address_list), safe=False)
