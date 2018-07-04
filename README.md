# Python-face_recognition
运用Python中的face_recognition和OpenCV实现最简单的动态人脸识别
*****

本文的程序是模仿学习国外的大神的[face_recognition](https://github.com/ageitgey/face_recognition)

Windows8.1 64位 Python版本`python3.6.3`<br>


首先安装好OpenCV和face_recognition  `pip install face_recognition`,`pip install opencv_python`<br>
安装这两个库之前要先安装对应版本的其他一些库，本文不在累赘叙述，安装的过程还是比较麻烦的。<br>
但是本人并没有像大多数网上的方法那样，编译Boost，然后在编译dlib，而是对应安装了相应版本的库，然后成功的安装face_recognition。<br>
推荐一个比较稳的方法：`上官网或是开源的镜像网站下载对应Windows和Python版本的face_recognition`，然后pip安装`whl`文件。<br>
***

本文并没有使用OpenCV人脸检测的xml，通过对比face_recognition的xml，只能吐槽OpenCV的训练力度不够啊，face_recognition的是真的不错。几乎就没有错误的识别。<br>

下图是OpenCV的xml检测的结果![](https://github.com/J-crow/Python-face_recognition/blob/master/image/me.jpg)<br>

下图是face_recognition的xml检测的结果（已经进行了静态的人脸识别）![](https://github.com/J-crow/Python-face_recognition/blob/master/image/mayun.jpg)<br>



首先将已知的人脸的图片存入文件夹，然后通过face_recognition指向那个文件夹，生成相应的已知人脸的model<br>
```python
Tatum_image = face_recognition.load_image_file("D:/GAMES/py3.6.3/face_id/known/jt.jpg") 
# 人脸位置加载函数 返回一个人脸图像（人脸位置的上下左右）的列表，第一个参数是图像，第二个参数是多少倍的上采样图像寻找面孔，数字越大，寻找较小的面孔，第三个参数是人脸检测模型，默认是hog
Tatum_face_encoding = face_recognition.face_encodings(Tatum_image)[0] 
# 人脸数据化，返回一个128个向量的列表（用于对比），0为图像里面第一个人的索引
```
<br>



通过OpenCV打开电脑的摄像头<br>
```python
video_capture = cv2.VideoCapture(0)  # 打开摄像头
```
然后进行实时检测，其中face_recognition中人脸对比函数
```python
face_recognition.compare_faces(known_face_encodings,face_encoding,tolerance=0.4)
```
中的`tolerance`的阈值设为0.4检测效果会更优，此阈值越低越严格。<br>

人脸识别结果如下<br>
![](https://github.com/J-crow/Python-face_recognition/blob/master/image/face1.gif)
