#1.Write python program:
#a)Convert two lists into a dictionary
if __name__ =='__main__':
    keys=['id','name','dob']
    value=[1000,'Le Bao Yen','02/04/2006']
    emp={}
    for i in range (len(keys)):
        emp[keys[i]] = value[i]
    print(emp)

# b)Merge two Python dictionaries into one.
dict1={'name':'Yen', 'age':20, 'dob':'02/04/2006'}
dict2={'class':'AS', 'ID':31241024243}
merge_dict=dict1|dict2
print("Merge dict: ",merge_dict)

# c)Print the value of key ‘history’ from the below dict
dict={'name':'Yen', 'age':20, 'history':'History of VN'}
his_value=dict.get('history')
print("Value of key history:", his_value)

#d)Initialize dictionary with default values.
items=['name','age','dob']
defaults=['None']
dict={}
for item in items:
    dict[item]=defaults
print(dict)

#e)Create a dictionary by extracting the keys from a given dictionary
dict={'name':'Yen', 'age':20, 'dob':'02/04/2006'}
key_extract={key:None for key in dict.keys()}
print("New dictionary:", key_extract)

#f)Delete a list of keys from a dictionary
dict={'name':'Yen', 'age':20, 'dob':'02/04/2006'}
del_key=['age']
for key in del_key:
    if key in dict:
        del dict[key]
print(dict)

#g)Check if a value exists in a dictionary
val=20
dict={'name':'Yen', 'age':20, 'dob':'02/04/2006'}
value_exist=val in dict.values()
print("Check:",value_exist)

#h)Rename key of a dictionary
dict={'name':'Le Yen', 'age':20, 'dob':'02/04/2006'}
if 'name' in dict:
    dict['full_name']=dict.pop('name')
print("Dictionary after rename", dict)

#i)Get the key of a minimum value from the following dictionary
dict={'Yen':20, 'Lan':18, 'Ngoc':24}
min_key=min(dict, key=dict.get)
print("Key of a minimum value is:", min_key)

#j)Change value of a key in a nested dictionary
nested_dict={'profile':{'name':'Yen', 'age':20}, 'dob':'02/04/2006'}
nested_dict['profile']['age']=19
print("Nested dictionary after change", nested_dict)

#2.Write a Python program that counts the number of times characters appear in a text paragraph.
s=("Write a Python program that counts the number of times characters appear in a text paragraph")
stats={}
for c in s:
    x=stats.get(c)
    if x==None:
        stats[c]=1
    else:
        stats[c]=int(stats[c]+1)
print(stats)

#3.Write a program using a dictionary containing keys starting from 1 and valuescontaining prime numbers less than a value N.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

N=50
primes=[x for x in range(2,N) if is_prime(x)]
prime_dict={i+1:primes[i] for i in range(len(primes))}
print(prime_dict)



