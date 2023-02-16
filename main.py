from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(text, text1,text2,text3,text4,text5,text6,text7,text8, fontname, fontsize, colorText, colorOutline, colorBackground):
    img = Image.open("img.jpg")
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size

    d.text((w//2.5, h//6.3), text, fill=colorText, font=font, align="center")
    d.text((w//4.2, h//4.3), text1, fill=colorText, font=font, align="center")
    d.text((w//5, h//2.8), text2, fill=colorText, font=font, align="center")
    d.text((w//5, h//2.4), text3, fill=colorText, font=font, align="center")
    d.text((w//5, h//2.1), text4, fill=colorText, font=font, align="center")
    d.text((w//5, h//1.9), text5, fill=colorText, font=font, align="center")
    d.text((w//5, h//1.7), text6, fill=colorText, font=font, align="center")
    d.text((w//5, h//1.55), text7, fill=colorText, font=font, align="center")
    d.text((w//13, h//1.2), text8, fill=colorText, font=font, align="center")
    
    img.save("ima.png")

    
print(text_to_image("IslomNur","               vilayoti uchun \n namoz vaqtlari", "Bomdod   ","Quyosh   ","Peshin   ","Asr   ","Shom   ","Xufton    ","Albatta Namoz mo'minlarga vaqtida \n farz qilingandir (Niso surasi. 103-oyat) ", "Ubuntu-Medium.ttf", 30, (251,240,147), "red", "white"))

# def getSize(txt, font):
#     testImg = Image.new('RGB', (1, 1))
#     testDraw = ImageDraw.Draw(testImg)
#     return testDraw.textsize(txt, font)

# if __name__ == '__main__':

#     fontname = "arial.ttf"
#     fontsize = 12  
#     text = "example@gmail.com"
    
#     colorText = "black"
#     colorOutline = "red"
#     colorBackground = "white"


#     font = ImageFont.truetype(fontname, fontsize)
#     width, height = getSize(text, font)
#     img = Image.new('RGB', (width+4, height+4), colorBackground)
#     d = ImageDraw.Draw(img)
#     d.text((2, height/2), text, fill=colorText, font=font)
#     d.rectangle((0, 0, width+3, height+3), outline=colorOutline)
    
#     img.save("D:/image.png")

# print(getSize("Salom Dunyo", "Arial.ttf"))