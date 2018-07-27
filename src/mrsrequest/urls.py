from django.urls import path, reverse_lazy

from mrsattachment.urls import factory

from .models import Bill, PMT
from . import views


app_name = 'mrsrequest'
urlpatterns = [
    path(
        'wizard/',
        views.generic.RedirectView.as_view(
            url=reverse_lazy('demande'), permanent=True),
        name='wizard'
    ),
]

urlpatterns += factory(PMT)
urlpatterns += factory(Bill)
