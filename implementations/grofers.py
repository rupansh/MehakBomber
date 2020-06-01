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
class Grofers(SmsApiInterface):
    def __init__(self):
        headers = {
            'origin': 'https://grofers.com',
            'referer': 'https://grofers.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'app_client': 'consumer_web',
            'auth_key': '729b06d118fd076436ee520b9235fb3db741a54a05d0a2dc2b03c3761fdd5ce0'
        }

        cookies = {
            '__cfduid' : 'de3c6d890ae664aa39f4e99a2bb1741021590687168',
            '__cfruid' : '3ec830e630224acbb7955dbf95d494cd3ed41667',
            'ajs_anonymous_id' : '%223fb1cddf-086c-4bef-b75f-04a1d589983d%22',
            'ajs_group_id' : 'null',
            'ajs_user_id' : 'null',
            'city' : '',
            'gr_1_deviceId' : '94fd853a-1014-43aa-8402-2695ff33c087',
            'gr_1_lat' : '28.4640810758775',
            'gr_1_locality' : '1849',
            'gr_1_lon' : '76.9942133969929',
            'rl_anonymous_id' : '%22e3c79578-aa82-4bc1-b91a-73a67ee0dd43%22',
            'rl_user_id' : '%22%22'
        }

        super().__init__('https://grofers.com/v2/accounts/', cookies, headers)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("Myntra: international numbers not supported!")
            return
        self.data["user_phone"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)
