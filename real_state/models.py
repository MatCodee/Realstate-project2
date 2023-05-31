from django.db import models
import boto3
from app.settings import AWS_STORAGE_BUCKET_NAME,DEBUG
import uuid


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Property(models.Model):

    REGION = (
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
    )
    PROPERTY_STATE = (
        ('','Estado'), 
        ('Venta', 'Venta'), 
        ('Arriendo', 'Arriendo')
    )
    
    PROPERTY_TYPE = (
        ("casa","casa"),
        ("departamento","departamento"),
        ("oficinas","oficinas"),
    )
    code = models.CharField(max_length=10, unique=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=PROPERTY_STATE)
    type_property = models.CharField(max_length=20,choices=PROPERTY_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_meters = models.DecimalField(max_digits=10, decimal_places=2)
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    car_parking = models.PositiveBigIntegerField(default=0)
    main_image = models.ImageField(upload_to='property_images')
    
    address = models.CharField(max_length=200,blank=True)
    
    region = models.CharField(max_length=50,choices=REGION)
    city = models.CharField(max_length=100,blank=True)
    google_maps_url = models.CharField(max_length=300,blank=True)
    google_maps_url_3d = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_popular = models.BooleanField(default=False)

    # Add other additional fields as needed, such as specific property features (pool, garage, etc.)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(uuid.uuid4())[:10].replace('-', '')
        super().save(*args, **kwargs)
    
    def delete(self):
        self.main_image.delete(save=False)
        super().delete()

    


class AdditionalImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return f"Additional Image for {self.property.title}"
    
    def delete(self):
        self.image.delete(save=False)
        super().delete()