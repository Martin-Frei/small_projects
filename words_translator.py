

from Number_translator import number_to_words as ntw

def word_to_number(word):
    numbers_dic = {
            'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'twenty': 20 , 'thirty': 30 , 'forty': 40 , 'fifty': 50 , 
            'sixty': 60 , 'seventy': 70 , 'eighty': 80 , 'ninety': 90 ,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 
            'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19
            }
    
    place_value_dic = { 'thousand' : 1000 , 'million' : 1000000 , 'billion' : 1000000000 }    
    
    
    wordlist = word.split(' ')
    print(wordlist)
    translation = 0
    temp = 0    
    # print without koma !!
    for word in wordlist:
        
        if word in numbers_dic:
            temp = temp + numbers_dic[word]         
            
        elif word in place_value_dic:           
           temp = temp * place_value_dic[word]
           translation = translation + temp
           temp = 0
           
        elif word == 'hundred' :
            temp = temp * 100     
     
    translation = translation + temp
    
    
    return translation



while True :
    user_number = input('Give me a number with max 12 digit:  ')
    
    if len(user_number) > 12:
        print('Sorry, to many digit. Try again')
        continue
        
    if not user_number.isdigit():
        print('Sorry, wrong input. Try again')
        continue
    
    if user_number == '0':
        print('zero')   
        break     
    else :        
        translation = ntw(int(user_number))
        break

x = word_to_number(translation)

print('Translation is', x)