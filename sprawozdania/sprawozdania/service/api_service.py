from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from sprawozdania.modules.Site_Config import Site_Config
from sprawozdania.utils.validator import filetype_validator
from sprawozdania.utils.renderer import render_html
from sprawozdania.utils.file import save_file, read_file
from sprawozdania.utils.time import get_time
import os

@csrf_exempt
def get_request(request):
    site_config = Site_Config()
    raw_html = read_file(site_config.get_html_location())
    if request.method == 'GET':
        return HttpResponse(f"{render_html(raw_html)}")
    if request.method == 'POST':
        file = request.FILES['file']
        validate_file_status = filetype_validator(file, site_config.get_allowed_extensions())
        name = request.POST['validationDefault01']
        surname = request.POST['validationDefault02']
        email = request.POST['validationDefault03']
        stud_class = request.POST['customRadioInline01']
        lab_group = request.POST['customRadioInline02']
        if validate_file_status:
            time = get_time()
            save_file(time, file, site_config.get_files_destination_final(), stud_class, lab_group, email)
            return HttpResponse(f"{render_html(raw_html, message=f'<span>{name} {surname}, informujemy że plik został przesłany.</span>')}")
        else:
            return HttpResponse(f"{render_html(raw_html, message=f'<span>Niepoprawny format pliku.</span>')}")
