# -*- coding: utf-8 -*-

import atx
import time

class YysHelper():
    def __init__(self):
        self.d = atx.connect()
        self.d.image_path = ['.', 'assets']

    def yuhun(self):
        while True:
            while True:
                ret = self.challenge()
                if not ret:
                    self.touchToContinue()
                    self.sleep(5)
                    continue
                break

            self.sleep(3)

            while True:
                self.sleep(10)
                ret = self.ready()
                if not ret:
                    self.touchToContinue()
                    self.sleep(5)
                    continue
                break

            self.sleep(20)

            count = 0
            while True:
                ret = self.clickToContinue()
                if not ret:
                    self.touchToContinue()
                    self.sleep(20)
                    continue
                count += 1
                if count >= 3:
                    break

    def ready(self):
        return self.clickImage('ready.1920x1080.png')

    def challenge(self):
        return self.clickImage('challenge.1920x1080.png')

    def clickToContinue(self):
        return self.clickImage('click_to_continue.1920x1080.png')

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

    def touchToContinue(self):
        self.d.click(200, 400)

def main():
    YysHelper().yuhun()

if __name__ == '__main__':
    main()
