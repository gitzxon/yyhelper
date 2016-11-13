# -*- coding: utf-8 -*-

import atx
import time


class YysHelper:
    image_name_of_challenge = "challenge.1920x1080.png"
    image_name_of_continue = "click_to_continue.1920x1080.png"
    image_name_of_ready = "ready.1920x1080.png"
    image_name_of_normal_enemy_sword = "sword.1920x1080.png"
    image_name_of_leader_enemy_sword = "leader_sword.1920x1080.png"
    image_name_of_gift = "fresh.1920x1080.png"
    image_name_of_gift_received = "gift_received.1920x1080.1920x1080.png"
    image_name_of_explore = "btn_explore.1920x1080.png"

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

    def dungeon2(self):
        '''
        探索副本。
        by default :
        点击副本列表最后一个可见的 item 的中心。
        如果想换副本刷的话，可以上下滚动目标副本到副本列表最后一个可见的 item
        :return:
        '''

        # show dungeon detail
        x_by_percentage = 0.93
        y_by_percentage = 0.66
        self.touch_by_percentage(x_by_percentage, y_by_percentage)
        self.sleep(3)

        # click btn explore
        self.click_img_until_success(self.image_name_of_explore)
        self.sleep(3)

        # inside dungeon
        is_leader_shown = False
        while True:
            if is_leader_shown is True:
                # 首领打完，开始收礼物
                while True:
                    result_for_click_gift = self.d.click_nowait(self.image_name_of_gift)
                    if result_for_click_gift is not None:
                        self.sleep(2)
                        self.touch_by_percentage(0.5, 0.5)
                        self.sleep(1)
                    else:
                        # 所有小纸人礼物已经收完
                        # 自动退回大地图界面。
                        # 大地图界面中可能会有 宝箱 或者 妖气发现 或者 章鱼
                        # 暂时只处理宝箱
                        # todo : 这里需要截一下宝箱的图 chest
                        return
            else:
                # 首领没打
                result_for_click_leader = self.d.click_nowait(self.image_name_of_leader_enemy_sword)

                if result_for_click_leader is not None:
                    is_leader_shown = True
                    self.fight_with_enemy_inside_dungeon()
                else:
                    is_leader_shown = False
                    result_for_find_normal_enemy = self.d.click_nowait(self.image_name_of_normal_enemy_sword)
                    if result_for_find_normal_enemy is not None:
                        self.fight_with_enemy_inside_dungeon()
                        continue
                    else:
                        # 没有首领，也没有普通怪，则滑动屏幕。
                        self.d.swipe(0.75, 0.50, 0.25, 0.50)
                        continue

    def dungeon(self):

        # show dungeon detail
        x_by_percentage = 0.93
        y_by_percentage = 0.66
        self.touch_by_percentage(x_by_percentage, y_by_percentage)
        self.sleep(3)

        # click btn explore
        self.click_img_until_success(self.image_name_of_explore)
        self.sleep(3)

        self.inside_dungeon()

    def inside_dungeon(self):

        is_leader_shown = False
        while True:

            # 优先点击“点击继续”
            result_for_continue = self.d.click_nowait(self.image_name_of_continue)
            if result_for_continue is not None:
                continue

            result_leader = self.d.click_nowait(self.image_name_of_leader_enemy_sword)
            if result_leader is not None:
                is_leader_shown = True

            if is_leader_shown:
                self.d.click_nowait(self.image_name_of_gift)
                result_for_gift_received = self.d.click_nowait(self.image_name_of_gift_received)
                if result_for_gift_received:
                    self.touch_by_percentage(0.50, 0.75)

            else:
                result_click_normal = self.d.click_nowait(self.image_name_of_normal_enemy_sword)
                if result_click_normal is None:
                    # 屏幕中没有怪了，右滑屏幕
                    self.swipe_by_percentage(0.75, 0.5, 0.25, 0.5)

    def fight_with_enemy_inside_dungeon(self):
        '''
        点击 FindPoint ，开始战斗。
        游戏在探索副本中会自动准备。
        只需要等待结束画面就可以了
        :param find_point:
        :return:
        '''
        # scene for the ending fo the fight
        self.click_img_until_success(self.image_name_of_continue)
        self.sleep(2)
        self.click_img_until_success(self.image_name_of_continue)
        self.sleep(2)
        self.click_img_until_success(self.image_name_of_continue)
        self.sleep(2)

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

    def click_img_until_success(self, img_name):
        while self.find_and_click_img(img_name) is not True:
            self.sleep(3)

    def find_and_click_img(self, image_name):
        print("start to find the img : " + image_name)
        result = self.d.click_nowait(image_name)
        if result is not None:
            print('%s clicked successfully' % image_name)
            return True
        else:
            print('%s button not found' % image_name)
            return False

    def find_and_click_randomly(self, image_name):
        find_point = self.d.exists(image_name, threshold=0.7)
        if find_point is not None:
            print(find_point.pos[0] + " | " + find_point.pos[1])
            self.d.click(find_point.pos[0], find_point.pos[1])
            self.d.click(find_point.pos[0] - 50, find_point.pos[1])
            self.d.click(find_point.pos[0] + 50, find_point.pos[1])
            return True
        else:
            return False

    def sleep(self, seconds, msg=""):
        if msg is not None and msg != "":
            print("sleep for " + msg)
        print("sleep : " + str(seconds))
        time.sleep(seconds)

    def touchToContinue(self):
        self.d.click(200, 400)

    def touch_by_percentage(self, x_percentage, y_percentage):
        '''
        d.display returns the value of portrait
        :param x_percentage:
        :param y_percentage:
        :return:
        '''
        x = self.d.display.height * x_percentage
        y = self.d.display.width * y_percentage
        self.d.click(x, y)

    def swipe_by_percentage(self, start_x_percentage, start_y_percentage, end_x_percentage, end_y_percentage):
        start_x = self.d.display.height * start_x_percentage
        start_y = self.d.display.width * start_y_percentage
        end_x = self.d.display.height * end_x_percentage
        end_y = self.d.display.width * end_y_percentage
        self.d.swipe(start_x, start_y, end_x, end_y, steps=20)


def main():
    # YysHelper().yuhun()
    YysHelper().dungeon()


if __name__ == '__main__':
    main()
