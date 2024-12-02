# Generated by Django 5.1.3 on 2024-12-02 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_peminjaman_kendaraan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kendaraan',
            name='harga_per_hari',
        ),
        migrations.RemoveField(
            model_name='kendaraan',
            name='kategori_promosi',
        ),
        migrations.AddField(
            model_name='kendaraan',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='kendaraan',
            name='harga_promo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='kendaraan',
            name='promo_aktif',
            field=models.CharField(choices=[('TIDAK', 'Tidak'), ('YA', 'Ya')], default='TIDAK', max_length=5),
        ),
        migrations.AlterField(
            model_name='kendaraan',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='kendaraan/'),
        ),
        migrations.AlterField(
            model_name='kendaraan',
            name='kategori',
            field=models.CharField(choices=[('MOBIL', 'Mobil'), ('MOTOR', 'Motor'), ('LAINNYA', 'Lainnya')], default='MOBIL', max_length=10),
        ),
        migrations.AlterField(
            model_name='kendaraan',
            name='merek',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.merek'),
        ),
        migrations.AlterField(
            model_name='kendaraan',
            name='stok',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='peminjaman',
            name='kendaraan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='peminjaman', to='rental.kendaraan'),
            preserve_default=False,
        ),
    ]
