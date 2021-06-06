'''Python program for generating random password'''

#Importing the modules
import random
import string

#Data setting
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

#Generating Passwords
class Password:
        
        #Initialising variables
        def __init__(self,char,length):
                self.char = char
                self.length = length
                self.charset = []
                self.pwd = 'Not Set'
                
        #Setting character set
        def setchar(self):
                if 'l' in self.char:
                        self.charset.extend(lowercase)
                if 'u' in self.char:
                        self.charset.extend(uppercase)
                if 'd' in self.char:
                        self.charset.extend(digits)
                if 's' in self.char:
                        self.charset.extend(symbols)

        #Generating password	
        def pwdgen(self):
                pwdlist = random.choices(self.charset, k = self.length)
                self.pwd = ''.join(pwdlist)

        #Getting character set
        def getset(self):
                return self.charset

        #Getting password
        def getpwd(self):
                return self.pwd
