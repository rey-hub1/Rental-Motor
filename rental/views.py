from django.shortcuts import get_object_or_404, render
from .models import Merek, Motor, Peminjaman
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UFT-8')

# Create your views here.
def home(request):
    nama =request.GET.get('motor')
    if nama :
        motors = Motor.objects.filter(nama__icontains=nama)
    else    :
        motors = Motor.objects.all()
    print(motors)
    return render(request, 'home.html', {'motors': motors})

def about(request):
    return render(request, 'about.html')
def detail(request, motor_id):
    motor = get_object_or_404(Motor, pk=motor_id)
    pesan_berhasil = None
    jumlah_bayar = None
    context = {
        'motor': motor,
        'pesan_berhasil': pesan_berhasil,
        'jumlah_bayar': jumlah_bayar
    }

    if request.method == 'POST':
        nik = request.POST.get('nik')
        nama_peminjam = request.POST.get('nama_peminjam')
        tanggal_pinjam = datetime.strptime(request.POST.get('tanggal_pinjam'), "%Y-%m-%d")
        tanggal_kembali = datetime.strptime(request.POST.get('tanggal_kembali'), "%Y-%m-%d")

        durasi_peminjaman = (tanggal_kembali - tanggal_pinjam).days

        if durasi_peminjaman <= 0:
            pesan_berhasil = "TANGGAL KEMBALI HARUS LEBIH BESAR"
            context['pesan_berhasil'] = pesan_berhasil
            return render(request, 'detail.html', context)

        jumlah_bayar = motor.harga_per_hari * durasi_peminjaman
        jumlah_bayar_rupiah = locale.currency(jumlah_bayar, grouping=True)

        # OBJEK PEMINJAMAN BARU
        peminjam = Peminjaman(
            nik=nik,
            nama_peminjam=nama_peminjam,
            motor=motor,
            tanggal_pinjam=tanggal_pinjam,
            tanggal_kembali=tanggal_kembali,
            jumlah_bayar=jumlah_bayar,
        )
        peminjam.save()

        # -1 stok motor
        motor.stok -= 1
        motor.save()

        pesan_berhasil = f"Terima kasih telah mempercayai produk kami. Silakan datang ke tempat untuk melakukan peminjaman. Total bayar: {jumlah_bayar_rupiah}."
        context['pesan_berhasil'] = pesan_berhasil

    # Selalu render template dengan konteks
    return render(request, 'detail.html', context)
