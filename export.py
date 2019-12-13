# -*- coding:utf-8 -*- 
# import pandas as p
# inputfile = "C:\\Users\\xietong\\Desktop\\111\\test1.xls"
# data = p.read_excel(inputfile)

# list1 = data.head()
# print(list1)

# df = p.read_excel(inputfile,sheet_name='表3 改造点开发工作量核算表')
# print(df)

# dd = data.loc[1,1].values
# print(dd)

# data = p.DataFrame(p.read_excel(inputfile,sheet_name='COSMIC软件评估标准模板'))
# print(data)
# df = data[[]]

from datetime import datetime,timedelta
from collections import namedtuple,deque,defaultdict,OrderedDict
import base64
import random,time,queue


now = datetime.now()
print(now)
print(type(now))
dt = datetime(2019,3,3,3,3,3)
print(dt)
timestamp = 0
print(timestamp)
dt.timestamp()
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
print(datetime.utcfromtimestamp(dt.timestamp()))
print(datetime.strptime('2010-2-2 12:12:12','%Y-%m-%d %H:%M:%S'))
print(now.strftime('%a,%b,%H,%M'))
now = datetime.now()
now
# datetime.datetime(2019,3,3,3,3,3,3454343)
now
print(now)
print(now-timedelta(days=1))
point = namedtuple('point',['x','y'])
p = point(1,2)
p.x
print(p.x)
print(p.y)
circle = namedtuple('circlec',['x','y','z'])
cd = circle(1,2,3)
print(cd.x)
# print(cd.circlec())
q = deque(['a','v','f'])
q.append('c')
q.appendleft('left')
print(q)
q.pop()
print(q)
q.popleft()
print(q)
d = defaultdict(lambda:'N/A')
d['key1'] = 'abc'
print(d['key1'])
d['key2']
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
