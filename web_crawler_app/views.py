from django.http import JsonResponse


def basic(request):
    return JsonResponse({
        "message": "This is a simple response !"
    })
