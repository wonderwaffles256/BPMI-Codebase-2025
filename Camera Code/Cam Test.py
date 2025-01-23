from picamera2 import Picamera2, Preview

cam0 = Picamera2(0)
cam1 = Picamera2(1)

cam0.start_preview(Preview.QTGL)
cam1.start_preview(Preview.QTGL)

cam0.start()
cam1.start()
