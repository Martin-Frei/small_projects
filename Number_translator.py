



def number_to_words(number):
    '''
    This function takes a number as an integer with max 12 digit 
    and converts it to a written number
    '''
    # The number was reversed and changed to a string, so the number iterable
    number = str(number)
    number = number[::-1]
    
    # This dic are use to replace the actual digit to written number
    ones_dic ={'1' : 'one','2':'two', '3':'three', '4':'four', '5':'five', '6': 'six', '7': 'seven','8': 'eight', '9': 'nine', '0': ''}
    tens_dic ={'1' : 'ten', '2':'twenty', '3': 'thirty', '4' : 'forty', '5':'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9':'ninety','0': ''}
    place_value_dic ={0 : '', 1 :'', 2 :'hundred', 3 : 'thousand', 4 : '', 5 : '', 6 : 'million', 7 :'', 8 :'', 9 :'billion', 10 : '', 11: ''}
    teens_dic ={'10' : 'ten', '11' :'eleven', '12' : 'twelve', '13' : 'thirteen', '14' : 'fourteen', '15' : 'fifteen', '16' : 'sixteen', '17' : 'seventeen', '18' : 'eighteen', '19' : 'nineteen'}
    
    translation = ''
    
    
    if len(number) ==1:
        translation = ones_dic[number] + ' ' + translation
    
    else:    
        for index in range(len(number)):
            
            try:
                if index %3 == 0 and number[index +1] != '1'  :
                    translation = place_value_dic[index] + ' ' + translation
                    translation = ones_dic[number[index]] + ' ' + translation
            except IndexError :
                translation = place_value_dic[index] + ' ' + translation
                translation = ones_dic[number[index]] + ' ' + translation
                continue
                
            if index %3 ==1 and number[index] == '1' :
                translation = place_value_dic[index - 1] + ' ' + translation
                translation = teens_dic[number[index]+ number[index -1]] + ' ' + translation
                
            elif index %3 ==1 and number[index] != '1' :
                translation = place_value_dic[index] + ' ' + translation
                translation = tens_dic[number[index]] + ' ' + translation
                
            elif index %3 == 2 :
                translation = ones_dic[number[index]] + ' ' + (place_value_dic[2] if number[index] != '0' else '' ) + ' ' + translation
        
    # Split all element from the translation to a list, remove the spaces  
    list = translation.split()    
    # Join the list to a string with only 1 space between
    translation = ' '.join(list)
    return translation
 
# print(__name__)
 
if __name__ == '__main__' :
       
    # print('I come from file 1 ')    
    # Usage example
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
        else :        
            print(number_to_words(int(user_number)))
            break
















