import os
import cv2
import numpy as np
import random

PATH = '../data/train_dataset_train/videos'
EFFECT = '../data/noise'


def random_img(path):
    l = os.listdir(path)
    ll = l[random.randint(0, len(l) - 1)]
    print(ll)
    return cv2.imread('{}/{}'.format(path, ll), cv2.IMREAD_UNCHANGED)



for folder in os.listdir(PATH):
    for file in os.listdir('{}/{}'.format(PATH, folder)):
        video_file_path = '{}/{}/{}'.format(PATH, folder, file)
        print(video_file_path)
        video = cv2.VideoCapture(video_file_path)

        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frame_count)
        frame_rate = int(video.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        video_out = cv2.VideoWriter(video_file_path.replace('.avi', '.mp4'),
                                    codec,
                                    frame_rate, (256, 256))

        for i in range(frame_count):
            video.set(1, i)
            _, frame = video.read()
            if frame is None:
                continue

            frame = cv2.resize(frame, (256, 256))

            noise = random_img(EFFECT)
            noise = cv2.resize(noise, (256, 256))
            frame = cv2.addWeighted(noise[:,:,:3], 0.5, frame, 0.5, 0)

            video_out.write(frame)

        video.release()
        video_out.release()
