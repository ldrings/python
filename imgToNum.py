__author__ = "LandiLiu"

from PIL import ImageEnhance, Image
import pytesseract


def getSecurityCode(path):
    # 原始图像
    image = Image.open (path)
    # image.show()
    # 亮度增强
    enh_bri = ImageEnhance.Brightness (image)
    brightness = 1.5
    image_brightened = enh_bri.enhance (brightness)
    image_brightened.save (path)
    # image_brightened.show()
    # 色度增强
    image = Image.open (path)
    enh_col = ImageEnhance.Color (image)
    color = 1.5
    image_colored = enh_col.enhance (color)
    image_colored.save (path)
    # image_colored.show()
    # 对比度增强
    image = Image.open (path)
    enh_con = ImageEnhance.Contrast (image)
    contrast = 1.5
    image_contrasted = enh_con.enhance (contrast)
    image_contrasted.save (path)
    # image_contrasted.show()
    # 锐度增强
    image = Image.open (path)
    enh_sha = ImageEnhance.Sharpness (image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance (sharpness)
    image_sharped.save (path)

    # 黑白化处理
    image = Image.open (path)
    blacked = image.convert ('L')
    blacked.save (path)
    # blacked.show ()
    text = pytesseract.image_to_string (blacked)
    print (text)
    data = Image.open (path)
    size = data.size

    w = size[0]
    h = size[1]
    buffer = 0
    #进行像素点过滤
    try:
        for i in range (1, w - 1):
            for j in range (1, h - 1):
                if data.getpixel ((i, j - 1)) > 150:
                    buffer += 1
                if data.getpixel ((i, j + 1)) > 150:
                    buffer += 1
                if data.getpixel ((i - 1, j)) > 150:
                    buffer += 1
                if data.getpixel ((i + 1, j)) > 150:
                    buffer += 1
                if data.getpixel ((i - 1, j - 1)) > 150:
                    buffer += 1
                if data.getpixel ((i - 1, j + 1)) > 150:
                    buffer += 1
                if data.getpixel ((i + 1, j - 1)) > 150:
                    buffer += 1
                if data.getpixel ((i + 1, j + 1)) > 150:
                    buffer += 1
                    # print (buffer)
                if buffer > 4:
                    data.putpixel ((i, j), 255)
                buffer = 0
        data.save ('test.png')
        text = pytesseract.image_to_string (data)
        return text.replace(' ','')
    except:return -1