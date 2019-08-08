import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")


#33-A
#1
#1-a 정규분포를 따르는 랜덤 샘플을 500개 생성
np.random.seed(100)
samples = np.random.normal(size=500)
print(samples)


#1-b 랜덤 샘플의 중앙값 계산
print(np.median(samples))
#결과 : -1.2413930609287396

#1-c 랜덤 샘플의 표준편차 계산
print(np.std(samples))
#결과 : 1.0328007104786638

#1-d 상위 20% 값 계산
print(stats.scoreatpercentile(samples, 80))
#결과 : 0.8629129507703023

#1-e 정규분포로 추측, 평균/표준편차 계산
loc, std = stats.norm.fit(samples)
print(loc, std)
#결과 : (-0.0054181737507954285, 1.0328007104786638)

#33-A
#2 행렬연산 (numpy or scipy로 구하기)
from scipy import linalg
import numpy as np

arr=np.array([[1,3,5],[2,4,6],[6,5,8]])


#2-a determinent 구하기
print(linalg.det(arr))
#결과 : -7.999999999999992

#2-b 역행열 inverted matrix구하기
print(linalg.inv(arr))
#결과 :
"""
array([[-0.25 , -0.125,  0.25 ],
       [-2.5  ,  2.75 , -0.5  ],
       [ 1.75 , -1.625,  0.25 ]])
"""

#3 determinent구하기, 오류 발생시 이유?

from scipy import linalg
import numpy as np

arr2=np.array([[1,2,3,4],[3,8,5,2],[4,3,6,2]])
print(linalg.det(arr2))
#결과:arr2 가 square matrix가 아니므로 determinent를 구할 수 없음



#33-A
#4 scipy사용하지 말고 numpy및 Gaussian 소거법을 사용하여 LU decom하기
A=np.array([[2,2,2],[4,7,7],[6,18,22]])
U=np.identity(3)
np.copyto(U,A)
print('U=\n' + str(U))
#결과:
'''
U=
[[ 2.  2.  2.]
 [ 4.  7.  7.]
 [ 6. 18. 22.]]
'''

#step 1
U[1] = U[1] + (-2)*U[0]


E_21=np.identity(3)
E_21[1,0] = -2

print('U=\n' + str(U))
print('E_21 = \n' + str(E_21))
#결과:
'''
U=
[[ 2.  2.  2.]
 [ 0.  3.  3.]
 [ 6. 18. 22.]]
E_21 = 
[[ 1.  0.  0.]
 [-2.  1.  0.]
 [ 0.  0.  1.]]
'''

#step 2
U[2]=U[2]+(-3)*U[0]


E_31=np.identity(3)
E_31[2,0] = -3

print('U=\n' + str(U))
print('E_31= \n' + str(E_31))
#결과:
'''
U=
[[ 2.  2.  2.]
 [ 0.  3.  3.]
 [ 0. 12. 16.]]
E_31= 
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [-3.  0.  1.]]
'''
#step 3
U[2]=U[2]+(-4)*U[1]

E_32=np.identity(3)
E_32[2,1] = -4
print('U=\n' + str(U))
print('E_32= \n' + str(E_32))
#결과
'''
U=
[[2. 2. 2.]
 [0. 3. 3.]
 [0. 0. 4.]]
E_32= 
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0. -4.  1.]]
 '''

#step 4
L = np.linalg.inv( np.matmul((E_32, E_31), E_21))
print('L=\n' + str(L))
print('U=\n' + str(U))
print('A=\n' + str(np.matmul(L,U)))
#결과
'''
L=
[[[ 1.  0.  0.]
  [ 2.  1.  0.]
  [ 0.  4.  1.]]

 [[ 1. -0. -0.]
  [ 2.  1.  0.]
  [ 3.  0.  1.]]]
U=
[[2. 2. 2.]
 [0. 3. 3.]
 [0. 0. 4.]]
A=
[[[ 2.  2.  2.]
  [ 4.  7.  7.]
  [ 0. 12. 16.]]

 [[ 2.  2.  2.]
  [ 4.  7.  7.]
  [ 6.  6. 10.]]]
'''


#5 4번 문제를 Scipy를 이용해서 LU decomp 코드 작성

A = np.array([[2,2,2],[4,7,7],[6,18,22]])

P,L,U =linalg.lu(A)
print('L=\n' + str(L))
print('U=\n' + str(U))
print('LU=\n' + str(np.matmul(P, np.matmul(L,U))))
#결과
'''
L=
[[1.         0.         0.        ]
 [0.66666667 1.         0.        ]
 [0.33333333 0.8        1.        ]]
U=
[[ 6.         18.         22.        ]
 [ 0.         -5.         -7.66666667]
 [ 0.          0.          0.8       ]]
LU=
[[ 2.  2.  2.]
 [ 4.  7.  7.]
 [ 6. 18. 22.]]
'''


#6
np.random.seed()
x_data= np.linspace(-5, 5, num=50)
y_data= 4*np.cos(2*x_data) + np.random.normal(size=50)

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.scatter(x_data, y_data)
plt.show()



#7 cos 함수로 생성된 것 vs sin 함수로 생성된 것의 진폭과 주기 구하기
from scipy import optimize
cos_params, cos_params_covariance = optimize.curve_fit( lambda x, a, b : a* np.cos(b*x), x_data, y_data, p0 = [2,2] )
sin_params, sin_params_covariance = optimize.curve_fit( lambda x, a, b : a* np.sin(b*x), x_data, y_data, p0 = [2,2] )

print(cos_params, sin_params)
#결과 [3.74335071 2.00161245] [-0.3500712   2.11013692]


#8 두 반의 몸무게 분포의 기댓값의 동일여부

class1 = [65.9, 53.6, 57.3, 59.3, 63.8, 59.2, 64.2, 75.0, 62.9]
class2 = [76.3, 82.1, 73.3, 69.3, 59.9, 72.1, 59.1, 86.8, 78.1]

print("estimator of class1: %f" %(np.mean(class1)))
print("estimator of class2: %f" %(np.mean(class2)))

#결과
"""
estimator of class1: 62.355556
estimator of class2: 73.000000
"""


