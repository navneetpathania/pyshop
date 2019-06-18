from django.shortcuts import render,redirect
from .models import Products
from django.core.files.storage import FileSystemStorage


def index(request):
    res = Products.objects.all()
    return render(request,"products_detailes/index.html",{"records":res})


def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        description = request.POST["description"]
        image = request.POST["image"]

        add_object = Products()
        add_object.name = name
        add_object.price = price
        add_object.stock = stock
        add_object.description = description
        add_object.image = image
        add_object.save()

        return redirect("/products")
    return render(request,"products_detailes/add.html")


def delete(request,id):
    Products.objects.filter(id=id).delete()
    return redirect("/products")


def edit(request,id):
    if request.method=="POST":
        id = request.POST["id"]
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        description = request.POST["description"]
        image = request.POST["image"]

        editrecords = Products.objects.get(id=id)
        editrecords.name = name
        editrecords.price = price
        editrecords.stock = stock
        editrecords.description = description
        editrecords.image = image
        editrecords.save()
        return redirect("/products")
    res = Products.objects.get(id=id)
    return render(request,"products_detailes/edit.html",{"records" : res })


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,"media/uploadfile.html")



