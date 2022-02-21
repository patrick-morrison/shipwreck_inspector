import json
from django.http import JsonResponse
from ..models import Site

def sites_json(request):
    sites = Site.objects.all()
    sites_json = json.dumps({
        'type': 'FeatureCollection',
        'features':[{
            'type': 'Feature','properties': {
                'name':s.name, 'sunk': s.sunk, 'pk':s.pk,},
            'geometry' : {
                'type': 'Point',
                'coordinates': [s.longitude, s.latitude]
                }
        }for s in sites]})
    return JsonResponse(json.loads(sites_json), safe=False)

