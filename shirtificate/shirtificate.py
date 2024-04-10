from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.image('./shirtificate.png', 10, 70, 190)
        self.set_font('Times', 'B', 24)
        self.cell(200, 5, "CS50 Shirtificate", ln=True, align="C")
        self.ln(5)

    def footer(self):
        pass

    def add_name(self, name):
        self.set_font('Times', 'B', 35)
        self.set_text_color(240, 240, 240)
        self.cell(0, 210, f'{name} took CS50', ln=True, align='C')

def main():
    name = input('Name: ')
    make_shirt(name)

def make_shirt(name):
    pdf = PDF()
    pdf.add_page(orientation='P', format='A4')
    pdf.add_name(name)
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/shirtificate
