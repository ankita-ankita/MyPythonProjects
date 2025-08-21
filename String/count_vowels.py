# count vowels

string = input ("Enter the string for which you want to count vowels: ")

vowel = 'aeiou'
count =0
for i in string.lower():
 if i in vowel: 
  count += 1

print("vowels number are : ", count)

