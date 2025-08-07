from django.shortcuts import render
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

from app import settings
# models:
from .models import Property,AdditionalImage
from blog.models import Blog
# forms
from .forms import ContactForm,PropertySearchForm


@csrf_protect
def HomeView(request):      
    if request.method == 'POST':
        form = PropertySearchForm(request.POST)
        if form.is_valid():
            properties = Property.objects.filter(
                transaction_type=form.cleaned_data['property_status'],
                category__name=form.cleaned_data['property_type'],
                region=form.cleaned_data['region'],
                bedrooms=form.cleaned_data['bedrooms'],
                bathrooms=form.cleaned_data['bathrooms']
            )
            paginator = Paginator(properties, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'propertie/properties.html', {
                'form': form,
                'properties': page_obj
            })
        return render(request, 'propertie/properties.html', {'form': form})

    properties = Property.objects.all()[:6]
    blogs = Blog.objects.all()[:3]
    return render(request, "home/home.html", {
        'properties': properties,
        'blogs': blogs
    })

class AboutView(TemplateView):
    template_name = "about/about.html"

class ServicesView(TemplateView):
    template_name = "services/services.html"

@csrf_protect
def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Nuevo mensaje de contacto'
            content = f'Nombre: {fullname}\nTeléfono: {phone}\nCorreo electrónico: {email}\nMensaje: {message}'
            send_mail(subject, content, settings.EMAIL_HOST_USER, ['matias.altamiranove@gmail.com'], fail_silently=False)            
            return render(request, 'status/success.html',{})
    else:
        form = ContactForm()
    return render(request,"contact/contact.html",{'form': form})


from user_act.models import CompanyMember
def TeamView(request):
    context = {}
    company_members = CompanyMember.objects.all()
    context['members'] = company_members
    return render(request,"team/team.html",context)



@csrf_protect
def PropertyView(request, city=None):
    context = {}
    if request.method == 'POST':
        form = PropertySearchForm(request.POST)
        print("Entro")
        context = {}
        if form.is_valid():
            property_status = form.cleaned_data['property_status']
            property_type = form.cleaned_data['property_type']
            region = form.cleaned_data['region']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            
            properties = Property.objects.filter(
                transaction_type=property_status,
                category__name=property_type,
                region=region,
                bedrooms=bedrooms,
                bathrooms=bathrooms
            )
            properties_pag = Paginator(properties, 10) 
            page_number = request.GET.get('page')
            page_obj = properties_pag.get_page(page_number)

            context = {
                'form': form,
                'properties': page_obj
            }

        return render(request, 'propertie/properties.html', context)
    else:
        properties = Property.objects.all()
        if city:
            properties = properties.filter(city__iexact=city)
        properties_pag = Paginator(properties, 10) 
        page_number = request.GET.get('page')
        page_obj = properties_pag.get_page(page_number)
    
        
        context['properties'] = page_obj
        return render(request,"propertie/properties.html",context)


def DetailPropertyView(request,id):
    context = {}
    property = get_object_or_404(Property,pk=id) 
    context['property'] = property
    context['images'] = AdditionalImage.objects.filter(property=property)
    return render(request,"propertie/detail_property.html",context)



