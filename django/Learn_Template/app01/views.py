from django.shortcuts import render,HttpResponse
from app01.models import *

# Create your views here.

import time,datetime
def show_time(req):
    # t=time.ctime()
    # return render(req,"show_time.html",{"time":t})

    t=datetime.datetime.now()
    return HttpResponse("<html><body> is %s</body></html>"%t)


class Person():
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex


def query(req):
    l=["zibo","rong","ziyan"]
    d={"name":"ziboris","age":19,"friend":l}
    c=Person("lihaocheng","male")
    
    testFilter="hello world"
    
    t=datetime.datetime.now()
    l2=[]
    link1="<a href='www.baidu.com'>click</a>"
    shjdcgjkhsgdksjaajhksgdvjkhag='hello'
    
    # return render(req,"index.html",{"list":l,"dictionary":dict})
    return render(req,"index.html",locals())
    

def login(req):
    return render(req,"login.html")


def backend(req):
    # return render(req,"main.html")
    return render(req,"base.html")
    
def student(req):
    # 链接数据库取出学生信息
    student_list=['ziboris','rongziyan','xijinping']
    # return render(req,"student.html",locals())
    # 采用继承，省去大段的重复冗余代码
    return render(req, "student2.html", locals())

# --------------
def indexDB(req):
    return render(req,"indexDB.html")

def addBook(req):

    # 方法1
    # b=Book(name="python",price=99,pub_date="2017-12-12",author="zhangzibo")
    # b.save()

    # 方法2 
    Book.objects.create(name="python基础",price=109,pub_date="2017-12-05",author="kakaka")
    return HttpResponse("add successfully!")

def updateBook(req):
    # 方法1
    # Book.objects.filter(author="zhangzibo").update(price=999)

    # 方法2 save不管是否修改字段 所有字段全部都修改一次，重新赋值，效率低下
    # b=Book.objects.filter(author="zhangzibo")
    # print(type(b))
    # print(b)
    # b[0].price=120
    # b[0].save()

    b=Book.objects.get(id=2) #只能取返回一条的结果，多条结果报错
    b.price=100
    b.save()



    return HttpResponse("update successfully")

def deleteBook ( req ) :
    # Book.objects.filter(author='kakaka').delete()
    Book.objects.filter(author='zhangzibo').delete() # 可以删除多条语句
    return HttpResponse("delete successfully")


def queryBook(req):
    book_list = Book.objects.all()[:3]
    # first
    # last
    # get 这单个都不是拿到的集合，不能迭代
    # print(book_list[0])

    ret=Book.objects.filter(author='boris').values('name','price')
    # value_list
    # exclude 和filter相反结果
    return render(req, "indexDB.html", {"book_list": book_list, 'ret':ret})







