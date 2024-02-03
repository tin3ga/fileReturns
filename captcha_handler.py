import os
import pytesseract
from PIL import Image


class CaptchaHandler:
    @staticmethod
    def process_captcha():
        """takes a png image as input. converts it into a string. performs calulation based on operation. returns
        answer"""
        image = Image.open('./captcha.png')
        pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_OCR_PATH')
        text = pytesseract.image_to_string(image=image, lang='eng', config='--oem 1')
        print(text)
        text = text[:-2]
        print(text)
        if '-' in text:
            numbers = text.split('-')
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            captcha_answer = num1 - num2
            print('sub')
            print(captcha_answer)
            return captcha_answer
        elif '+' in text:
            numbers = text.split('+')
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            captcha_answer = num1 + num2
            print('add')
            print(captcha_answer)
            return captcha_answer


