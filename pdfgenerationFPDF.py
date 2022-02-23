from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(0, 0, 0)

pdf.image('bg_report1.png', x = 0, y = 0, w = 210, h = 297)

x = 70
y = 70
pdf.set_xy(x, y)
w = 10
h = 10
BORDER = 0
ALIGN = 'L'
pdf.cell(w, h, "Hello PDF", border = BORDER, align = ALIGN, fill = False)

pdf.output('Automated PDF Report.pdf')
