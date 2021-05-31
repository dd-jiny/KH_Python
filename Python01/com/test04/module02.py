# pip install numpy  ->수치해석
# pip install matplotlib -> 그래프 (시각화)

#import <module_name> as <alias>
import numpy as np
import matplotlib.pyplot as plt
import random

def plt01():
    x = np.arange(0, 11) #numpy가 가지고 있는 배열 
    y = x
    # print(x)
    
    plt.plot(x, y)
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    # 범례
    plt.legend(['y=x'])
    
    plt.show() 
    
#plt01()

#바차트 그리기 
def plt02():
    y = [random.randint(0, 10) for _ in range(10)] # _ 쓰면 range 안에 있는 값을 담아놓고 버릴것이다 라는 뜻 
    x = range(10)
    
    plt.bar(x, y)
    
    # 축 간격 설정 
    plt.xticks(range(11))
    plt.yticks(range(11))
    
    plt.show()
    
#plt02()

def plt03():
    data = [random.randint(100, 1000) for _ in range(4)]
    
    plt.pie(data)
    
    category = ['first', 'second', 'third', 'fourth']
    plt.legend(category)
    
    plt.show()
    
plt03()


























    