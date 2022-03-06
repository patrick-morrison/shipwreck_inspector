"""shipwreck_inspector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from wrecks import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('data', views.data, name = 'data'),
    # AUTH
    path('accounts/signup', views.SignUp.as_view(), name = 'signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('preferences', views.preferences, name = 'preferences'),
    #Sites
    path('sites', views.sites.as_view(), name = 'sites'),
    path('sites/map', views.sites_map, name = 'sites_map'),
    path('sites.json', views.sites_json, name = 'sites_json'),
    path('sites.csv', views.sites_csv, name = 'sites_csv'),
    path('sites/create', views.CreateSite.as_view(), name = 'create_site'),
    path('sites/<slug:slug>', views.DetailSite.as_view(), name = 'detail_site'),
    path('sites/<slug:slug>/edit', views.UpdateSite.as_view(), name = 'update_site'),
    path('sites/<slug:slug>/delete', views.DeleteSite.as_view(), name = 'delete_site'),
    #Reports
    path('reports', views.reports.as_view(), name = 'reports'),
    path('reports.csv', views.reports_csv, name = 'reports_csv'),
    path('sites/<slug:slug>/report', views.CreateReport, name = 'create_report'),
    path('report/<int:pk>', views.DetailReport.as_view(), name = 'detail_report'),
    path('report/<int:pk>/edit', views.UpdateReport.as_view(), name = 'update_report'),
    path('report/<int:pk>/delete', views.DeleteReport.as_view(), name = 'delete_report'),
    path('sites/<slug:slug>/reports', views.site_reports.as_view(), name = 'site_reports'),
    #Publications
    path('publications', views.publications.as_view(), name = 'publications'),
    path('publications.csv', views.publications_csv, name = 'publications_csv'),
    path('publications/create', views.CreatePublication, name = 'create_publication'),
    path('publications/<int:pk>', views.DetailPublication.as_view(), name = 'detail_publication'),
    path('publications/<int:pk>/edit', views.UpdatePublication.as_view(), name = 'update_publication'),
    path('publications/<int:pk>/delete', views.DeletePublication.as_view(), name = 'delete_publication'),
    #People
    path('people', views.persons.as_view(), name = 'people'),
    path('people.csv', views.people_csv, name = 'people_csv'),
    path('person/create', views.CreatePerson.as_view(), name = 'create_person'),
    path('person/<int:pk>', views.DetailPerson.as_view(), name = 'detail_person'),
    path('person/<int:pk>/edit', views.UpdatePerson.as_view(), name = 'update_person'),
    path('person/<int:pk>/delete', views.DeletePerson.as_view(), name = 'delete_person'),
    #Photos
    path('report/<int:pk>/photo/add', views.CreatePhoto, name = 'create_photo'),
    path('photos.csv', views.photos_csv, name = 'photos_csv'),
    path('photo/<int:pk>/edit', views.UpdatePhoto.as_view(), name = 'update_photo'),
    path('photo/<int:pk>/delete', views.DeletePhoto.as_view(), name = 'delete_photo'),
    #Projects
    path('projects', views.projects.as_view(), name = 'projects'),
    path('projects.csv', views.projects_csv, name = 'projects_csv'),
    path('projects/create', views.CreateProject, name = 'create_project'),
    path('project/<slug:slug>', views.DetailProject.as_view(), name = 'detail_project'),
    path('project/<slug:slug>/edit', views.UpdateProject.as_view(), name = 'update_project'),
    path('project/<slug:slug>/delete', views.DeleteProject.as_view(), name = 'delete_project'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path(
        'person-autocomplete/',
        views.PersonAutocomplete.as_view(),
        name='person-autocomplete',
    ),
        path(
        'project-autocomplete/',
        views.ProjectAutocomplete.as_view(),
        name='project-autocomplete',
    ),
        path(
        'site-autocomplete/',
        views.SiteAutocomplete.as_view(),
        name='site-autocomplete',
    ),
        path(
        'report-autocomplete/',
        views.ReportAutocomplete.as_view(),
        name='report-autocomplete',
    ),
        path(
        'user-autocomplete/',
        views.UserAutocomplete.as_view(),
        name='user-autocomplete',
    ),
        path(
        'publication-autocomplete/',
        views.PublicationAutocomplete.as_view(),
        name='publication-autocomplete',
    ),
]
