import cv2
import numpy as np


def psnr(img1, img2):
    # 将图像转换为浮点数类型
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)

    # 计算图像的均方误差
    mse = np.mean((img1 - img2) ** 2)

    # 如果均方误差为 0，则返回无穷大
    if mse == 0:
        return float('inf')

    # 计算 PSNR
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))

    return psnr_value


# 读取两张彩色图片
img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

# 调用psnr函数计算PSNR值
psnr_value = psnr(img1, img2)
print("PSNR值:", psnr_value)
