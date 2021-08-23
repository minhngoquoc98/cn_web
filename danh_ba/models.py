from django.db import models

# Create your models here.


class Khoa(models.Model):
    ten = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'Khoa'

    def __str__(self):
        return self.ten


class BoMon(models.Model):
    ten = models.CharField(max_length=255, blank=False)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Bo_mon'

    def __str__(self):
        return self.ten


class DanhBa(models.Model):
    ten = models.CharField(max_length=255, blank=False)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'Danh_ba'

    def __str__(self):
        return self.ten


class CanBo(models.Model):
    ho_ten = models.CharField(max_length=255, blank=False)
    chuc_vu = models.CharField(max_length=200, blank=True, null=True)
    dien_thoai_co_quan = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(null=True, blank=False)
    dien_thoai_didong = models.CharField(max_length=200, blank=False, null=True)
    bo_mon = models.ForeignKey(BoMon, on_delete=models.SET_NULL, blank=True, null=True)
    danh_ba = models.ForeignKey(DanhBa, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'can_bo'

    def __str__(self):
        return self.ho_ten
