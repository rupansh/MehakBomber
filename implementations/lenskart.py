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
class LensKart(SmsApiInterface):
    def __init__(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache, no-store",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-api-client": "desktop",
            "x-b3-traceid": "991590653358998",
            "x-session-token": "66febc2f-c672-4b99-8459-3803001e52f5",
            "referrer": "https://www.lenskart.com/",
            "referrerPolicy": "no-referrer-when-downgrade",
        }

        cookies = {
            '__cfduid' : 'd3a65bcb99d7ba375200260ca6e4e111b1590653359',
            '__cfruid' : '58f4a287e9879eb4395e8f7edc3ceb51aa0969bd'
        }

        super().__init__("https://api.lenskart.com/v2/customers/sendOtp", cookies, headers)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("LensKart: international numbers not supported!")
            return
        self.data["telephone"] = num

    def send(self, cc: int, num: int):
        return super().send(cc, num)


class LensKart2(SmsApiInterface):
    def __init__(self):
        headers = {
            'Host': 'www.ref-r.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '26',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        data = {
          'submit': '1',
          'undefined': ''
        }

        super().__init__('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("LensKart2: international numbers not supported!")
            return
        self.data["mobile"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)
