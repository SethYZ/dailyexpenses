from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ExpensesList,Item
from .forms import createnewlist

# Create your views here.

lists = [
    {
    'author': '',
    'name': '',
    'date_created': ''
    }
]

def home_view(request):
    return render(request, 'main/home.html', {})

def index_view(request):

    context = {
        'lists' : ExpensesList.objects.all()
    }

    return render(request, "main/index.html", context)

#    ls = ExpensesList.objects.get(id=id)
#
#    if request.method == "POST":
#        print(request.POST)
#
#        if request.POST.get("update"):
#            for item in ls.item_set.all():
#                if request.POST.get("UpdateItemName") != "" and request.POST.get("UpdateItemPrice") != 0:
#                    newName = request.POST.get("UpdateItemName")
#                    newPrice = request.POST.get("UpdateItemPrice")
#
#                    item.item_name = newName
#                    item.price = newPrice

#                    item.save()
#
#            else:
#                    print("Please insert a valid name!")

#        if request.POST.get("delete"):
#            for item in ls.item_set.all():
#                if request.POST.get("c" + str(item.id)) == "checked":
#                    d = ls.item_set.get(id=item.id)
#                    d.delete()
#                else:
#                    print("Please select a item to delete")

#        elif request.POST.get("newItem"):
#            text=request.POST.get("AddItem")
#            p=request.POST.get("AddPrice")
#
#            if len(text) > 2:
#                ls.item_set.create(item_name=text, price=p)
    #        else:
#                print("Insert A Valid Data")


@login_required()
def create(request):
    if request.method == "POST":
        form = createnewlist(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            request.user.ExpensesList_set.create(name="n")


        return render(request, "main/create.html", {"form":form})

    else:
        form = createnewlist()

        return render(request, "main/index.html", {"form":form})


@login_required()
def list(request):
    return render(request, "main/list.html", {})
