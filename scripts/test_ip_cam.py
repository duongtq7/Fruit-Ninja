import ffmpegcv
import cv2
import os
CAP_WIDTH, CAP_HEIGHT = 1280, 720 # size of video capture

stream_url = "rtsp://admin:admin123@192.168.1.125:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"
cap = cv2.VideoCapture(stream_url, cv2.CAP_FFMPEG)
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"]="hwaccel;cuvid|video_codec;h264_cuvid|vsync;0"
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"]="video_codec;h264_cuvid"
# stream_url = 'http://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/gear2/prog_index.m3u8'
# cap  = ffmpegcv.VideoCaptureStream(stream_url, resize=(CAP_WIDTH, CAP_HEIGHT), resize_keepratio=True)
# vidout = ffmpegcv.VideoWriterNV(vfile_out, 'h264', vidin.fps)
# cap = cv2.VideoCapture(stream_url, cv2.CAP_FFMPEG)
# cap = cv2.VideoCapture(stream_url, cv2.CAP_FFMPEG, [cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY ]);
# cap = cv2.cudacodec.createVideoReader(stream_url)
# cap.get(cv2.CAP_PROP_BUFFERSIZE)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT)
# cap = ffmpegcv.VideoCaptureStream(stream_url)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        pass
    if not ret:
        break
    pass