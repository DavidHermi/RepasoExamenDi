
from reportlab.platypus import SimpleDocTemplate,PageBreak,Image,Spacer,Paragraph,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate ('examploTaboas.pdf' , pageSize = A4)
operaciones = []
datos = [('', 'Ventas', 'Compras'),
         ('Xaneiro', 300, 500),
         ('Febreiro', 400 , 500),
         ('Marzo', 30, 2000)]

taboa = Table (datos, colWidths=100, rowHeights=30)
estilo = (
    [
        ('TEXTCOLOR', (0,1), (0,-1), colors.blue),
        ('TEXTCOLOR', (1,1), (2,-1), colors.green),
        ('BACKGROUND', (1,1), (1,-1), colors.lightgreen),
        ('BOX', (1,1), (2,-1),1.5, colors.grey),
        ('INERGRID',(1,1), (1,-1), colors.lightgrey),
        ('VALING',(0,0), (-1,-1), 'MIDDLE')
        ])

for f, linha in enumerate(datos):
    for c, valor in enumerate (linha):
        if type (valor) == int :
            if valor > 0:
                estilo.append(('BACKGROUND', (c,f), (c,f), colors.lightgreen))
            else :
                estilo.append(('BACKGROUND', (c,f), (c,f), colors.lightpink))
taboa.setStyle(estilo)


operaciones.append(taboa)

doc.build(operaciones)