from reportlab.pdfgen import canvas




def hello(c):
 c.drawString(200,800,"Hello World")
 c.drawString(50,750,"i love my  india and will always be proud of it")
 c.drawString(10,50,'thanks')






c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()