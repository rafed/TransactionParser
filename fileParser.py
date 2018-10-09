from lxml import etree
from fpdf import FPDF
import os, sys

Headers = ["Message Header","Reprint From MFA-0000-000000",
           "Instance Type and Transmission","Message Text",
           "Message Trailer","Report Footer"]	#Check if any other headers	

def parseXML(file):
    NS = "{urn:schemas-microsoft-com:office:spreadsheet}"

    tree = etree.parse(file)

        
    root = tree.getroot()

    worksheet = root.find(f"{NS}Worksheet")
    table = worksheet.find(f"{NS}Table")

    rows = table.findall(f'{NS}Row')

    msgs = []
    for i,row in enumerate(rows):
        data = row.find(f"{NS}Cell").find(f"{NS}Data")
        if data==None or data.text!="Message Text": continue
        j = i+1
        msg = ''.join(rows[j].find(f"{NS}Cell").find(f"{NS}Data").itertext())
        while msg.split("\n")[0].startswith("F20") :
            print(i+1)
            msgs.append(msg)
            j+=1
            msg = ''.join(rows[j].find(f"{NS}Cell").find(f"{NS}Data").itertext())
    return msgs

def parseText(file):
    global Headers

    with open(file) as fileHandler:
        lines = fileHandler.readlines()

    msgs = []
    for i,line in enumerate(lines):
        if "Message Text" in line:
            msg = ""
            j = i+1
            curLine = lines[j]
            while all([head not in curLine for head in Headers]):
                msg+=curLine+"\n"
                j+=1
                curLine = lines[j]
            msgs.append(msg)
    return msgs

def makeCSV(msgs, outputDir):
    outputFile = os.path.join(outputDir, "csv.csv")

    file = open(outputFile, "w")
    i=1
    for msg in msgs:
        msg = msg.lstrip()
        s = "Message %d,\"%s\"\n" % (i,msg)
        file.write(s)
        i = i + 1

    file.close()


def makePdf(msgs, outputDir):
    outputFile = os.path.join(outputDir,"pdf.pdf")
    print(outputFile)

    pdf = FPDF()

    i = 1
    for msg in msgs:
        msg = msg.lstrip()

        pdf.add_page()

        pdf.set_font('Arial', 'B', 12)
        s = "Message %d\n" % (i)
        pdf.multi_cell(180, 10, s)

        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(180, 10, msg)

        i = i + 1

    pdf.output(outputFile, 'F')
 

def parseFile(inputFile, outputDir):
    

    if inputFile.endswith("txt"):
        msgs = parseText(inputFile)
    elif inputFile.endswith("xml") or inputFile.endswith("xls"):
        msgs = parseXML(inputFile)
    else:
       return []

    return msgs











