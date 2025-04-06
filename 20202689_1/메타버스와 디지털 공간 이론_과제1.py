import os, sys
from math import sqrt
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Tkinter 창 숨기기


# 백터 클래스 정의
class Vector:
    def __init__(self):
        pass

    def mag(self, a):
        return sqrt(a[0]**2 + a[1]**2 + a[2]**2)
        
    def add(self,a,b):
        return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]
    
    def inner(self, a, b):
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    
    def cross(self, a, b):
        return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
    
# 행렬 클래스 정의
class Matrix:
    def __init__(self):
        pass

    def add(self, a, b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            return "Invalid input"
        
        return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    
    def mult(self, a, b):
        if len(a[0]) != len(b):
            return "Invalid input"
        
        # 최대 4x4 행렬까지 지원
        if len(a) > 4 or len(a[0]) > 4 or len(b) > 4 or len(b[0]) > 4:
            return "Up to 4 rows and 4 columns"
        
        return [[sum([a[i][k]*b[k][j] for k in range(len(a[0]))]) for j in range(len(b[0]))] for i in range(len(a))]
    
    def trans(self, a):
        return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


# input data
if getattr(sys, 'frozen', False):   # pyinstaller로 빌드된 경우 임시 디렉토리를 가리키는 것을 방지
    working_dir = os.path.dirname(sys.executable)
else:
    working_dir = os.path.dirname(__file__)
input_path = os.path.join(working_dir, "input.txt")
output_path = os.path.join(working_dir, "output_20202689.txt")

print("Input file path:", input_path)
try:
    f = open(input_path, 'r')

    data = []
    # 개행문자 제거 후 리스트 append
    for i in f:
        i = i.replace("\n", "")
        data.append(i)
    f.close()
except FileNotFoundError:
    print("Input file not found.")
    messagebox.showerror("Error", "Input file not found.")
    exit()

print("==============\n", data)

result = []   # 결과값
# 대상 판별
if data[0] == "vector": # 벡터 연산
    # 연산 명령
    if data[1] == "mag": # 벡터 길이
        a = list(map(float, data[2].split()))
        result.append('scalar\n')
        result.append(round(Vector().mag(a), 2))
    
    elif data[1] == "add":  # 덧셈
        a = list(map(float, data[2].split()))
        b = list(map(float, data[3].split()))
        result.append('vector\n')
        result.append("   ".join(map(str,Vector().add(a, b))))

    elif data[1] == "inner": # 내적
        a = list(map(float, data[2].split()))
        b = list(map(float, data[3].split()))
        result.append('scalar\n')
        result.append(Vector().inner(a, b))

    elif data[1] == "cross": # 외적
        a = list(map(float, data[2].split()))
        b = list(map(float, data[3].split()))
        result.append('vector\n')
        result.append("   ".join(map(str,Vector().cross(a, b))))

    else:
        result = "Invalid input"

elif data[0] == "matrix":
    if data[1] == "add": # 덧셈
        row_a, col_a = map(int, data[2].split())
        row_b, col_b = map(int, data[3+row_a].split())
        a = []
        b = []
        for i in range(row_a):
            a.append(list(map(float, data[3+i].split())))
        for i in range(row_b):
            b.append(list(map(float, data[4+row_a+i].split())))
        result.append('matrix\n')

        temp = Matrix().add(a, b) # 결과가 올바른지 확인
        if temp == "Invalid input":
            result.append(temp)
        else:
            result.append(f"{len(temp)}   {len(temp[0])}\n")
            for i in range(len(temp)):
                result.append("   ".join(map(str,temp[i])))
                result.append("\n")

    elif data[1] == "mult": # 곱셈
        row_a, col_a = map(int, data[2].split())
        row_b, col_b = map(int, data[3+row_a].split())
        a = []
        b = []
        for i in range(row_a):
            a.append(list(map(float, data[3+i].split())))
        for i in range(row_b):
            b.append(list(map(float, data[4+row_a+i].split())))

        # print("!!!!!!!!!!!", a, b)
        
        result.append('matrix\n')
        
        temp = Matrix().mult(a, b)  # 결과가 올바른지 확인
        if temp == "Invalid input":
            result.append(temp)
        else:
            result.append(f"{len(temp)}   {len(temp[0])}\n")
            for i in range(len(temp)):
                result.append("   ".join(map(str,temp[i])))
                result.append("\n")
        
    elif data[1] == "trans": # 전치
        row, col = map(int, data[2].split())
        a = []
        for i in range(row):
            a.append(list(map(float, data[3+i].split())))
        print("!!!!!!!!!!!", a)
        result.append('matrix\n')
        result.append(f"{len(a[0])}   {len(a)}\n")
        a = Matrix().trans(a)
        print("!!!!!!!!!!!2222222222", a)
        for i in range(len(a)):
            result.append("   ".join(map(str,a[i])))
            result.append("\n")

    else:
        result = "Invalid input"

    

else:
    result = "Invalid input"



print("==============\n", result)

# output data
f = open(output_path, 'w')
for i in result:
    f.write(str(i))
f.close()