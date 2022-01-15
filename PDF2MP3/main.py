import pyttsx3
import PyPDF2
from tkinter import filedialog

#Get the file
location = filedialog.askopenfilename()
full_text =""

with open(location, 'rb') as book:

	try:
		reader = PyPDF2.PdfFileReader(book)
		audio = pyttsx3.init()
		print('\n')
		print('Recommended Speed is 115 for good experience')

		set_speed = input('Please Enter Your Preferred Reading Speed here ==> ')
		audio.setProperty('rate', int(set_speed))

		total_pages = reader.numPages

		print('\n')
		print('Location of File  -------> ' + location)
		print('\n')
		print('Total Number of Pages -------> ' + str(total_pages))

		try:
			for page in range(total_pages):
				next_page = reader.getPage(page)
				content = next_page.extractText()
				full_text += content

			audio.save_to_file(full_text, 'output.mp3')
			print("Converting... \n Please Wait....")
			audio.runAndWait()

		except:
			print('Task Failed Successfully! ')

	except:
		print('\n')
		print('--------->Cannot Read PDF<---------')
		print('\n')
		print('--------->Invalid PDF format<--------')
		print('\n')
		print('--------->Please select valid file which is in PDF format<--------')