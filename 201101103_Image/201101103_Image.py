##################################
# Name - Vikramaditya Kokil
# ID   - 201101103
##################################
try:
 import sys
 import os
except:print ''' OS lib not found'''
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

ALPHA=0.5
id = "ID - 201101103"
ft = ImageFont.load_default()
im1=Image.open("pic1.jpg");#
im2=Image.open("back.jpg");#

def finishing(im,name,alpha):
	draw = ImageDraw.Draw(im)
	(width, height) = im.size
	draw.line((0,10,width,10),fill = (0,0,255))
	draw.line((0,40,width,40),fill = (0,0,255))
	wh = ft.getsize(id)
	draw.text((width/2-wh[0]/2,15), id, fill=(255, 0, 0), font=ft)
	draw.line((0,height-10,width,height-10),fill = (0,0,255))
	draw.line((0,height-40,width,height-40),fill = (0,0,255))
	description = name+" , Alpha = "+str(alpha)
	wh = ft.getsize(description)
	draw.text((width/2 - wh[0]/2, height - 30),description, fill=(255, 0, 0), font=ft)
	del draw  
	im = im.resize((1920, 1080), Image.ANTIALIAS)
	im.save(name+".jpg",'JPEG')


im=Image.blend(im1,im2,ALPHA)
im2=Image.blend(im1,im2,ALPHA)
im3=Image.blend(im1,im2,ALPHA)

#Original Blending of two Images with Watermark
finishing(im2,'Original Blending',ALPHA)

#Rank Filter
Imrank = im.filter(ImageFilter.RankFilter(7,1))
finishing(Imrank,'Rank Blending, Rank = 1 Size = 3',ALPHA)

#Color Blending
r, g, b = im3.split()
ImColor = Image.merge("RGB", (r,r,g))
finishing(ImColor,'Color Blending',ALPHA)

#Unsharp Mask
ImMask = im.filter(ImageFilter.UnsharpMask(radius=2))
finishing(ImMask,'UnsharpMask Filtered',ALPHA)

#Min filter
ImMin = im.filter(ImageFilter.MinFilter)
finishing(ImMin,'MinFilter Blending',ALPHA)

#Max filter
ImMax = im.filter(ImageFilter.MaxFilter)
finishing(ImMax,'MaxFilter Blending',ALPHA)

#Median filter
ImMedian = im.filter(ImageFilter.MedianFilter)
finishing(ImMedian,'MedianFilter Blending',ALPHA)

#Mode filter
ImMode = im.filter(ImageFilter.ModeFilter)
finishing(ImMode,'ModeFilter Blending',ALPHA)

#Inverted image
ImInv = ImageChops.invert(im)
finishing(ImInv,'Color Invertion Blending',ALPHA)
 
#BLUR filter
ImBlur = im.filter(ImageFilter.BLUR)
finishing(ImBlur,'Blurred Image',ALPHA)
 
#Gaussian BLUR filter
ImGBlur = im.filter(ImageFilter.GaussianBlur(radius = 2))
finishing(ImGBlur,'GaussianBlur',ALPHA)

#CONTOUR filter
ImContour = im.filter(ImageFilter.CONTOUR)
finishing(ImContour,'ContourFilter',ALPHA)
 
#DETAIL filter
ImDetail = im.filter(ImageFilter.DETAIL)
finishing(ImDetail,'Detailed',ALPHA)
 
#EDGE_ENHANCE filter
ImEH = im.filter(ImageFilter.EDGE_ENHANCE)
finishing(ImEH,'EdgeEnhanced',ALPHA)
 
#EDGE_ENHANCE_MORE filter
ImEHM = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
finishing(ImEHM,'More EdgeEnhanced',ALPHA)
 
#EMBOSS filter
ImEmb = im.filter(ImageFilter.EMBOSS)
finishing(ImEmb,'Emboss Filtered',ALPHA)
 
#FIND_EDGES filter
ImEdges = im.filter(ImageFilter.FIND_EDGES)
finishing(ImEdges,'Find_Edges',ALPHA)
 
#SMOOTH filter
ImSmooth = im.filter(ImageFilter.SMOOTH)
finishing(ImSmooth,'Smooth Filtered',ALPHA)
 
#SMOOTH_MORE filter
ImSmoothMore = im.filter(ImageFilter.SMOOTH_MORE)
finishing(ImSmoothMore,'More Smooth Filtered',ALPHA)
 
#SHARPEN filter
ImSharp = im.filter(ImageFilter.SHARPEN)
finishing(ImSharp,'Sharp Filtered',ALPHA)
