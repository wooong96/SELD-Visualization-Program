import numpy as np
import csv
import math
from PIL import Image, ImageFont, ImageDraw
import cv2


import play

path = 'C:\\Users\\TSP\\Desktop\\base_picture'
square_base = (700, 40)
square_base_2 = (700, 80)

rgb = (0,0,0)
f = open(path+'\\new_metadata_training.csv', 'r')
rdr = csv.reader(f)
font_elevation = ImageFont.truetype(path+"\\강한육군 Bold.ttf",15)
font=cv2.FONT_HERSHEY_SIMPLEX
size =0.4
count = 0

#클래스 분류
sound = ['alarm','baby','crash','dog','engine','female_scream','female_speech','fire','footsteps','knock','male_scream','male_speech','phone','piano']


r = 400
index_num0 = []
index_num1 = []
index_num3 = []
index_num4 = []
index_num5 = []
for item in rdr:
    index_num0.append(int(item[0]))
    index_num1.append(int(item[1]))
    index_num3.append(float(item[3]))
    index_num4.append(float(item[4]))
    index_num5.append(float(item[5]))
for index in range(1,601):
    if(count == len(index_num0) -1):
        count = len(index_num0) -2

    if(index != index_num0[count]):
        print(index)


        im = Image.open(path + '\\base.png')
        im = im.resize((1024, 1024))
        draw = ImageDraw.Draw(im)
        draw.text(square_base, 'x: 0.000 y: 0.000 z: 0.000', 'black', font_elevation)
        im.save(path + "\\results\\" + "{}".format(index + 1000) + ".png")

    elif(index == index_num0[count] and index_num0[count+1] == index_num0[count]):
        print(index)

        im = Image.open(path+'\\base.png')
        im = im.resize((1024, 1024))
        im2 = Image.open(path+'\\' + sound[index_num1[count]] + '.png')
        im2 = im2.resize((100, 100))
        im3 = Image.open(path+'\\' + sound[index_num1[count+1]] + '.png')
        im3 = im3.resize((100, 100))
        x = 0
        y = 0
        angle = np.arctan2(index_num4[count], index_num3[count]) * 180 / np.pi
        angle1 = np.arctan2(index_num4[count+1], index_num3[count+1]) * 180 / np.pi
        elevation = np.arctan2(index_num5[count],
                               np.sqrt(index_num3[count] ** 2 + index_num4[count] ** 2)) * 180 / np.pi
        elevation2 = np.arctan2(index_num5[count + 1],
                                np.sqrt(index_num3[count + 1] ** 2 + index_num4[count + 1] ** 2)) * 180 / np.pi


        Draw = ImageDraw.Draw(im2)
        Draw.text((0,0),' 고도: '+str(int(elevation))+"°",'black',font_elevation)
        Draw = ImageDraw.Draw(im3)
        Draw.text((0, 0),' 고도: ' + str(int(elevation2))+"°", 'black', font_elevation)
        Draw = ImageDraw.Draw(im)
        Draw.text(square_base,  "x: "+str(round(index_num3[count],3))+" y: "+str(round(index_num4[count],3))+" z: "+str(round(index_num5[count],3)) , 'black', font_elevation)
        Draw.text(square_base_2,  "x: "+str(round(index_num3[count+1],3))+" y: "+str(round(index_num4[count+1],3))+" z: "+str(round(index_num5[count+1],3)) , 'black', font_elevation)
        print(str(index) + str(angle))

        for i in range(2):
            if(i == 1):
                angle = angle1
                im2 = im3
            if (angle < 0):
                angle = -1 * angle
                if angle < 90:
                    x = im.size[0] / 2 + r * math.sin(angle * (math.pi) / 180)

                    y = im.size[0] / 2 - r * math.cos(angle * (math.pi) / 180)

                else:
                    x = im.size[0] / 2 + r * math.sin((180 - angle) * (math.pi) / 180)

                    y = im.size[0] / 2 + r * math.cos((180 - angle) * (math.pi) / 180)

            else:

                if angle < 90:
                    x = im.size[0] / 2 - r * math.sin(angle * (math.pi) / 180)

                    y = im.size[0] / 2 - r * math.cos(angle * (math.pi) / 180)

                else:
                    x = im.size[0] / 2 - r * math.sin((180 - angle) * (math.pi) / 180)

                    y = im.size[0] / 2 + r * math.cos((180 - angle) * (math.pi) / 180)

            im.paste(im2, (int(x)-50, int(y)-50))

        im.save(path+"\\results\\" + "{}".format(index + 1000) + ".png")
        count+= 2
    else:
        print(index)
        im = Image.open(path + '\\base.png')
        im = im.resize((1024, 1024))
        im2 = Image.open(path + '\\' + sound[index_num1[count]] + '.png')
        im2 = im2.resize((100, 100))

        elevation = np.arctan2(index_num5[count],np.sqrt(index_num3[count] ** 2 + index_num4[count] ** 2)) * 180 / np.pi

        draw = ImageDraw.Draw(im2)
        draw.text((0, 0), ' 고도: ' + str(int(elevation))+"°", 'black', font_elevation)
        draw = ImageDraw.Draw(im)
        draw.text(square_base,
                  "x: " + str(round(index_num3[count], 3)) + " y: " + str(round(index_num4[count], 3)) + " z: " + str(
                      round(index_num5[count], 3)) , 'black', font_elevation)

        x = 0
        y = 0
        angle = np.arctan2(index_num4[count], index_num3[count]) * 180 / np.pi
        print(str(index)+str(angle))
        if (angle < 0):
            angle = -1 * angle

            if angle < 90.0:
                x = im.size[0] / 2 + r * math.sin(angle * (math.pi) / 180)

                y = im.size[0] / 2 - r * math.cos(angle * (math.pi) / 180)

            else:
                x = im.size[0] / 2 + r * math.sin((180 - angle) * (math.pi) / 180)

                y = im.size[0] / 2 + r * math.cos((180 - angle) * (math.pi) / 180)

        else:

            if angle < 90:
                x = im.size[0] / 2 - r * math.sin(angle * (math.pi) / 180)

                y = im.size[0] / 2 - r * math.cos(angle * (math.pi) / 180)

            else:
                x = im.size[0] / 2 - r * math.sin((180 - angle) * (math.pi) / 180)

                y = im.size[0] / 2 + r * math.cos((180 - angle) * (math.pi) / 180)

        im.paste(im2, (int(x)-50, int(y)-50))
        im.save(path+"\\results\\" + "{}".format(index + 1000) + ".png")
        count += 1



play.main()