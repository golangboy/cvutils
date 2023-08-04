# -*- coding: utf-8 -*-
import os

import cv2
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-368-g19bcc292)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_roseg2yolo = wx.Button(self, wx.ID_ANY, u"Robotflow语义分割数据转yolo", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer1.Add(self.m_roseg2yolo, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"yolo一键处理文件夹", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"去掉后缀_mask", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"添加后缀_mask", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"获取所有分类值", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button12, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_roseg2yolo.Bind(wx.EVT_LEFT_DOWN, self.roseg2yolo)
        self.m_button9.Bind(wx.EVT_LEFT_DOWN, self.yolo_dirs)
        self.m_button10.Bind(wx.EVT_LEFT_DOWN, self.rmmask)
        self.m_button11.Bind(wx.EVT_LEFT_DOWN, self.addmask)
        self.m_button12.Bind(wx.EVT_LEFT_DOWN, self.getids)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def roseg2yolo(self, event):
        event.Skip()
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            import JSON2YOLO.general_json2yolo as g2y
            g2y.convert_coco_json(target, True)
            # 执行ls -la 并且输出结果到控制台
            os.system(f"cp {target}/*.jpg new_dir/images")
            os.system(f"cp new_dir/labels/_annotations.coco/*.txt new_dir/labels")
            os.system(f"rm -rf new_dir/labels/_annotations.coco")

            dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                os.system(f"mv new_dir {dlg.GetPath()}")

    def yolo_dirs(self, event):
        event.Skip()
        from ultralytics import YOLO
        # 选择模型文件
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() != wx.ID_OK:
            return
        model_path = dlg.GetPath()
        model = YOLO(model_path)

        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            dlg = wx.DirDialog(self, "Choose a directory:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                save_dir = dlg.GetPath()
                fs = os.listdir(target)
                for f in fs:
                    if not f.endswith('.jpg'):
                        continue
                    src_img = os.path.join(target, f)
                    model.predict(source=src_img, project=save_dir, name=f[:-4], verbose=True, save=True)
                cw = os.getcwd()
                os.chdir(save_dir)
                os.system("mv ./*/*.jpg .")
                os.system("find . -type d -exec rm -r {} \;")
                os.chdir(cw)

    def rmmask(self, event):
        event.Skip()
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            fs = os.listdir(target)
            for f in fs:
                if not f.endswith('_mask.png'):
                    continue
                os.system(f"mv {os.path.join(target, f)} {os.path.join(target, f[:-9] + '.png')}")

    def addmask(self, event):
        event.Skip()
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            fs = os.listdir(target)
            for f in fs:
                if not f.endswith('.png'):
                    continue
                os.system(f"mv {os.path.join(target, f)} {os.path.join(target, f[:-4] + '_mask.png')}")

    def getids(self, event):
        event.Skip()
        import numpy as np
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            fs = os.listdir(target)
            ids = set()
            for f in fs:
                if not f.endswith('.png'):
                    continue
                img = cv2.imread(os.path.join(target, f))
                uniid = np.unique(img)
                ids.update(uniid)
            print(ids)
            wx.MessageBox(' '.join(str(ids)), "Message", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()
