from translate import Translator

translator = Translator(to_lang='zh-TW')
translation = translator.translate('this is a pen!')
print(translation)

text1 = input('Sentences that you want to translate:')
trans1 = translator.translate(text1)
print(trans1)


try:
   with open('text.txt',mode= 'r') as my_file:
     text = my_file.read()
     trans = translator.translate(text)
     print(trans)
     with open('text-zh.txt', mode = 'w') as my_file1:
         text1 = my_file1.write(trans)
except FileNotFoundError as err:
    print('check your file path')


