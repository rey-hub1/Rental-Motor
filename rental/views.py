from django.shortcuts import get_object_or_404, render
from .models import Merek, Kendaraan, Peminjaman
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import locale

# Atur locale untuk format mata uang dan tanggal
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

# Home view - Menampilkan kendaraan dengan filter kategori
def home(request):
    kendaraan_promo = Kendaraan.objects.filter(promo_aktif='aktif')  # Kendaraan dengan promo aktif
    kendaraan_mobil = Kendaraan.objects.filter(kategori='mobil')
    kendaraan_motor = Kendaraan.objects.filter(kategori='motor')

    context = {
        'kendaraan_promo': kendaraan_promo,
        'kendaraan_mobil': kendaraan_mobil,
        'kendaraan_motor': kendaraan_motor,
    }
    return render(request, 'home.html', context)

# About page - Menampilkan halaman tentang
def about(request):
    return render(request, 'about.html')

# Detail view - Menampilkan detail kendaraan dan memproses peminjaman
def detail(request, kendaraan_id):
    kendaraan = get_object_or_404(Kendaraan, pk=kendaraan_id)
    pesan_berhasil = None

    if request.method == 'POST':
        # Ambil data dari form
        nik = request.POST.get('nik')
        nama_peminjam = request.POST.get('nama_peminjam')
        tanggal_pinjam = datetime.strptime(request.POST.get('tanggal_pinjam'), "%Y-%m-%d")
        tanggal_kembali = datetime.strptime(request.POST.get('tanggal_kembali'), "%Y-%m-%d")

        # Hitung durasi peminjaman
        durasi_peminjaman = (tanggal_kembali - tanggal_pinjam).days
        if durasi_peminjaman <= 0:
            return render(request, 'detail.html', {
                'kendaraan': kendaraan,
                'pesan_berhasil': "Tanggal kembali harus lebih besar dari tanggal pinjam.",
            })

        # Hitung jumlah bayar
        harga_harian = kendaraan.harga_promo if kendaraan.promo_aktif == 'aktif' else kendaraan.harga_per_hari
        jumlah_bayar = harga_harian * durasi_peminjaman
        jumlah_bayar_rupiah = locale.currency(jumlah_bayar, grouping=True)

        # Simpan peminjaman
        peminjaman = Peminjaman(
            kendaraan=kendaraan,
            nik=nik,
            nama_peminjam=nama_peminjam,
            tanggal_pinjam=tanggal_pinjam,
            tanggal_kembali=tanggal_kembali,
            jumlah_bayar=jumlah_bayar,
        )
        peminjaman.save()

        # Kurangi stok kendaraan
        kendaraan.stok -= 1
        kendaraan.save()

        pesan_berhasil = f"Terima kasih telah melakukan peminjaman. Total yang harus dibayar: {jumlah_bayar_rupiah}."

    return render(request, 'detail.html', {
        'kendaraan': kendaraan,
        'pesan_berhasil': pesan_berhasil,
    })

def search(request):
    query = request.GET.get('search', '')  # Ambil parameter "search" dari URL
    results = Kendaraan.objects.filter(nama__icontains=query) if query else []

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search_results.html', context)