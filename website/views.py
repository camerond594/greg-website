from django.shortcuts import render, render_to_response

from greg.setup import setup_criminal_verbiage, setup_family_verbiage, setup_civil_verbiage, setup_about_verbiage, \
    setup_drug_verbiage
from website.models import Verbiage


def base_site(request):
    return render(request, 'website/base.html', {})

def services(request):
    return render(request, 'website/pages/services.html', {})

def about(request):
    try:
        about_verbiage = Verbiage.objects.get(name="about")
    except:
        about_verbiage = setup_about_verbiage()
    context= {
        "verbiage": about_verbiage,
    }
    return render_to_response('website/pages/about-us.html', context=context)
    # return render(request, 'website/pages/about-us.html', {})

def criminal(request):
    try:
        criminal_verbiage = Verbiage.objects.get(name="criminal")
    except:
        criminal_verbiage = setup_criminal_verbiage()
    context= {
        "verbiage": criminal_verbiage,
    }
    return render_to_response('website/pages/criminal-law.html', context=context)
    # return render(request, 'website/pages/criminal-law.html', {})

def civil(request):
    try:
        civil_verbiage = Verbiage.objects.get(name="civil")
    except:
        civil_verbiage = setup_civil_verbiage()
    context= {
        "verbiage": civil_verbiage,
    }
    return render_to_response('website/pages/civil-litigation.html', context=context)
    # return render(request, 'website/pages/civil-litigation.html', {})

def drug(request):
    try:
        drug_verbiage = Verbiage.objects.get(name="drug")
    except:
        drug_verbiage = setup_drug_verbiage()
    context= {
        "verbiage": drug_verbiage,
    }
    return render_to_response('website/pages/drug-law.html', context=context)
    # return render(request, 'website/pages/drug-law.html', {})

def family(request):
    try:
        family_verbiage = Verbiage.objects.get(name="family")
    except:
        family_verbiage = setup_family_verbiage()
    context= {
        "verbiage": family_verbiage,
    }
    return render_to_response('website/pages/family-law.html', context=context)
    # return render(request, 'website/pages/family-law.html', {})

def contact(request):
    return render(request, 'website/pages/contact.html', {})