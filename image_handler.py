# 画像に関するUtility

import glob

import cv2
import numpy as np
from PIL import Image

from torchvision import transforms
import torch


def load_image_PIL(image_path: str) -> Image:
    """PILを使って画像を読み込む

    Args:
        image_path (str): 画像のパス

    Returns:
        PIL.Image: 画像
    """
    image = Image.open(image_path).convert("RGB")
    return image

def load_image_cv2(image_path: str) -> np.ndarray:
    """cv2を使って画像を読み込む

    Args:
        image_path (str): 画像のパス

    Returns:
        numpy.ndarray: 画像
    """
    image = cv2.imread(image_path)
    return image

def resize_image_PIL(image: Image, size: tuple) -> Image:
    """PILを使って画像をリサイズする

    Args:
        image (PIL.Image): 画像
        size (tuple): リサイズ後のサイズ

    Returns:
        PIL.Image: リサイズ後の画像
    """
    image = cv2.resize(np.array(image), size, interpolation=cv2.INTER_CUBIC)
    return image

def resize_image_cv2(image: np.ndarray, size: tuple, interpolation = "INTER_CUBIC") -> np.ndarray:
    """cv2を使って画像をリサイズする

    Args:
        image (numpy.ndarray): 画像
        size (tuple): リサイズ後のサイズ
        interpolation (str, optional): リサイズ時の補間方法. Defaults to "INTER_CUBIC".

    Returns:
        numpy.ndarray: リサイズ後の画像
    """
    if interpolation == "INTER_NEAREST":
        image = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
    elif interpolation == "INTER_AREA":
        image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
    else:
        image = cv2.resize(image, size)
    return image

def normalize_image_PIL(image: np.ndarray) -> torch.Tensor:
    """pytorchのnormalizeを使って画像を正規化する

    Args:
        image (numpy.ndarray): 画像

    Returns:
        numpy.ndarray: 正規化後の画像
    """
    trans = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    image = trans(Image.fromarray(image))[None, :]
    return image

def normalize_image_cv2(image: np.ndarray) -> torch.Tensor:
    """pytorchのnormalizeを使って画像を正規化する

    Args:
        image (numpy.ndarray): 画像

    Returns:
        numpy.ndarray: 正規化後の画像
    """
    trans = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    image = trans(image)        

    return image


def load_image_PIL_from_directory(directory_path = "./images/") -> Image:
    """
    ディレクトリ内の画像を順に読み込みyieldで返す

    使用例:
        for image in load_image_PIL_from_directory(directory_path = "./images/"):
    
    Args:
        directory_path (str): ディレクトリのパス

    Yields:
        PIL.Image: 画像
    """
    for image_path in glob.glob(directory_path + "*"):
        image = load_image_PIL(image_path)
        yield image

def load_image_cv2_from_directory(directory_path = "./images/") -> np.ndarray:
    """
    ディレクトリ内の画像を順に読み込みyieldで返す

    使用例:
        for image in load_image_cv2_from_directory(directory_path = "./images/"):
    
    Args:
        directory_path (str): ディレクトリのパス

    Yields:
        numpy.ndarray: 画像
    """
    for image_path in glob.glob(directory_path + "*"):
        image = load_image_cv2(image_path)
        yield image