# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this



# array_Object=[
#     {"January":2200},
#     {"February":2350},
#     {"March":2600},
#     {"April":2130},
#     {"May":2190},
# ]

# solution 1
# print(array_Object[1]["February"]-array_Object[0]["January"])
# print(array_Object[1].get("February") - array_Object[0].get("January"))


# solution 2
# print(array_Object[0]["January"] + array_Object[1]["February"] + array_Object[2]["March"])

# solution 3


# array_Object_with_month=[
#     {'month':'January',
#     'expense':2200
#     },
#     {'month':'February',
#     'expense':2350
#     },
#     {'month':'March',
#     'expense':2600
#     },
#     {'month':'April',
#     'expense':2130
#     },
#     {'month':'May',
#     'expense':2190
#     },

# ]

# for i in range(len(array_Object_with_month)):
#     find="None";
#     if array_Object_with_month[i].get('expense')==2190:
#       find=array_Object_with_month[i].get('month');
# print(find);

# solution 4

# June_month={
#     'month':'June',
#     'expense':1980,
#     }

# array_Object_with_month.append(June_month);


# solution 5

# for i in range(len(array_Object_with_month)):
#     if array_Object_with_month[i].get('month')=='April':
#         new_value=array_Object_with_month[i]['expense']-200
#         array_Object_with_month[i]['expense']=new_value;
    # print(array_Object_with_month)



heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


# solution 1
# print(len(heros))

# solution 2
# heros.append('black panther')
# print(heros);

# solution 3
# heros.pop();
# print(heros);
# heros.insert(3,'black panther')
# print(heros);

# solution 4
# heros[1:3]=['doctor strange'];
# print(heros);

# solution 5
# heros.sort()
# print(heros)


# odd number

# values2=int(input('Enter a max value: '))

# odd_numbers=[]
# for i in range(1,values2):
#     if i%2!=0:
#         odd_numbers.append(i)

# print(odd_numbers)
# max = int(input("Enter max number: "))

# odd_numbers = []

# for i in range(1, max):
#     if i % 2 == 1:
#         odd_numbers.append(i)

# print("Odd numbers: ", odd_numbers)


