## 重写
* 内置可重写函数  
  Python中，以双下划线开头、双下划线结尾的是系统定义的成员。  
  我们可以在自定义类中进行重写，从而改变其行为。  
  __str__函数：将对象转换为字符串(对人友好的)  
  __repr__函数：将对象转换为字符串(解释器可识别的)  
  
* 运算符重载  
  定义：让自定义的类生成的对象(实例)能够使用运算符进行操作。
  * 算数运算符
  * 反向算数运算符
  
* 多继承  
  一个子类继承两个或两个以上的基类，父类中的属性和方法同时被子类继承下来。  
  同名方法的解析顺序（MRO， Method Resolution Order）:  
  类自身 --> 父类继承列表（由左至右）--> 再上层父类  