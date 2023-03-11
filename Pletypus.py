import os

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

estiloHoja = getSampleStyleSheet()

story = []

cabecera = estiloHoja['Heading4']

cabecera.pageBreakBefore = 0

cabecera.keepWithNext = 0

cabecera.backColor = colors.cyan

parrafo = Paragraph("CABECERA DEL DOCUMENTO ", cabecera)

story.append(parrafo)

cadena = " El Viaje del Navegante " * 600

estilo = estiloHoja['BodyText']
parrafo2 = Paragraph(cadena, estilo)

story.append(parrafo2)

story.append(Spacer(0, 20))

fichero_imagen = ""
imagen_logo = Image(os.path.realpath(fichero_imagen), width=400, height=100)
story.append(imagen_logo)

doc = SimpleDocTemplate("ejemplo1.pdf", pagesize=A4, showBoundary=1)

doc.build(story)
