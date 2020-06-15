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

#        if response.POST.get("update"):
#            for item in ls.item_set.all():
#                if response.POST.get("UpdateItemName") != "" and response.POST.get("UpdateItemPrice") != 0:
#                    newName = response.POST.get("UpdateItemName")
#                    newPrice = response.POST.get("UpdateItemPrice")
#
#                    item.item_name = newName
#                    item.price = newPrice

#                    item.save()
#
#            else:
#                    print("Please insert a valid name!")

        if response.POST.get("delete"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "checked":
                    d = ls.item_set.get(id=item.id)
                    d.delete()
                else:
                    print("Please select a item to delete")

        elif response.POST.get("newItem"):
            text=response.POST.get("AddItem")
            p=response.POST.get("AddPrice")

            if len(text) > 2:
                ls.item_set.create(item_name=text, price=p)
            else:
                print("Insert A Valid Data")


    return render(response, "main/list.html", {"ls":ls})

def create(response):
    if response.method == "POST":
        form = createnewlist(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            response.user.ExpensesList_set.create(name="n")


        return render(response, "main/create.html", {"form":form})

    else:
        form = createnewlist()

        return render(response, "main/create.html", {"form":form})

def list(response):
    return render(response, "main/list.html", {})
