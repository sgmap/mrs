from crudlfap import shortcuts as crudlfap

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from contact.views import ContactView
from mrs.views import MaintenanceView
from mrsrequest.views import (
    MRSRequestCancelView,
    MRSRequestCreateView,
    # MRSRequestUpdateView,
)
from mrs.settings import TITLE_SUFFIX

from . import views

admin.site.site_header = 'MRS Admin' + TITLE_SUFFIX
admin.site.site_title = 'MRS Admin' + TITLE_SUFFIX

crudlfap.site.title = 'MRS Admin' + TITLE_SUFFIX
crudlfap.site.urlpath = 'admin'
crudlfap.site.views['home'] = views.Dashboard

handler400 = 'mrs.views.bad_request_view'
handler403 = 'mrs.views.forbidden_view'
handler404 = 'mrs.views.not_found_view'
handler500 = 'mrs.views.internal_server_error_view'

urlpatterns = [
    crudlfap.site.get_urlpattern(),
    path('', views.IndexView.as_view(), name='index'),
    # TBD : move the following static files to nginx or traefik
    path('favicon.ico', views.StaticView.as_view(
        path='img/favicon.ico',
    )),
    path('apple-touch-icon.png', views.StaticView.as_view(
        path='img/apple-touch-icon.png',
    )),
    path('apple-touch-icon-precomposed.png', views.StaticView.as_view(
        path='img/apple-touch-icon-precomposed.png',
    )),
    path('apple-touch-icon-120x120.png', views.StaticView.as_view(
        path='img/apple-touch-icon-120x120.png',
    )),
    path('apple-touch-icon-120x120-precomposed.png', views.StaticView.as_view(
        path='img/apple-touch-icon-120x120-precomposed.png',
    )),
    path('demande', MRSRequestCreateView.as_view(), name='demande'),
    # too early for this little one
    # path(
    #     'modifier-demande/<pk>/<token>',
    #     MRSRequestUpdateView.as_view(),
    #     name='demande-update'
    # ),
    path(
        'annuler-demande/<pk>/<token>',
        MRSRequestCancelView.as_view(),
        name='demande-cancel'
    ),
    path('contact', ContactView.as_view(), name='contact'),
    path('mentions-legales', views.LegalView.as_view(), name='legal'),
    path('faq', views.FaqView.as_view(), name='faq'),
    path('manifest.json', views.StaticView.as_view(
        path='manifest.json',
        content_type='application/manifest+json',
        stream=False,
    )),
    path('explorer/', include('explorer.urls')),
    path('captcha/', include('captcha.urls')),
    path('mrsrequest/', include('mrsrequest.urls', namespace='mrsrequest')),
    path('institution/', include('institution.urls', namespace='institution')),
    path('oldadmin/', admin.site.urls),
    path('doc/', include('django.contrib.admindocs.urls')),
    path('maintenance/', MaintenanceView.as_view(), name='maintenance'),
]

if 'debug_toolbar' in settings.INSTALLED_APPS and settings.DEBUG:  # noqa pragma: no cover
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
