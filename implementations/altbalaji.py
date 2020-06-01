# Copyright (C) 2020 rupansh <rupanshsekar@hotmail.com>
#
# Licensed under the GNU General Public License v3.0;
#
# You may not use this file except in compliance with the license.
#
# If you think you will copy my hardwork and get away with it, DMCA welcomes you!

from api import SmsApiInterface
from implementations import sms_api_impl


@sms_api_impl
class AltBalaji(SmsApiInterface):
    def __init__(self):
        headers = {
            'Host': 'api.cloud.altbalaji.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://lite.altbalaji.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Referer': 'https://lite.altbalaji.com/subscribe?progress=input',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }
        super().__init__('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers)

    def set_num(self, cc: int, num: int):
        self.data["country_code"] = cc
        self.data["phone_number"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)