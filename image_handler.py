# 画像に関するUtility

import glob

import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms


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

def comp_similar_image(image1: np.ndarray, image2: np.ndarray) -> float:
    """画像の類似度を計算する
    類似度の最大値は1.0, 最小値は-1.0

    Args:
        image1 (numpy.ndarray): 画像1
        image2 (numpy.ndarray): 画像2

    Returns:
        float: 類似度
    """
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    image1 = cv2.resize(image1, (64, 64))
    image2 = cv2.resize(image2, (64, 64))
    similar = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)[0][0]
    return similar

def comp_similar_image_from_directory(directory_path = "./images/"):
    """
    ディレクトリ内のすべての画像の類似度を計算する
    
    Args:
        directory_path (str): ディレクトリのパス
    """

    images = []
    for image in load_image_cv2_from_directory(directory_path):
        images.append(image)

    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            similar = comp_similar_image(images[i], images[j])
            print(f"image{i}とimage{j}の類似度: {similar}")

def check_same_image(image1: np.ndarray, image2: np.ndarray) -> bool:
    """画像が同じかどうかを判定する

    Args:
        image1 (numpy.ndarray): 画像1
        image2 (numpy.ndarray): 画像2

    Returns:
        bool: 同じ画像ならTrue, 違う画像ならFalse
    """
    similar = comp_similar_image(image1, image2)
    if similar > 0.99:
        return True
    else:
        return False
    
def check_same_image_from_directory(directory_path = "./images/"):
    """ディレクトリ内すべての画像が同じかどうかを判定する
    手順
    1. ディレクトリ内のすべての画像を順に読み込み，画素値の合計を計算，画像パスをキーとした辞書に格納
    2. リストをもとに，同一画像である可能性のあるペアを列挙
    3. check_same_imageで同一画像かどうかを判定 同一画像であった場合，その画像のパスを表示

    Args:
        directory_path (str, optional): _description_. Defaults to "./images/".
    """
    image_pixel_sum = {}
    for image_path in glob.glob(directory_path + "*"):
        image = load_image_cv2(image_path)
        image_pixel_sum[image_path] = np.sum(image)

    key_list = list(image_pixel_sum.keys())

    for i, key in enumerate(key_list):
        value = image_pixel_sum[key]
        for j in range(i + 1, len(key_list)):
            key2 = key_list[j]
            value2 = image_pixel_sum[key2]
            if value == value2:
                # 画素値の合計が同じ場合
                if check_same_image(load_image_cv2(key), load_image_cv2(key2)):
                    print(f"同一画像: {key}, {key2}")

