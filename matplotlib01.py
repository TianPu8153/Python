# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
# z = np.cos(x**2)

# plt.figure(figsize=(8,4))
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
# plt.plot(x,z,"b--",label="$cos(x^2)$")
# plt.xlabel("Time(s)")
# plt.ylabel("Volt")
# plt.title("PyPlot First Example")
# plt.ylim(-1.2,1.2)   
# plt.legend()
# plt.show()
nums=[]
x=[]
y=[]
for i in range(0,1000):
	nums.append(random.randint(0,20))
print len(nums)
i=0
while i < len(nums):
	if nums[i] in x:
		i=i+1
	else:
		x.append(nums[i])
		i=i+1
x.sort()
print x
i=0
j=0
count=0
for i in x:
	while j < len(nums):
		if i == nums[j]:
			count=count+1
		j=j+1
	y.append(count)
	count=0
	j=0
print y

#print nums,x
# for i in x:
# 	print i

plt.figure(figsize=(8,4))
plt.plot(x,y,':o',label="$random$",color="red",linewidth=2)
plt.xlabel("random")
plt.ylabel("count")
plt.title("PyPlot First Example")
plt.ylim(0,100)   
plt.legend()
plt.show()