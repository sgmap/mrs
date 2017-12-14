import io
import uuid

from django import http
from django.views import generic

from .forms import MRSRequestCreateForm
from .models import MRSRequest


class MRSRequestCreateView(generic.FormView):
    form_class = MRSRequestCreateForm
    template_name = 'mrsrequest/form.html'

    def post(self, request, *args, **kwargs):
        if 'id' not in request.POST:
            return http.HttpResponseBadRequest('Nous avons perdu le UUID')

        self.id = request.POST['id']
        self.object, created = MRSRequest.objects.get_or_create(
            id=self.id)
        if not self.object.is_allowed(request):
            return http.HttpResponseBadRequest()

        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.id = str(uuid.uuid4())
        MRSRequest(self.id).allow(request)
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        return dict(
            id=self.id,
        )

    def form_valid(self, form):
        return http.HttpResponseCreated('Merci!')


class MRSFileUploadMixin(object):
    def post(self, request, *args, **kwargs):
        if 'mrsrequest_uuid' not in kwargs:
            return http.HttpResponseBadRequest('Nous avons perdu le UUID')
        self.uuid = kwargs['mrsrequest_uuid']

        if not MRSRequest(id=self.uuid).is_allowed(request):
            return http.HttpResponseBadRequest('Token de formulaire invalidé')

        if 'file' not in request.FILES:
            return http.HttpResponseBadRequest('Pas de fichier reçu')

        self.mrsrequest, created = MRSRequest.objects.get_or_create(
            id=self.uuid,
        )
        self.upload = request.FILES['file']
        self.object = self.create_object()

        return http.JsonResponse(
            dict(
                deleteUrl=self.object.get_delete_url()
            ),
            status=201,
        )

    def get_upload_body(self, f):
        body = io.BytesIO()
        for chunk in f.chunks():
            body.write(chunk)
        body.seek(0)  # rewind read point to beginning of registry
        return body.read()
