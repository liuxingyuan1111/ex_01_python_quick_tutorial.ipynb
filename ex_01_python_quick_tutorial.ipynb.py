#第一部分
print("Hello Liu Xingyuan")
print("2"*50)
print("我想做一个好人")
#简单计算
print(10**5)
x=5
func=8*x+10
# 先给变量定义
print(func)
x=5.0
func=2*x+1
 #格式化的两种方法
print("func=",func)
print("func=%.2f"%func)
print("func={:.2f}".format(func)) 
#石家庄经纬度
city_name="shijiazhuang"
coordinate_longitude=114.48333
coordiante_latitude=38.03333
print("The longitude of the shijiazhuang coordinate is {lon:.2f}, and the latitude is {lat}.".format(lon=coordinate_longitude,lat=coordiante_latitude))
x,y,b=2,5,7 #unpacking 序列解包。尝试，x,y,*z=0,1,2,3,4,5,6; x,y,*z=0,1; (x,y),(a,b)=(0,1),(2,3)
func_2=2*x+3*y+b
print("func_2={}".format(x,y,b,func_2))
#建立列表
lst_1=list(range(2,16,2)) 
print(lst_1)
print("The list length={}".format(len(lst_1)))
print("Maximum value={}".format(max(lst_1)))
print("Minimum value={}".format(min(lst_1)))
#分片练习
lst_2=list(map(chr,range(10,20)))
print(lst_2)
print("_"*50)
print("[5:10->{}".format(lst_2[5:10]))
print("[-5:-1]->{}".format(lst_2[-5:-1]))
print("[-10:]->{}".format(lst_2[-10:]))
print("[:5]->{}".format(lst_2[:5]))
print("[:]->{}".format(lst_2[:]))
#用help可以查看说明
help(chr)
help(map)
#带有步长的参数分片
lst_2=list(map(chr,range(100,110)))
print("_"*50)
print(lst_2)
print("_"*50)
print("[0:10:2]->{}".format(lst_2[0:10:2]))
print("[::3]->{}".format(lst_2[::3]))
print("[9:3:-2]->{}".format(lst_2[9:3:-2]))
print("[20:3:-2]->{}".format(lst_2[20:3:-2]))
print("[7::-2]->{}".format(lst_2[7::-2]))
print("[:3:-2]->{}".format(lst_2[:3:-2]))
#元素赋值
print(lst_2)
print("_"*50)
lst_2[5]=6
#分片赋值
lst_s=list(map(chr,range(100,110)))
print("_"*50)
print("lst_s[5]=99->{}".format(lst_s))
lst_none=lst_s+[None]*6
print("lst_s+[None]*6->{}".format(lst_none))
lst_none[13]=2015
print("lst_none[13]=2015->{}".format(lst_none))
lst_none[-6:-3]=list(range(100,104,2))
#删除元素
print("lst_none[-5:-3]=list(range(100,104,2))->{}".format(lst_none))
lst_none[1:1]=[0,0,0,12]
print("lst_none[1:1]=[0,0,0,11]->{}".format(lst_none))
del lst_none[-5:]
print("del lst_none[-2:]->{}".format(lst_none))
#列表的方法
lst_s_2=list(map(chr,range(100,105)))
print(lst_s_2)
print("_"*50)
lst_s_2.append(99)
print("lst_s_2.append(99)->{}".format(lst_s_2))
lst_s_2.append(list(range(50,80,5)))
print("lst_s_2.append(list(range(50,80,5)))->{}".format(lst_s_2))
lst_spechars=['*',')','*']
lst_s_2.extend(lst_spechars)
print("lst_s_2.extend(lst_spechars)->{}".format(lst_s_2))
print("lst_s_2.count('*')={}".format(lst_s_2.count('*')))
print("lst_s_2.index('e')={}".format(lst_s_2.index('e')))
lst_s_2.insert(2,[1000,1200,1500])
print("lst_s_2.insert(2,[1000,1200,1500])->{}".format(lst_s_2))
print("lst_s_2.pop(7)_popup->{}".format(lst_s_2.pop(7)))
print("lst_s_2.pop(7)_retention->{}".format(lst_s_2))
lst_s_2.remove('*')
print("lst_s_2.remove('*')_retention->{}".format(lst_s_2))
list_n_2=[2,42,6,95,4,3]
list_n_2.sort()
print("list_n_2.sort()->{}".format(list_n_2))
#tuple元组
tuple_1=10,11,12,
print("tuple_1=2,3,5,->{}".format(tuple_1))
print("10*(5+5,)->{}".format(10*(5+5,)))
print("tuple((1,2,3))->{}".format(tuple((1,2,3)))) 
print("tuple([1,2,3])->{}".format(tuple([1,2,3])))
#使用dict建立字典
import random
items=[(0,[i for i in range(10)]),(1,[random.sample(list(range(100,400,2)),3)]),(2,'python')] #[i for i in range(5)] 为列表推导式 list comprehension/derivation
print("items->{}".format(items))
dic=dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[1]->{}".format(dic[1]))
#有关字典的一些基本操作
print("len(dic)->{}".format(len(dic)))
dic[3]=(random.random(),random.uniform(200,300))
print("dic[3]=(random.random(),random.uniform(200,300))->{}".format(dic))
del dic[3]
print("del dic[1]->{}".format(dic))
print("3 in dic->{}".format(3 in dic))
print("5 in dic->{}".format(5 in dic))
print("dic.keys()->{}".format(dic.keys())) 
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print("_"*50)
print("list(dic.keys())->{}".format(list(dic.keys())))
#字典的方法
lst_A=list(range(6,20,3))
lst_B=list(range(100,150,15))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("dic_2={}".format(dic_2))
print("_"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(1,9,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy={}".format(dic_copy))
dic_copy[5].remove(5)
print("dic_copy[5].remove(5)->{}".format(dic_copy))
#返回指定键的值，如果不存在该键，则字典增加新的键/值对
dic_copy.setdefault(6,[77,99]) 
print("dic_copy.setdefault(6,[77,99])->{}".format(dic_copy))
#移除指定键/值，并返回该值
dic_2.pop(5) 
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,7,6,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
#更新字典
dic_2.update(dic_update) 
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
#随即弹出一对键/值，并在该字典中移除
dic_2.popitem() 
print("dic_2.popitem()->{}".format(dic_2))
#给定键，建立值为空的字典
dic_3={}.fromkeys([0,1,2,3,4,'A']) 
print("dic_3={}"+".fromkeys([0,1,2,3,4,'A'])->{}".format(dic_3)) #找下escape characters 脱字符
#string的基础用法
lst_3=list("Harry potter!")
#"\" 是转换字符
print("lst_3=list(\"Harry potter!\")->{}".format(lst_3)) #"\" escape character
print("\"Harry\"+\" Potter!\"->{}".format("Harry"+" Potter!"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("len(\"Harry potter!\")->{}".format(len("Harry potter!")))
#eval()方法:将字符串转换为数值形式；
coordinates="114.48333,38.03333,9.7"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates))) 
#大小写转化
print("\"Harry potter!\".lower()->{}".format("Harry potter!".lower()))
print("\Harry potter!\".upper()->{}".format("Harry potter!".upper()))
#截取后半部分
print("\Harry potter!\"[8:]->{}".format("Harry potter!"[8:]))
#新建的goodbye_list
print("\"    Harry potter!    \".strip()->{}".format("    Harry potter!    ".strip()))
print("\"Harry potter!\".replace(\"DA\",\"PA\")->{}".format("Harry potter!".replace("DA","PA")))
goodbye_lst=list("Harry potter!")
goodbye_lst.sort()
print("goodbye_lst.sort()>{}".format(goodbye_lst))
print("\"Harry potter!\".find(\"Py\")->{}".format("Harry potter!".find("po")))
#字符串格式化
format_str_1="harrt,%s or %s!"
values=("DA","PA")
new_str_1=format_str_1 % values
print("new_str_1=format_str % values->{}".format(new_str_1))
#第二种：#本身如果就有%，这时候可以用两个%来进行表示
format_repr_1="Pi with three decimals:%.3f,and enter a value with percent sign:%.2f %%" 
from math import pi#从别的库中引入了数学上的字符
new_repr_1=format_repr_1 % (pi,3.1415926)#r	字符串（使用repr转换任意Python对象)
format_repr_3="%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_repr_3=format_repr_3%(pi,pi,pi,"Hello Python!",5,"Hello Python!",52,52,pi)
print("{}".format(new_repr_3))
#Template()函数-模板字符串+$+st.substitute()
from string import Template
#第一种类型
s_template_1=Template("$x,shameless,$x!")
s_1=s_template_1.substitute(x="basterd")
print("s_1=s_template_1.substitute(x=\"basterd\")->{}".format(s_1))
#第二种类型
s_template_2=Template("${x}thon is amazing!")
s_2=s_template_2.substitute(x="ba")
print("s_2=s_template_2.substitute(x=\"ba\")->{}".format(s_2))
s_template_3=Template("$x and $y are both shameless!")
substitute_dict=dict([('x','basterd'),('y','alien')])
print("substitute_dict={}".format(substitute_dict))
# 第三种类型
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))
#string-re(regular expression)正则表达式
import re
#text
pattern_1='sunshine'
text="you are my sunshine!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))
pattern_2='sunshine'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))
#(.)点号
print("re.findall('.otter','Harry potter!')->{}".format(re.findall('.otter','Harry potter!')))
print("re.findall('.otter','Harry potter!')->{}".format(re.findall('.otter','Harry potter!')))
print("re.findall('.otter','Harry gpotter!')->{}".format(re.findall('.otter','Harry potter!')))
print("re.findall('.otter','Harry potter!')->{}".format(re.findall('.otter','Harry potter!')))
#* + ？ {m,n}与r’string’
print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')))
print("re.findall(r'w{2}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{1,3}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{1,3}\.cadesign\.cn','www.cadesign.cn')))
#[] (^)
print("re.findall('[po]*tter!','Harry potter!')->{}".format(re.findall('[po]*tter!','Harry potter!')))
print("re.findall('[po]*tter!','Harry potter!')->{}".format(re.findall('[po]*tter!','Harry potter!')))
print("re.findall('[po]*tter!','Harry potter!')->{}".format(re.findall('[po]*tter!','Harry potter!')))
print("re.findall('[po]*tter!','Harry potter!')->{}".format(re.findall('[po]*tter!','Harry potter!')))
#(|)管道符号
print("re.findall('practice|geograrhy','practice')->{}".format(re.findall('practice|geograrhy','practice')))
print("re.findall('practice|geograrhy','geograrhy')->{}".format(re.findall('practice|geograrhy','geograrhy')))
print("re.findall('practice|geograrhy','geograrhy and practice')->{}".format(re.findall('practice|geograrhy','geograrhy and practice')))
#\d \D
#re模块的方法
print("re.findall('[1-26]','potter')->{}".format(re.findall('[1-26]','potter-3.0')))
print("re.search('[1-26]+','potter')->{}".format(re.search('[1-26]+','potter')))
if re.search('[1-26]+','potter'):
    print("re.search('[1-26]+','potter')->found it!")
print("re.split(',','Harry,,,,,,potter!')->{}".format(re.split(',','harry,,,,,,potter!')))
print("re.sub('potter','geography','potter potter!')->{}".format(re.sub('potter','geography','Harry potter!')))

pattern_compile=re.compile('potter')
print("pattern_compile.findall('Harry,,,,,,potter!')->{}".format(pattern_compile.findall('Harry,,,,,,potter!')))

if re.match('p','potter'):
    print("re.match('p','potter')->found it!")
#
print("_"*50)
print("\'goodbye\'.find(\'goodbye\')->{}".format('goodbye'.find('goodbye')))
print("\'goodbye\'.find(\'dbye\')->{}".format('goodbye'.find('dbye')))
print("\'goodbye\'.find(\'y\')->{}".format('goodbye'.find('y')))
print("\'g\' in \'goodbye\'->{}".format('g' in 'goodbye'))
#
print("_"*50)
print("\'Nihao,,,,,,Beijing!\'.split('.')->{}".format( 'Nihao,,,,,,Beijing!'.split('.')))
print("\'Nihao Beijing!\'.replace(\'Beijing\',\'Xian\')->{}".format( 'Nihao Beijing!'.replace('Beijing','Xian')))
#匹配对象和组
match_2=re.match(r'www\.(.*)\.(.{3})','www.python.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))
match_1=re.match(r'www\.(.*)\..{3}','www.python.org')
print("match_1.gourp(1)->{}".format(match_1.group(1)))
print("match_1.start(1)->{}".format(match_1.start(1)))
print("match_1.end(1)->{}".format(match_1.end(1)))
print("match_1.span(1)->{}".format(match_1.span(1)))
#基本语句
#for循环
for letter in 'Python':     # 第一个实例
   print("当前字母: %s" % letter)
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果: %s'% fruit)
print ("Good bye!")
#while循环
row = 1
while row <= 9:
   column = 1
   while column <= row:
       result = row * column
       # print默认end属性为“\n”，需要去掉改属性
       print("%d * %d = %d\t" % (column, row, result), end="")
       column += 1
   # 结束end=''的影响，另起一行
   print("")
   row += 1
#While True/break语句
#并行迭代
name=['a','b','c','d','e','f']
num=[1,2,3,4,5,6]
for name,num in zip(name,num):
    print(name,'是',num)
#编号迭代
name=['a','b','c','d','e','f']
for index,name in enumerate(name):
    print(index,name)
#list comprehension(列表推导式)
print("[x*x for x in range(3,37,5) if x%2==0]->{}".format([x*x for x in range(3,37,5) if x%2==0]))
print("[(x,y) for x in range(3)for y in range(2)]->{}".format([(x,y) for x in range(3)for y in range(2)]))
print("[(x,y) for x,y in zip(range(3),range(2))]->{}".format([(x,y) for x,y in zip(range(3),range(2))]))
nested_list=[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]
print("[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]->{}".format(nested_list)) #嵌套列表推导式

flatten_lst=lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst] #展平列表常用，可以放置到单独的.py文件中调用。lambda函数后文阐述
print("flatten_lst(nested_list)->{}".format(flatten_lst(nested_list)))    
#条件语句

#
x=y=[3,6,9]
z=[3,6,9]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x),id(y),id(z))) #Memory Location


