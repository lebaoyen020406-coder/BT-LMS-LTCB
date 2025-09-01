import random

lst=[]
for i in range(10):
    lst.append(random.randint(1,10))

def print_list():
    for item in lst:
        print(item, end=",")
    print()

#1. Write a Python program to sum all the items in a list.
def ex_01():
    sum=0
    for item in lst:
        sum+=item
    print(f"Sum of item in list: {sum}")

# 2. Write a Python program to multiply all the items in a list
def ex_02():
    product=1
    for item in lst:
        product*=item
    print(f"Product of item in list: {product}")

#3. Write a Python program to get the largest number from a list.
def ex_03():
    biggest=lst[0]
    for item in lst:
        if biggest<item:
            biggest=item
    print(f"Biggest number of our list is: {biggest}")

#4. Write a Python program to get the smallest number from a list
def ex_04():
    smallest=lst[0]
    for item in lst:
        if smallest>item:
            smallest=item
    print(f"Biggest number of our list is: {smallest}")

#6.7. Write a Python program to remove duplicates from a list.
def ex_07():
    number=lst
    print("Remove duplicates:",list(dict.fromkeys(number)))

# 7.8. Write a Python program to check if a list is empty or not.
def ex_08():
    input_list=lst
    if input_list==[]:
        print("The list is empty")
    else:
        print("The list is not empty")
#
if __name__ == '__main__':
    print_list()
    ex_01()
    ex_02()
    ex_03()
    ex_04()
    ex_07()
    ex_08()


# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
list=['abc','xyz','aba','1221']
count=0
for item in list:
    if len(item)>=2 and item[0]==item[-1]:
        count+=1
print(count)

#8.9. Write a Python program to clone or copy a list.
fruits=['apple','banana','orange']
new_list=fruits.copy()
print(new_list)

#9. 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
def ex_09(n,str):
    word_len=[]
    x=str.split(" ") #split words to list
    for i in x:
        if len(i) > n:
            word_len.append(i)
    return word_len
print("Long word:",(ex_09(4,"Python is really hard")))

#10. 11. Write a Python function that takes two lists and returns True if they have at
# least one common member.
def ex_10(list_1,list_2):
    final=False
    for i in list_1:
        for j in list_2:
            if i==j:
                final=True
                return final
print("Check number:",(ex_10([1,2,3,4,5],[5,7,9])))

#11.12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove=[x for (i,x) in enumerate(list) if i not in (0,4,5)]
print("List:",list)
print("List after remove:",remove)

