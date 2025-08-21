# Reverse a word/string

string = input ("Enter the word you want to reverse: ")
print ("Reverse of your string is: ", string[::-1])

# Reverse a sentence 
list1 = input ("Enter the sentence you want to reverse: ").split(" ")
rev = "" 
for i in list1[::-1]:
 rev +=  i +" "
print ("Reverse of your sentence is: ", rev)
