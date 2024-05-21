from fpdf import  FPDF

# Creates a new class, passing in the FPDF class
class Pdf(FPDF):
    def header(self):
        ''' Add header '''
        # Moves cursor down
        self.set_y(30)
        # Set font
        self.set_font("times", "", 42)
        # Add cell with text, centering it in cell, and horizontally on page
        self.cell(txt="CS50 Shirtificate", align="C", center=True)

    def add_shirt(self, name):
        ''' Add shirt '''
        self.add_page()
        # Add image, with a width of 180, position x at 15 since the width (210-180) / 2 = 15 leaving 15 mm on each side
        self.image("shirtificate.png", x=15, y=70, w=180)

        ''' Overlay text on shirt '''
        # Set font
        self.set_font("helvetica", "", 24)
        # Text to white
        self.set_text_color(255, 255, 255)
        # Move cursor down
        self.set_y(130)
        # Add text to shirt
        self.cell(txt=f"{name} took CS50", align="C", center=True)





def main():

    pdf = Pdf()
    name = input("What's your name? ")
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()