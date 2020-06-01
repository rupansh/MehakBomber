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
class HeroMoto(SmsApiInterface):
    def __init__(self):
        headers = {
            'Host': 'www.heromotocorp.com',
            'Connection': 'keep-alive',
            'Content-Length': '126',
            'Accept': '*/*',
            'Origin': 'https://www.heromotocorp.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.heromotocorp.com/en-in/xpulse200/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        cookies = {
        '_ga': 'GA1.2.1273460610.1561191565',
        '_gid': 'GA1.2.172574299.1561191565',
        '_gcl_au': '1.1.833556660.1561191566',
        '_fbp': 'fb.1.1561191568709.1707722126',
        'PHPSESSID': 'm5tap7nr75b2ehcn8ur261oq86',
        }

        data = {
          'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=',
          'mobile_no_otp': '',
          'csrf': '523bc3fa1857c4df95e4d24bbd36c61b'
        }

        super().__init__('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', cookies, headers, data)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("HeroMoto: international numbers not supported!")
            return
        self.data["mobile_no"] = num

    def send(self, cc: int, num: int) -> bool:
        return super().send(cc, num)
