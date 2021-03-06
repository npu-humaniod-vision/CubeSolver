from Pretreat import *

import cv2
import numpy as np
import glob
from sklearn.cluster import KMeans

class Img2Status:
    def __init__(self, scalars):
        self.scalars = scalars 
        return 
    def Cluster(self):
        kmeans_cluster = KMeans(n_clusters=6, n_init=100, tol=0.0001)
        kmeans_cluster.fit(self.scalars)
        self.labels = kmeans_cluster.labels_
        return
    def ToStatus(self):
        label2str = {}
        faces = ['U', 'R', 'F', 'D', 'L', 'B']
        for i in range(6):
            label2str[self.labels[i*9+4]] = faces[i]
            print(self.labels[i*9+4], faces[i])

        status = [label2str[i] for i in self.labels]
        # status[-7] = 'B'
        print("".join(status))
        # for i in self.labels:

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("../BackupSource/pretreat_config.ini")

    pic_path = "../BackupSource/*.jpg"
    pic_paths = [i for i in glob.glob(pic_path)]
    pics = []
    for i in pic_paths:
        img = cv2.imread(i)
        print(i)

        pics.append(img)

        cv2.imshow("233", img)
        cv2.waitKey(0)
    pp = Pretreat(pics, config)
    pp.DoPreproc()
    pp.CutImage()
    pp.GetSampleRectAvg()
    result = pp.sample_scalars

    ya = Img2Status(result)
    ya.Cluster()
    labels = ya.labels
    for i in range(6):
        for j in range(9):
            print(labels[i*9+j], end=" ")
        print()
    ya.ToStatus()