#
a,b,c=0,10,15
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b kidding!!!')
#定义函数

#递归
def factorial(n):
    if n==2:
        return 2
    else:
        return n*factorial(n-2)
print(factorial(6))
#类 class
# 定义类
class Canine:
    fly='wolves' #
    def __init__(self):
        self.tired=True
    def eat(self):
        if self.tired:
            print('Nooooo...')
            self.tired=False
        else:
            print('Thanks!')

class Jackal (Canine):  #豺类
    def __init__(self):
        super(Jackal,self).__init__()
        self.sound='goby cichlid!' #狐狸类
    def sing(self):
        print(self.sound)
        
swift=Jackal()
print("swift.fly->{}".format(swift.fly))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()
#类与类的实例
blackswift=Jackal()
scarceswift=Jackal()
print("blackswift.sing()->")
blackswift.sing()
print("scarceswift.sing()->")
scarceswift.sing()
#类的属性
print("blackswift.fly->{}".format(blackswift.fly))
blackswift.fly='humming' #重新赋予实例的属性
print("blackswift.fly after redefining the blackswif's attribute->{}".format(blackswift.fly))
print("scarceswift.fly->{}".format(scarceswift.fly))
#类的方法
blackswift.sing()
# 迭代+迭代器
class Fibs():
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):  #实现迭代器的next方法
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self): #实现迭代方法
        return self
