"""
    加密演示
"""

import getpass
import hashlib

pwd = getpass.getpass()
print(pwd)

# 加密处理
hash = hashlib.md5("*#06#".encode())  # 加盐处理
hash.update(pwd.encode())
pwd = hash.hexdigest()
print(pwd)