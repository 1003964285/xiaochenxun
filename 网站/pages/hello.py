from urllib import request

#print('hello world')
#print(100*100)

#name=input('请输入你的名字：')
#print('你的名字是：', name)

#age = int(input("请输入你的出生年份："))
#if age>2000:
#	print("你出生时",age)
#	print("你是00后")
#elif age>1990:
#	print("你出生时",age)
#	print('你是90后')
#else:
#	print("你出生时",age)
#	print('你老了')


#循环
#L = ['Bart', 'Lisa', 'Adam']
#for item in L:
#	print("你好：",item)
	
#n = 1
#while n<10:
#	if n==6:
#		print('已经满足条件n=',n) 
#		break 
#	n = n+1

#函数
#def add(x,y,*args):
#	print(args.set())
#	pass
#add(5,4,5,6)

#数组切片
#l = list(range(1,7))  #[1,2,3,4,5,6]
#print(l[2:4])#从下标2开始，截取到下标4但不包含4  
#l[0:2] 或 l[:2] 	#得到[1,2]
#l[-2:] 			#得到[5,6]

#l = []
#for item in range(1,11):
#	l.append(item*item)
#print(l)
	
url = 'https://search.51job.com/list/020000,000000,0000,32,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
rsp = request.urlopen(url)

html = rsp.read()
html = html.decode()
print(html)
