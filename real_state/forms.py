from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
    
    
class PropertySearchForm(forms.Form):
    property_status = forms.ChoiceField(
        choices=[
            ('','Estado'), 
            ('Venta', 'Venta'), 
            ('Arriendo', 'Arriendo')
        ])
    property_type = forms.ChoiceField(
        choices=[
            ('','Tipo de Propiedad'), 
            ('Casa', 'Casa'), 
            ('Departamento', 'Departamento'), 
            ('Oficinas', 'Oficinas'), 
        ])

    region = forms.ChoiceField(
        choices=[
            ('','Locations'), 
            ('R.Arica y Parinacota', 'R.Arica y Parinacota'), 
            ('R.Tarapacá', 'R.Tarapacá'), 
            ('R.Antofagasta', 'R.Antofagasta'), 
            
            ('R.Atacama', 'R.Atacama'), 
            ('R.Coquimbo', 'R.Coquimbo'), 
            ('R.Valparaíso', 'R.Valparaíso'), 
            ('R.Metropolitana de Santiago', 'R.Metropolitana de Santiago'), 
            ('R.Bernardo OHiggins', 'R.Bernardo OHiggins'),
            ('R.Maule', 'R.Maule'),
            ('R.Ñuble', 'R.Ñuble'),
            ('R.Biobío', 'R.Biobío'),
            ('R.Araucanía', 'R.Araucanía'),
            ('R.Los Ríos', 'R.Los Ríos'),
            ('R.Los Lagos', 'R.Los Lagos'),
            ('R.Aysén', 'R.Aysén'),
            ('R.Magallanes', 'R.Magallanes'),
        ])

    bedrooms = forms.ChoiceField(
        choices=[
            ('','Bedrooms'), 
            ('1', '1'), 
            ('2', '2'), 
            ('3', '3'), 
            ('4 o mas', '4 o mas'), 
        ])
    bathrooms = forms.ChoiceField(
        choices=[
            ('','Bathrooms'), 
            ('1', '1'), 
            ('2', '2'), 
            ('3', '3'), 
            ('4 o mas', '4 o mas')
        ])
