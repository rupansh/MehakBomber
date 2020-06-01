# Copyright (C) 2020 rupansh <rupanshsekar@hotmail.com>
#
# Licensed under the GNU General Public License v3.0;
#
# You may not use this file except in compliance with the license.
#
# If you think you will copy my hardwork and get away with it, DMCA welcomes you!

import abc
import requests


class SmsApiInterface(abc.ABC):
    @abc.abstractmethod
    def __init__(self, url, cookies={}, headers={}, data={}):
        self.url = url
        self.cookies = cookies
        self.headers = headers
        self.data = data

    @abc.abstractmethod
    def set_num(self, cc: int, num: int):
        pass

    @abc.abstractmethod
    def send(self, cc: int, num: int) -> bool:
        self.set_num(cc, num)
        resp = requests.post(self.url, headers=self.headers, cookies=self.cookies, json=self.data)
        if resp.status_code == 200:
            return True
