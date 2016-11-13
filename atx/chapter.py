# -*- coding: utf-8 -*-

import atx
import time

class YysHelper():
    def __init__(self):
        self.d = atx.connect()
        self.d.image_path = ['.', 'assets']

    def chapter(self, level):
        """
        章节循环一轮游，进章节把屏幕内的小怪打完就出来
        """
        while True:
            chapterImage = "chapter%d.1920x1080.png" % level

            ret = self.clickImage(chapterImage)

            if ret:
                self.sleep(2)

            ret = self.clickImage("explore.1920x1080.png")

            if ret:
                self.sleep(8)

            ret = self.clickImage("lock.1920x1080.png", time=5)

            fightedWithLeader = False

            while not fightedWithLeader:
                swordExists = True
                while True:
                    ret = self.clickImage("sword.1920x1080.png")
                    if not ret:
                        ret = self.clickImage("leader_sword.1920x1080.png", time=5)
                        fightedWithLeader = ret

                    if ret:
                        self.sleep(10)
                        ret = self.d.exists("friend.1920x1080.png")
                        if ret:
                            break
                    else:
                        swordExists = False
                        break

                if not swordExists:
                    break

                if ret:
                    count = 0
                    while True:
                        ret = self.clickImage("click_to_continue.1920x1080.png")
                        if not ret:
                            if count >= 3:
                                self.sleep(7)
                                break
                        else:
                            count += 1

            while fightedWithLeader:
                ret = self.clickImage("fresh.1920x1080.png")
                if ret:
                    self.clickImage("back.1920x1080.png")
                else:
                    break

            ret = self.clickImage("back.1920x1080.png")

            if ret:
                self.sleep(2)
                ret = self.clickImage("chapter_quit_confirm.1920x1080.png")
                if ret:
                    self.sleep(7)

    def clickImage(self, image, time=10):
        try:
            self.d.click_image(image, timeout=time)
            return True
        except atx.ImageNotFoundError:
            print('%s button not found' % image)
            return False

    def sleep(self, seconds, msg=""):
        if msg is not None and msg != "":
            print("sleep for " + msg)
        print("sleep : " + str(seconds))
        time.sleep(seconds)

def main():
    YysHelper().chapter(13)

if __name__ == '__main__':
    main()
