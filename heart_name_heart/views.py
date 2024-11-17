from io import BytesIO

from django.http import HttpResponse

from core.heart_name_heart.generator import generate
from heart_name_heart.forms import GenerateForm


def generate_api(request):
    req = GenerateForm()
    name = req.name.clean(request.GET.get('name'))
    angle = req.angle.clean(request.GET.get('angle', 5))
    download = req.download.clean(request.GET.get('download', False))

    resp = HttpResponse()
    generate(name, angle, resp)

    resp.headers["Content-Type"] = "image/jpeg"
    if download:
        resp.headers["Content-Disposition"] = f"attachment; filename=\"heart_{name}_heart.jpg\""
    return resp
