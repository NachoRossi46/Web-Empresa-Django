from .models import Link

def diccionario_contexto(request):
    contexto = {}
    links = Link.objects.all()
    for link in links:
        contexto[link.key] = link.url
    return contexto