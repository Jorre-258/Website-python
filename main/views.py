from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import Create_New_List
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():


        #{"save":["save"], "c1":["clicked"]}
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")

        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {})

def home(response):
    return render(response, "main/home.html", {} )

def create(request):
    if request.method == "POST":
        form = Create_New_List(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = Create_New_List()
    return render(request, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})

