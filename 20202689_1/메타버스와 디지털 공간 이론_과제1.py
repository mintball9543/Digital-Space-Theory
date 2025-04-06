import os
from math import sqrt

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
working_dir = os.path.dirname(__file__)
input_path = os.path.join(working_dir, "input.txt")
output_path = os.path.join(working_dir, "output_20202689.txt")

f = open(input_path, 'r')

data = []
for i in f:
    i = i.replace("\n", "")
    data.append(i)
f.close()

print("==============\n", data)

result = []   # 결과값
# 대상 판별
if data[0] == "vector": # 벡터 연산
    # 연산 명령
    if data[1] == "mag": # 벡터 길이
        a = list(map(float, data[2].split()))
        result.append('scalar\n')
        result.append(Vector().mag(a))
    
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
    if data[1] == "add":

    elif data[1] == "mult":

    elif data[1] == "trans":

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