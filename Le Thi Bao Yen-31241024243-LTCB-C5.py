#1. 1. Write a Python program to calculate the length of a string.
#import string

a=(input("Enter string:"))
print(len(a))

#2. 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.

b=input("Enter string:")
c=len(b)
if c>2:
    x=b[0:2]
    y=b[-2:]
    print(x+y)
else:
    print(" ")

#3. 4. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

a=input("Enter string:")
def replace_char(a):
    b=a[0]
    a=a.replace(b,'$')
    a=b+a[1:]
    return a
print(replace_char(a))

#4. 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz

str1=input("Enter string 1:")
str2=input("Enter string 2:")
print(str1,str2)
str1_new=str2[0:3]+str1[3:]
str2_new=str1[0:3]+str2[3:]
print(str1_new,str2_new)

#5. 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.

a=input("Enter string:")
if len(a) <3:
    print(a)
elif a[-3:] =="ing":
    print(a+ "ly")
else:
    print(a+ "ing")

#6. 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def find_longest_word(words_list):
    longest_word=max(words_list, key=len)
    return longest_word, len(longest_word)
words=(["LTCB","Exercises", "LBY"])
longest,length=find_longest_word(words)
print("Longest word:", longest)
print("Length of longest word:", length)

#7. 9. Write a Python program to remove the nth index character from a nonempty string.

x=input("Enter string:")
y=int(input("Enter index number:"))
a=x[0:y]
b=x[y+1:]
print("String after remove nth index:", a+b)

#8. 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.

x=input("Enter string:")
new_string=x[-1]+x[1:-1]+x[0]
print("String after change:",new_string)

#9.11 Write a Python program to remove characters that have odd index values in a given string.
x=input("Enter string:")
new_string=""
for index, letter in enumerate(x):
    if index % 2 == 0:
        new_string += letter
print("String after removing Odd index:",x)
print(new_string)

#10. 12. Write a Python program to count the occurrences of each word in a given sentence.
x=input("Enter string:")
y=input("Enter word:")
a=[]
count=0
a=x.split(" ")
for i in range(0,len(a)):
    if(y==a[i]):
        count+=1
print("The occurrences of word in a given sentence:", count)

#11. 13. Write a Python script that takes input from the user and displays that input back in upper
# and lower cases.
x=input("Enter:")
print(x.upper())
print(x.lower())

# 12.16. Write a Python function to insert a string in the middle of a string.
x=input("Enter string 1:")
y=input("Enter string 2")
def insert_string_middle(x,y):
    mid=len(x)//2
    return x[:mid]+y+x[mid:]
print(insert_string_middle(y,x))

#13. 17. Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2c).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def insert_end():
    x = input("Enter string:")
    if len(x)>=2:
     last_two=x[-2:]
     result=last_two*4
     print("Result",result)
    else:
        print("length must be at least 2")
insert_end()

#14. 20. Write a  Python function to reverse a string if its length is a multiple of 4.
# def insert_end():
    x = input("Enter string:")
    if len(x)%4==0:
     new_string=x[::-1]
     print("Result:",new_string)
    else:
        print("Result:",x)
insert_end()

#15. 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
x=input("Enter string:")
y=''
for i in x[:5]:
    if i.isupper():
        y=y+i
if len(y)>=2:
    print(x.upper())
else:
    print("Result:",x)

#16.22.Write a  Python program to sort a string lexicographically.
x=input("Enter string:")
sorted_text=''.join(sorted(x))
print("Result:",sorted_text)

#17. 23. Write a Python program to remove a newline in Python.
x="welcome\n"
y=x.strip()
print(y)

#18.24. Write a Python program to check whether a string starts with specified characters.
x=input("Enter string:")
y=input("Enter characters:")
y_len = len(y)
if x[:y_len]==y:
    print(f'String starts with: {y})')
else:
    print(f'String does not start with: {y}')

#19. 27. Write a  Python program to remove existing indentation from all of the lines in a given text.
import textwrap
print("Enter text:")
import sys
text=sys.stdin.read()
no_indent = textwrap.dedent(text)
print("\nText without indent:")
print(no_indent)

