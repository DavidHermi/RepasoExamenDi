from reportlab.pdfgen import canvas

oracion = ['Y en tu ausencia las paredes','se pintarán de tristeza',\
     'y enjaularé mi corazón entre tus huesos.']


aux = canvas.Canvas("prueba2.pdf")

textobject = aux.beginText()
textobject.setTextOrigin(100, 500)
textobject.setFont("Courier", 16)
for line in oracion:
    uniLine = unicode(line, 'latin-1')
    textobject.textOut(uniLine)
    # "Y" es positivo y mueve el cursor hacia abajo.
    textobject.moveCursor(20,15)
textobject.setFillColorRGB(0.2,0,0.6)
aux.drawText(textobject)

# Salvamos.
aux.showPage()
aux.save()