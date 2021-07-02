import ffmpeg
import numpy as np
import cv2
import os


def main():
    directory = os.getcwd()
    print(os.getcwd())
    os.chdir('C:\\Users\\TSP\\Desktop\\base_picture\\')

    video_stream = ffmpeg.input('results\\test.mp4')
    audio_stream = ffmpeg.input('test.wav')

    ffmpeg.output(audio_stream, video_stream, 'result_video.avi').run()




