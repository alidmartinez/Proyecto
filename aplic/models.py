from django.db import models

class Usuario(models.Model):
    Identificacion       = models.CharField(max_length=15)
    RazonSocial          = models.CharField(max_length=200, blank=True)
    idTipoId             = models.IntegerField()
    Nombres              = models.CharField(max_length=100, blank=True)
    Apellidos            = models.CharField(max_length=100, blank=True)
    Email                = models.EmailField(max_length=100, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoUsuario      = models.IntegerField()
    Telefonos            = models.CharField(max_length=100, blank=True)
    Eliminado            = models.BooleanField(default=False)
    
    
    def __str__(self):
        if self.Nombres <>'' and self.Apellidos <>'':
            return "%s %s"  % (self.Nombres,self.Apellidos)
        elif self.RazonSocial <>'' :
            return self.RazonSocial

class Tercero(models.Model):
    CodTercero           = models.CharField(max_length=15)
    IdTipoTercero        = models.BooleanField(default=False)
    RazonSocial          = models.CharField(max_length=200, blank=True)
    Email                = models.EmailField(max_length=200, blank=True)
    Telefono             = models.CharField(max_length=200, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoTercero      = models.IntegerField()
    eliminado            = models.BooleanField(default=False)

    def __str__(self):
        return self.RazonSocial
 

  
class Kardex(models.Model):
    CodKardex           = models.CharField(max_length=10, unique=True)
    TipoMovimiento      = models.IntegerField()
    Fecha               = models.DateField()
    CodTercero          = models.ForeignKey('Tercero')
    CodProduc           = models.ForeignKey('Producto')
    CantProduc          = models.IntegerField()
    ValorUnitario       = models.DecimalField(max_digits=10, decimal_places=2)
    EstadoKardex        = models.IntegerField()
    ValorPublico       = models.DecimalField(max_digits=10, decimal_places=2)
    Eliminado           = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.CodKardex
    

class Producto(models.Model):
    refProducto          = models.CharField(max_length=100, blank=True,unique=True)
    descProducto         = models.CharField(max_length=100, blank=True)
    idTipoProducto       = models.IntegerField()
    idCategoriaProducto  = models.IntegerField()
    idEstadoProducto     = models.IntegerField()   
    Eliminado            = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descProducto

class Parametro(models.Model):
    atributo        =models.CharField(max_length=50)
    descripcion      =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)
 
    def __str__(self):
        return self.atributo


class ValorParametro(models.Model):
    
    valor                =models.CharField(max_length=30)
    parametro            = models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)
    

    def __str__(self):
        return self.valor