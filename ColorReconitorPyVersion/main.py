import cv2
import glob
import numpy as np
from Pretreat import *
from KmeansVision import *

if __name__ == "__main__":
    # test set params
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
    for i in pp.perspectived_imgs:
        cv2.imshow("233", i)
        cv2.waitKey()
    pp.GetSampleRectAvg()
    result = pp.sample_scalars

    mat_for_show = []
    for i in range(6):
        mat_for_show.append(np.ndarray([300, 300, 3], dtype='uint8'))
    for i in range(len(result)):
        # result[i] = cv2.cvtColor(result[i], cv2.COLOR_BGR2HLS_FULL)
        j = i%9
        cv2.rectangle(mat_for_show[i//9], (j%3*100+40, j//3*100+40), (j%3*100+60, j//3*100+60), result[i], 5)
        # print("%f\t%f\t%f"%(b, g, r))
    for i in mat_for_show:
        cv2.imshow("233", i)
        cv2.waitKey()