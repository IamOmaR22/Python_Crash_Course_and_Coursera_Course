# pip install pyttsx3

import pyttsx3
import PyPDF2
book = open('cheatsheet-a5.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
a = pyttsx3.init()
for i in range(7, pages): # 7 is the page number. (7, 15)
    page = pdfReader.getPage(i) 
    text = page.extractText()
    a.say(text)
    a.runAndWait()
