# test for image_handler.py
# use pytest

import pytest
import numpy as np
import PIL

from image_handler import *


def test_load_image_PIL():
    image = load_image_PIL("./images/lena.jpg")
    print(type(image))
    assert isinstance(image, PIL.JpegImagePlugin.JpegImageFile)


def test_load_image_PIL_from_directory():
    for image in load_image_PIL_from_directory("./images/"):
        assert isinstance(image, PIL.JpegImagePlugin.JpegImageFile)


def test_load_image_cv2():
    image = load_image_cv2("./images/lena.jpg")
    assert isinstance(image, np.ndarray)


def test_load_image_cv2_from_directory():
    for image in load_image_cv2_from_directory("./images/"):
        assert isinstance(image, np.ndarray)


def test_resize_image_PIL():
    image = load_image_PIL("./images/lena.jpg")
    image = resize_image_PIL(image, (100, 100))
    print(type(image))
    assert isinstance(image, PIL.Image.Image)
    assert image.size == (100, 100)


def test_resize_image_cv2():
    image = load_image_cv2("./images/lena.jpg")
    image = resize_image_cv2(image, (100, 100))
    assert isinstance(image, np.ndarray)
    assert image.shape == (100, 100, 3)
