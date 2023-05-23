from PIL import Image, ImageDraw, ImageFont

# TEXT TO IMAGE and pillow
def text_to_image(city,text, text1,text2,text3,text4,text5, fontname, fontsize, colorText):
    img = Image.open("ima.png")
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontname ,fontsize)
    # image draw text size

    image_width, image_height = img.size
    text_width, text_height = d.textsize(city, font)
    image_width, image_height = img.size
    x = (image_width - text_width) // 2
    y = (image_height - text_height) //4
    
    d.text((x,y), city, fill=colorText, font=font, align="center")
    d.text((w//2, h//2.35), text, fill=colorText, font=font, align="center")
    d.text((w//2, h//2.05), text1, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.8), text2, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.62), text3, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.48), text4, fill=colorText, font=font, align="center")
    d.text((w//2, h//1.35), text5, fill=colorText, font=font, align="center")
    
    img.save("ima1.png")


