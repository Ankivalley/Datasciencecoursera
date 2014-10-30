http://www.pythonchallenge.com/pc/def/map.html

Base_Dict = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:"", 13:"", 14:"", 15:"", 16:"", 17:"", 18:"", 19:"", 20:"", 21:"", 22:"", 23:"", 
24:"", 25:"", 26:""}

abc = list("abcdefghijklmnopqrstuvwxyz")



def insert_abc():
    count = 0
    for c in abc:
        if count <= 26:
            Base_Dict[count] = c
            count += 1
        else:
            return Base_Dict
            break

def get_Key(v):
    for key, value in Base_Dict:
        if value == v:
            return key
    return None

def charachter_shift(text):
    New_Text = []
    for C in text:
        New_Key = (get_Key(C) + 2
        New_Charachter = Base_Dict.get(New_Key, Default=None)
        New_Text.append(New_Charachter)
    print New_Text
    
charachter_shift("Hello world")
        
        
                    
    