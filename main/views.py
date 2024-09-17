from django.shortcuts import render
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product


def show_main(request):
    Products = Product.objects.all()
    context = {
        'name' : 'Teh Botol Sosro',
        'price': 'Rp.20.000',
        'description': 'Nikmati kesegaran yang tiada duanya dengan Teh Botol Sosro, minuman teh melati berkualitas tinggi yang dikemas praktis dan siap diminum kapan saja. Terbuat dari daun teh pilihan dan bunga melati alami, Teh Botol Sosro menghadirkan rasa manis yang pas dan aroma teh yang khas, memberikan kesegaran sempurna di setiap tegukan.',
        'rating': '3',
        'Product' : Products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

