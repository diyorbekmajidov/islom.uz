from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(text, fontname, fontsize, colorText, colorOutline, colorBackground):
    img = Image.open("unnamed.jpg")
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    d.text((2, 2), text, fill=colorText, font=font)
    img.save("image.png")

    
print(text_to_image("Salom Dunyo", "Ubuntu-Medium.ttf", 12, "black", "red", "white"))

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