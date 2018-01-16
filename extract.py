import textract
import sentences_proccess
import csv

path = "input.pdf"

#Load pdf to text
text = textract.process(path, method='pdftotext')

#Split text to sentences
process = sentences_proccess.SplitSentence(text.decode('utf-8'))

#Save sentences to csv
with open('output.csv', 'w') as csvfile:
    fieldnames = ['id', 'sentence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

    writer.writeheader()
    i = 0;
    for sentence in process:
        sentence = sentence.replace("\n", " ")
        if len(sentence) >= 10:
            i += 1;
            writer.writerow({'id': str(i), 'sentence': sentence + "."})

