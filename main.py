from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(text, text1, text2, text3, text4, text5, text6, text7, text8,fontname, fontsize, colorText,):
    img = Image.open("image.png")
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size
    d.text((w/6, h/4.3), text, fill=colorText, font=font)
    d.text((w/3.5, h/3), text1, fill=colorText, font=font)
    d.text((w/1.2, h/3), text2, fill=colorText, font=font)
    d.text((w/3.7, h/2.5), text3, fill=colorText, font=font)
    d.text((w/1.8, h/2.5), text4, fill=colorText, font=font)
    d.text((w/3.7, h/2.2), text5, fill=colorText, font=font)
    d.text((w/1.2, h/2.2), text6, fill=colorText, font=font)
    d.text((w/3.7, h/1.9), text7, fill=colorText, font=font)
    d.text((w/1.2, h/1.9), text8, fill=colorText, font=font)
    
    img.save("image1.png")

    
# print(text_to_image("Ubuntu-Medium.ttf", 30, (251,240,147), "red", "white"))
