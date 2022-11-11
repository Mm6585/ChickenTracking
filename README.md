# 창의설계 경진대회 - ChickenTracking


#### 바쁜 농부를 대신하여 닭의 행동을 관찰할 수 있는 AI 카메라를 만들어라!
> 게이츠재단은 10만 마리의 닭을 아프리가 빈곤층에 나누어주는 사업을 하고있다.
> 재단의 연구에 따르면 닭 약 40마리를 지속적으로 키우면 일년에 $1000을 벌 수 있어서 서아프리카의 빈곤선( $700/year )을 넘길 수 있다.
> 그러나 가난한 농가에서는 판매를 위한 닭의 품질을 일정하게 유지하게 힘들다.
> 이를 돕기위해 닭의 행동량을 자동으로 계산해주는 시스템을 개발하고자 한다.


## ChickTrack


### AI

라즈베리파이를 사용해 카메라 모듈 또는 다른 카메라를 사용하여 영상을 획득하고 라즈베리파이 내부에서 객체 추적 프로그램을 구동합니다.Detector는 실시간 객체 추적에 용이한 [yolov5](https://github.com/search?q=yolo)를 사용합니다

> Tracker는  occlusion과 ID switching 에 유리한 StrongSORT를 사용합니다  
> TrainDataset : [Animals Detection Images Dataset by ANTOREEPJANA](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset) , [Chicken Detection > and Tracking Image Dataset](https://universe.roboflow.com/chickens/chicken-detection-and-tracking/dataset/12)





```
$ python3 track.py --source [source_path] --user-id [user-id]
                              0  # webcam
                              img.jpg  # image
                              vid.mp4  # video
                              path/  # directory
                              path/*.jpg  # glob
                              'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                              'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

### Algorithm

![image](https://user-images.githubusercontent.com/71868697/200842821-ea4599cd-1f3d-46f1-a357-cc2039c1991f.png)

### IOS
Xcode 13.2.1  환경에서 구축하였으며 추가적으로 [iosDeviceSupport](https://github.com/filsv/iOSDeviceSupport)에서 버전에 맞는 ios version을 추가해 구동하였습니다

> package
> [SwiftUIChart](https://github.com/AppPear/ChartView)
> [SwiftUIFontIcon](https://github.com/huybuidac/SwiftUIFontIcon)

<img width="40%" alt="2" src="https://user-images.githubusercontent.com/71868697/200848386-9900b88a-6b6d-45b3-a825-1249f8215542.png"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img width="40%" alt="1" src="https://user-images.githubusercontent.com/71868697/200848538-16333fc5-372b-4028-9835-a06f937fa8fa.png">


### Vue


### Pushbullet
안드로이드 사용자에게 푸시 알림을 보내기 위해 Pushbullet을 사용합니다.</br>
![image](https://user-images.githubusercontent.com/101806955/201338457-fb5f9f96-f576-48f7-b993-27acf8c52f88.png)
알림을 전송하기 위해서는 DB에 유저 정보를 추가해야 하고,</br>
이를 위해서 수동으로 서비스 계정에 pushbullet 메시지를 보내야 합니다.</br>
pushbullet_python의 main.py가 자동응답 봇의 역할을 수행합니다.</br>
![image](https://user-images.githubusercontent.com/101806955/201338365-83d5938f-36e6-4452-b08c-4e8cccf973e1.png)
