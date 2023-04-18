# test for plot_handler.py
# use pytest

import pytest
import numpy as np
import os

from plot_handler import *
from image_handler import load_image_cv2_from_directory

def test_init():
    # ablation_4_image.jpg, ablation_2_image.jpgを削除する
    if os.path.exists("./test/images/ablation_4_image.jpg"):
        os.remove("./test/images/ablation_4_image.jpg")
    if os.path.exists("./test/images/ablation_2_image.jpg"):
        os.remove("./test/images/ablation_2_image.jpg")

def test_ablation_4_image():
    # ./images/の画像を読み込んで，4つの画像を比較する
    image1 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()
    image2 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()
    image3 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()
    image4 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()

    # 画像はBGRなので，RGBに変換する
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
    image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2RGB)

    ablation_4_image(image1, image2, image3, image4, save_dir = "./test/images/", save_name = "ablation_4_image.jpg", title = "Ablation Study")

def test_ablation_2_image():
    # ./images/の画像を読み込んで，2つの画像を比較する
    image1 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()
    image2 = load_image_cv2_from_directory(directory_path = "./test/images/").__next__()

    # 画像はBGRなので，RGBに変換する
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    ablation_2_image(image1, image2, save_dir = "./test/images/", save_name = "ablation_2_image.jpg", title = "Ablation Study")