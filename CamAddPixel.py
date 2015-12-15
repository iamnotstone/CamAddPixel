# -*- coding: utf-8 -*-
from VideoCapture import Device
import wx
from PIL import Image

SIZE = (640, 480)

def generateSque():
    a = []
    for i in range(10000):
        a.append((255,0,0))
    return a


def get_image():
    # Put your code here to return a PIL image from the camera.
    cam = Device(0)
    
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
        wx.CallLater(100, self.update)
    def create_bitmap(self):
        image = get_image()
        #image = image.convert('L')
        #print list(image.getdata())
        a = generateSque()
        image.putdata(a)
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
