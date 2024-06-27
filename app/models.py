from django.db import models


class Biblioteca(models.Model):
    idBiblioteca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    class Meta:
        db_table = 'Biblioteca'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    idLibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    anioPublicacion = models.DateField(verbose_name="Año de Publicación")
    idBiblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, verbose_name="Biblioteca")

    class Meta:
        db_table = 'Libro'

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    fechaPrestamo = models.DateField(verbose_name="Fecha de Prestamo")
    fechaDevolucion = models.DateField(verbose_name="Fecha de Devolución")
    estado = models.CharField(max_length=200)
    idLibro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")

    class Meta:
        db_table = 'Prestamo'

    def __str__(self):
        return str(self.idPrestamo) + ' - ' + self.idLibro.titulo + ' - ' + self.idUsuario.nombre
