import Mod.mod1 as mod1

class Calculator:           # 클래스 선언
    def __init__(self):     # 생성자, self=this, __init__=호출X
        self.result = 0     # result=객체에 소속된 전역변수

    def add(self, num):     # 호출은 중복되어도 메모리는 한 번만 만듦 
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result
    def div(self, num):
        pass                # pass는 아무것도 수행하지 않는 문법

cal1 = Calculator()         # cal1=객체로서 별도의 메모리 공간에 만듦
cal2 = Calculator()

'''여러 줄 주석
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print(cal1.sub(3))
print(cal1.sub(4))
print(cal2.sub(3))
print(cal2.sub(7))
'''

class FourCal:
    def __init__(self, first=0, second=0):  # first=0, second=0 초기화하면 b = FourCal(2,1)도 실행가능
        self.first=first
        self.second=second
        self.result=0
    def setdata(self,a,b):                  # setdata메서드(클래스 내부의 함수), (self,a,b)매개변수
        self.first=a                        # 메서드의 수행문
        self.second=b
    def add(self):                          # self는 전달된 객체 a,b
        self.result=self.first+self.second
        return self.result
    def sub(self):
        self.result=self.first-self.second
        return self.result
    def mul(self):
        self.result=self.first*self.second
        return self.result
    def div(self):
        self.result=self.first/self.second
        return self.result

class MoreFourCal(FourCal):                 # 상속=기존 클래스 변경없이 기능 추가or기존 기능변경
    def pow(self):
        self.result=self.first**self.second # 제곱
        return self.result

class SafeFourCal(FourCal):                 # 함수 오버라이딩(덮어쓰기)
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(2, 5)
print(a.pow())

a = SafeFourCal(4, 0)
print(a.div())


#a = FourCal()
#b = FourCal(2,1)
#a.setdata(4, 2)                             # 연산을 수행할 대상을 객체에 지정
#FourCal.setdata(a,6,3)                      # 객체를 호출하는 다른 방법
#print(id(a.first))                          # 클래스로 만든 객체의 객체변수는 고유 값을 저장할 수 있는 공간

#print(a.add())
#print(a.sub())
#print(a.mul())
#print('{0:.2f}'.format(a.div()))            # 보간문자열 사용, 소수점 이하 2자리 출력

from Mod.mod1 import *

# __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름
import Mod.mod1 as mod1
print(mod1.__name__)

import game.sound as sound

sound.sound.echo.echo_test()