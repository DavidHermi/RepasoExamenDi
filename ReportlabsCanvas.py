# -*- coding: cp1252 -*-

'''
from reportlab.pdfgen import canvas

aux = canvas.Canvas("prueba.pdf")

aux.drawString(0,0,"Posicion Original (X,Y) = (0,0)")
aux.drawString(50,100,"Posicion (X,Y) = (50,100)")
aux.drawString(150,20,"Posicion (X,Y) = (150,20)")

aux.showPage()
aux.save()
'''

'''
# -*- coding: cp1252 -*-

from reportlab.pdfgen import canvas

aux = canvas.Canvas("prueba1.pdf")

aux.drawImage("d:\\python\\pdf\\logo_blog.jpg",50,200,600,600)
aux.drawString(50,200,"EJEMPLO DE INSERCION DE IMAGEN EN PDF")

aux.showPage()
aux.save()
'''
# -*- coding: cp1252 -*-

from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = []

# Creamos imagen de logotipo de empresa, y lo colocamos en
# la esquina inferior derecha.
imagen = Image(400, 0, 130, 150, "d:\\python\\pdf\logo_empresa.jpg")

# Creamos dibujo y le añadimos imagen.
dibujo = Drawing(30, 30)
dibujo.add(imagen)

# Trasladamos el dibujo a la esquina superior derecha.
dibujo.translate(0, 700)

# Incluimos en imágenes.
imagenes.append(dibujo)

# Volvemos a crear otro dibujo con logotipo de empresa. Darse cuenta
# que la imagen sigue en la esquina inferior derecha. Ahora incluimos
# en el dibujo la imagen.
dibujo = Drawing(30, 30)
dibujo.add(imagen)

# Rotamos, con eje de rotación la esquina inferior izquierda (coordenadas (0,0))
# el dibujo.
dibujo.rotate(45)

# Y lo escalamos, haciéndolo un poquito mas grande.
dibujo.scale(1.5, 0.5)

# Lo trasladamos un poco, para centrarlo.
dibujo.translate(-90, 300)

# Y finalmente lo incluimos.
imagenes.append(dibujo)

# Volvemos a crear otro dibujo con logotipo de empresa. Darse cuenta
# que la imagen sigue en la esquina inferior derecha. Ahora incluimos
# en el dibujo la imagen.
dibujo = Drawing(30, 30)
dibujo.add(imagen)

# Rotamos. Se nos puede salir de la hoja!
dibujo.rotate(90)

# Trasladamos a la izquierda del documento.
dibujo.translate(-20, -110)

# Incluimos.
imagenes.append(dibujo)

# Como vemos el objeto Drawing puede escalarse, rotarse y trasladarse, pero
# las operaciones son acumulativas.
dibujo = Drawing(A4[0], A4[1])
for aux in imagenes:
    dibujo.add(aux)
renderPDF.drawToFile(dibujo, "prueba3.pdf")
