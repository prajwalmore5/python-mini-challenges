# --------------
#Code starts here
def palindrome(num):
    while True:
        num+=1
        if str(num) == str(num)[::-1]:
         return num
         break

print(palindrome(123))


# --------------
#Code starts here

#Function to find anagram of one word in another

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)

#Code ends here


# --------------
#Code starts here
def check_fib(num):
    if num == 0: return False
    elif num == 1: return True
    else:
        A = 1
        B = 1
        FLIP = True
        while(True):
            new = A + B
            if new > num: return False
            elif new == num: return True
            else:
                if(FLIP):
                    A = new 
                    FLIP = not FLIP
                else:
                    B = new
                    FLIP = not FLIP


# --------------
def compress(word):
    word = word.lower()
    if len(word) == 0:
        return None
    final_arr = []
    index = 0
    letter = word[0]
    
    for el in word:
        if el == letter and ord(el) == ord(letter):
            index += 1
        else: 
            final_arr.append(letter + repr(index))
            letter = el
            index = 1
            
    final_arr.append(letter + repr(index))       
    return "".join(final_arr)

print(compress("xxcccdex"))


# --------------
#Code starts here

def k_distinct(string,k):
    string = string.lower()
    if len(list(set(string))) == k:
        return True
    else:
        return False
        
print(k_distinct('SUBBOOKKEEPER',8))
#Code ends here


