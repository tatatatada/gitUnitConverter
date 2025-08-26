from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def length_converter(request):
    result = None
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        factors = {
            'millimeter': 0.001,
            'centimeter': 0.01,
            'meter': 1,
            'kilometer': 1000,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.34,
        }

        result = value * factors[from_unit] / factors[to_unit]
    
    return render(request, 'length.html', {'result': result})


