from django.contrib import admin
from .models import Merek, Motor, Peminjaman

# Register your models here.
admin.site.register(Merek)
admin.site.register(Peminjaman)
admin.site.register(Motor)
# @admin.site.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_peminjam', 'motor', 'tanggal_pinjam', 'tanggal_kembali', 'jumlah_bayar', 'sudah_bayar', 'status')
    list_filter = ('status',)
    search_fields = ('nik', 'nama_peminjam', 'motor__nama')
    ordering = ('-tanggal_pinjam',)

    def save_model(self, request, obj, form, change):
        # JIKA DIKEMBALIKAN MAKA STOK DITAMBAH KEMBALI
        if obj.status == 'DIKEMBALIKAN':
            motor = obj.motor
            motor.stok += 1
            motor.save()
        super().save_model(request, obj, form, change)