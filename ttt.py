#string
counter,miles,name=100,1000.0,"lucc"
print(counter)
print(miles)
print(name)
str='qwertyu'
print(str[0:-1])
print(str[4])
print(str*2)
#list数组
list=['dfas',56,86,'fsdfaf']
list[0]='dddddddddd'
tinylisst=['fsdfa',5656]
print(list)
print(list[1])

listtotal=list+tinylisst
print(listtotal)
#set 集合集合（set）是一个无序不重复元素的序列。
#基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
stutent={'tom','jerry','mary','andy'}

print(stutent)
if('tom' in stutent):
    print('tomhere')
else:
    print('buzai')
#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
#字典（dictionary）是Python中另一个非常有用的内置数据类型。
#列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
#键(key)必须使用不可变类型。
#在同一个字典中，键(key)必须是唯一的。
dict={}
dict['one']="1-菜鸟教程"
dict[2]="2-菜鸟工具"
tinyDict={'name':'runn','code':12}
print(dict['one'])
print(tinyDict.keys())
float(miles)
print(miles)
#
# 函数	描述
# int(x [,base])
# 将x转换为一个整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串

# Python 访问字符串中的值
# Python 不支持单字符类型，单字符也在Python也是作为一个字符串使用。
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
str1='hewewe'
str2='runnoob'
print('var1[0]:',str1[0])
print('str2[0:2]',str2[0:2])

# Python字符串更新
# 你可以截取字符串的一部分并与其他字段拼接，如下实例：str
str3='qwertyyouoypuoypup'
print("已经跟新字符串\t\t：",str3[:6]+str1)
if 'q' in str3:
    print("qzai")

    # Python字符串格式化
    # Python
    # 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 % s
    # 的字符串中。
    # 在
    # Python
    # 中，字符串格式化使用与
    # C
    # 中
    # sprintf
    # 函数一样的语法。
    print( "我叫%s,今年%d岁了"%("小明",100))

    print(str3.capitalize())
# Python3
# 列表
# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

list1=['fsdf','fewrwe',"ffsadfasdf","fwerewtyfdsf","fwerewtyfdsfettt"]
# 访问列表中的值

print(list1[0])
#更新列表
list1[0]="哈哈发"
print(list1[0])
#删除列表元素
del  list1[0]
print(list1[0])
print(list1[1:-1])


# 访问字典里的值
# 把相应的键放入熟悉的方括弧，如下实例:
dict1={'1':10,'2':20,'3':'fsadf'}
print(dict1['1'])
del dict1['1']
print(dict1)
#dict1.clear()
print(dict1.__len__())
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a,b=0,1
while(b<10):
    print(b)
    a,b=b,a+b
if (5==6):
    print("ad")
elif(5==5):
    print('yes')
else:
    print("fsdfasd")
if(5==5):
    if(5>3):
        print("qiantao")

while(5==8):
    print("666")
else:
    print("wrong")

# for i in counter:
#      print(chr(i))
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
     print (x)
for i in range(languages.__len__()):
    print(languages.__len__())
for i in range(0,11,2):
    print(i)
for letter in 'Runoob':     # 第一个实例
   if letter == 'u':
      break
   print ('当前字母为 :', letter)
for ll in 'qweret':
    if ll == 'e':
        break
    print(ll)
sequence = [12, 34, 34, 23, 45, 76, 89]
for i,j in enumerate(sequence):
    print(i,j)

# Python3 迭代器与生成器
# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：


list2=[0,1,4,5]
it=iter(list2)
#print(next(it))
# for x in it:
#     print(x,end="")
# import  sys
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
# 以下实例使用 yield 实现斐波那契数列：

# import sys
# def fibonacci(n): #生成器函数
#     a,b,count=0,1,0
#     while True:
#         if(count>0):
#             return
#         yield  a
#         a,b=b,a+b
#         count+=1
# f=fibonacci(10)
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()




# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
 #计算圆的面积

def area(width,height):
    return width*height

def printname(name):
    print("ww",name)
printname('llll')
w=4
h=5
print(area(w,h))

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def printinfo(arg1,*vartuple):
     #"打印传入的参数"
     print(":output:")
     print(arg1)
     for var in vartuple:
         print(var)
     return
printinfo(10)
printinfo(70,'dfsdf','erew',100)





# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;
printinfo(10)
printinfo(10,'ewr','re',45)
# 匿名函数
# python
# 使用
# lambda 来创建匿名函数。

sum=lambda  arg1,arg2:arg1+arg2
#调用
print("相加值",sum(10,20))
# return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：

def sum(arg1,arg2):
    #返回2个参数的和
    total=arg1+arg2
    print('函数内：',total)
    return total;

#调用sum函数
total=sum(10,20)
print("函数外：",total)