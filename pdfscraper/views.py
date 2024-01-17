import pdb
from django.shortcuts import render

from .pdfscraper import PDFScraper

def homepage(request):
    data = {'data': None}
    if request.method == "POST":
        data['data'] = PDFScraper.run(request.FILES['file'].file).to_html()

    return render(request, template_name='home.html', context=data)