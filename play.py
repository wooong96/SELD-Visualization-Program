import ffmpeg
import os
import cv2
from PIL import Image
import combine_video


def generate_video():
    image_folder = '.'
    video_name = 'test.mp4'
    os.chdir("C:\\Users\\TSP\\Desktop\\base_picture\\results")

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # 프레임 높이와 너비를 설정
    # 첫번째 사진의 높이와 너비
    height, width, layers = frame.shape
    fourcc = 0x7634706d
    video = cv2.VideoWriter(video_name, fourcc, 10, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))


    cv2.destroyAllWindows()
    video.release()  # 비디오 생성
    directory = os.getcwd()
    print(os.getcwd())
    os.chdir('C:\\Users\\TSP\\Desktop\\base_picture\\')

    video_stream = ffmpeg.input('results\\test.mp4')
    audio_stream = ffmpeg.input('test.wav')

    ffmpeg.output(audio_stream, video_stream, 'result_video.avi').run()

def main():
    os.chdir("C:\\Users\\TSP\\Desktop\\base_picture\\results")
    path = "C:\\Users\\TSP\\Desktop\\base_picture\\results"

    mean_height = 0
    mean_width = 0

    num_of_images = len(os.listdir('.'))


    for file in os.listdir('.'):
        im = Image.open(os.path.join(path, file))
        width, height = im.size
        mean_width += width
        mean_height += height

    mean_width = int(mean_width / num_of_images)
    mean_height = int(mean_height / num_of_images)

    for file in os.listdir('.'):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            # PIL을 사용하여 이미지를 open
            im = Image.open(os.path.join(path, file))

            # im.size는 이미지의 높이와 너비를 가지고 있음
            width, height = im.size
            print(width, height)

            # resizing
            imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
            imResize.save(file, 'PNG', quality=95)  # setting quality
            # resize된 각각의 이미지들을 print
            print(im.filename.split('\\')[-1], " is resized")

        # 비디오 생성함수

    # 비디오 생성함수 호출 및 음성 combine
    generate_video()
    combine_video.main()
