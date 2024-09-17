from django.shortcuts import render
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product


def show_main(request):
    products = Product.objects.all()
    context = {
        'Products': products  # Ganti key menjadi 'Products' agar sesuai dengan template
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

