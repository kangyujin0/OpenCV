# 이미지 특징 추출
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt # 단일 플롯에 다수 이미지 그리기
import matplotlib.image as img

fig=plt.figure() # 도화지 생성
ax1=fig.add_subplot(1, 3, 1) # 이미지 삽입 ()=1행,3열,인덱스
ax2=fig.add_subplot(1, 3, 2) # add_subplot_한 화면에 여러개 그리기
ax3=fig.add_subplot(1, 3, 3)
ori_img=img.imread('girl.jpg') # 왼쪽_파일_속성_경로

# 그래프 자체가 배열의 인덱스에 위치
ax1.imshow(ori_img)
print(ori_img.shape) # size 확인

# convolution -> API
# API -> 4차원 (이미지 개수, 세로, 가로, 채널)
# (429, 640, 3) -> (1, 429, 640, 3)로 변경
input_image = ori_img.reshape((1,) + ori_img.shape) # tuple + tiple(수정 불가능 배열)
input_image = input_image.astype(np.float32) # 정수값 -> tf에서 float처리
print(input_image.shape)

ch1_input_image=input_image[:,:,:,0:1] # 채널 수를 1로 변경_데이터 양을 줄여 계산을 간단하게
print(ch1_input_image.shape)

# 입력 데이터를 필터가 순회하며 불필요한 정보를 걸러내고 중요한 특징만 추출해 만든 출력(행렬)
filter = np.array([[[[1]],[[0]],[[1]]],
                   [[[1]],[[0]],[[1]]],
                   [[[1]],[[0]],[[1]]]])

print(filter.shape)

conv2d=tf.nn.conv2d( 
    ch1_input_image,
    filter,
    strides=[1,1,1,1], # 이동하는 간격,filter와 stride 작용으로 특징맵의 크기는 입력 데이터보다 작아짐(손실)
    padding='VALID' # 해결방안:padding 패딩을 고려x, 원래값으로    
)

conv2d_result=conv2d.numpy()
print(conv2d_result.shape)

t_img=conv2d_result[0,:,:,:]
ax2.imshow(t_img,cmap='gray')
plt.show()