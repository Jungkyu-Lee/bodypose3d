import cv2

# 카메라 1 및 2에 대한 비디오 캡처 객체 생성
cap1 = cv2.VideoCapture(0)  # 카메라 1의 인덱스 (0은 기본 카메라)
cap2 = cv2.VideoCapture(1)  # 카메라 2의 인덱스 (1은 다음 카메라)

# 비디오 캡처 객체를 열었는지 확인
if not cap1.isOpened() or not cap2.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

frame_id = 0
frames0 = []
frames1 = []
while True:
    # 프레임 읽기
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break  # 두 개의 비디오 스트림 중 하나라도 더 이상 프레임이 없으면 종료


    # 화면에 프레임 표시 (선택적)
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)
    frames0.append(frame1)
    frames1.append(frame2)

    # frame_id += 1




    # # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if len(frames0) > 200:
        break

# 비디오 캡처 및 녹화 객체 해제
cap1.release()
cap2.release()

# 비디오 코덱 및 FPS qq설정
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # mp4 코덱을 사용할 수 있습니다.
fps = 30  # 초당 프레임 수

# 비디오 녹화 객체 생성 (카메라 1)
out1 = cv2.VideoWriter('camera1_output.mp4', fourcc, fps, (1920, 1080))  # 파일명 및 해상도 설정

# 비디오 녹화 객체 생성 (카메라 2)
out2 = cv2.VideoWriter('camera2_output.mp4', fourcc, fps, (1920, 1080))  # 파일명 및 해상도 설정

print(frames0[0].shape)
print(frames0[1].shape)
print(frames1[0].shape)
print(frames1[1].shape)
# 프레임 저장 (카메라 1)
    # print(frame1)
for f in frames0:
    # resized = cv2.resize(crop_img, (new_size[1], new_size[0]))
    out1.write(f)

for f in frames1:
    out2.write(f)

    # 프레임 저장 (카메라 2)

out1.release()
out2.release()



# OpenCV 창 닫기
cv2.destroyAllWindows()
