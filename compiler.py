import re,glob,sys


def main():
    pass

variables = {}
identifier = []
addition = []
writecommand = []
regexleft = r'^[a-zA-Z_]'
regexright = r'([0-9]|[0-9]+[\\+\\-\\*\\/]{1}[0-9]+)+([\\+\\-\\*\\/]{1}[0-9]+)*$'
regexshow = r'^show+\s{1}'
regexwrite = r'write+\s{1}\"(.+?)\"'    
regexmid = r'[\=]'
regexcomm=r'^#.'
showwritereg = r'\bshow\b|\bwrite\b'
extention =  glob.glob('*.nycl')

class Interpreter:
    def __init__(self):
        pass
        
    def printTheValues(self,theValue):
        print(theValue)

    def printTheWriteCommand(self,writeText):
        writeText = writeText.replace('\n','')
        txt = writeText.split(' ')
        print(str(txt[1]))


inter = Interpreter()

def addToVariables(ide,add):   # take the 2 lists and add them in 1 dictionary    
    for k,v in zip(ide,add):   # for the variables
            variables[k] = v

def doTheCooking(identifier,addition,txt): # separate the string i give in the 
    identifier.append(txt[0])          # file in variables and do the result
    result = eval((txt[1]))            # bad approach, for now use the eval
    addition.append(result)
    addToVariables(identifier,addition)
    identifier.pop(0)
    addition.pop(0)
    # txt1 = identifier.pop(0)    
    # txt2 = addition.pop(0)
    # text = txt1 + '=' + str(txt2)
    # return text

def checkTheCommands(text,variables):
        text = text.strip()
        txt = text.split(' ')
        if (bool(variables)) == False:
            if re.match(showwritereg,txt[0]):
                print("This name of variable is committed from the system: \'%s\'" %(txt[0]))
            else:
                print("Undefined variable: \'%s\'" %(txt[1]))        
            # sys.exit(None)    
            return False
        else:        
            for key,value in variables.items():
                if key == txt[1]:
                    theValue = "The value of %s variable is: %s"%(txt[1],value)
                    return theValue
                # else:    
                #     print("Undefined variable: \'%s\'" %(txt[1]))
            if key != txt[1]:
                print("Undefined variable: \'%s\'" %(txt[1]))
                return False
                    

def checkTheVariables(txt):
    txt = txt.split('=')
    if re.match(regexleft,txt[0]) and re.match(regexright,txt[1]):
            # text = doTheCooking(identifier,addition)
        doTheCooking(identifier,addition,txt)  
            #print("The line matches: %s" %(text))  
    elif(txt[0] == '' or txt[1] == '\n') :
        print("Syntax error or undefined variable")
        return False 

def openTheFile(extention):    # takes every file with this extension from    
    for i in extention:        # the specific folder
        file = open('./' + i, 'r')
        return file

theFile = openTheFile(extention)   

for text in theFile:
        if text == '\n' or re.match(regexcomm,text):
            continue
        else:
            #temp.append(text.split())
            if re.match(regexshow,text):
                flag = checkTheCommands(text,variables) #solution
                if flag == False:
                    break
                else:    
                    inter.printTheValues(flag)
            elif re.match(regexwrite,text):
                inter.printTheWriteCommand(text) #solution           
            else:
                txt = text.replace(' ','')
                if '=' in txt:    
                    flag = checkTheVariables(txt)
                    if flag == False:
                        break
                elif re.match(showwritereg,text):
                    print('This name of variable is committed from the system: %s'%text)                     
                    break
                else:
                    print('Undefined variable: %s'%text)
                    break
