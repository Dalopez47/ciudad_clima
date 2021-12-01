import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ciudades.models import Consulta, Ciudad


class DatoVista(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            datos = list(Consulta.objects.filter(id=id).values())
            if len(datos) > 0:
                dato = datos[0]
                mensaje = {'message': "success", 'ciudad': dato}
            else:
                mensaje = {'message': "registro no encontrado..."}
            return JsonResponse(mensaje)
        else:
            datos = list(Consulta.objects.values())
            if len(datos) > 0:
                mensaje = {'message': "Success", 'ciudades': datos}
            else:
                mensaje ={'message': "registro no encontrado.."}
            return JsonResponse(mensaje)

    def post(self, request):
        jd = json.loads(request.body)
        Consulta.objects.create(hora=jd['hora'], temperatura=jd['temperatura'], humedad=jd['humedad'], viento=jd['viento'])
        mensaje = {'message': "Success"}
        return JsonResponse(mensaje)

    def put(self, request, id):
        jd = json.loads(request.body)
        datos = list(Consulta.objects.filter(id=id).values())
        if len(datos) > 0:
            dato = Consulta.objects.get(id=id)
            dato.hora = jd['hora']
            dato.temperatura= jd['temperatura']
            dato.humedad = jd['humedad']
            dato.viento = jd['viento']
            dato.save()
            mensaje = {'message': "Success"}
        else:
            mensaje = {'message': "registro no encontrado.."}

        return JsonResponse(mensaje)

    def delete(self, request, id):
        datos = list(Consulta.objects.filter(id=id).values())
        if len(datos) > 0:
            Consulta.objects.filter(id=id).delete()
            mensaje = {'message': "success"}
        else:
            mensaje = {'message': "registro no encontrado.."}
        return JsonResponse(mensaje)



class CiudadVista(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            ciudades = list(Ciudad.objects.filter(id=id).values())
            if len(ciudades) > 0:
                ciudad = ciudades[0]
                mensaje = {'message': "success", 'ciudad': ciudad}
            else:
                mensaje = {'message': "registro no encontrado..."}
            return JsonResponse(mensaje)
        else:
            ciudades = list(Ciudad.objects.values())
            if len(ciudades) > 0:
                mensaje = {'message': "Success", 'ciudades': ciudades}
            else:
                mensaje ={'message': "registro no encontrado.."}
            return JsonResponse(mensaje)

    def post(self, request):
        jd = json.loads(request.body)
        Ciudad.objects.create(nombre=jd['nombre'])
        mensaje = {'message': "Success"}
        return JsonResponse(mensaje)

    def put(self, request, id):
        jd = json.loads(request.body)
        ciudades = list(Ciudad.objects.filter(id=id).values())
        if len(ciudades) > 0:
            ciudad = Ciudad.objects.get(id=id)
            ciudad.nombre = jd['nombre']
            ciudad.save()
            mensaje = {'message': "Success"}
        else:
            mensaje = {'message': "registro no encontrado.."}

        return JsonResponse(mensaje)

    def delete(self, request, id):
        ciudades = list(Ciudad.objects.filter(id=id).values())
        if len(ciudades) > 0:
            Ciudad.objects.filter(id=id).delete()
            mensaje = {'message': "success"}
        else:
            mensaje = {'message': "registro no encontrado.."}
        return JsonResponse(mensaje)