from django.contrib import admin
from .models import Merek, Kendaraan, Peminjaman

# Admin untuk Merek
class MerekAdmin(admin.ModelAdmin):
    list_display = ['nama']  # Menampilkan kolom nama di halaman admin
    search_fields = ['nama']  # Fitur pencarian berdasarkan nama merek

admin.site.register(Merek, MerekAdmin)

# Admin untuk Kendaraan
class KendaraanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'merek', 'tipe', 'tahun', 'stok', 'harga_per_hari', 'promo_aktif', 'harga_promo']
    list_filter = ['kategori', 'promo_aktif', 'merek']  # Filter berdasarkan kategori, promo, dan merek
    search_fields = ['nama', 'deskripsi', 'merek__nama']  # Pencarian berdasarkan nama kendaraan, deskripsi, dan nama merek
    ordering = ['harga_per_hari']  # Urutkan berdasarkan harga per hari

admin.site.register(Kendaraan, KendaraanAdmin)

# Admin untuk Peminjaman@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    # Menampilkan kolom di daftar admin
    list_display = [
        'nik', 
        'nama_peminjam', 
        'kendaraan', 
        'tanggal_pinjam', 
        'tanggal_kembali', 
        'jumlah_bayar', 
        'sudah_bayar', 
        'status'
    ]

    # Filter di sisi kanan admin
    list_filter = ['status', 'sudah_bayar', 'tanggal_pinjam', 'tanggal_kembali']

    # Menambahkan pencarian berdasarkan kolom tertentu
    search_fields = ['nama_peminjam', 'nik', 'kendaraan__nama']

    # Membuat semua field bisa diedit di halaman detail
    fields = [
        'nik', 
        'nama_peminjam', 
        'kendaraan', 
        'tanggal_pinjam', 
        'tanggal_kembali', 
        'jumlah_bayar', 
        'sudah_bayar', 
        'status'
    ]

from django import forms
from django.contrib import admin
from .models import Peminjaman

# Form untuk validasi khusus di Admin
class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        sudah_bayar = cleaned_data.get('sudah_bayar')
        status = cleaned_data.get('status')

        # Validasi: Tidak bisa mengubah status jadi 'Dikembalikan' jika belum bayar
        if status == 'DIKEMBALIKAN' and not sudah_bayar:
            raise forms.ValidationError(
                "Tidak bisa mengubah status menjadi 'Dikembalikan' jika belum membayar."
            )
        return cleaned_data

# Tambahkan Form ke PeminjamanAdmin
@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    form = PeminjamanForm
    list_display = [
        'nik', 
        'nama_peminjam', 
        'kendaraan', 
        'tanggal_pinjam', 
        'tanggal_kembali', 
        'jumlah_bayar', 
        'sudah_bayar', 
        'status'
    ]
    list_filter = ['status', 'sudah_bayar', 'tanggal_pinjam', 'tanggal_kembali']
    search_fields = ['nama_peminjam', 'nik', 'kendaraan__nama']
    fields = [
        'nik', 
        'nama_peminjam', 
        'kendaraan', 
        'tanggal_pinjam', 
        'tanggal_kembali', 
        'jumlah_bayar', 
        'sudah_bayar', 
        'status'
    ]