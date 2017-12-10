from nltk.tokenize import sent_tokenize
import os

n = 50

def writingToFile(addr):
    open(addr, 'w', encoding='utf-8').close()
    filenames = []
    for i in range(1, n + 1):
        filenames.append('aligned' + str(i) + '.txt')
    with open(addr, 'w', encoding='utf-8') as outfile:
        for fname in filenames:
            with open(fname, encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)
            os.system('del ' + fname)


for i in range(1, n+1):
    open('textENG.txt', 'w', encoding='utf-8').close()
    open('textCRT.txt', 'w', encoding='utf-8').close()
    tmpENG = open(str(i) + '\english.txt', encoding='utf-8').readlines()
    en = ''
    for line in tmpENG:
        if line not in ['\n', '\r\n']:
            line = line.replace('...', '')
            line = line.replace('..', '')
            line = line.replace('•', '')
            en = en + line
    tmpCRT = open(str(i) + '\croatian.txt', encoding='utf-8').readlines()
    cr = ''
    for line in tmpCRT:
        if line not in ['\n', '\r\n']:
            line = line.replace('...', '')
            line = line.replace('..', '')
            line = line.replace('•', '')
            cr = cr + line
    sent_tokenize_list_ENG = sent_tokenize(en)
    sent_tokenize_list_CRT = sent_tokenize(cr)
    textENG = open('textENG.txt', 'w', encoding='utf-8')
    textCRT = open('textCRT.txt', 'w', encoding='utf-8')
    for item in sent_tokenize_list_ENG:
        if not str(item) in ['\n', '\r\n']:
            textENG.write("%s\n" % item)
    for item in sent_tokenize_list_CRT:
        if not str(item) in ['\n', '\r\n']:
            textCRT.write("%s\n" % item)
    textCRT.close()
    textENG.close()
    os.system('cd > tmp' + str(i) + '.dict')
    os.system('hunalign\hunalign.exe -text -utf -realign tmp' + str(i) + '.dict textENG.txt textCRT.txt > aligned' + str(i) + '.txt')
    os.system('del tmp' + str(i) + '.dict')

writingToFile('result.txt')

