# test for image_handler.py
# use pytest

import pytest
import numpy as np
import PIL

from image_handler import *


def test_load_image_PIL():
    image = load_image_PIL("./test/images/lena.jpg")
    assert isinstance(image, PIL.Image.Image)


def test_load_image_PIL_from_directory():
    for image in load_image_PIL_from_directory("./test/images/"):
        assert isinstance(image, PIL.Image.Image)


def test_load_image_cv2():
    image = load_image_cv2("./test/images/lena.jpg")
    assert isinstance(image, np.ndarray)


def test_load_image_cv2_from_directory():
    for image in load_image_cv2_from_directory("./test/images/"):
        assert isinstance(image, np.ndarray)


def test_resize_image_PIL():
    image = load_image_PIL("./test/images/lena.jpg")
    image = resize_image_PIL(image, (100, 100))
    assert isinstance(image, np.ndarray)
    assert image.shape == (100, 100, 3)


def test_resize_image_cv2():
    image = load_image_cv2("./test/images/lena.jpg")
    image = resize_image_cv2(image, (100, 100))
    assert isinstance(image, np.ndarray)
    assert image.shape == (100, 100, 3)


def test_normalize_image_cv2():
    image = load_image_cv2("./test/images/lena.jpg")
    image = normalize_image_cv2(image)
    assert isinstance(image, torch.Tensor)


def test_normalize_image_PIL():
    image = load_image_PIL("./test/images/lena.jpg")
    image = resize_image_PIL(image=image, size=(224, 224))
    image = normalize_image_PIL(image)
    assert isinstance(image, torch.Tensor)

def test_comp_similar_image():
    # ./imagesのlena, lena_2, nekoを読み込み
    lena_image = load_image_cv2("./test/images/lena.jpg")
    lena_2_image = load_image_cv2("./test/images/lena_2.jpg")
    neko_image = load_image_cv2("./test/images/neko.jpg")

    # 類似度を計算
    lena_lena_2_similar = comp_similar_image(lena_image, lena_2_image)
    lena_neko_similar = comp_similar_image(lena_image, neko_image)
    lena_2_neko_similar = comp_similar_image(lena_2_image, neko_image)

    assert lena_lena_2_similar > 0.99
    assert lena_neko_similar < 0.9
    assert lena_neko_similar == lena_2_neko_similar

def test_comp_similar_image_from_directory():
    directory_path = "./test/images/"

    comp_similar_image_from_directory(directory_path)

def test_check_similar_image_from_directory():
    # ./imagesのlena, lena_2, nekoを読み込み
    lena_image = load_image_cv2("./test/images/lena.jpg")
    lena_2_image = load_image_cv2("./test/images/lena_2.jpg")
    neko_image = load_image_cv2("./test/images/neko.jpg")

    assert check_same_image(lena_image, lena_2_image) == True
    assert check_same_image(lena_image, neko_image) == False
    assert check_same_image(lena_2_image, neko_image) == False

def test_check_same_image_from_directory():
    directory_path = "./test/images/"

    check_same_image_from_directory(directory_path)
