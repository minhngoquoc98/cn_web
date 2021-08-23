from django.contrib import admin

# Register your models here.
from danh_ba.models import CanBo, DanhBa, Khoa, BoMon


class DanhBaAdmin(admin.ModelAdmin):
    list_display = ("khoa", "ten")
    # inlines = (CanBoInline,)
    list_per_page = 25
    list_filter = ('khoa',)
    search_fields = ('ten',)


class KhoaAdmin(admin.ModelAdmin):
    list_display = ("ten", )
    list_per_page = 25
    search_fields = ('ten',)


class BoMonAdmin(admin.ModelAdmin):
    list_display = ("ten", "khoa")
    list_per_page = 25
    list_filter = ('khoa',)
    search_fields = ('ten',)


class CanBoAdmin(admin.ModelAdmin):
    list_display = ("ho_ten", "chuc_vu", 'bo_mon', 'danh_ba', 'dien_thoai_co_quan', 'email', 'dien_thoai_didong', )
    list_per_page = 25
    list_filter = ('bo_mon', 'danh_ba')
    search_fields = ('ho_ten', 'chuc_vu')


admin.site.register(DanhBa, DanhBaAdmin)
admin.site.register(Khoa, KhoaAdmin)
admin.site.register(BoMon, BoMonAdmin)
admin.site.register(CanBo, CanBoAdmin)
