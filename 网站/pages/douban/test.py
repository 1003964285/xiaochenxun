# str = 'hello world'
# print(str.find('he'))
# print('l' in str)
# list = ['kd','fdk','华为','ls']
# list = [1,0,4,2]
#index = list.count(0)
# print(index)
#print(list.index(4))
# print(list)
# json = {'k':'1','s':'2'}
# print(json[0:1])

# s = int(input('请输入分数：'))
# print(s)



# def a(s):   # 负责接收装饰器的参数
#     def decorate(fn):   # 负责接收函数
#         def wrapper(*args,**kwargs):    # 负责接收函数的参数
#             fn(*args,**kwargs)
#             print('开始铺装{}'.format(s))
#         return wrapper
#     return decorate
# @a(10)  #调用装饰器
# def ss(kk):
#     print('毛坯的价格{}'.format(kk))
# ss(20);


#   作用域：本层—>套嵌—>全局—>内置

# list = [{'a':2,'b':3},{'a':4,'b':9},{'a':6,'b':7},]
# print(max(list,key=lambda x:x['b'])) #取出最大值为{'a': 4,'b': 9}
# print(min(list,key=lambda x:x['a'])) #取出最小值为{'a': 2,'b': 3}

names = ['flk','kfsdk','qldf','flk','dfsdk','sldf']
# 过滤掉字母少四个的
ss = [name.title() for name in names if len(name)>3]
print(ss)

ll = [i for i in range(100) if i%3==0]
print(ll)















