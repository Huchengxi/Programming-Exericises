# -*- coding:utf-8 -*-

# 鸭子类型，当看见一只鸟，有鸭子的行为，可以称他为鸭子


class Cat:
    def say(self):
        print("i am a cat")


class Dog:
    def say(self):
        print("i am a dog")


class Duck:
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]

for animal in animal_list:
    animal().say()