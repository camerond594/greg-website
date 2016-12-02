from website.models import Verbiage


def setup_criminal_verbiage():
    criminal_file = open("static/verbiage/criminal.txt", 'rb')
    criminal = criminal_file.read()
    criminal_file.close()

    criminal_verbiage = Verbiage(name='criminal', text=criminal)
    criminal_verbiage.save()
    return criminal_verbiage

def setup_family_verbiage():
    family_file = open("static/verbiage/family.txt", 'rb')
    family = family_file.read()
    family_file.close()

    family_verbiage = Verbiage(name='family', text=family )
    family_verbiage.save()
    return family_verbiage

def setup_civil_verbiage():
    civil_file = open("static/verbiage/civil-litigation.txt", 'rb')
    civil = civil_file.read()
    civil_file.close()

    civil_verbiage = Verbiage(name='civil', text=civil)
    civil_verbiage.save()
    return civil_verbiage

def setup_about_verbiage():
    about_file = open("static/verbiage/about.txt", 'rb')
    about = about_file.read()
    about_file.close()

    about_verbiage = Verbiage(name='about', text=about)
    about_verbiage.save()
    return about_verbiage

def setup_drug_verbiage():

    drug_file = open("static/verbiage/drug.txt", 'rb')
    drug = drug_file.read()
    drug_file.close()

    drug_verbiage = Verbiage(name='about', text=drug)
    drug_verbiage.save()
    return drug_verbiage