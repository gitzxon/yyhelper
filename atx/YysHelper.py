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
    image_name_of_gift_received = "gift_received.1920x1080.png"
    image_name_of_explore = "btn_explore.1920x1080.png"
    image_name_of_automatic = "automatic.1920x1080.png"
    image_name_of_back_to_map_of_world = "back_to_map_of_world.1920x1080.png"
    image_name_of_left_bottom_menu = "left_bottom_menu.1920x1080.png"

    def __init__(self):
        self.d = atx.connect()
        self.d.image_path = ['.', 'assets']

    def yuhun(self):
        while True:
            while True:
                ret = self.challenge()
                if not ret:
                    self.touch_to_continue()
                    self.sleep(5)
                    continue
                break

            self.sleep(3)

            while True:
                self.sleep(10)
                ret = self.ready()
                if not ret:
                    self.touch_to_continue()
                    self.sleep(5)
                    continue
                break

            self.sleep(20)

            count = 0
            while True:
                ret = self.click_to_continue()
                if not ret:
                    self.touch_to_continue()
                    self.sleep(20)
                    continue
                count += 1
                if count >= 3:
                    break

    def dungeon(self):

        is_exploration_finished = True
        while True:
            if is_exploration_finished:

                self.sleep(2)

                # todo : click the chest

                # show dungeon detail
                x_by_percentage = 0.93
                y_by_percentage = 0.66
                self.touch_by_percentage(x_by_percentage, y_by_percentage)
                self.sleep(3 + "waiting for the dungeon detail to show")

                # click btn explore
                result_for_clicking_explore_btn = self.find_and_click_img(self.image_name_of_explore)
                # 用是否能看见大地图的菜单来判断是否在副本中，而不是用是否点击成功 explore
                # 这样可以副本中途开脚本而不影响逻辑。
                map_of_world_find_point = self.d.exists(self.image_name_of_left_bottom_menu)
                if map_of_world_find_point is None:
                    self.sleep(3)
                    is_exploration_finished = False
                    is_exploration_finished = self.inside_dungeon_mechanically()
                else:
                    # 可能因为从副本内出来耗时间过长，
                    continue

            else:
                # just wait for finishing the exploration
                continue

    def inside_dungeon_mechanically(self):
        is_leader_shown = False
        while True:

            # 优先点击“点击继续”
            print("find and click continue")
            result_for_continue = self.d.click_nowait(self.image_name_of_continue)
            if result_for_continue is not None:
                continue

            print("find and click leader")
            result_leader = self.d.click_nowait(self.image_name_of_leader_enemy_sword)
            if result_leader is not None:
                is_leader_shown = True

            print("find and click gift")
            if is_leader_shown:
                self.d.click_nowait(self.image_name_of_gift)
                self.sleep(2, " after clicking the gift ")
                result_for_gift_received = self.d.click_nowait(self.image_name_of_gift_received)
                if result_for_gift_received:
                    self.touch_by_percentage(0.50, 0.75) # 随机点击一个区域以继续

                world_map_find_point = self.d.exists(self.image_name_of_left_bottom_menu)
                if world_map_find_point is None:
                    continue
                else:
                    return True

            else:
                print("check is fighting")
                back_find_point = self.d.exists(self.image_name_of_back_to_map_of_world)
                if back_find_point is None:
                    is_fighting_with_normal = True
                    print(" fighting ")
                else:
                    is_fighting_with_normal = False
                    print(" not fighting ")

                if is_fighting_with_normal:
                    continue
                else:
                    result_for_clicking_normal_enemy = self.find_and_click_img(self.image_name_of_normal_enemy_sword)
                    if result_for_clicking_normal_enemy:
                        # 画面中有 normal_enemy 但是不一定点击上了。
                        continue
                    else:
                        # find normal enemy failed. swipe
                        self.swipe_by_percentage(0.50, 0.50, 0.25, 0.5)

    def ready(self):
        return self.click_image('ready.1920x1080.png')

    def challenge(self):
        return self.click_image('challenge.1920x1080.png')

    def click_to_continue(self):
        return self.click_image('click_to_continue.1920x1080.png')

    def click_image(self, image, timeout=10):
        try:
            self.d.click_image(image, timeout=timeout)
            return True
        except atx.ImageNotFoundError:
            print('%s button not found' % image)
            return False

    def click_img_until_success(self, img_name):
        while self.find_and_click_img(img_name) is not True:
            self.sleep(3)

    def find_and_click_img(self, image_name):
        '''
        True : find the img success
        False : find the img failed
        :param image_name:
        :return:
        '''
        print("start to find the img : " + image_name)
        result = self.d.click_nowait(image_name)
        if result is not None:
            print('%s clicked successfully' % image_name)
            return True
        else:
            print('%s button not found' % image_name)
            return False

    def sleep(self, seconds, msg=""):
        if msg is not None and msg != "":
            print("sleep for " + msg)
        print("sleep : " + str(seconds))
        time.sleep(seconds)

    def touch_to_continue(self):
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
    YysHelper().dungeon()


if __name__ == '__main__':
    main()