f=Fibs()
fa=[]
fb=[]
for i in range(9):
    fa.append(f.next())
print("fa={}".format(fa))
for i in range(5):
    fb.append(f.next())
print("fb={}".format(fb))

lst_d=list(range(3,20,2))
print("lst_d={}".format(lst_d))
print("_"*50)
lst_iter=iter(lst_d)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
next(lst_iter)
next(lst_iter)
#生成器(generator)
#生成器方法
def flatten(lst): #定义生成器（包含yield语句的函数）
    try: #使用语句try\except捕捉异常        
        for n_lst in lst:  #循环列表            
            for m in flatten(n_lst): #使用递归的方法循环子列表                
                yield m  #使用yield语句，每次产生多个值，当返回一个值时函数就会被冻结，当再次激活时，从停止的那点开始执行
    except TypeError:  #当函数被告知展开一个元素时，引发TypeError异常，生成器返回一个值
        yield lst #生成器返回引发异常的一个值        

print("list(flatten(lst_e))->{}".format(list(flatten(lst_e))))
#建立无穷列表
def infinite():
    n=0
    while True:
        yield 'num#'+str(n)
        n+=1
#生成器表达式(generator expression)        
n=3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]->{}".format([[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]))
print("_"*50)
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))->{}".format(([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))))
gen=([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))
print("next(gen)->{}".format(next(gen)))
print("next(gen)->{}".format(next(gen))