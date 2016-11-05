# -*- coding=utf-8 -*-

import os
import time
import re

class YyHelper:

    device = ""
    device_x = 0
    device_y = 0
    # Sumsung s6 2560 * 1440
    # Xiaomi 5 1920 * 1080

    def __init__(self, device=""):
        self.device = device
        self.adb = Adb(device)
        self.initDeviceResolution()

    def initDeviceResolution(self):
        '''
        获取屏幕分辨率
        '''
        resolution = self.adb.getResolution()
        self.device_x = resolution[1]
        self.device_y = resolution[0]

    def startFightForMaterial(self):
        '''
        点击挑战按钮
        :return:
        '''
        challengeBtnByPercentage = [0.75, 0.75]
        readyBtnByPercentage = [0.90, 0.75]
        finishByPercentage = [0.50, 0.50]

        challengeBtnCoordinate = [challengeBtnByPercentage[0] * self.device_x, challengeBtnByPercentage[1] * self.device_y]
        readyBtnCoordinate = [self.device_x * readyBtnByPercentage[0], self.device_y * readyBtnByPercentage[1]]
        finishCoordinate = [self.device_x * finishByPercentage[0], self.device_y * finishByPercentage[1]]

        self.adb.touch(challengeBtnCoordinate)
        self.sleep(20)

        self.adb.touch(readyBtnCoordinate)
        self.sleep(70)  # wait for fighting

        self.adb.touch(finishCoordinate)
        self.sleep(5)  # wait for showing the pangwawa
        self.adb.touch(finishCoordinate)
        self.sleep(5)  # gifts come from the pangwawa
        self.adb.touch(finishCoordinate)
        self.sleep(20)  # quit the fight scenario

    def fightForMaterialEndless(self):
        '''
        无尽模式刷御魂和觉醒材料
        :return:
        '''
        challengeBtnByPercentage = [0.75, 0.75]
        readyBtnByPercentage = [0.90, 0.75]
        finishByPercentage = [0.50, 0.50]

        challengeBtnCoordinate = [challengeBtnByPercentage[0] * self.device_x, challengeBtnByPercentage[1] * self.device_y]
        readyBtnCoordinate = [self.device_x * readyBtnByPercentage[0], self.device_y * readyBtnByPercentage[1]]
        finishCoordinate = [self.device_x * finishByPercentage[0], self.device_y * finishByPercentage[1]]

        while True:
            self.adb.touch(challengeBtnCoordinate)
            self.sleep(1)
            self.adb.touch(readyBtnCoordinate)
            self.sleep(1)
            self.adb.touch(finishCoordinate)
            self.sleep(1)

    def startFightForEnchantment(self):
        enchantment_start_x = 640
        enchantment_start_y = 300
        enchantment_middle_x = 1280
        enchantment_middle_y = 530
        enchantment_attack_start_x = 790
        enchantment_attack_start_y = 500

        interval_x = enchantment_middle_x - enchantment_start_x
        interval_y = enchantment_middle_y - enchantment_start_y

        enchantment_list = range(0, 9)
        for enchantment_index in enchantment_list:
            # if enchantment_index <= 7:
            #     continue
            index_x = enchantment_index % 3
            index_y = (enchantment_index - enchantment_index % 3) / 3

            print("index x | y is : " + str(index_x) + " | " + str(index_y))

            enchantment_x = enchantment_start_x + index_x * interval_x
            enchantment_y = enchantment_start_y + index_y * interval_y
            self.adb.touch([enchantment_x, enchantment_y])
            # wait for the showing of the challenge btn
            self.sleep(2)

            enchantment_attack_x = enchantment_attack_start_x + interval_x * index_x
            enchantment_attack_y = enchantment_attack_start_y + interval_y * index_y
            self.adb.touch([enchantment_attack_x, enchantment_attack_y])
            # be ready for fighting
            self.sleep(15)

            self.touchReadyBtn()
            self.sleep(100)
            self.endTheFightAndSleep()

            if enchantment_index % 3 == 2:
                self.touchPangwawa()

    def touchReadyBtn(self):
        ready_btn_coordinate = [2340, 1100]
        self.adb.touch(ready_btn_coordinate)

    def endTheFightAndSleep(self):
        finish_coordinate = [1300, 750]
        self.adb.touch(finish_coordinate)
        self.sleep(10)  # wait for showing the pangwawa
        self.touchPangwawa()

    def touchPangwawa(self):
        finish_coordinate = [1300, 750]
        self.adb.touch(finish_coordinate)
        self.sleep(10)  # gifts come from the pangwawa
        self.adb.touch(finish_coordinate)
        self.sleep(15)  # quit the fight scenario

    def sleep(self, seconds, msg=""):
        if msg is not None and msg != "":
            print("sleep for " + msg)
        print("sleep : " + str(seconds))
        time.sleep(seconds)

class Adb:
    def __init__(self, device=""):
        self.device = device
        if self.device == "" or self.device == None:
            self.cmdPrefix = "adb"
        else:
            self.cmdPrefix = "adb -s %s" % self.device

    def touch(self, coordinate):
        print("adb : touch %d,%d" % (coordinate[0], coordinate[1]))
        cmd = "%s shell input tap %d %d" % (self.cmdPrefix, coordinate[0], coordinate[1])
        os.system(cmd)

    def getResolution(self):
        print("adb : get resolution")
        pattern = re.compile(r'.* (\d+)x(\d+).*')
        cmd = "%s shell wm size" % self.cmdPrefix
        proc = os.popen(cmd)
        output = ''.join(proc.readlines())
        proc.close()
        rematch = pattern.match(output)
        if rematch is not None:
            resolution = [int(rematch.group(1)), int(rematch.group(2))]
            print("adb : resolution is %dx%d" % (resolution[0], resolution[1]))
            return resolution
        else:
            print("adb : get reslution failed!\noutput is %s" % output)
            exit()

def fight_for_material():
    for i in range(0, 100):
        print("------ game : " + str(i + 1) + "------")
        YyHelper().startFightForMaterial()

def fight_for_material_endless():
    YyHelper().fightForMaterialEndless()

def fight_for_enchantment():
    YyHelper().startFightForEnchantment()

if __name__ == '__main__':
    # fight_for_material()
    fight_for_material_endless()
    # fight_for_enchantment()
