import datetime

#1

x=datetime.datetime.now()

d=datetime.timedelta(days=5)

x-=d


print(x)

#2

x=datetime.datetime.now()

d=datetime.timedelta(days=1)

print(x.day)

x-=d

print(x.day)

x+=2*d

print(x.day)

#3

x=datetime.datetime.now().replace(microsecond=0)

print(x)

#4

x=datetime.datetime.now()

d=datetime.timedelta(weeks=12)

a=x-d

print((x-a).total_seconds())

