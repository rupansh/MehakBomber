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
class Ajio(SmsApiInterface):
    def __init__(self):
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'Access-Control-Request-Headers': 'content-type',
            'Connection': 'keep-alive',
            'Host': 'login.web.ajio.com',
            'Origin': 'https://www.ajio.com',
            'Referer': 'https://www.ajio.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }

        data = {
            'firstName': "Ayam",
            'genderType': "Male",
            'login': "adobhal1@mail.ccsf.edu",
            'password': "Bruh@1234",
            'requestType': "SENDOTP"
        }

        super().__init__('https://login.web.ajio.com/api/auth/signupSendOTP', headers=headers, data=data)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("Ajio: international numbers not supported!")
            return
        self.data["mobileNumber"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)