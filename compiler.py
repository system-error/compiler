#regular expression for the identifier ^[a-zA-Z_]
#print kai insert times
import re,os

def doTheDictionaryJob(ide,add):
    for k,v in zip(ide,add):
            variables[k] = v

def doTheCooking(identifier,addition):
    identifier.append(txt[0])
    result = eval((txt[1]))
    addition.append(result)
    doTheDictionaryJob(identifier,addition)
    txt1 = identifier.pop(0)    
    txt2 = addition.pop(0)
    text = txt1 + '=' + str(txt2)
    return text
    
file = open('testfile.texter', 'r') 
variables = {}
identifier = []
addition = []
regexleft = r'^[a-zA-Z_]'
regexright = r'([0-9]|[0-9]+[\\+\\-\\*\\/]{1}[0-9]+)+([\\+\\-\\*\\/]{1}[0-9]+)*$'
regexshow = r'^show'
# regexmid = r'[^\=]'
for text in file:
    if text == '\n':
        continue
    else:
        if re.match(regexshow,text):
            text = text.strip()
            txt = text.split(' ')
            if (bool(variables)) == False:
                print("Undefined variable: \'%s\'" %(txt[1]))
            else:        
                for key,value in variables.items():
                    if key == txt[1]:
                        print("The value of %s variable is: %s"%(txt[1],value))
                        break
                    # else:    
                    #     print("Undefined variable: \'%s\'" %(txt[1]))
                if key != txt[1]:
                    print("Undefined variable: \'%s\'" %(txt[1]))          
        else:
            # if re.match(regexeq,text):
            #     print("Undefined variable:")
            # else:        
            txt = text.replace(' ','')
            txt = txt.split('=')
            if re.match(regexleft,txt[0]) and re.match(regexright,txt[1]):
                text = doTheCooking(identifier,addition)  
                print("The line matches: %s" %(text))  
            else:
                print("The line doesn't mach:  %s"%(text))    
                        
                     
# elif re.match(regexeq,check[1]):
#                 print("Undefined variable: \'%s\'" %(txt[0]))

#  check = text.split() 
# for i in check:
            #     if i != '=':
            #         continue
            #     else: 










#regex = r'^[a-zA-Z_]+(\=)+([0-9]|[0-9]+[\\+\\-\\*\\/]{1}[0-9]+)+([\\+\\-\\*\\/]{1}[0-9]+)*$'

# summary = eval(text)
    # print (summary) 
 # if re.match(regex,txt):
    #     txt = txt.split('=')
    #     identifier.append(txt[0])
    #     addition.append(eval(txt[1]))
    #     txt1 = identifier[0]    
    #     txt2 = addition[0]
    #     text = txt1 + '=' + str(txt2)
        
    #     print("The line matches: %s" %(text))
    # else:
    #     print("The line doesn't mach:  %s"%(text))