from django.shortcuts import render
import MySQLdb
def showUserProduct(request):
  return render(request,'userProduct.html',{'mesg':''})

def submitUserProduct(request):
 try:
   conn=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='electronics')
   cmd=conn.cursor()
   q="insert into userproduct(productid,channel,place,email) values('{}','{}','{}','{}')".format(request.GET['productid'],request.GET['channel'],request.GET['place'],request.GET['email'])
   cmd.execute(q)
   conn.commit()
   conn.close()
   mesg='Record Submitted'
 except Exception as e:
   mesg=e
 return render(request,'userProduct.html',{'mesg':mesg})      	

def ShowUserProduct(request):
 try:
   conn=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='electronics')
   cmd=conn.cursor()
   q="select P.*,UP.* from products P,userproduct UP where P.productid=UP.productid and UP.email='{}'".format(request.session['EMAIL'])
   cmd.execute(q)
   result=cmd.fetchall()
   conn.close()
 except Exception as e:
   result=e
 return render(request,'ShowAllUserProducts.html',{'result':result})

    	