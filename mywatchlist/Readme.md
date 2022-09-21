# Readme.md for Tugas 3 PBP Semester Gasal 2022/2023 Rafi Madani
## Link to my website : https://pbp-project-2.herokuapp.com/mywatchlist/html/
> You can see the json and xml just by replacing the "htmlview" with "json" or "xml". Go try it yourself!

## 1.  Jelaskan perbedaan antara JSON, XML, dan HTML!
##### Perbedaan JSON dan XML
- JSON memiliki format .json, sementara XML memiliki format .xml
- JSON adalah pengembangan dari Javascript, sementara XML pengembangan dari SGML
- Code JSON jauh lebih mudah dipelajari dari XML
- JSON support _array_, sementara XML tidak
- JSON hanya support text dan data type yang berbentuk angka, sementara XML bisa text, angka, grafik, gambar, dan lain-lain
##### Perbedaan HTML dan XML
- HTML memiliki format .html, sementara XML memiliki format .xml
- HTML adalah bahasa static, sementara XML bersifat dinamis
- HTML bersifat _case insensitive_, sementara XML bersifat _case sensitive_
- HTML digunakan untuk menampilkan data, XML digunakan untuk menyimpan data
- Ukuran file HTML berukuran jauh lebih kecil dibandingkan ukuran file XML

## 2.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Bila kita sedang membangun website/ platform lainnya, pasti ada suatu keadaan dimana platform tersebut akan meminta data ke server. Jenis data yang diminta pun bisa banyak, data yang diproses misalnya  HTML, css, atau data raw yang berbentuk JSON atau XML. Memiliki penegtahuan tentang data delivery bisa meningkatkan kapabilitas dari platform kita dalam _handling_ data.

## 3.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat aplikasi baru bernama "mywatchlist" dan menambahkan path nya.
```
python manage.py startapp mywatchlist
```
```
.
.
path('mywatchlist/',include('mywatchlist.urls'))
.
.
```
-  Membuat sebuah model MyWatchList yang memiliki beberapa atribut dan membuat minimal 10 data untuk objek MyWatchList yang sudah dibuat sebelumnya
```
class moviesitem(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=50)
    review = models.TextField()
```
```
 {
        "model": "mywatchlist.moviesitem",
        "pk": 1,
        "fields": {
            "watched": "Yes",
            "title": "Fight Club",
            "rating": "4.7/5", 
            "release_date": "11 November 1999",
            "review": "A good representation about consumerism habit of modern society"
        }
    },
   #and to be continued
```
-  Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format yaitu html, json, xml
```
def show_movies_html(request):
    data_barang_movies = moviesitem.objects.all()
    context = {
    'list_movies': data_barang_movies,
    'nama': 'Rafi Madani',
    'npm' : '2106750856',
    "watched": moviesitem.objects.filter(watched="Yes").count(),
    "not_watched": moviesitem.objects.filter(watched="No").count(),
    }
    return render(request, "mywatchlist.html",context)

def show_movies_json_id(request,id):
    data = moviesitem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def show_movies_xml_id(request,id):
    data = moviesitem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_movies_xml(request):
    data = moviesitem.objects.all()
    return HttpResponse(serializers.serialize("xml", data),content_type="application/xml")

def show_movies_json(request):
    data = moviesitem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```
-  Membuat routing sehingga data di atas dapat diakses melalui URL:
```
urlpatterns = [
    path('html/', show_movies_html, name='show_movies_html'),
    path('xml/', show_movies_xml, name='show_movies_xml'),
    path('json/', show_movies_json, name='show_movies_json'),
    path('json/<int:id>', show_movies_json_id, name='show_json_by_id'),
    path('xml/<int:id>', show_movies_xml_id, name='show_xml_by_id'),
]
```
- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Untuk deploy sendiri, step nya sama persis seperti di lab dan tugas tugas sebelumnya. Hanya perlu push, lalu otomatis akan deploy

## 4. Screenshoot Postman HTML, JSON, XML
![HTML](https://github.com/rafimadani/tugas2/blob/main/mywatchlist/ScreenShoot%20Tugas3/Screen%20Shot%202022-09-21%20at%2023.01.00.png)
![JSON](https://github.com/rafimadani/tugas2/blob/main/mywatchlist/ScreenShoot%20Tugas3/Screen%20Shot%202022-09-21%20at%2014.47.16.png)
![XML](https://github.com/rafimadani/tugas2/blob/main/mywatchlist/ScreenShoot%20Tugas3/Screen%20Shot%202022-09-21%20at%2014.47.10.png)




