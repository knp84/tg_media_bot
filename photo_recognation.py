from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Pyton310\Project\venv\Lib\TES\tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))  
    return text

s = ocr_core('score.jpg')

sum_score = 0
count_score = 0

for i in range(len(s) - 1):
    sum_score += int(s[i])
    count_score += 1

avr_score = sum_score / count_score
print(avr_score)

question = input('До какого числа следует посчитать?(Введите цифру)\n')

if question == '4':
    if avr_score >= 3.5:
        print('У вас уже 4 или 5')
    else:
        count_score_5 = count_score_4 = avr_score_5 = avr_score_4 = 0
        sum_score_5 = sum_score_4 = sum_score
        while avr_score_5 < 3.5:
            sum_score_5 += 5
            count_score_5 += 1
            avr_score_5 = sum_score_5 / (count_score_5 + count_score)
        while avr_score_4 < 3.5:
            sum_score_4 += 4
            count_score_4 += 1
            avr_score_4 = sum_score_4 / (count_score_4 + count_score)
        print(f'До {avr_score_4} вам нужно {count_score_5} пятёрок или {count_score_4} четвёрок')
elif question == '5':
    if avr_score >= 4.5:
        print('У вас уже 5')
    else:
        sum_score_5_2 = sum_score
        count_score_5_2 = avr_score_5_2 = 0
        while avr_score_5_2 < 4.5:
            sum_score_5_2 += 5
            count_score_5_2 += 1
            avr_score_5_2 = sum_score_5_2 / (count_score_5_2 + count_score)
        print(f'До {avr_score_5_2} вам осталось {count_score_5_2} пятерок')