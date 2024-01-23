
#x=[[1,2,3],[4,5,6],['hello','world']] # 모든 type와 자료형은 객체
y=[10,11,12]
z=[1,2,3]
z.append(4)         # z에 원소로 하나의 값 4를 추가
z.extend([5,6])     # z에 다른 리스트 [5, 6]의 모든 원소를 추가
print(z)

print(z*3)          # 연산이 아닌 3번 반복
print(z[1]+1)       # list의 요소와 연산가능

z.sort(reverse=True)# 내림차순
z.sort()            # 오름차순

#del (z[1:3]) 
print(z)
#z.remove()

a=(1,2,3)
b=list(a[0:2])      # tuple자료형을 list로 바꿈
print(b)
print(type(y))      # <class 'list'>

t1=(1,2,3)
t2=(4,5,6)
c=t1*3
print(len(t1))
print(type(y))

d=11
if d > 10:
    print(' d is')          # 들여쓰기에 따라 if문에 속하는 여부를 알 수 있다
    print(' d is smaller than 11')
elif d < 10:                # python은 switch문 없는 대신 elif문이 있다
    print(' e is')
elif d == 10:
    print(' d is 10')
    
import numpy as np          #넘파이(NumPy)라는 라이브러리
import random

num = [1,2,3,4,5]
x = np.array(num)           # 벡터(1차원 배열)은 np.array(list 형)으로 정의
print(num*3)
print(x*3)
print(type(x))              # <class 'numpy.ndarray'>
print(np.random.rand(2, 3)) # 요소가 랜덤(임의)인 행렬을 생성, 0과 1 사이의 균일 분포에서 난수를 생성

random.seed(1)
print(random.random())
a = np.arange(12)           # 요소의 값이 1씩 증가하는 벡터 배열을 생성
#print(a)
a.reshape(2, 6)             # 행렬의 크기를 변경
print(a)

def my_func1():             # 함수는 def 함수명():시작, 함수 내용은 들여쓰기
    print('Hi')
    
my_func1()
    