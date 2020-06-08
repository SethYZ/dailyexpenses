from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ExpensesList,Item
from .forms import createnewlist

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def index(response, id):
    ls = ExpensesList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)

        if response.POST.get("delete"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "checked":
                    pass
                else:
                    print("Please select a item to delete")

        elif response.POST.get("newItem"):
            text=response.POST.get("AddItem")
            p=response.POST.get("AddPrice")

            if len(text) > 2:
                ls.item_set.create(item_name=text, price=p)
            else:
                print("Insert Valid Data")
                

    return render(response, "main/list.html", {"ls":ls})

def create(response):
    if response.method == "POST":
        form=createnewlist(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            e = ExpensesList(name=n)
            e.save()

    else:
        form = createnewlist()
        return render(response, "main/create.html", {"form":form})
