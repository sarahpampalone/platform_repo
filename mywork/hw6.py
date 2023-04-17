# Sarah Pampalone
# Cite any sources you used to help with the homework 
# including TAs and classmates

def string3(str):
    '''
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    '''
    new = str[-2] + str[-1] + str[-2] + str[-1] + str[-2] + str[-1]
    return new

def exchange(str):
    """
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """
    if(len(str)) > 1 :
        new = str[-1] + str[1:len(str)-1] + str[0]
    else :
        new = str
    return new


def count_list(lst):
    '''
    Given a list of numbers, return a new list with a count of each number stored at the 
    index place of that number.
    For example, if given the list [1,1,5,6,6,7,3] return a new list [0,2,0,1,0,1,2,1]
    '''
    new = [0] * (max(lst)+1)
    for i in range(len(lst)):
        new[lst[i]]+=1
    return new

def remove_range(alist, min, max):
    """
    Use comprehension to write a method named removeRange that accepts an list of
    integers and two integer values min and max as parameters and removes all elements
    values in the range min through max (inclusive).
    For example, if a alist named list stores
    [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], the call of remove_range(alist, 5, 7);
    should change the list to store [9, 4, 2, 3, 1, 8].

    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    """
    return [x for x in alist if (x<min or x>max)]

def word_count_in_set(words):
    """
    Write a function named wordCount that accepts a list of strings as a parameter and
    returns a count of the number of unique words in the list. Do not worry about
    capitalization and punctuation; for example, "Hello" and "hello" and "hello!!" are
    different words for this problem.
    Hint: Use a set as auxiliary storage.
    *** Solution should not be more than 3 lines of code (can be less)
    including the return statement ***
    """
    new = set(words)
    return len(new)
    

def topping1(dict):
    """
    Given a dictionary of food keys and topping values, modify and return the dictionary
    as follows:
    if the key "ice cream" is present, set its value to "cherry".
    In all cases, set the key "bread" to have the value "butter".
    Examples:
    topping1({"ice cream": "peanuts"}) returns {"bread": "butter", "ice cream": "cherry"}
    topping1({})  {"bread": "butter"} returns {"bread": "butter"}
    topping1({"pancake": "syrup"}) returns {"bread": "butter", "pancake": "syrup"}
    """
    if 'ice cream' in dict:
        dict["ice cream"]="cherry"
    dict["bread"] = "butter"
    Keys = list(dict.keys())
    Keys.sort()
    new_dict = {key: dict[key] for key in Keys}
    # https://sparkbyexamples.com/python/python-sort-dictionary-by-key/
    return new_dict
    

def friend_list(friend_dictionary):
    """
    Write a method named friendList that accepts a dictionary as a parameter and reads
    friend relationships and stores them into a new dictionary that is returned.
    You should create a new dictionary where each key is a person's name from the original
    simple dictionary, and the value associated with that key is a set of all friends of
    that person. Friendships are bi-directional:
    if Marty is friends with Danielle, Danielle is friends with Marty.

    The dictionary parameter contains one friend relationship per key/value pair,
    consisting of two names. If the dictionary parameter,friendMap looks like this:
    Marty: Cynthia
    Danielle: Marty
    Then the call of friendList(friendMap) should return a dictionary with the following
    contents:
    {Cynthia:[Marty], Danielle:[Marty], Marty:[Cynthia, Danielle]}
    """
    temp = {}
    for person, friend in friend_dictionary.items():
        if friend not in temp:
            temp[friend]=[person]
        else:
            temp[friend].append(person)
        if person not in temp:
            temp[person]=[friend]
        else:
            temp[person].append(friend)
    new_dict = dict(sorted(temp.items())) 
    return new_dict

# #Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert count_list([1,1,5,6,6,7,3]) ==  [0,2,0,1,0,1,2,1], 'expected  [0,2,0,1,0,1,2,1]'
print("correct")
assert count_list([0,0,0,1]) ==  [3,1], 'expected  [3,1]'
print("correct")
assert count_list([10,9,8,7,6,5,4,3,2,1,0]) ==  [1,1,1,1,1,1,1,1,1,1,1], 'expected  [1,1,1,1,1,1,1,1,1,1]'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# # Problems found on https://codingbat.com/python



