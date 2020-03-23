import sys
import os
'''
import win32com.client
wdFormatPDF = 17
in_file = os.path.abspath ("document.docx")
print(in_file)
out_file = os.path.abspath("document.pdf")
word = win32com.client.DispatchEx('Word.Application')

doc = word.Documents.Open(in_file)
doc.Variables.Item("firma").Value = "Емитент"
doc.Variables.Item("email").Value = "Адрес"
doc.Variables.Item("fio").Value = "Директор"
doc.Fields.Update
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
'''
from docxtpl import DocxTemplate

import win32com.client
wdFormatPDF = 17


fio1='ИВАНОВ222'
firma1='Рога и копыта222'
email1='ostap222@roga.ru'
in_file = os.path.abspath ("document.docx")
out_file=firma1+'.docx'
doc = DocxTemplate(in_file)
context = { 'fio' : fio1,'firma' : firma1,'email' : email1 }
doc.render(context)
doc.save(out_file)
in_file=os.path.abspath(out_file)
out_file=os.path.abspath(firma1+'.pdf')
word = win32com.client.DispatchEx('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
word.Documents.Close()
word.Quit()