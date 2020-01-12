
import PyPDF2
from PIL import Image
import pytesseract 
#import sys 
from pdf2image import convert_from_path 
#import os
from googletrans import Translator
from nltk.translate.bleu_score import sentence_bleu
import numpy as np
import h5py
import argparse


def input_paths(stud_path,ref_path):
    stud_pages = convert_from_path(stud_path,200,first_page=1,last_page=9)
    image_counter = 1
    outfile_stud = "output_student_text.txt"
    f = open(outfile_stud, "a",encoding="utf-16")
    for page in stud_pages:
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        text=str(pytesseract.image_to_string(Image.open("page_"+str(image_counter)+".jpg"),lang='ara'))
        translator=Translator()
        a=translator.translate(text,dest='english')
        f.write(a.text.lower())
        image_counter = image_counter + 1
    f.close()
    
    
    ref_pages = convert_from_path(ref_path,200,first_page=1,last_page=9)
    image_counter = 1
    outfile_ref = "output_reference_text.txt"
    f = open(outfile_ref, "a")
    for page in ref_pages:
        filename = "page_origin_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        text=str(pytesseract.image_to_string(Image.open("page_origin_"+str(image_counter)+".jpg")))
        f.write(text.lower())
        image_counter = image_counter + 1

    f.close()
    
#----------------------------------------------------------------------------------------------------
input_paths('D:\DPA\Training Set\Al Othaim 3Q_Arb.pdf','D:\DPA\Training Set\Al Othaim 3Q_Eng.pdf')


#-----------------------------------------------------------------------------------------------
ref = open('output_reference_text.txt', 'r').readlines()
cand = open('output_student_text.txt', 'r',encoding='utf-16').readlines()
import re

ref2=[re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in ref]
cand2=[re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in cand]
a="final_ref_text.txt"
b="final_stud_text.txt"
f = open(a, "a",encoding="utf-16")
f.write(str(ref2))
f.close()

s = open(b, "a",encoding="utf-16")
s.write(str(cand2))
s.close()

import numpy as np
import h5py
import argparse

def argparser():
        Argparser = argparse.ArgumentParser()
        Argparser.add_argument('--reference', type=str, default='final_ref_text.txt', help='Reference File')
        Argparser.add_argument('--candidate', type=str, default='final_stud_text.txt', help='Candidate file')

        args = Argparser.parse_args()
        return args

args = argparser()

reference = open(args.reference, 'r').readlines()
candidate = open(args.candidate, 'r').readlines()

if len(reference) != len(candidate):
    raise ValueError('The number of sentences in both files do not match.')

score = 0.

for i in range(len(reference)):
    score += sentence_bleu([reference[i].strip().split()], candidate[i].strip().split())

score /= len(reference)
print("The bleu score is: "+str(score))




    
