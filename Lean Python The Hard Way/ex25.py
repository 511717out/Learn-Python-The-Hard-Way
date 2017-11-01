# _*_ coding:utf-8 _*_

"""
# Python split()通过指定分隔符对字符串进行切片，
# 如果参数num 有指定值，则仅分隔 num 个子字符串
# 语法：str.split(str="", num=string.count(str)).
"""
"""
# sorted() 函数对所有可迭代的对象进行排序操作。
# sorted(iterable[, cmp[, key[, reverse]]])
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
http://www.runoob.com/python/python-func-sorted.html
"""
def break_words(stuff):
   """This function will break up words for us."""
   words = stuff.split(' ')
   return words

def sort_words(words):
   """Sorts the words"""
   # sorted() 函数对所有可迭代的对象进行排序操作。
   # sorted(iterable[, cmp[, key[, reverse]]])
   return sorted(words)

def print_first_word(words):
   """Prints the first word after popping it off."""
   # pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
   # list.pop(obj=list[-1])
   word = words.pop(0)
   print word

def print_last_word(words):
   """Prints the last word after popping it off."""
   word = words.pop(-1)
   print word

def sort_sentence(sentence):
   """Takes in a full sentence and returns the sorted words."""
   words = break_words(sentence)
   return sort_words(words)

def print_first_and_last(sentence):
   """Prints the first and last wordss of the sentence."""
   words = break_words(sentence)
   print_first_word(words)
   print_last_word(words)

def print_first_and_last_sorted(sentence):
   """Prints the words then prints the first and last one."""
   words = sort_sentence(sentence)
   print_first_word(words)
   print_last_word(words)