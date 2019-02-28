#-*-coding:utf-8

# 연습문제 1
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

for i in range(10):
    print(fib(i), end=" ")
print()

# 연습문제 2
f = open("sample.txt", "r", encoding="utf8")
lines = f.readlines() # 파일을 한줄씩 모든 내용을 읽음
# 리스트에 읽은 내용을 모두 반환
# 파일에서 읽은 내용은 모두 문자열 타입임
f.close()

sum = 0
avg = 0

for val in lines:
    val = int(val) # 문자열 타입을 숫자형 타입으로 변환
    sum += val

avg = sum / len(lines)
print("파일 내용의 숫자의 총합 : {0}".format(sum))
print("파일 내용의 숫자의 평균 : {0}".format(avg))

f = open("result.txt", "w", encoding="utf8")
f.write(str(avg)) # 파일에 내용을 쓸때 모두 문자열 타입으로 써야함
# 숫자형 타입을 문자열 타입으로 변환 후 쓰기
f.close()


# 문제 3) 파일을 열고, 메뉴에 따라서 파일의 내용을 확인하고 파일의 내용을 입력하는 형태의 프로그램을 작성하세요
# 파일명 : memory.txt
# 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 0. 종료
# 내용 입력 시 기존 내용을 덮어쓰기하는 형태로 작성

print("{0}3번 문제{0}".format("-" * 5))
while True:
    print("1. 내용 입력 | 2. 내용 출력 | 0. 종료")
    menu = input("메뉴를 선택하세요 : ")
    menu = int(menu)

    if menu == 1:
        print("파일에 저장할 내용을 입력하세요")
        tmp = input("> ")
        f = open("memory.txt", "w", encoding="utf8")

        # while True:
        #     tmp = input("> ")
        #     if tmp == "0":
        #         f.close()
        #         break
        #     f.write(tmp)

        f.write(tmp)
        f.close()

    elif menu == 2:
        f = open("memory.txt", "r", encoding="utf8")
        memory = f.readlines()
        f.close()

        for memo in memory:
            print("내용 출력 > {0}".format(memo))

    elif menu == 0:
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
        continue


# 문제 4) 위의 문제 3번을 함수를 이용하여 프로그램을 작성하세요
# 내용 입력 함수명 memoryWrite
# 내용 출력 함수명 memoryRead
# 다른 사항은 문제 3번과 동일
print("{0}4번 문제{0}".format("-" * 5))

def memoryWrite(tmp, fileName):
    f = open(fileName, "w", encoding="utf8")
    f.write(tmp)
    f.close()

def memoryRead(fileName):
    f = open(fileName, "r", encoding="utf8")
    memory = f.readlines()
    f.close()

    for memo in memory:
        print("내용 출력 > {0}".format(memo))

while True:
    print("1. 내용 입력 | 2. 내용 출력 | 0. 종료")
    menu = input("메뉴를 선택하세요 : ")
    menu = int(menu)

    if menu == 1:
        print("파일에 저장할 내용을 입력하세요")
        tmp = input("> ")
        memoryWrite(tmp, "memory.txt")

    elif menu == 2:
        memoryRead("memory.txt")

    elif menu == 0:
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
        pass

# 성적표 출력 함수를 사용하여 프로그램 제작
# 5점에 한단계식 낮아짐
# 95점 이상 A+, 90 이상 A, ...
# 60점 미만은 F

# score = input("성적을 입력하세요 : ")
# score = int(score)

# if score >= 95:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("A+"))
# elif score >= 90:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("A"))
# elif score >= 85:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("B+"))
# elif score >= 80:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("B"))
# elif score >= 75:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("C+"))
# elif score >= 70:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("C"))
# elif score >= 60:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("D"))
# else:
#     print("성적은 {0}이며, ".format(score))
#     print("등급은 {0}입니다.".format("F"))

print()

def scorePrint(score, level):
    print("성적은 {0}이며, ".format(score))
    print("등급은 {0}입니다.".format(level))

def selectLevel(score):
    if score >= 95:
        scorePrint(score, "A+")
    elif score >= 90:
        scorePrint(score, "A")
    elif score >= 85:
        scorePrint(score, "B+")
    elif score >= 80:
        scorePrint(score, "B")
    elif score >= 75:
        scorePrint(score, "C+")
    elif score >= 70:
        scorePrint(score, "C")
    elif score >= 60:
        scorePrint(score, "D")
    else:
        scorePrint(score, "F")

def inputScore():
    score = input("당신의 점수를 입력하세요 : ")
    score = int(score)

    return score


selectLevel(inputScore())

# selectLevel(score)

# score = input("당신의 점수를 입력하세요 : ")
# score = int(score)

# selectLevel(score)