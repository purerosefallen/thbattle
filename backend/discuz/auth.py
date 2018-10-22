# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
import hashlib
import time

# -- third party --
# -- own --
from backend.settings import DISCUZ


# -- code --
def md5(s):
    return hashlib.md5(s).hexdigest()


def _discuz_authcode(string, operation, key, expiry=0):
    try:
        ckey_length = 4
        key = md5(key)
        keya = md5(key[:16])
        keyb = md5(key[16:])
        if ckey_length:
            if operation == 'DECODE':
                keyc = string[:ckey_length]
            else:
                keyc = md5(str(time.time()))[-ckey_length:]
        else:
            keyc = ''

        cryptkey = keya + md5(keya + keyc)
        key_length = len(cryptkey)

        if operation == 'DECODE':
            pads = len(string) % 4 - 4
            if pads != -4:
                string += '=' * -pads

            string = string[ckey_length:].decode('base64')
        else:
            string = str(int(time.time()) + expiry if expiry else 10000000000)[-10:]
            string += md5(string + keyb)[:16] + string

        string_length = len(string)
        result = []

        box = range(256)
        rndkey = [ord(cryptkey[i % key_length]) for i in range(256)]
        j = 0
        for i in range(256):
            j = (j + box[i] + rndkey[i]) % 256
            box[i], box[j] = box[j], box[i]

        a = j = 0
        for i in range(string_length):
            a = (a + 1) % 256
            j = (j + box[a]) % 256
            box[a], box[j] = box[j], box[a]
            result.append(
                chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
            )

        result = ''.join(result)

        if operation == 'DECODE':
            cond = int(result[:10]) == 0 or int(result[:10]) - time.time() > 0
            cond = cond and result[10:26] == md5(result[26:] + keyb)[:16]
            if cond:
                return result[26:]
            else:
                return ''

        else:
            return keyc + result.encode('base64').replace('=', '')

    except Exception:
        return ''


def authencode(plain, saltkey):
    return _discuz_authcode(plain, 'ENCODE', md5(DISCUZ['authkey'] + saltkey))


def authdecode(encrypted, saltkey):
    return _discuz_authcode(encrypted, 'DECODE', md5(DISCUZ['authkey'] + saltkey))


def check_password(password, hash, salt):
    return md5(md5(password) + salt) == hash


def decode_cookie(auth, saltkey):
    rst = authdecode(auth, saltkey).split('\t')
    if not rst:
        return {}
    password, uid = rst
    return {'uid': uid, 'password': password}


def check_cookie_pwd(pwd, password):
    # return user.dz_member.password == password
    return pwd == password
