# Data-Extraction-and-Translation

A data extraction and translation problem. The dataset consists of Arabic scanned PDF and their respective translated English PDF

The aim of the challenge is to build a model which can extract data from the Arabic scanned pdf and translates the text to English. 
here i was used convert_to_path function from pdf2image to convert each pdf page into image

then i saved image in JPEG format.after that i passed this image into pytesseract OCR library to read text from images
used image_to_string from pytesseract to convert text from image with the help of 'lang=' parameter to specifies language (arabic)

after that i used googletrans library to transalte arabic to english. Googletrans is a free and unlimited python library that implemented Google Translate API.The maximum character limit on a single text is 15k. that why i specified ddf page range in convert_from_path (first_page=1,last_page=9)

in second part i simply read english pdf (refrence for compaired and calculate BLEU score) 
cleaned both saved file, all character in lower case, removing unwanted character, spl character.
