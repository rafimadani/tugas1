## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Perbedaan simple dari asynchronous dan synchronous adalah asynchronous proramming memperbolehkan pengguna untuk melakukan aktivitas lain ketika proses programming berjalan, sementara synchrnous programming memaksa pengguna untuk "click-wait-refresh".
Contoh dari asynchronous programming adalah ketika kita scroll media sosial di website, seperti di tiktok.com
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming itu adanya event yang muncul ketika suatu aktivitas spesifik dilakukan oleh user. Contoh aktivitas mungkin meng-_click_ tombol, hover di tombol. Aplikasi nya adalah menekan tomboll add task, maka modal akan muncul.
## Jelaskan penerapan asynchronous programming pada AJAX.
Ajax membuat user bisa memberi request ke web dan web bisa memberikan hasil tersebut tanpa harus melakukan reload website keseluruhan.
##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Untuk AJAX GET, maka kita tinggal merubah code di views.py, html, dan urls.py (jangan lupa sebelumnya install ajax di html masing-masing)

```
#views.py
def show_json(request):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    data_task = Task.objects.filter(user=user)
    context = {
        'data' : data_task,
        'username' : username,
        'user': user
    }
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

#html
    <script>
        function refresh(){
            $(document).ready(function(){
                    $.ajax({
                    url : "{% url 'todolist:showjson' %}",
                    success : function(result){
                        document.getElementById("card").innerHTML = ""
                        for (i=0;i<result.length;i++){
                            let card = `
                            <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
                                <div class="card-header">${result[i].fields.title}</div>
                                    <div class="card-body">
                                        <p class="card-text">${result[i].fields.description}<p>
                                    </div>
                                    <div class="card-footer">
                                        <small class="text-muted">${result[i].fields.date}</small>
                                </div>
                            </div>
                            `;
                            document.getElementById("card").innerHTML += card
                        }
        
                    }
                });
            });
        }
 #urls.py
 path('json',show_json,name='showjson'),
```
- Untuk AJAX POST, maka tinggal ubah juga di views.py, html, dan urls.py

```
#views.py
def create_task_json(request):
    form = TaskCreationForm()
    if request.method == "POST" and request.is_ajax():
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit = False)
            todolist.user = request.user
            form.save()
            return JsonResponse(b"CREATED", status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "todolist_json.html", {"form": form})
 #html
 function addWishlist() {
                fetch("{% url 'todolist:create-task' %}", {
                    method: "POST",
                    body:  new TaskCreationForm(document.querySelector('#form'))
                })
                return false
            }
        document.getElementById("submit").onclick = addWishlist()
  #urls.py
  path('add', create_task_json, name='add'),

 
```
