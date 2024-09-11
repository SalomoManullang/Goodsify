from django.shortcuts import render


def show_main(request):
    context = {
        'name' : 'Teh Botol Sosro',
        'price': 'Rp.20.000',
        'description': 'Nikmati kesegaran yang tiada duanya dengan Teh Botol Sosro, minuman teh melati berkualitas tinggi yang dikemas praktis dan siap diminum kapan saja. Terbuat dari daun teh pilihan dan bunga melati alami, Teh Botol Sosro menghadirkan rasa manis yang pas dan aroma teh yang khas, memberikan kesegaran sempurna di setiap tegukan.',
        'rating': '3',
    }

    return render(request, "main.html", context)