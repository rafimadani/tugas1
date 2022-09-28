# Readme.md for Tugas 4 PBP Semester Gasal 2022/2023 Rafi Madani
## Link to my website : https://pbp-project-2.herokuapp.com/todolist/
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  CSRF token berfungsi untuk meng-_generate_ token/data yang bersifat unik yang disediakan oleh server untuk setiap http request dari user. Ketika user mengirimkan http request ke server, web server akan memvalidasi request yang memiliki token yang sesuai, dan menolak request yang tidak. Apabila tidak ada CSRF Token tidak ada, maka server akan rentan oleh breach tipe _Cross-site Request Forgery_
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
  Ya bisa, langkah pertama membuat form dengan method POST sebagai wrapper nya. Lalu, dibawahnya kita taruh "{% csrf_token %}". Setelahnya, kita taruh fielf html nya dibawahnya, tidak lupa dengan button yang ber-_type_ submit.
##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
User akan menambahkan data di form, lalu data di form tersebut akan dioper melalui method POST. Setelah di POST, maka data user akan tersimpan di database (umumnya class, bisa bentuk lain). 
Setelahnya, HTMl akan mengambil data dari database melalui looping (salah satu cara).
##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
-  Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
```
 python manage.py startapp todolist
```
-  Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
> urls.py di project_django
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('katalog.urls')),
    path('mywatchlist/',include('mywatchlist.urls')),
    path('todolist/',include('todolist.urls')),
]
```
-  Membuat sebuah model Task yang memiliki beberapa atribut  berikut:
 ```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    title = models.CharField(max_length=50)
    description = models.TextField()
 ```
 - Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
```
from todolist.models import Task

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.forms import TaskCreationForm

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login')
def show_todolist(request):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    data_task = Task.objects.filter(user=user)
    context = {
        'data' : data_task,
        'username' : username,
        'user': user
    }
    return render(request, "todolist.html", context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('username', user.get_username()) # membuat cookie username dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login')
def create_task(request):
    form = TaskCreationForm()

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit = False)
            todolist.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
        
    context = {"forms": form}

    return render(request, 'create_task.html', context)

```
- Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
```
{% extends 'base.html' %}

 {% block content %}
  <h1>Rafi's To Do List Website</h1>
  <h2>Tugas 4 PBP Semester Gasal 2022/2023</h2>

  <h5>Username: </h5>
  <p>{{user}}</p>


  <table>
    <tr>
      <th>Date</th>
      <th>Title</th>
      <th>Description</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for task in data %}
    <tr>
        <td>{{task.date}}</td>
        <td>{{task.title}}</td>
        <td>{{task.description}}</td>
    </tr>
{% endfor %}
  </table>
  <button><a href="{% url 'todolist:create-task' %}">Create Task</a></button>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
 {% endblock content %}
```
- Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
```
{% extends 'base.html' %}

{% block content %}
<h1>Task Creation Segment</h1>


<form method="POST" action="">
    {% csrf_token %}
    <table>
        <tr>
            <td>Title: </td>
            <td><input type="text" name="title" class="form-control"></td>
        </tr>
                
        <tr>
            <td>Description: </td>
            <td><input type="text" name="description" class="form-control"></td>
        </tr>

        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Buat!"></td>
        </tr>
    </table>
</form>

{% endblock content %}
```
-  Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
> urls.py di todolist
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('create-task',create_task,name='create-task')
    ]
```
- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

  Melakukan deploy memiliki step yang sama persis dengan deploy sebelum-sebelumnya (lab dan tugas), hanya perlu add, commit, push. Setelahnya, deploy akan berjalan dan bila berhasil, website bisa diakses.
- Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

  Caranya simpel, register akun baru -> login -> create 3 task -> selesai

  Username & password - > (rafimadani & rafim555) (rafimadani2 & rafim555)