#12.13. Write a Python program to generate a 3*4*6 3D array whose each element is
# *.
array=[[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(array)

#13. 14. Write a Python program to print the numbers of a specified list after removing
# even numbers from it.
number=[1,2,3,4,5,6,7,8,9,10]
number=[i for i in number if i%2!=0]
print(number)

#14.15. Write a Python program to shuffle and print a specified list
# from random import shuffle
list=['apple','banana','orange','strawberry','grape']
shuffle(list)
print(list)

# 15.16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both
# included)
def ex_15():
    x=list()
    for i in range(1,31):
        x.append(i**2)
    print(x[:5])
    print(x[-5:])
print(ex_15())

# 16.17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
def ex_16(nums):
    return all(is_prime(i) for i in nums)
def is_prime(n):
    if n ==1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
            return True
nums=[0,3,4,7,9]
print("Original list:",nums)
print("Resutl:",ex_16(nums))

nums=[3,5,7,13]
print("Original list:",nums)
print("Resutl:",ex_16(nums))

nums=[1,5,3]
print("Original list:",nums)
print("Resutl:",ex_16(nums))

#17.18. Write a Python program to generate all permutations of a list in Python.
numbers=[1,2,3]
print("Number:",list)
from itertools import permutations
perms=list(permutations(numbers))
print("Permutations:",perms)

# 18.19. Write a Python program to calculate the difference between the two lists.
list1=[1,2,3,4,5]
list2=[2,4,6,8,10]
difference_list1_list2=list(set(list1) - set(list2))
difference_list2_list1=list(set(list2) - set(list1))
total_difference=difference_list1_list2 + difference_list2_list1
print(total_difference)

# 19.20. Write a Python program to access the index of a list.
list=[2,4,6,8,10]
for num_index, num_val in enumerate(list):
    print(num_index, num_val)

# 20.21. Write a Python program to convert a list of characters into a string.
list=['a','b','c','d','e','f']
str=''.join(list)
print(str)

# 21.22. Write a Python program to find the index of an item in a specified list.
list=['a','b','c','d','e','f','g','h']
print(list)
index=list.index('c')
print(index)

#22.23. Write a Python program to flatten a shallow list.
import itertools
original_list=[[1,2,3],[4,6,8],[5,7,9]]
flatten=list(itertools.chain(*original_list))
print(flatten)

# 23.24. Write a Python program to append a list to the second list.
list1=[1,2,3,4,5]
list2=[6,7,8,9]
list1+=list2
print(list1)

# 24.25. Write a Python program to select an item randomly from a list.
import random
list=[1,'a',3,'b',5,'c',7,'d',9,'e']
print("Random item:",random.choice(list))

# 25.26. Write a Python program to check whether two lists are circularly identical.
list1=[1,1,0,0,1]
list2=[10,1,1,0,0]
list3=[1,0,0,1,1]
print("Compare list1 and list2")
print(' '.join(map(str,list2)) in ' '.join(map(str,list1*2)))
print("Compare list1 and list3")
print(' '.join(map(str,list3)) in ' '.join(map(str,list1*2)))

#26.27. Write a Python program to find the second smallest number in a list.
numbers=[1,4,2,8,5,9,4,0]
print("Original list:",numbers)
numbers.remove(min(numbers))
print("Second smallest number:",min(numbers))

#27.28. Write a Python program to find the second largest number in a list.
numbers=[1,4,2,8,5,9,4,0,10]
print("Original list:",numbers)
numbers.remove(max(numbers))
print("Second largest number:",max(numbers))

#28.29. Write a Python program to get unique values from a list.
lst=[1,2,3,0,4,1,5,6,8,7,10,3]
print("Original list:",lst)
unique_values=list(set(lst))
print("Unique value:",unique_values)

#29.30. Write a Python program to get the frequency of elements in a list.
def ex_29():
 list=[1,2,3,2,4,6,4,'b',1,'a','b']
 freq={}
 for i in list:
   freq[i] = freq.get(i,0) + 1
 return freq
print("Frequency of elements:",ex_29())

#30.31. Write a Python program to count the number of elements in a list within a
#specified range.
def ex_30(list,min,max):
    list=[95,25,40,45,55,65,30,80,90,15]
    ctr=0
    for i in list:
        if min<=i<=max:
            ctr+=1
    return ctr
print("Count range:",(ex_30(list,50,100)))

#31.32. Write a Python program to check whether a list contains a sublist.
def ex_31(l,s):
    sub_set=False
    if s==[]:
        sub_set=True
    elif s==1:
        sub_set=True
    elif len(s) > len(l):
        sub_set=False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n=1
                while (n < len(s)) and (l[i+n]==s[n]):
                    n+=1
                if n==len(s):
                    sub_set=True
    return sub_set
list1=[1,2,3,4,5]
list2=[2,3]
list3=[2,5]
print(ex_31(list1,list2))
print(ex_31(list1,list3))

#32.33. Write a Python program to generate all sublists of a list.
from itertools import combinations
def sub_list(lst):
    subs=[]
    for i in range(0,len(lst)+1):
        temp=[list(x) for x in combinations(lst,i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs
lst=[5,10,15,20,25]
print("Original list:",lst)
print("Sublists:",sub_list(lst))

#33.34. Write a Python program that uses the Sieve of Eratosthenes method to
#compute prime numbers up to a specified number.
from math import isqrt
def prime_less_than(n:int) ->list[int]:
    if n<=2:
        return []
    is_prime = [True] *n
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,isqrt(n)):
        if is_prime[i]:
            for x in range(i*i,n,i):
                is_prime[x]=False
    return [i for i in range(n) if is_prime[i]]
if __name__ == '__main__':
     print(prime_less_than(100))

#34.35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def ex_34(sample_lst,n):
    lst=[]
    for num in range(1,n+1):
        for item in sample_lst:
            lst.append(f"{item}{num}")
    return lst
sample_lst=['p','q']
n=5
result=ex_34(sample_lst,n)
print(result)

#35.36. Write a Python program to get a variable with an identification number or
#string.
x=50
print(format(id(x),'x'))
s='lebaoyen'
print(format(id(s),'x'))

#36.37. Write a Python program to find common items in two lists.
lst1=['apple','banana','orange']
lst2=['apple','banana','cherry','grape']
print(set(lst1)& set(lst2))

#37.38. Write a Python program to change the position of every n-th value to the
#(n+1)th in a list.
from itertools import zip_longest,chain,tee
def ex_37(lst):
    lst1,lst2=tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n=[0,1,2,3,4,5]
print("Result:",ex_37(n))

#38.39. Write a Python program to convert a list of multiple integers into a single
#integer
lst=[11,33,50]
print("Original list:",lst)
x=int("".join(map(str,lst)))
print("Single integer:",x)

#39.40. Write a Python program to split a list based on the first character of a word.
from itertools import groupby
from operator import itemgetter
lst= ['apple','banana','cherry','grape']
for letter, words in groupby(sorted(lst), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

#40.41. Write a Python program to create multiple lists
x={}
for i in range(10):
    x[str(i)] = []
print(x)

#41.42. Write a Python program to find missing and additional values in two lists
lst1=['a','b','c','d','e','f']
lst2=['d','e','f','g','h']
print("Missing values in second list:",','.join(set(lst1).difference(lst2)))
print("Additional values in first list:",','.join(set(lst2).difference(lst1)))

#42.43. Write a Python program to split a list into different variables.
lst=[
    ('a','b','c','d'),
    ('apple','banana','cherry','dragonfruit'),
    ]
var1,var2=lst
print(var1)
print(var2)

#43.44. Write a Python program to generate groups of five consecutive numbers in a
#list
lst=[[5*i+j for j in range(1,6)] for i in range(5)]
print(lst)

#44.45. Write a Python program to convert a pair of values into a sorted unique array
lst=[(1,2),(3,4),(5,6),(1,2),(7,8),(9,10)]
print("Original list:",lst)
print("New list:",sorted(set().union(*lst)))

#45.46. Write a Python program to select the odd items from a list.
lst=[1,2,3,4,5,6,7,8,9,10]
print("Odd items:",lst[::2])

#46.47. Write a Python program to insert an element before each element of a list.
lst=['apple','banana','cherry','grape']
print("Original list:",lst)
lst=[v for elt in lst for v in ('fruit',elt)]
print("Result:",lst)

#47.48. Write a Python program to print nested lists (each list on a new line) using
#the print() function.
list=[['apple'],['banana'],['cherry']]
print('\n'.join([str(lst) for lst in list]))

#48.49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
# 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon',
color_name=['Black','Red','Maroon','Yellow']
color_code=['#000000','#FF0000','#800000','#FFFF00']
print([{'color_name':f,'color_code':c} for f,c in zip(color_name,color_code) ])

#49.50. Write a Python program to sort a list of nested dictionaries.
lst = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original list:", lst)
lst.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted list:", lst)

#50.51. Write a Python program to split a list every Nth element.
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
def ex_50(s, step):
    return [s[i::step] for i in range(step)]
print("Original list:", lst)
print(ex_50(lst,3))

#51.52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green",
# "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
from collections import Counter
color1=["red", "orange", "green", "blue", "white"]
color2=["black", "yellow", "green","blue"]
counter1=Counter(color1)
counter2=Counter(color2)
print("Color1=Color2:",list(counter1-counter2))
print("Color2=Color1:",list(counter2-counter1))

#52.53. Write a Python program to create a list with infinite elements
import itertools
c=itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))

#53.54. Write a Python program to concatenate elements of a list
lst=['apple','banana','cherry','grape']
print('-'.join(lst))
print(''.join(lst))

#54.55. Write a Python program to remove key-value pairs from a list of dictionaries.
lst=[{'name':'Le Yen','class':'AS'}]
print("Original list:",lst)
new_lst=[{k: v for k,v in d.items() if k != 'name'} for d in lst]
print("New list:",new_lst)

#55.56. Write a Python program to convert a string to a list.
import ast
lst="['apple','banana','cherry','grape']"
print("Original list:",lst)
print("Convert to list:", ast.literal_eval(lst))



