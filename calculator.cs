import random

count = 1

 

print('< 100가지의 계산을 해볼까요?')

print('  계산의 정답을 입력해 보세요 >')

 

while True :

    r = random.randint(1,9)

    s = random.randint(1,9)

    print()

    print(count,'.',r,'x',s)

 

       

    number = int(input('= '))

 

    if r*s == number :

        print("정답입니다! 다른 문제로 넘어가볼까요?")

        count += 1

        

    else:

        print("안타깝지만 오답이에요.다시 해볼까요?"

              " 계산을 다시 해봐요!")

        print(r,'x',s)

        number = int(input('= '))

        if r*s == number:

            print('잘했어요~ 다음 문제로 넘어가요')

        else:

            print('오답이에요! 마지막으로 다시 해볼까요?')

        print(r,'x',s)

        number = int(input('= '))

        count += 1

        if r*s==number:
            print('게임을 모두 통과했습니다. 프로그램을 종료합니다.')
            
        else:
            from tkinter import *
            from tkinter import messagebox

            #전역 변수 선언
            btnList = [None] * 9 
            fnameList = ["bird1.gif", "bird2.gif", "bird3.gif", "bird4.gif", "bird5.gif",
                         "bird6.gif","bird7.gif", "bird8.gif", "bird9.gif"] 
            photoList = [None] * 9 
            i, k = 0, 0
            xPos, yPos = 0, 60
            num = 0

            correct, false = 0, 0


            #함수
            def macroCorrect():
                global correct
                correct += 1


            def macroFalse():
                global false
                false += 1


            def func():
                global correct
                global false
                if correct == 3 and false == 0:
                    messagebox.showinfo('맞았습니다','계산으로 돌아가세요.')
                    correct, false = 0, 0
                    # 계산 실행
                    
                else:
                    messagebox.showinfo('틀렸습니다', '프로그램이 종료됩니다.')
                    window.quit()
                    window.destroy()
                    # 프로그램 종료
               
                



            #메인코드
            window = Tk() 
            window.geometry("300x400") 

            for i in range(0,9): 
                photoList[i] = PhotoImage(file = "/Users/zziey/OneDrive/바탕 화면/bird/" + fnameList[i])
                if i == 2 or i == 4 or i == 5:
                    btnList[i] = Button(window, image = photoList[i], command = macroCorrect)

                else:
                    btnList[i] = Button(window, image = photoList[i], command = macroFalse)
                    

            for i in range(0, 3): 
                for k in range(0, 3): 
                    btnList[num].place(x = xPos, y = yPos)
                    num += 1
                    xPos += 100

                xPos = 0
                yPos += 100



            button1 = Button(window, text = "확인", command = func)
            button1.pack(side = BOTTOM, ipadx = 210)

            button2 = Button(window, text = "새가 있는 칸을 모두 클릭하세요.\n (캡차는 봇이나 자동화된 해킹으로부터 \n 웹사이트를 보호하기 위해 만들어진 기술입니다.) ")
            button2.pack(side = TOP, ipadx = 210)




            window.mainloop() 



 

    if count == 101:

        break

    

print()

print('게임이 종료되었습니다')

 

 

# **연결할 때 그림찾기 나온 후 정답 나오도록 부탁드려요~

#print(r,'x',s,'=',r*s)
