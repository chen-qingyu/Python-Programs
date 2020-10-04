import time

print("你好！这是一个对话小程序，测试用。后期要改成网页版的。")
print("我叫陈青羽，很高兴你能来这里！")

print("--------------------")
print("1. 很高兴认识你！")
print("2. 似曾相识的对话呢。")
print("0. 再见……")

x = input()
print("--------------------")

time.sleep(1)
while True:
    if x == '1':
        print("我也很高兴认识你！（虽然可能并不认识……）")
        break
    elif x == '2':
        print("看来你知道我的套路了")
        break
    elif x == '0':
        print("Good Bye!")
        exit()
    else:
        print("what?")


print("你有什么想知道的吗？")

print("--------------------")
print("1. 你为什么这么无聊？")
print("2. 你会哪些技能？")
print("3. 这个对话是你预先写好的吗？")
print("0. 再见……")

x = input()
print("--------------------")

time.sleep(1)
while True:
    if x == '1':
        print("这种无礼的问题，拒绝回答，哼")
        break
    elif x == '2':
        print("问就是啥都不会，百度也不会")
        print("不过关于编程还是可以讨论一下的")
        break
    elif x == '3':
        print("对的。写死我了。")
        break
    elif x == '0':
        print("Good Bye!")
        exit()
    else:
        print("what?")

print("你有什么想知道的吗？")

print("--------------------")
print("1. 你为什么这么无聊？")
print("2. 你会哪些技能？")
print("3. 这个对话是你预先写好的吗？")
print("0. 再见……")

x = input()
print("--------------------")

time.sleep(1)
while True:
    if x == '1':
        print("这种无礼的问题，拒绝回答，哼")
        break
    elif x == '2':
        print("问就是啥都不会，百度都不会")
        print("不过关于编程有趣的问题还是可以讨论一下的")
        break
    elif x == '3':
        print("对的。")
        break
    elif x == '0':
        print("Good Bye!")
        exit()
    else:
        print("what?")
