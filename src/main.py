#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import string
import secrets


# 按照[a-zA-Z0-9_]{6,20}的正则生成一个密码，其中小写、大写、数字分别为6位，下划线为2位
def genPassword():
    # 判断字符串是否属于特殊字符，其实是判断该字符是否为下划线_
    def assertStr(s):
        if s and (s in string.punctuation):
            return True
        else:
            return False
    password = ""
    char = string.ascii_letters + string.digits + "_"
    while True:
        password = ''.join(secrets.choice(char) for i in range(20))
        if (sum(c.islower() for c in password) == 6
                and sum(c.isupper() for c in password) == 6
                and sum(c.isdigit() for c in password) == 6
                and sum(assertStr(s) for s in password) == 2):
            break
    return password


if __name__ == "__main__":
  print(genPassword())
