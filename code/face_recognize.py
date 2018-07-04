#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @GitHub  : J-crow
# @Author  : Aries
# @Date  : 2018/4/24

import cv2
import face_recognition
import numpy as np
from PIL import Image,ImageDraw


video_capture = cv2.VideoCapture(0)  # 打开摄像头
# 加载已知图片
Tatum_image = face_recognition.load_image_file(
    "D:/GAMES/py3.6.3/face_id/known/jt.jpg")  # 人脸位置加载函数 返回一个人脸图像（人脸位置的上下左右）的列表，第一个参数是图像，第二个参数是多少倍的上采样图像寻找面孔，数字越大，寻找较小的面孔，第三个参数是人脸检测模型，默认是hog
Tatum_face_encoding = face_recognition.face_encodings(Tatum_image)[0]  # 人脸数据化，返回一个128个向量的列表（用于对比），0为图像里面第一个人的索引

me_image = face_recognition.load_image_file("D:/GAMES/py3.6.3/face_id/known/text1.jpg")
me_face_encoding = face_recognition.face_encodings(me_image)[0]

Leonard_image = face_recognition.load_image_file("D:/GAMES/py3.6.3/face_id/known/kl.jpg")
Leonard_face_encoding = face_recognition.face_encodings(Leonard_image)[0]
# 创建一个人脸编码/已知人脸名字的list
known_face_encodings = [
    Tatum_face_encoding,
    me_face_encoding,
    Leonard_face_encoding
]
known_face_names = [
    "Jayson Tatum",
    "crow",
    "Kawhi Leonard"
]

face_locations = []
face_encodings = []
face_names = []
t = True

while True:

    ret, frame = video_capture.read()  # 创建一个1帧的视频框架   返回两个参数，ret是true/false代表有没有读到图片，frame是截取当前一帧的图片

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 将视频的大小调整为1/4大小以获得更快的人脸识别处理  显示出来的还是原来的1帧视频

    # 将图像从BGR颜色（OpenCV使用）转换为RGB颜色（人脸识别使用）
    rgb_small_frame = small_frame[:, :, ::-1]

    # 每隔一帧处理一次的视频来节省时间
    if t:
        # 加载视频中的人脸
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings,face_encoding,tolerance=0.4)  # 人脸对比函数  对比那128个向量  返回一个True/False的列表，第一个参数为已知的编码过的人脸列表，第二个是未知的编码过的人脸，第三个tolerance=0.6人脸对比的严格度，越低越严格
            name = "Unknown"

            # 如果在已知的编码中找到了匹配，就使用第一个
            if True in matches:
                first_match_index = matches.index(True)  # 检测字符串中是否包含子字符串True  返回值为子字符串的位置（从0开始算）
                name = known_face_names[first_match_index]

            face_names.append(name)

    t = not t

    for (top, right, bottom, left), name in zip(face_locations,
                                                face_names):  # zip可作为迭代的参数  对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表，返回列表长度与最短的对象相同  上下左右迭代成locations，encoding迭代成encodings
        # 放大4倍 还原成像
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4


        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),2)  # 画出人脸矩形框    第一个参数是图片 第二个（left, top）是矩阵的左上点坐标  第三个（right, bottom）是矩阵的右下点坐标  第三个是画线对应的bgr颜色  第四个是所画的线的宽度

        # 在人脸框下面"画"出名字
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)  #各参数依次是：照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细

    cv2.imshow('Video', frame)  # 展示视频

    # 输入q跳出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):  # cv2.waitKey是键盘绑定函数
        break

video_capture.release()  # 释放视频流
cv2.destroyAllWindows()  # 关闭所有窗口