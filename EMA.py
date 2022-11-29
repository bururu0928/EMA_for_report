from manim import *
from template import*
import time

class EMA(explanatoryTools):
    def construct(self):

        while 1:
            question=input('Input a question\n')
            #判斷輸入的運算類別
            if '+' in question:
                a,b = map(int,question.split('+'))
                sign = '+'
                ans = a+b
                break
            elif '-' in question:
                a,b = map(int,question.split('-'))
                sign = '-'
                ans = a-b
                break
            elif '*' in question:
                a,b = map(int,question.split('*'))
                sign = '×'
                ans = a*b
                break
            else:
                a=b=sign=''
                print('Invalid Input')
        start=time.time()
        #self.ask(a, b, sign=sign)
        self.ans(ans)
        match sign:
            case '+':
                self.add_line(a,b)
                self.add_column_form(a,b)
            case '-':
                self.sub_column_form(a,b)
                self.sub_line(a,b)
                #self.sub_column_form(a,b)
        #self.ans(ans)
        self.ask(a, b, sign=sign)
        self.pause()
        print(time.time()-start)

if __name__ == '__main__':
    while 1:
        with tempconfig({'quality':'medium_quality', 'disable_caching':True, "preview":True}):
                scene = EMA()
                scene.render()