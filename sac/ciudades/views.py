import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ciudades.models import Consulta


class ciudadVista(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            ciudades = list(Consulta.objects.filter(id=id).values())
            if len(ciudades) > 0:
                ciudad = ciudades[0]
                datos = {'message': "success", 'ciudad': ciudad}
            else:
                datos = {'message': "registro no encontrado..."}
            return JsonResponse(datos)
        else:
            ciudades = list(Consulta.objects.values())
            if len(ciudades) > 0:
                datos = {'message': "Success", 'ciudades': ciudades}
            else:
                datos ={'message': "registro no encontrado.."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Consulta.objects.create(hora=jd['hora'], temperatura=jd['temperatura'], humedad=jd['humedad'], viento=jd['viento'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        ciudades = list(Consulta.objects.filter(id=id).values())
        if len(ciudades) > 0:
            ciudad = Consulta.objects.get(id=id)
            ciudad.hora = jd['hora']
            ciudad.temperatura= jd['temperatura']
            ciudad.humedad = jd['humedad']
            ciudad.viento = jd['viento']
            ciudad.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "registro no encontrado.."}

        return JsonResponse(datos)

    def delete(self, request, id):
        ciudades = list(Consulta.objects.filter(id=id).values())
        if len(ciudades) > 0:
            Consulta.objects.filter(id=id).delete()
            datos = {'message': "success"}
        else:
            datos = {'message': "registro no encontrado.."}
        return JsonResponse(datos)

