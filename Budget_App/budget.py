import math

class Category:
  type=''
  ledger=[]
  balance=0.0
  def __init__(self,typ):
    self.type=typ
    self.ledger=[]
    self.balance=0.0
  
  #deposit an amount of money
  def deposit(self,amount,description=''):
    dummy={}
    dummy["amount"]=float(amount)
    self.balance=amount+self.balance
    dummy["description"]=description
    self.ledger.append(dummy)
    
  #withdraw money from a category  
  def withdraw(self,amount,description=''):
    dummy={}
    dummy["amount"]=float(-amount)
    dummy["description"]=description
    if(self.check_funds(amount)):
      self.ledger.append(dummy)
      return True  
    else:
      return False

  #get balance of a category  
  def get_balance(self):
    final_balance = self.balance
    for i in self.ledger:
      if (i["amount"]<0):
        final_balance = final_balance + float(i['amount'])
    return final_balance
  
  #transfer money to another category
  def transfer(self,amount,obj):
    string = str(obj.type)
    string1 = str(self.type)
    string ="Transfer to " + string
    string1 ="Transfer from " + string1
    if (self.check_funds(amount)):
      self.withdraw(amount,string)
      obj.deposit(amount,string1)
      return True
    else:
      return False
    
  #check whether the necessary funds exist
  def check_funds(self,amount):
    bal = self.get_balance()
    if(bal>=amount):
      return True
    else:
      return False
  
  #print info
  def __repr__(self):
    name = self.type
    header = name.center(30,"*")+"\n"
    stri = str(float(self.get_balance()))
    for i in self.ledger:
      a=i["description"]
      b=i["amount"]
      c=format(b,'.2f')[0:7].rjust(7)
      strings = str(a)[0:23].ljust(23) + c + "\n"
      header = header + strings
    header = header + "Total: " + stri
    return header
        
def create_spend_chart(categories):
  #create dimensions of output
  dict = {}
  output = ''
  strings = []
  for i in categories:
    key = i.type
    initial = i.balance
    final = i.get_balance()
    number = math.floor(initial-final)
    dict[key] = math.floor(number/10)*10
  
  indexes = (len(dict.keys())*3)+1
  max = 100
  #create the necessary strings line by line
  strings.append("Percentage spent by category\n")
  for i in range(100,-10,-10):
    output= str(i).rjust(3)+'|'
    
    for j in dict.keys():
      if (dict[j]>=i):
        output = output + " o "
      else:
        output = output + "   "
    output = output + " \n"
    strings.append(output)   

  output=''
  for i in range(0,indexes):
    output = output + "-"
  output = output + '\n'
  strings.append(output.rjust(5+indexes))

  output = ""
  lengths = 0
  for k in dict.keys():
    letters = 0
    for m in k:
      letters = letters + 1
    if (lengths <= letters):
      lengths = letters
      
  for i in range(0,lengths):
    output = output + "    ".ljust(4)
    for j in dict.keys():
      if (i<len(j)):
        output = output + " " + j[i] + " "
      else:
        output = output + "   "
    output = output + ' \n'
  strings.append(output[:-1])
  #join all the lines so as to get the full string  
  strings=''.join(strings)
  return strings
