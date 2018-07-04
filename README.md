# Python-face_recognition
运用Python中的face_recognition和OpenCV实现最简单的动态人脸识别
*****

本文的程序是模仿学习国外的大神的[face_recognition](https://github.com/ageitgey/face_recognition)

Windows8.1 64位 Python版本`python3.6.3`<br>
首先安装好OpenCV和face_recognition  `pip install face_recognition`,`pip install opencv_python`<br>
安装这两个库之前要先安装对应版本的其他一些库，本文不在累赘叙述，安装的过程还是比较麻烦的。<br>
但是本人并没有像大多数网上的方法那样，编译Boost，然后在编译dlib，而是对应安装了相应版本的库，然后成功的安装face_recognition。<br>
推荐一个比较稳的方法：`上官网或是开源的镜像网站下载对应Windows和Python版本的face_recognition`，然后pip安装`whl`文件。<br>


本文并没有使用OpenCV人脸检测的xml，通过对比face_recognition的xml，只能吐槽OpenCV的训练力度不够啊，face_recognition的是真的不错。几乎就没有错误的识别。<br>
OpenCV的xml检测的结果![](https://github.com/J-crow/Python-face_recognition/blob/master/image/me.jpg)<br>
face_recognition的xml检测的结果（已经进行了静态的人脸识别）![](https://github.com/J-crow/Python-face_recognition/blob/master/image/mayun.jpg)<br>
