
import re

symbols = ["()","[]","{}","'",";","=","."] 
operators = ['+','-','*','/','&','|','~','<','>']
Program_components = ['class','constructor','method','function']
Primitive_types = ['int','boolean','char','void']
variable_declaration = ['var','static','field:']
statements = ['let','do','if','else','while','return']
constant_values = ['true','false','null']
object_reference = ['this:']

file = open('lexical.txt','r+')
contents = file.read()
splitCode = contents.split() 
length = len(splitCode)      
for i in range(0,length):
    if splitCode[i] in symbols:
        print("symbols -->",splitCode[i])
        continue
    if splitCode[i] in operators:
        print("Operators --> ",splitCode[i])
        continue
    if splitCode[i] in Program_components:
        print("Program Components -->",splitCode[i])
        continue
    if splitCode[i] in Primitive_types:
        print("Primitive types -->",splitCode[i])
        continue
    if splitCode[i] in variable_declaration:
        print("variable declaration -->",splitCode[i])
        continue
    
    if splitCode[i] in statements:
        print("statements -->",splitCode[i])
        continue
    if splitCode[i] in constant_values:
        print("constant values -->",splitCode[i])
        continue
    if splitCode[i] in object_reference:
        print("object refernce -->",splitCode[i])
        continue
    
    
    if re.match(r'^[-+]?[0-9]+$',splitCode[i]):
        print("Numerals --> ",splitCode[i])
        continue
    if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):
        print("Identifier --> ",splitCode[i])
        