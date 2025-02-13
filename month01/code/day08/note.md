# day08
#### 函数返回值
* 定义者传递给调用者的信息
* debug 快捷键   
F8 (跳过方法)  
F7 (进入方法) 
#### return语句  
  1.返回结果  
  2.结束程序,return 后面的语句不执行
#### 可变／不可变类型在传参时的区别
* 1.不可变类型参数有:  
  数值型(整数，浮点数,复数)  
  布尔值bool  
  None 空值  
  字符串str  
  元组tuple  
  固定集合frozenset
* 2.可变类型参数有:  
  列表 list  
  字典 dict  
  集合 set  
* 3.传参说明：  
  不可变类型的数据传参时，函数内部不会改变原数据的值。  
  可变类型的数据传参时，函数内部可以改变原数据。
```
# 在方法区存储函数代码，不执行函数体
def func01(a):
    a[0] = 100  # 改变的是传入对象的指向
def func02(a):
    a = 100  # 改变的是栈帧中 a 的指向

list01 = [1]
number01 = 1
# 函数调用时，开辟内存空间，结束后释放
func01(list01)
func02(number01)
print(list01)  # [100]
print(number01)  # 1
```
#### 函数作用域
    1. 作用域：变量起作用的范围。
    2. Local局部作用域：函数内部。
    3. Enclosing  外部嵌套作用域 ：函数嵌套。 
    4. Global全局作用域：模块(.py文件)内部。 
    5. Builtin内置模块作用域：builtins.py文件。
### 形参和实参
#### 实参
* 位置实参.
``` 
def func(a,b,c,d):
    print(a,b,c,d)
func(1,2,3,4)  # 1 2 3 4
```
* 关键字实参.
``` 
func(b=1,c=2,d=3,a=4)  # 4 1 2 3  
```
* 序列实参:一个星号将序列拆分后按位置与形参对应.   
如果参数过多，可以存储在序列中(字符串列表元组)
``` 
list01 = [1,2,3,4]
func(*list01)  # 1 2 3 4
```
* 字典实参:两个星号将字典拆分后按名称与形参对应.  

``` 
dict01 = {"a":1,"b":2,"c":3,"d":4}
func(**dict01)  # 1 2 3 4
```

#### 形参
* 默认形参：如果参数不提供，可以使用默认值
```
def func(a=1):
    print(a)
func()  # 1
func(2)  # 2
```
* 位置形参：
```
def func(a, b, c):
    print(a, b, c)
```
* 星号元组形参:让位置实参无限
```
def func(*args):
    print(args)
func(1,2,3,4)  # (1, 2, 3, 4)
```
* 位置形参 + 星号元组形参
``` 
def func(a, *args):
    print(a, args)
func(1,2,3,4)  # 1 (2, 3, 4)
```
* 位置形参 + 星号元组形参 + 关键字形参：  
(对于关键字形参，调用时必须使用关键字实参)
```
def func(a, *args, b):
    print(a, args, b)
func(1, 2, 3, b=4)  # 1 (2, 3) 4
```
* 字典形参：实参可以传递无限的关键字实参
``` 
def func(**kwargs):
    print(kwargs)
func(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
```
* 参数自左至右的顺序  
  位置形参 --> 星号元组形参 -->   
  命名关键字形参 --> 双星号字典形参