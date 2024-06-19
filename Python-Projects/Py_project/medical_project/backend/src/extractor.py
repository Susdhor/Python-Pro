
from pdf2image import convert_from_path
import pytesseract

import numpy as np
import util

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

POPPLER_PATH = r'C:/Users/E7440/poppler-23.11.0/Library/bin'


def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    for page in pages:
        processed_img = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_img, lang='eng')
        document_text = '\n' + text

    return document_text

    # if file_format == 'prescription':
    #     pass
    # elif file_format == 'patient_detais':
    #     pass

    # else:
    #     raise Exception('Invalid file format')


if __name__ == '__main__':
    data = extract(
        '../medical_project/patient_details/pd_2.pdf', 'prescription')
    print(data)
