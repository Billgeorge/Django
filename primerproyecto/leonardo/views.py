from django.http import HttpResponse,Http404
from leonardo.models import Leonardo
from django.shortcuts import render_to_response,get_object_or_404


def perfil_detalle(request):
	leonar=get_object_or_404(Leonardo,pk=1)
	return render_to_response('leonardo/index.html',
								{'leonar':leonar})
