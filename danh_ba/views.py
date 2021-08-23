from django.shortcuts import render

# Create your views here.
from danh_ba.models import DanhBa, CanBo


def home(request):
    danhba = DanhBa.objects.all()
    context = {'danh_ba': danhba}
    return render(request, 'trang_chu.html', context)


def detail_danhba(request, id):
    can_bo = CanBo.objects.filter(danh_ba_id=id)
    context = {'can_bo': can_bo, 'danh_ba': can_bo.last().danh_ba.ten}
    return render(request, 'danh_ba.html', context)
