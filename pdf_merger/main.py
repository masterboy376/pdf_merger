import PyPDF2

pdffiles = ['input/1.pdf','input/2.pdf','input/3.pdf','input/4.pdf']

merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdffile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfReader)
pdffile.close()

merger.write("output/merged.pdf")