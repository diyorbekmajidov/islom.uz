from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(text, text1, fontname, fontsize, colorText, ):
    img = Image.open("image.jpg")
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size

    
    img.save("image1.png")

    
print(text_to_image("", "Ubuntu-Medium.ttf", 30, (251,240,147),))

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