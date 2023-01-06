import os
import sys
from PIL import Image
from tkinter import filedialog
from tkinter import Tk

while True:

# 이미지 파일을 선택할 수 있는 GUI 창을 생성
    root = Tk()
    root.withdraw()

# 이미지 파일의 경로를 입력받음, 경로가 없을시 프로그램 종료
    image_path = filedialog.askopenfilename()
    if image_path == '':
        exit()

# 이미지 파일을 열기
    image = Image.open(image_path)

# 이미지의 가로, 세로 길이를 가져옴
    width, height = image.size

# 이미지의 가로, 세로 길이를 2/3로 줄임
    new_width = width * 2 // 3
    new_height = height * 2 // 3

# 이미지를 새로운 가로, 세로 길이로 리사이즈
    resized_image = image.resize((new_width, new_height))

# 새로운 이미지 저장
    resized_image.save(image_path)
