import pypdf
import os
# Made by Thiago Schulz 
merger = pypdf.PdfMerger()
name_pdf = input("Name the final PDF: ")

# path DIRs
pwd_arqv = "venv/Script-PDF/files/"
pwd_output ="venv/Script-PDF/output/"

# list Files
list_files = os.listdir(pwd_arqv)
list_files.sort()

# check if list is not null
if not list_files:
    print("Please insert pdf's in files directory!")
    
for file in list_files:
    if ".pdf" in file:
        merger.append(f"{pwd_arqv}/{file}")

# writing in output directory
merger.write(f"{pwd_output}{name_pdf}.pdf")
    




