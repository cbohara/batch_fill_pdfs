Task: 
batch fill PDFs based on csv file data

Tools:
PDFescape is used to create and name fields to be filled out in PDF

http://www.pdfescape.com/

PDFtk is a PDF toolkit that is used to populate the fields

https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/

The download link on the website for MacOS is buggy
Use updated link below for download 

https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk_server-2.02-mac_osx-10.11-setup.pkg

fdf files contain the field data used to populate PDFs
fdfgen is used to generate the fdf file

https://github.com/ccnmtl/fdfgen

Resources:

https://stackoverflow.com/questions/1890570/how-can-i-auto-populate-a-pdf-form-in-django-python

https://stackoverflow.com/questions/10476265/batch-fill-pdf-forms-from-python-or-bash

Instructions:

Open terminal program

Install a package manager on your computer. Copy and paste the line below into the terminal and hit enter:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install the programming language you will use to run the script. Copy and paste the line below into your terminal and hit enter:

```
brew install python3
```

Create and activate a virtual environment

```
python3 -m venv venv
. venv/bin/activate
```

Install the python module that will take care of filling in the pdf.  Copy and paste the line below into your terminal and hit enter:

```
pip3 install fdfgen
```

Now you have everything you need installed

Now you will need to enter into the folder where the files were downloaded

```
cd Downloads
```

If you enter ls you should see the listing of files in the Download folder

Now to run a test execution of the script using the same data I used to fill out the PDFs earlier today enter the following into your terminal

```
python3 solid_fill_pdf.py GR5056.pdf data.csv
```

When you run this script it will generate a folder called output in the location you executed the script

The pdfs will be in the output folder
