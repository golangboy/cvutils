# -*- coding: utf-8 -*-
import os
import shutil

import cv2
import numpy as np
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
                          size=wx.Size(470, 503), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"调色板类转单通道mask", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"提取voc数据集的分割任务", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button71 = wx.Button(self, wx.ID_ANY, u"提取voc数据集的分割任务(test)", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer1.Add(self.m_button71, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"单通道mask转为调色板", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_button91 = wx.Button(self, wx.ID_ANY, u"扫描计算miou", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button91, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"所有的jpg转为png", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button121 = wx.Button(self, wx.ID_ANY, u"二值化", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button121, 0, wx.ALL, 5)

        self.m_button131 = wx.Button(self, wx.ID_ANY, u"img[img==255]=1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button131, 0, wx.ALL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button15, 0, wx.ALL, 5)

        self.m_button1312 = wx.Button(self, wx.ID_ANY, u"img[img==255]=1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1312, 0, wx.ALL, 5)

        self.m_button1311 = wx.Button(self, wx.ID_ANY, u"img[img==1]=255", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1311, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_roseg2yolo.Bind(wx.EVT_LEFT_DOWN, self.roseg2yolo)
        self.m_button9.Bind(wx.EVT_LEFT_DOWN, self.yolo_dirs)
        self.m_button10.Bind(wx.EVT_LEFT_DOWN, self.rmmask)
        self.m_button11.Bind(wx.EVT_LEFT_DOWN, self.addmask)
        self.m_button12.Bind(wx.EVT_LEFT_DOWN, self.getids)
        self.m_button6.Bind(wx.EVT_LEFT_DOWN, self.patto8)
        self.m_button7.Bind(wx.EVT_LEFT_DOWN, self.handlevoc)
        self.m_button71.Bind(wx.EVT_LEFT_DOWN, self.handlevoc_test)
        self.m_button8.Bind(wx.EVT_LEFT_DOWN, self.mask2pat)
        self.m_button91.Bind(wx.EVT_LEFT_DOWN, self.calciou)
        self.m_button13.Bind(wx.EVT_LEFT_DOWN, self.jpg2png)
        self.m_button121.Bind(wx.EVT_LEFT_DCLICK, self.twovalue)
        self.m_button1312.Bind(wx.EVT_LEFT_DCLICK, self.img255to1)
        self.m_button1311.Bind(wx.EVT_LEFT_DCLICK, self.img1to255)

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
                # os.system(f"mv {os.path.join(target, f)} {os.path.join(target, f[:-9] + '.png')}")
                shutil.move(os.path.join(target, f), os.path.join(target, f[:-9] + '.png'))

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
                # os.system(f"mv {os.path.join(target, f)} {os.path.join(target, f[:-4] + '_mask.png')}")
                shutil.move(os.path.join(target, f), os.path.join(target, f[:-4] + '_mask.png'))

    def getids(self, event):
        event.Skip()
        import numpy as np
        from PIL import Image
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            fs = os.listdir(target)
            ids = set()
            mode_set = set()
            for f in fs:
                if not f.endswith('.png'):
                    continue
                img = Image.open(os.path.join(target, f))
                mode = img.mode
                if mode == 'L':
                    uniid = np.unique(img)
                    ids.update(uniid)
                elif mode == 'P':
                    uniid = np.unique(img)
                    ids.update(uniid)
                else:
                    wx.InfoMessageBox("Image mode do not support", "Message", wx.OK | wx.ICON_INFORMATION)
                    return
                mode_set.add(mode)
            print(ids)
            print(mode_set)
            wx.MessageBox(' '.join(str(ids)), "Message", wx.OK | wx.ICON_INFORMATION)

    def patto8(self, event):
        event.Skip()
        import numpy as np
        from PIL import Image
        # 打开选择文件夹
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            target = dlg.GetPath()
            fs = os.listdir(target)
            ids = set()
            mode_set = set()
            for f in fs:
                if not f.endswith('.png'):
                    continue
                img = Image.open(os.path.join(target, f))
                mode = img.mode
                if mode == 'L':
                    uniid = np.unique(img)
                    ids.update(uniid)
                elif mode == 'P':
                    uniid = np.unique(img)
                    ids.update(uniid)
                else:
                    wx.InfoMessageBox("Image mode do not support", "Message", wx.OK | wx.ICON_INFORMATION)
                    return
                mode_set.add(mode)
            print(ids)
            print(mode_set)
            for f in fs:
                if not f.endswith('.png'):
                    continue
                img = Image.open(os.path.join(target, f))
                img = np.array(img)
                # img[img == 255] = 0
                # for index, cl in enumerate(ids):
                #     img[img == cl] = index
                cv2.imwrite(os.path.join(target, f), img)

    def handlevoc(self, event):
        event.Skip()
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            voc_path = dlg.GetPath()
            segmentation_train = os.path.join(voc_path, 'ImageSets', "Segmentation", "train.txt")
            segmentation_val = os.path.join(voc_path, 'ImageSets', "Segmentation", "val.txt")
            dlg = wx.DirDialog(self, "Choose a output directory:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                save_path = dlg.GetPath()
                os.makedirs(os.path.join(save_path, "train", "images"), exist_ok=True)
                os.makedirs(os.path.join(save_path, "train", "masks"), exist_ok=True)
                os.makedirs(os.path.join(save_path, "val", "images"), exist_ok=True)
                os.makedirs(os.path.join(save_path, "val", "masks"), exist_ok=True)
                with open(segmentation_train, 'r') as f:
                    fs = f.readlines()
                    for line in fs:
                        shutil.copy(os.path.join(voc_path, "JPEGImages", line[:-1] + ".jpg"),
                                    os.path.join(save_path, "train", "images"))
                        shutil.copy(os.path.join(voc_path, "SegmentationClass", line[:-1] + ".png"),
                                    os.path.join(save_path, "train", "masks"))

                with open(segmentation_val, 'r') as f:
                    fs = f.readlines()
                    for line in fs:
                        shutil.copy(os.path.join(voc_path, "JPEGImages", line[:-1] + ".jpg"),
                                    os.path.join(save_path, "val", "images"))
                        shutil.copy(os.path.join(voc_path, "SegmentationClass", line[:-1] + ".png"),
                                    os.path.join(save_path, "val", "masks"))

    def handlevoc_test(self, event):
        event.Skip()
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            voc_path = dlg.GetPath()
            segmentation_test = os.path.join(voc_path, 'ImageSets', "Segmentation", "test.txt")
            dlg = wx.DirDialog(self, "Choose a output directory:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                save_path = dlg.GetPath()
                os.makedirs(os.path.join(save_path, "test", "images"), exist_ok=True)
                with open(segmentation_test, 'r') as f:
                    fs = f.readlines()
                    for line in fs:
                        shutil.copy(os.path.join(voc_path, "JPEGImages", line[:-1] + ".jpg"),
                                    os.path.join(save_path, "test", "images"))

    def mask2pat(self, event):
        event.Skip()
        from PIL import Image
        dlg = wx.DirDialog(self, "maks directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            mask_path = dlg.GetPath()
            # choice a file
            dlg = wx.FileDialog(self, "Choose a file",
                                style=wx.FD_DEFAULT_STYLE | wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                file_path = dlg.GetPath()
                std_file = Image.open(file_path)
                pat = std_file.getpalette()
                fs = os.listdir(mask_path)
                for f in fs:
                    if not f.endswith('.png'):
                        print(f)
                        continue
                    img = Image.open(os.path.join(mask_path, f)).convert('P')
                    img.putpalette(pat)
                    img.save(os.path.join(mask_path, f))

    def calciou(self, event):
        def cal_iou(output, mask):
            pred_uni = np.unique(output)
            mask_uni = np.unique(mask)
            uni = set()
            uni.update(pred_uni)
            uni.update(mask_uni)
            iou = 0
            for j in uni:
                ins = (output == j) & (mask == j)
                union = (output == j) | (mask == j)
                iou += ins.sum() / union.sum()
            return iou / len(uni)

        event.Skip()
        dlg = wx.DirDialog(self, "maks A directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            path_a = dlg.GetPath()
            dlg = wx.DirDialog(self, "maks B directory:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                path_b = dlg.GetPath()
                mask_dira = os.listdir(path_a)
                mask_dirb = os.listdir(path_b)
                assert len(mask_dira) == len(mask_dirb)
                import tqdm
                import cv2
                from PIL import Image
                alliou = 0
                alliou2 = 0
                for index in tqdm.tqdm(range(len(mask_dira))):
                    filea_name = mask_dira[index]
                    fileb_name = mask_dirb[index]
                    assert filea_name == fileb_name
                    imga = Image.open(os.path.join(path_a, filea_name))
                    imgb = Image.open(os.path.join(path_b, fileb_name))
                    imga = np.array(imga)
                    imgb = np.array(imgb)
                    assert imga.shape == imgb.shape and len(imga.shape) == 2
                    # 扫描分类数
                    classa = np.unique(imga)
                    classb = np.unique(imgb)
                    ids = set()
                    ids.update(classa)
                    ids.update(classb)
                    iou = 0
                    for c in ids:
                        ins = (imga == c) & (imgb == c)
                        uni = (imga == c) | (imgb == c)
                        ciou = np.sum(ins) / np.sum(uni)
                        iou += ciou
                    iou /= len(ids)
                    alliou += iou
                    alliou2 += cal_iou(imga, imgb)
                    pass
                print(alliou / len(mask_dira))
                print(alliou2 / len(mask_dira))
                wx.MessageBox("miou:{}".format(alliou / len(mask_dira)), "miou")

    def jpg2png(self, event):
        event.Skip()
        from PIL import Image
        import shutil
        dlg = wx.DirDialog(self, "jpg directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            jpg_path = dlg.GetPath()
            fs = os.listdir(jpg_path)
            for f in fs:
                if not f.endswith('.jpg'):
                    continue
                shutil.move(os.path.join(jpg_path, f), os.path.join(jpg_path, f[:-4] + '.png'))

    def twovalue(self, event):
        event.Skip()
        from PIL import Image
        dlg = wx.DirDialog(self, "images directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            img_path = os.listdir(dlg.GetPath())
            for f in img_path:
                if f.endswith(".png") or f.endswith(".jpg"):
                    img = Image.open(os.path.join(dlg.GetPath(), f))
                    print(f, img.mode)
                    img = img.convert("L")
                    img_np = np.array(img)
                    img_np[img_np > 200] = 255
                    img_np[img_np <= 200] = 0
                    Image.fromarray(img_np).save(os.path.join(dlg.GetPath(), f))
                    pass
            pass

    def img255to1(self, event):
        event.Skip()
        from PIL import Image
        dlg = wx.DirDialog(self, "images directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            img_path = os.listdir(dlg.GetPath())
            for f in img_path:
                if f.endswith(".png") or f.endswith(".jpg"):
                    img = Image.open(os.path.join(dlg.GetPath(), f))
                    img_np = np.array(img)
                    img_np[img_np == 255] = 1
                    Image.fromarray(img_np).save(os.path.join(dlg.GetPath(), f))

    def img1to255(self, event):
        event.Skip()
        from PIL import Image
        dlg = wx.DirDialog(self, "images directory:",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            img_path = os.listdir(dlg.GetPath())
            for f in img_path:
                if f.endswith(".png") or f.endswith(".jpg"):
                    img = Image.open(os.path.join(dlg.GetPath(), f))
                    img_np = np.array(img)
                    img_np[img_np == 1] = 255
                    Image.fromarray(img_np).save(os.path.join(dlg.GetPath(), f))


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()
