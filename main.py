import json
import keyboard
import random
from utils import version

# 定义音符和对应的键位
notes = {
    "q": "1+",
    "w": "2+",
    "e": "3+",
    "r": "4+",
    "t": "5+",
    "y": "6+",
    "u": "7+",
    "a": "1",
    "s": "2",
    "d": "3",
    "f": "4",
    "g": "5",
    "h": "6",
    "j": "7",
    "z": "1-",
    "x": "2-",
    "c": "3-",
    "v": "4-",
    "b": "5-",
    "n": "6-",
    "m": "7-"
}

def practice1():
    # 一个简单的练习乐谱
    with open('practice.json', 'r') as f:
        list = json.load(f)

    print("开始练习乐谱！")
    for note in list:
        print(f"请输入 '{notes[note]}' : ", end="")
        user_input = ""
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "space":
                    break
                user_input += event.name

        if user_input == note:
            print("正确！")
        else:
            print(f"错误！正确答案是 {note} ({notes[note]})")

    print("练习结束！")

def practice2():
    print("开始练习乐谱！")
    print("请输入对应的键位，然后按空格结束输入")
    while True:  # 无限循环来确保练习永远不会结束
        note = random.choice(list(notes.keys()))  # 随机选择一个字母
        print(f"请输入 '{notes[note]}' : ", end="")
        user_input = ""
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "space":
                    break
                user_input += event.name

        if user_input == note:
            print("正确！")
        else:
            print(f"错误！正确答案是 {note} ({notes[note]})")

def main(mode):
    if mode == "1":
        practice1()
    elif mode == "2":
        practice2()

if __name__ == '__main__':
    version()
    mode = input("input: ")
    main(mode)