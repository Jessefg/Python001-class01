学习笔记  
1. render() 将给定的模板与给定的上下文字典组合在一起，并以渲染文本返回一个HttpResponse对象  
2. redirect() 将HttpResponseRedirect跳转到传递的参数的适当的URL  
3. get_object_or_404() 在给定的模型管理器（model manager）上调用get()，但它会引发404，而不是模型的DoesNotExist异常
  
 代码优先控制db  
 ```
python manage.py makemigrations  # 让django确定该如何修改数据库
python manage.py migrate  #执行转化为实质的sql
python manage.py inspectdb >douban/models.py   # 将mysql字段转化为django的 models.py
```