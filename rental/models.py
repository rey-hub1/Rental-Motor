from django.db import models
from django.utils.timezone import now

# Create your models here.
class Merek(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
    
class Motor(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE, related_name='motor')
    stok = models.PositiveBigIntegerField(default=0)
    harga_per_hari = models.DecimalField(max_digits=12, decimal_places=2)
    gambar = models.ImageField(upload_to='project/motor', blank=True, null=True)
    
    def __str__(self):
        return self.nama
    
class Peminjaman(models.Model):
    STATUS_CHOICE = [
        ('DIPESAN', "Dipesan"),
        ('DIPINJAM', "Dipinjam"),
        ('DIKEMBALIKAN', "Dikembalikan"),
    ]
    nik = models.CharField(max_length=10)
    nama_peminjam = models.CharField(max_length=100)
    motor= models.ForeignKey(Motor, on_delete=models.CASCADE, related_name='Perminjaman')
    tanggal_pinjam = models.DateField(default=now)
    tanggal_kembali = models.DateField()
    jumlah_bayar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sudah_bayar = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='DIPESAN'
    )
    def __str__(self):
        return f"{self.nama_peminjam} - {self.motor.nama} ({self.tanggal_pinjam})"