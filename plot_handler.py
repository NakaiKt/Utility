# 図のプロットに関するutility郡

import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob

def ablation_4_image(image1: np.ndarray,
                     image2: np.ndarray,
                     image3: np.ndarray,
                     image4: np.ndarray,
                     image1_title: str = "image1",
                     image2_title: str = "image2",
                     image3_title: str = "image3",
                     image4_title: str = "image4",
                     save_dir: str = "./images/", save_name: str = "ablation_4_image.jpg", title: str = "Ablation Study"):
    """4つの画像を比較する
    画像は保存され，タイトルが付けられる

    Args:
        image1 (numpy.ndarray): 左上
        image2 (numpy.ndarray): 右上
        image3 (numpy.ndarray): 左下
        image4 (numpy.ndarray): 右下
        image1_title (str, optional): 左上のタイトル. Defaults to "image1".
        image2_title (str, optional): 右上のタイトル. Defaults to "image2".
        image3_title (str, optional): 左下のタイトル. Defaults to "image3".
        image4_title (str, optional): 右下のタイトル. Defaults to "image4".
        save_dir (str, optional): 保存先のディレクトリ. Defaults to "./images/".
        save_name (str, optional): 保存するファイル名. Defaults to "ablation_4_image.jpg".
        title (str, optional): タイトル. Defaults to "Ablation Study".
    """
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title(image1_title)
    ax1.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax1.imshow(image1)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(image2)
    ax2.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax2.set_title(image2_title)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.imshow(image3)
    ax3.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax3.set_title(image3_title)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.imshow(image4)
    ax4.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax4.set_title(image4_title)

    plt.savefig(save_dir + save_name)
    plt.close()

def ablation_2_image(image1: np.ndarray,
                     image2: np.ndarray,
                     image1_title: str = "image1",
                     image2_title: str = "image2",
                     save_dir: str = "./images/",
                     save_name: str = "ablation_2_image.jpg",
                     title: str = "Ablation Study"):
    """2つの画像を比較する
    画像は保存され，タイトルが付けられる

    Args:
        image1 (numpy.ndarray): 左
        image2 (numpy.ndarray): 右
        image1_title (str, optional): 左のタイトル. Defaults to "image1".
        image2_title (str, optional): 右のタイトル. Defaults to "image2".
        save_dir (str, optional): 保存先のディレクトリ. Defaults to "./images/".
        save_name (str, optional): 保存するファイル名. Defaults to "ablation_2_image.jpg".
        title (str, optional): タイトル. Defaults to "Ablation Study".
    """
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)

    # 目盛りの削除
    plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
    plt.tick_params(bottom=False, left=False, right=False, top=False)

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(image1)
    ax1.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax1.set_title(image1_title)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(image2)
    ax2.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # 目盛り削除
    ax2.set_title(image2_title)

    plt.savefig(save_dir + save_name)
    plt.close()
