from nltk.tokenize import sent_tokenize
import os

n = 50

def saveResult(addr):
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

def deleteSpecialSymbols(line):
    line = line.replace('...', '')
    line = line.replace('..', '')
    line = line.replace(' . . . ', '')
    line = line.replace(' . . ', '')
    line = line.replace('. . .', '')
    line = line.replace('. .', '')
    line = line.replace(' . ', '')
    line = line.replace(' .', '')
    line = line.replace('. ', '')
    line = line.replace('	.	', '')
    line = line.replace('\t', '')
    line = line.replace('\t.\t', '')
    line = line.replace('•', '')
    line = line.replace('▪', '')
    line = line.replace('~', '')
    line = line.replace('*', '')
    line = line.replace('@@', '')
    line = line.replace('@@@', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('', '')
    line = line.replace('�', '')
    line = line.replace('ꕲ', '')
    line = line.replace('ꘃ', '')
    line = line.replace('ꔉ', '')
    line = line.replace('ꕊ', '')
    line = line.replace('ꔂ', '')
    line = line.replace('ꔦ', '')
    line = line.replace('ꔅ', '')
    line = line.replace('❶', '')
    line = line.replace('❷', '')
    line = line.replace('❸', '')
    line = line.replace('❹', '')
    line = line.replace('❺', '')
    line = line.replace('❻', '')
    line = line.replace('❼', '')
    line = line.replace('❽', '')
    line = line.replace('❾', '')
    line = line.replace('◉', '')
    line = line.replace('◀', '')
    line = line.replace('▶', '')
    line = line.replace('■', '')
    return line

for i in range(1, n+1):
    open('textENG.txt', 'w', encoding='utf-8').close()
    open('textCRT.txt', 'w', encoding='utf-8').close()
    tmpENG = open(str(i) + '\english.txt', encoding='utf-8').readlines()
    en = ''
    for line in tmpENG:
        if line not in ['\n', '\r\n']:
            line = deleteSpecialSymbols(line)
            if line not in ['.\n', '.\r\n', ' .\n', ' .\r\n', '. \n', '. \r\n', ' . \n', ' . \r\n']:
                en = en + line
    tmpCRT = open(str(i) + '\croatian.txt', encoding='utf-8').readlines()
    cr = ''
    for line in tmpCRT:
        if line not in ['\n', '\r\n']:
            line = deleteSpecialSymbols(line)
            if line not in ['.\n', '.\r\n', ' .\n', ' .\r\n', '. \n', '. \r\n', ' . \n', ' . \r\n']:
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

saveResult('result.txt')
