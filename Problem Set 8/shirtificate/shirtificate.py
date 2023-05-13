# importing the FPDF class from the fpdf module
from fpdf import FPDF


# Defining a new class Shirtificate that inherits from the FPDF class
class Shirtificate(FPDF):
	# defining a constructor method that takes a name parameter
	def __init__(self, name):
		# call the constructor of the parent class (FPDF), which sets up the base PDF object
		super().__init__()
		# add a new page to the pdf
		self.add_page()
		# set the font style and size
		self.set_font("helvetica", "B", 50)
		# creating a new cell that spans the full width of the page and has a height of 60 points with the specified text
        # new_x and new_y parameters specify the x and y positions of the cell, and align parameter specifies the text alignment
		self.cell(0, 60, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
		# adding an image to the PDF document
        # the image file name is "shirtificate.png" and it is scaled to the page width (self.epw).
		self.image("shirtificate.png", w = self.epw)
		# setting font size
		self.set_font_size(32)
		# setting the text colour (in RGB)
		self.set_text_color(255, 255, 255)
		# addint the text to the pdf doc and centering the text (x and y)
		self.text(x = 48, y = 140, txt = f"{name} took CS50")



# creating a new object with the name entered by the user
shirtificate = Shirtificate(input("Name: "))
# save the pdf with a specified file name
shirtificate.output("shirtificate.pdf")