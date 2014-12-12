import string

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique_words(string1):
	#lower case the sring.
	#order the list and append the words to an intitialized list
	#loop through the list and use setdefault to add each key/value pair to an initialized dictionary. Add one if the key is already in the dictionary.
	#return dictionary

	words_list = string1.lower().split()
	count_dict = {}

	for word in words_list:
		count_dict[word] = count_dict.setdefault(word, 0) +1

	return count_dict

print "count_unique_words", count_unique_words(string1)

def count_unique_letters(string1):

	# if elements are letters, not words: runtime: O(n) ?
	# lower case, import string library, if element in ascii_letters, append to initialized empty list
	# sort list
	# loop through list, setdefault dict with count

	letters_list = []
	for i in string1:
		if i in string.ascii_letters:
			letters_list.append(i)

	letter_dict = {}

	for letter in letters_list:
		letter_dict[letter] = letter_dict.setdefault(letter, 0) + 1
	return letter_dict

print "unique count letters:", count_unique_letters(string1)


"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):

	# method 1: runtime: quadratic (bad!)
	# deduplify first list and second list with a for loop
	# make a nested for loop and compare each element of each deduped list to the other. If they match, append that element to an initialized list. 

	list1_deduped = []
	for i in list1:
		if i not in list1_deduped:
			list1_deduped.append(i)

	list2_deduped = []
	for i in list2:
		if i not in list2_deduped:
			list2_deduped.append(i)

	common_items_list = []

	for i in list1_deduped:
		for j in list2_deduped:
			if i == j:
				common_items_list.append(i)
			
	return common_items_list

print "common_items with quadratic runtime", common_items(list1, list2)

def common_items_sets(list1, list2):

	# method 2: runtime? returns unordered list
	main_list = list(set(list1)&set(list2))
	return main_list 

print "common items with sets:", common_items_sets(list1, list2)


def common_items_OofN(list1, list2):

	#method3: runtime o(n)
	#initialize 2 empty dicts.
	#loop through list1. Add keys, values to list.
	#loop through list2: if dict1.get(item) is True, append that item to initialized empty list

	dict1 = {}
	dict2 = {}
	common_items = []

	for i in list1:
		dict1[i] = dict1.setdefault(i, True)

	for i in list2:
		if dict1.get(i, False) == True:
			common_items.append(i)

	return common_items


print 'common_items_dicts', common_items_OofN(list1, list2)



"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):

	#nested for loop: if items add to 0, append them as tuple pair to empty list
	#problem: returning repeats of same pairs because tuples are unique in order and not iterable.

	# sum_0_pairs = []

	# for i in list1:
	# 	for j in list1:
	# 		if i + j ==0:
	# 			sum_0_pairs.append([i,j])

	# return sum_0_pairs


	# initialize empty dict.
	# loop through list and add each item to empty dict with item also as value.
	# loop through dict: if -i equals dict.get(i), append both values as a tuple to empty list.
	#problem: returns repeats.


	# sum_zero = {}
	# sum_zero_pairs = []

	# for i in list1:
	# 	sum_zero[i] = sum_zero.setdefault(i, i)

	# for i in list1:
	# 	if i + sum_zero.get(i, False) == 0:
	# 		sum_zero_pairs.append((i, sum_zero[i]))

	# return sum_zero_pairs
	num_pairs = []
	sum = 0

	for i in list1:
		num = list1.pop()
		diff = sum - num
		if diff in list1:
			num_pairs.extend([[num, diff]])

	return num_pairs

print "sum to zero", sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""