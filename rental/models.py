from django.db import models

class Merek(models.Model):
    nama = models.CharField(max_length=100, unique=True)  # Nama merek kendaraan (seperti Honda, Yamaha)
    
    def __str__(self):
        return self.nama

class Kendaraan(models.Model):
    # Pilihan kategori kendaraan
    KATEGORI_CHOICES = [
        ('mobil', 'Mobil'),
        ('motor', 'Motor'),
    ]

    # Pilihan status promo
    PROMO_CHOICES = [
        ('aktif', 'Aktif'),
        ('tidak_aktif', 'Tidak Aktif'),
    ]

    # Pilihan tipe kendaraan
    TIPE_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    # Field model Kendaraan
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, default='motor')
    merek = models.ForeignKey(Merek, on_delete=models.SET_NULL, null=True, blank=True)  # Relasi ke tabel Merek
    tipe = models.CharField(max_length=10, choices=TIPE_CHOICES, default='manual')
    tahun = models.IntegerField(default=2020)
    harga_per_hari = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    promo_aktif = models.CharField(max_length=20, choices=PROMO_CHOICES, default='tidak_aktif')
    harga_promo = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='kendaraan_images/', null=True, blank=True)
    stok = models.IntegerField(default=1)  # Tambahkan stok dengan nilai default 1

    def __str__(self):
        return self.nama

class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('DIPINJAM', 'Dipinjam'),
        ('DIKEMBALIKAN', 'Dikembalikan'),
    ]
    
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE)
    nik = models.CharField(max_length=20)
    nama_peminjam = models.CharField(max_length=100)
    tanggal_pinjam = models.DateTimeField(auto_now_add=True)
    tanggal_kembali = models.DateTimeField(null=True, blank=True)
    jumlah_bayar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sudah_bayar = models.BooleanField(default=False)  # Tidak dihapus, tetap ada
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DIPINJAM')

    def __str__(self):
        return self.nama_peminjam
