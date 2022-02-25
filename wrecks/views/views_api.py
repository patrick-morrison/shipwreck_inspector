import json, csv
from django.http import JsonResponse, HttpResponse
from ..models import Site, Report, Publication, Person, Photo
from django.shortcuts import render

def data(request):
    return render(request, 'wrecks/data.html')

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

def sites_csv(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="sites.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'slug', 'name', 'sunk', 'built', 'built_details', 'description', 'construction', 'owner', 'size', 'location', 'underwater', 'sinking', 'region', 'latitude', 'longitude', 'image', 'image_caption', 'museum_link', 'dave_link', 'user_id'])

    sites = Site.objects.all()

    for s in sites:
        writer.writerow([s.id, s.slug, s.name, s.sunk, s.built, s.built_details, s.description, s.construction, s.owner, s.size, s.location, s.underwater, s.sinking, s.get_region_display(), s.latitude, s.longitude, s.image, s.image_caption, s.museum_link, s.dave_link, s.user.id])

    return response

def reports_csv(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)

    reports = Report.objects.all()

    writer.writerow(['id', 'title', 'date', 'authors', 'authors_id', 'project', 'project_id', 'site', 'site_id', 'user', 'user_id', 'abstract', 'file'])
    
    for r in reports:
        authors = ','.join([str(a) for a in r.authors.all()])
        authors_id = ','.join([str(a.id) for a in r.authors.all()])

        projects = ','.join([str(a) for a in r.project.all()])
        projects_id = ','.join([str(a.id) for a in r.project.all()])

        writer.writerow([r.id, r.title, r.date, authors, authors_id, projects, projects_id, r.site, r.site.id, r.user,r.user.id, r.abstract, r.file])

    return response


def publications_csv(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="publications.csv"'

    writer = csv.writer(response)

    publications = Publication.objects.all()

    writer.writerow(['id', 'title', 'date', 'authors', 'authors_id', 'project', 'project_id', 'reports', 'reports_id', 'site', 'site_id', 'user', 'user_id', 'abstract', 'file'])
    
    for p in publications:
        authors = ','.join([str(a) for a in p.authors.all()])
        authors_id = ','.join([str(a.id) for a in p.authors.all()])

        projects = ','.join([str(a) for a in p.project.all()])
        projects_id = ','.join([str(a.id) for a in p.project.all()])

        reports = ','.join([str(a) for a in p.reports.all()])
        reports_id = ','.join([str(a.id) for a in p.reports.all()])

        sites = ','.join([str(a) for a in p.site.all()])
        sites_id = ','.join([str(a.id) for a in p.site.all()])

        writer.writerow([p.id, p.title, p.date, authors, authors_id, projects, projects_id, reports, reports_id, sites, sites_id, p.user, p.user.id, p.abstract, p.file])

    return response


def people_csv(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="people.csv"'

    writer = csv.writer(response)

    people = Person.objects.all()

    writer.writerow(['id', 'first_name', 'last_name', 'position', 'user', 'user_id', 'bio'])
    
    for p in people:
        writer.writerow([p.id, p.first_name, p.last_name, p.get_position_display(), p.user, p.user_id, p.bio])

    return response

def photos_csv(request):
    response = HttpResponse(
        content_type='text/csv',
    )
    response['Content-Disposition'] = 'attachment; filename="photos.csv"'

    writer = csv.writer(response)

    photos = Photo.objects.all()

    writer.writerow(['id', 'caption', 'date', 'authors', 'authors_id', 'report', 'report_id', 'site', 'site_id', 'user', 'user_id', 'file'])
    
    for r in photos:
        authors = ','.join([str(a) for a in r.authors.all()])
        authors_id = ','.join([str(a.id) for a in r.authors.all()])

        writer.writerow([r.id, r.caption, r.date, authors, authors_id, r.report, r.report.id, r.report.site, r.report.site.id, r.user,r.user.id,r.file])

    return response