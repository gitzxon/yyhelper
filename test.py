# -*- coding=utf-8 -*-

import os
import time

class YyHelper:

    device = ""
    device_x = 1920
    device_y = 1080
    #sumsung s6 2560 * 1440

    def __init__(self, device=""):
        self.device = device

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

        self.adbSendTouchCmd(challengeBtnCoordinate)
        self.sleep(20)

        self.adbSendTouchCmd(readyBtnCoordinate)
        self.sleep(70)  # wait for fighting

        self.adbSendTouchCmd(finishCoordinate)
        self.sleep(5)  # wait for showing the pangwawa
        self.adbSendTouchCmd(finishCoordinate)
        self.sleep(5)  # gifts come from the pangwawa
        self.adbSendTouchCmd(finishCoordinate)
        self.sleep(20)  # quit the fight scenario

    def fightForMaterialEndless(self):
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

        while True:
            self.adbSendTouchCmd(challengeBtnCoordinate)
            self.adbSendTouchCmd(readyBtnCoordinate)
            self.adbSendTouchCmd(finishCoordinate)
            self.sleep(5)

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
            self.adbSendTouchCmd([enchantment_x, enchantment_y])
            # wait for the showing of the challenge btn
            self.sleep(2)

            enchantment_attack_x = enchantment_attack_start_x + interval_x * index_x
            enchantment_attack_y = enchantment_attack_start_y + interval_y * index_y
            self.adbSendTouchCmd([enchantment_attack_x, enchantment_attack_y])
            # be ready for fighting
            self.sleep(15)

            self.touch_ready_btn()
            self.sleep(100)
            self.end_the_fight_and_sleep()

            if enchantment_index % 3 == 2:
                self.touch_pangwawa()


    def touch_ready_btn(self):
        ready_btn_coordinate = [2340, 1100]
        self.adbSendTouchCmd(ready_btn_coordinate)


    def end_the_fight_and_sleep(self):
        finish_coordinate = [1300, 750]
        self.adbSendTouchCmd(finish_coordinate)
        self.sleep(10)  # wait for showing the pangwawa
        self.touch_pangwawa()


    def touch_pangwawa(self):
        finish_coordinate = [1300, 750]
        self.adbSendTouchCmd(finish_coordinate)
        self.sleep(10)  # gifts come from the pangwawa
        self.adbSendTouchCmd(finish_coordinate)
        self.sleep(15)  # quit the fight scenario


    def adbSendTouchCmd(self, coordinate):
        print("adb : send touch cmd")

        if self.device == "" or self.device == None:
            adb_touch_cmd = "adb shell input tap"
        else:
            adb_touch_cmd = "adb -s " + str(self.device) + " shell input tap"

        x = str(coordinate[0])
        y = str(coordinate[1])
        cmd_to_run = adb_touch_cmd + " " + x + " " + y
        os.system(cmd_to_run)


    def sleep(self, seconds, msg=""):
        if msg is not None and msg != "":
            print("sleep for " + msg)
        print("sleep : " + str(seconds))
        time.sleep(seconds)


def fight_for_material():
    for i in range(0, 100):
        print("------ game : " + str(i + 1) + "------")
        YyHelper().startFightForMaterial()

def fight_for_material_endless():
    YyHelper().fightForMaterialEndless()

def fight_for_enchantment():
    YyHelper().startFightForEnchantment()


if __name__ == '__main__':
#     fight_for_material()
    fight_for_material_endless()
    # fight_for_enchantment()
