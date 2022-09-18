# TUGAS 2 PBP 
## Rafi Madani / 2106750856
### https://pbp-project-2.herokuapp.com/catalog/
## Bagan
![This is an image](https://github.com/rafimadani/tugas2/blob/main/Screen%20Shot%202022-09-15%20at%2000.02.25.png)
Pertama-tama, http request masuk melalui urls.py. Dari sana, urls.py memanggil function dari views.py untuk melihat data. Agar bisa melihat data, views.py mengambil data dari models.py. Setelah mempunyai data nya, data akan di present ke user sesuai format di catalog.html
## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawabannya, kita menggunakan virtual environtmen agar kita bisa "mengisolasi" project kita. Andaikan kita mempunyai  project A dan A memakai Django versi 2.0, lalu kita membuat project baru bernama B dan kita membutuhkan Django versi 3.0 sehingga kita mengupgrade versi Django kita. Problemnya adalah, bila kita tidak memiliki virtual enviorenment, versi Django di projek A juga akan terupdate, akan menjadi masalah apabila projek A menjadi eror ketika versi Django nya di update. Dengan virtual environment, kita bisa mengisolasi projek kita sehingga peristiwa di contoh sebelumnya tidak terjadi. Walaupun begitu, kita tetap bisa membuat aplikasi web Django tanpa menggunakan virtual environment.
## Penjelasan Cara Mengimplementasikan Poin 1 sampai dengan 4
### urls.py
Pada _Urls.py_, kita menambahkan code berikut 
```
from django.urls import path
from katalog.views import show_catalog

app_name = 'catalog'

urlpatterns = [
    path('catalog/', show_catalog, name='show_catalog'),
]

```
Tujuan dari _app_name = 'catalog'_ adalah untuk meng-_set_ nama aplikasi menjadi _catalog_. 
```
path('catalog/', show_catalog, name='show_catalog'),
```
Fungsi dari command diatas adalah untuk agar nanti data yang disajikan hanya akan terbuka bila link _http://localhost:8000/catalog/_ diakses. Agar informasi yang diinginkan lebih jelas lokasinya. Selain itu, terdapat juga pemanggilan fungsi _show_katalog_ agar data yang diinginkan bisa ditampilkan
### models.py
```
from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    description = models.TextField()
    item_stock = models.IntegerField()
    rating = models.IntegerField()
    item_url = models.URLField()
```
Di code atas, kita mengdefinisikan jenis-jenis data type yang akan di pakai dari setiap variabel yang akan dipanggil di _views.py_
### views.py
```
from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.

def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_catalog,
    'nama': 'Rafi Madani',
    'npm' : '2106750856'
    }
    return render(request, "catalog.html", context)
```
Di code atas, pertama-tama kita melakukan import _CatalogItem_ dari models. Setelah berhasil import, kita membuat function _show_catalog(request)_ yang berfungsi untuk menjadi data yang akan ditampilkan di html
### catalog.html
```
{% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
```
Code di atas berfungsi untuk mem-_print_ output berupa data dari file json dan _views.py_
_