# 20. 28. Write a Python program to add prefix text to all of the lines in a string.
x=input("Enter string:")
y="**"+x
y.replace("","**")
print(y)

# 21.29. Write a Python program to set the indentation of the first line.
text=input("Enter text:")
indent=""*4
indented_text=indent+text
print("\nText with indentation on the first line:", indented_text)

#22. 30. Write a Python program to print the following numbers up to 2 decimal places.
x=float(input("Enter number:"))
print("Result:{:.2f}".format(x))

#23. 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
x=float(input("Enter number:"))
print("Result:{:+.2f}".format(x))


#24. 32. Write a Python program to print the following positive and negative numbers with no
#decimal places.
x=float(input("Enter number:"))
print("Result:{:+.0f}".format(x))

#25. 35. Write a Python program to display a number with a comma separator.
x=int(input("Enter a number: "))
print(f"{x:,}")

#26.36. Write a Python program to format a number with a percentage.
x=float(input("Enter a number: "))
print("Result:{:.2%}".format(x))

#27.37. Write a Python program to display a number in left, right, and center aligned with a width of 10
x=input("Enter number:")
left_align=f"{x:<10}"
right_align=f"{x:>10}"
center=f"{x:^10}"
print(f"left_align:",left_align)
print(f"right_align:",right_align)
print(f"center:",center)


#28.38. Write a Python program to count occurrences of a substring in a string.
x=input("Enter string: ")
y=input("Enter substring: ")
my_count=x.count(y)
print(f"Result:",my_count)

#29.39. Write a  Python program to reverse a string.
x=input("Enter string:")
print(x[::-1])

#30.40. Write a Python program to reverse words in a string.
x=input("Enter string:")
for word in x.split():
    print(word[::-1],end=" ")

#31.41. Write a Python program to strip a set of characters from a string.
x=input("Enter string:")
y=input("Enter characters to remove:")
result=x.translate(str.maketrans('','',y))
print("Result:",result)

#32.42. Write a Python program to count repeated characters in a string.

from collections import Counter
def count_repeated_chars(s):
    counter=Counter(s)
    for char,count in counter.items():
        if count > 1:
            print(f"{char} {count}")
x=input("Enter string:")
count_repeated_chars(x)

#33.43. Write a Python program to print the square and cube symbols in the area of a rectangle and
the volume of a cylinder.
l=float(input("Enter length:"))
w=float(input("Enter width:"))
area=l*w

r=float(input("Enter radius:"))
h=float(input("Enter height:"))
pi=3.14
volume=pi*r**2*h
print(area)
print(f"The area of the rectangle is {area:.2f}cm\u00b2")
print(f"The volume of the cylinder is {volume:.2f}cm\u00b3")

#34.44. Write a  Python program to print the index of a character in a string.
def print_char_index(s):
    for index,char in enumerate(s):
        print(f"Current character {char} position {index}")
x=input("Enter string:")
print_char_index(x)

#35. 45. Write a  Python program to check whether a string contains all letters of the alphabet.
import string
def is_pangram(s):
 alphabet=set(string.ascii_lowercase)
 return alphabet <= set(s.lower())
x=input("Enter string:")
print(f"'{x}' -> {is_pangram(x)}")

# 36. 46. Write a Python program to convert a given string into a list of words.
x=input("Enter string:")
y=x.split()
print(y)

# 37.47. Write a  Python program to lowercase the first n characters in a string.
x=input("Enter string:")
y=int(input("Enter value of n:"))
output_string=""
for index,letter in enumerate(x):
    if index <y:
        output_string+=letter.lower()
    else:
        output_string+=letter
print("Modified string:",output_string)

#38.48. Write a Python program to swap commas and dots in a string.
def swap_commas_dot(x):
    x=x.replace('.','#')
    x=x.replace(',','.')
    x=x.replace('#', ',')
    return x
a=input("Enter number:")
result=swap_commas_dot(a)
print("Original:",a)
print("Swapped:",result)

