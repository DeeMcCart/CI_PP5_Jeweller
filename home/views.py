from django.shortcuts import render
from .models import AboutSection, AboutText

# Create your views here.


def about(request):
    """ This controls the display of text for the About page """
    """ Text typically is About / FAQ/ Enquiries """
    """ The model is designed to allow administrator to update """
    """ or periodically add to the displayed text """
    """ Text with hide_display=True will not be returned"""

    about_sections = AboutSection.objects.filter(hide_display=False)
    about_text = AboutText.objects.filter(hide_display=False)

    context = {
        'about_sections': about_sections,
        'about_text': about_text,
        'return_to': 'About',
    }

    return render(request, 'home/about.html', context)


def index(request):
    return render(request, 'home/index.html')


def error_400(request, exception):
    data = {}
    return render(request, '400.html', data)


def error_403(request, exception):
    data = {}
    return render(request, '403.html', data)


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request, *args, **argv):
    return render(request, '500.html', status=500)
