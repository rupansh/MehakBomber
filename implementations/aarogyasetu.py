import requests
import json
from api import SmsApiInterface
from implementations import sms_api_impl


@sms_api_impl
class AarogyaSetu(SmsApiInterface):
    def __init__(self):
        super().__init__("https://api.swaraksha.gov.in/generateOTP", headers={"x-api-key": "ykixqE5H352HalBW4MNvI7HGJBXreLFx1APCkqEl"})

    def set_num(self, cc: int, num: int):
        self.data["primaryId"] = f"+{cc}{num}"

    def send(self, cc: int, num: int):
        self.set_num(cc, num)
        resp = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        if resp.status_code == 200:
            return True