# Copyright (C) 2020 rupansh <rupanshsekar@hotmail.com>
#
# Licensed under the GNU General Public License v3.0;
#
# You may not use this file except in compliance with the license.
#
# If you think you will copy my hardwork and get away with it, DMCA welcomes you!

import requests
from api import SmsApiInterface
from implementations import sms_api_impl


@sms_api_impl
class ConfirmTkt(SmsApiInterface):
    def __init__(self):
        super().__init__("https://securedapi.confirmtkt.com/api/platform/register")

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("ConfirmTkt: International Numbers Not Supported!!!")
            return
        self.data["mobileNumber"] = num

    def send(self, cc: int, num: int):
        self.set_num(cc, num)
        requests.get(self.url, params=self.data)
        return True