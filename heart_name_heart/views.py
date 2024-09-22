from io import BytesIO

from django.http import HttpResponse

from core.heart_name_heart.generator import generate
from heart_name_heart.forms import GenerateForm


def generate_api(request):
    req = GenerateForm()
    req.name = request.GET.get('name')
    req.angle = request.GET.get('angle', 5)
    req.download = request.GET.get('download', False) == 'true'

    name = req.name
    angle = req.angle
    download = req.download

    resp = HttpResponse()
    generate(name, angle, resp)

    resp.headers["Content-Type"] = "image/jpeg"
    if download:
        resp.headers["Content-Disposition"] = f"attachment; filename=\"heart_{name}_heart.jpg\""
    return resp
