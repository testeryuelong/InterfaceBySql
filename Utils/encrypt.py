# -*-coding:utf-8 -*-
# @Author : Zhigang

import hashlib

def encrypt(text):
    md5=hashlib.md5()
    md5.update(text.encode("utf-8"))
    encrypt_text=md5.hexdigest()
    return encrypt_text

if __name__=="__main__":
    print (encrypt("123"))