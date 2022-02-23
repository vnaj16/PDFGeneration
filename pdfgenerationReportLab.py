# importing modules
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)

def drawMyRuler(pdf):
    pdf.drawString(100,810,'x100')
    pdf.drawString(200,810,'x200')
    pdf.drawString(300,810,'x300')
    pdf.drawString(400,810,'x400')
    pdf.drawString(500,810,'x500')

    pdf.drawString(10,100,'y100')
    pdf.drawString(10,200,'y200')
    pdf.drawString(10,300,'y300')
    pdf.drawString(10,400,'y400')
    pdf.drawString(10,500,'y500')
    pdf.drawString(10,600,'y600')
    pdf.drawString(10,700,'y700')
    pdf.drawString(10,800,'y800')

def StrategyOne(data, filename):
    # creating a pdf object
    pdf = canvas.Canvas(filename)
    drawMyRuler(pdf)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawImage('logo.png', 50, 750, width=80, height=80, preserveAspectRatio=True)


    # creating the title by setting it's font
    # and putting it on the canvas
    #pdf.setFont('abc', 36)
    pdf.drawCentredString(500, 770, 'PERU, 22 de Febrero del 2022')
    pdf.drawCentredString(300, 750, 'FICHA DE LA MARCA')
    pdf.line(50,735,550,735)

    textLines = [
        'Linea 1',
        'Linea 2',
        'Linea 3',
        'Linea 4',
    ]

    text = pdf.beginText(50,700)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)
    # saving the pdf
    pdf.save()

def StrategyTwo(data, filename):
    # creating a pdf object
    pdf = canvas.Canvas(filename)
    drawMyRuler(pdf)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawImage('logo.png', 50, 750, width=80, height=80, preserveAspectRatio=True)


    # creating the title by setting it's font
    # and putting it on the canvas
    #pdf.setFont('abc', 36)
    pdf.drawCentredString(500, 770, 'PERU, 22 de Febrero del 2022')
    pdf.drawCentredString(300, 750, 'FICHA DE LA MARCA')
    pdf.line(50,735,550,735)

    name = data['name']
    age = data['age']
    city = data['city']
    textLines = [
        f'Name: {name}',
        f'Age: {age}',
        f'City: {city}'
    ]

    text = pdf.beginText(50,700)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)
    # saving the pdf
    pdf.save()    

#PARA APLICAR EL PATRON STRATEGY EN PTYHON, VER COMO UTILIZAR CLASES Y SI HAY UN POST DE COMO HACER ESTE PATRON EN PYTHON
def GeneratePdf(data, filename, strategy):
    strategy(data, filename)

GeneratePdf(y,'Prueba.pdf',StrategyOne)
GeneratePdf(y,'PruebaData.pdf',StrategyTwo)