#39.49. Write a Python program to count and display vowels in text.
x=input("Enter text:")
y="AEIOUaeiou"
count=len([letter for letter in x if letter in y])
vowels_to_display=set([letter for letter in x if letter in y])
print("Count of vowels:",count)
print("Vowels contain in text:",vowels_to_display)

#40.50. Write a Python program to split a string on the last occurrence of the delimiter.
x=input("Enter string:")
delimiter=input("Enter delimiter:")
if delimiter in x:
    result=x.rsplit(delimiter,1)
    print("Result:",result)
else:
    print("Delimiter not found.")

# 41.51. Write a  Python program to find the first non-repeating character in a given string.
x=input("Enter string:")
char_count={}
for c in x:
    char_count[c]=char_count.get(c,0)+1
first_non_repeat=None
for c in x:
    if char_count[c]==1:
        first_non_repeat=c
        break
if first_non_repeat:
    print("First_non_repeat:",first_non_repeat)
else:
    print("Non_repeating characters not found:")

# 42. 53. Write a Python program to find the first repeated character in a given string.
x=input("Enter string:")
y=set()
first_repeated=None
for c in x:
    if c in y:
        first_repeated = c
        break
    else:
        y.add(c)
if first_repeated:
    print("First_repeated:",first_repeated)
else:
    print("First_repeated not found:")

#43.55.Write a Python program to find the first repeated word in a given string.
x=input("Enter string:")
words=x.split()
seen=set()
first_repeated=None
for word in words:
    if word in seen:
        first_repeated=word
        break
    else:
        seen.add(word)
if first_repeated:
    print("The first repeated word is:",first_repeated)
else:
    print("First repeated word not found.")

#44.56. Write a Python program to find the second most repeated word in a given string.
x=input("Enter string:")
words=x.split(" ")
seen=dict()
for word in words:
    if word in seen:
        seen[word]+=1
    else:
        seen[word]=1
freg_list=sorted(seen,key=seen.get, reverse=True)
print("The second most repeated word:",freg_list[1])

#45.47.Write a  Python program to remove spaces from a given string.
x=input("Enter string:")
y=""
for i in x:
    if i !=" ":
        y+=i
print(y)

# #46.58. Write a Python program to move spaces to the front of a given string.
x=input("Enter string:")
y=""
space=""
for i in x:
    if i ==" ":
        space+=i
    else:
        y=y+i
result=space+y
print("Result:",repr(result))

#47.59. Write a Python program to find the maximum number of characters in a given string.
def max_char_frequency(s):
    if not s:
        return None,0
    freg={}
    for c in s:
        freg[c]=freg.get(c,0)+1
    max_char=max(freg, key=freg.get)
    return max_char,freg[max_char]
x=input("Enter string:")
char,count=max_char_frequency(x)
if char:
    print(f"The character '{char}' appears most: {count} times")
else:
    print("Empty string")

#48.60. Write a  Python program to capitalize the first and last letters of each word in a given string.
def capitalize_first_last(word):
    if len(word)==1:
        return word.upper()
    return word[0].upper()+word[1:-1]+word[-1].upper()
def process_string(s):
    words = s.split()
    result = [capitalize_first_last(w) for w in words]
    return " ".join(result)
string=input("Enter string:")
print("Result:", process_string(string))

# 49.61. Write a Python program to remove duplicate characters from a given string.
def remove_duplicates(s):
 result=""
 seen = set()
 for c in s:
     if c not in seen:
         result+=c
         seen.add(c)
 return result
x=input("Enter string:")
print("Result:",remove_duplicates(x))

#50.62. Write a Python program to compute the sum of the digits in a given string.
x=int(input("Enter string:"))
num=x
sum=0
while x>0:
    dig=x%10
    sum=sum+dig
    x=x//10
print("Sum of digits:",sum)

#51.63. Write a Python program to remove leading zeros from an IP address.
x=input("Enter IP adress:")
y=".".join(map(str,map(int,x.split("."))))
print("IP adress:",y)

#52.67. Write a Python program to remove all consecutive duplicates of a given string.
x=input("Enter string:")
y=" "
for i in x:
    if y==" " or i!=y[len(y)-1]:
        y=y+i
print(y)




