# spør i en loop som varer 8 ganger og saver de i både en dictionary og en array
def ask_code():
    code = {}
    code_ar = []
    for x in range(8):
        char = input()
        if(char in code):
            code[char] += 1
        else:
            code[char] = 1
        code_ar.append(char)
    
    for x in range(len(code_ar)):
        try:
            code_ar[x] = int(code_ar[x])
        
        except:
            pass

    return (code, code_ar)

# calculater max antall tries for å løse koden og hvilke karakterer som er ukjente
def calculate_tries_unknown(import_dict):
    max_tries = 1
    ukjente = []
    for key in import_dict.keys():
        try:
            x = int(key)
        except:
            max_tries *= 10
            ukjente.append(key)
    return ukjente, max_tries

#funksjon som printer info om hva de ukjente er og hvor mange forsøk som trengs
def print_info(ukjente, tries):
    printstatement = "the unknown are:"
    for x in ukjente:
        printstatement += " " + x
    printstatement += ".\nmax amount of tries: " + str(tries) + " tries."
    print(printstatement)

#funksjon som tar 2 arrays or setter de opp mot hverandre og returner koden med en ukjent
def calculate_code(first, second):
    solved_arr = []
    løst_kode = {}

    for idx in range(8):
        if(type(first[idx]) != type(second[idx])):

            if(isinstance(first[idx], int)):
                solved_arr.append(first[idx])

            elif(isinstance(second[idx], int)):
                solved_arr.append(second[idx])
                løst_kode[first[idx]] = second[idx]

        elif(type(first[idx] == type(second[idx]))):
            found_match = False
            
            for x, y in løst_kode.items():
                if(x == first[idx]):
                    solved_arr.append(y)      
                    found_match = True
                    break
            
            if(not found_match):
                solved_arr.append(first[idx])


    return solved_arr

#siden det kun er en karakter igjen, betyr det at det max er 10 løsninger for koden
def print_codes(solved_arr):
    all_solved = []
    for x in range(10):

        new_arr = []
        for i in solved_arr:
            if(isinstance(i, str)):
                new_arr.append(x)
            else:
                new_arr.append(i)
        
        print(str(x) + ": " + str(new_arr))



### FØRSTE KEYCARD ###
print("-----------------\nfirst code:\n")
first_dict, first_arr = ask_code()
first_unknown, first_max_tries = calculate_tries_unknown(first_dict)
print_info(first_unknown, first_max_tries)

### ANDRE KEYCARD ###
print("\n-----------------\nsecond code:\n")
second_dict, second_arr = ask_code()
print("Your codes are:\n-----------------\n")
print_codes(calculate_code(first_arr, second_arr))
