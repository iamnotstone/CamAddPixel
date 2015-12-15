# -*- coding: utf-8 -*-
from VideoCapture import Device
import wx
from PIL import Image

SIZE = (640, 480)

def generateSque():
    a = []
    for i in range(640):
        a.append((255,0,0))
    return a

def getRectFromImage(LeftTop,RightButtom):
    dataAry = []
    for i in range(LeftTop[1],RightButtom[1]):
        raw = i
        if raw == LeftTop[1]:
            for j in range(LeftTop[0],RightButtom[0]):
                dataAry.append((j,i))
        elif raw == RightButtom[1] - 1:
            for j in range(LeftTop[0],RightButtom[0]):
                dataAry.append((j,i))
        else:
            dataAry.append((LeftTop[0],i))
            dataAry.append((RightButtom[0] - 1,i))
    return dataAry
    
def get_image():
    # Put your code here to return a PIL image from the camera.
    cam = Device(1)
    
    #return Image.new('L', SIZE)
    return cam.getImage(1)

def pil_to_wx(image):
    width, height = image.size
    buffer = image.convert('RGB').tostring()
    bitmap = wx.BitmapFromBuffer(width, height, buffer)
    return bitmap

class Panel(wx.Panel):
    def __init__(self, parent):
        super(Panel, self).__init__(parent, -1)
        self.SetSize(SIZE)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.update()
    def update(self):
        self.Refresh()
        self.Update()
        wx.CallLater(10, self.update)
    def create_bitmap(self):
        image = get_image()
        #image = image.convert('L')
        #print list(image.getdata())
        a = generateSque()
        dataAry = getRectFromImage((100,200),(400,400))
        #print len(dataAry)
        #print len(list(image.getdata()))
        for pos in dataAry:
            image.putpixel(pos,(255,0,0))
        
            
        bitmap = pil_to_wx(image)
        return bitmap
    def on_paint(self, event):
        bitmap = self.create_bitmap()
        dc = wx.AutoBufferedPaintDC(self)
        dc.DrawBitmap(bitmap, 0, 0)

class Frame(wx.Frame):
    def __init__(self):
        style = wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX
        super(Frame, self).__init__(None, -1, 'Camera Viewer', style=style)
        panel = Panel(self)
        self.Fit()

def main():
    app = wx.App()
    frame = Frame()
    frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
