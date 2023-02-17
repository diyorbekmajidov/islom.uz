from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(city,text, text1,text2,text3,text4,text5, fontname, fontsize, colorText):
    img = Image.open("ima.png")
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size
    d.text((w//4.2, h//4.3), city, fill=colorText, font=font, align="center")
    d.text((w//2, h//2.8), text, fill=colorText, font=font, align="center")
    d.text((w//2, h//2.4), text1, fill=colorText, font=font, align="center")
    d.text((w//2, h//2.1), text2, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.9), text3, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.7), text4, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.55), text5, fill=colorText, font=font, align="center")
    
    img.save("ima1.png")

    

# from PIL import Image, ImageDraw, ImageFont

# # TEXT TO IMAGE and pillow
# def text_to_image(text, text1,text2,text3,text4,text5,text6,text7,text8, fontname, fontsize, colorText, colorOutline, colorBackground):
#     img = Image.open("img.jpg")
#     w, h = img.size
#     d = ImageDraw.Draw(img)
#     font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size

    # d.text((w//2.5, h//6.3), text, fill=colorText, font=font, align="center")
#     d.text((w//4, h//4.3), text1, fill=colorText, font=font, align="center")
#     d.text((w//4, h//2.8), text2, fill=colorText, font=font, align="center")
#     d.text((w//4, h//2.4), text3, fill=colorText, font=font, align="center")
#     d.text((w//4, h//2.1), text4, fill=colorText, font=font, align="center")
#     d.text((w//4, h//1.9), text5, fill=colorText, font=font, align="center")
#     d.text((w//4, h//1.7), text6, fill=colorText, font=font, align="center")
#     d.text((w//4, h//1.55), text7, fill=colorText, font=font, align="center")
#     d.text((w//13, h//1.2), text8, fill=colorText, font=font, align="center")
    
#     img.save("ima.png")

    
# print(text_to_image("IslomNur","          vilayoti uchun \n namoz vaqtlari", "Bomdod   ","Quyosh   ","Peshin   ","Asr   ","Shom   ","Xufton    ","Albatta Namoz mo'minlarga vaqtida \n farz qilingandir (Niso surasi. 103-oyat) ", "Ubuntu-Medium.ttf", 30, (251,240,147), "red", "white"))

