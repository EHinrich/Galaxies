from django.db import models

# Create your models here.


#content=models.TextField(verbose_name='Message')
#timestamp=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Date')
#updated=models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Update date')

class Galaxy(models.Model):
    galaxy_name=models.CharField(max_length=120, verbose_name='Galaxy name', primary_key=True)
    radius=models.FloatField(verbose_name='Radius')
    age=models.FloatField(verbose_name='Age')

    def __str__(self):
        return self.galaxy_name

    class Meta:
        verbose_name='Galaxy'
        verbose_name_plural='Galaxies'

class System(models.Model):
    system_name=models.CharField(max_length=120, verbose_name='System name', primary_key=True)
    radius=models.FloatField(verbose_name='Radius')
    age=models.FloatField(verbose_name='Age')

    def __str__(self):
        return self.system_name
    
    class Meta:
        verbose_name='System'
        verbose_name_plural='Systems'

class Object(models.Model):
    id=models.AutoField(primary_key=True)
    object_name=models.CharField(max_length=120, verbose_name='Object name')
    mass=models.FloatField(verbose_name='Mass')
    radius=models.FloatField( verbose_name='Radius')
    system_name=models.ForeignKey(System, on_delete=models.CASCADE, default='')
    galaxy_name=models.ForeignKey(Galaxy, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name='Object'
        verbose_name_plural='Objects'
