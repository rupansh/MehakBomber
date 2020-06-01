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
class PharmEasy(SmsApiInterface):
    def __init__(self):
        headers = {
            'origin': 'https://pharmeasy.in',
            'referer': 'https://pharmeasy.in/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length': '30',
            'content-type': 'application/json'
        }

        cookies = {
            'X-App-Version' : '1.0',
            'X-Phone-Platform':'web',
            'X-Default-City':'1',
            'X-Pincode':'400001',
            'XdI':'2011082f3a2776aac04f4ae7a79c1adc'
        }

        super().__init__('https://pharmeasy.in/api/auth/requestOTP', cookies, headers)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("PharmEasy: international numbers not supported!")
            return
        self.data["contactNumber"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)