from django.http import JsonResponse

def get_data(request):
    data = [{"id": i, "name": f"Product {i}", "price": i * 10} for i in range(1, 11)]
    return JsonResponse(data, safe=False)