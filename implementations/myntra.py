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
class Myntra(SmsApiInterface):
    def __init__(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-meta-app': 'channel=web',
            'x-myntra-network': 'yes',
            'x-myntraweb': 'Yes',
            'x-requested-with': 'browser'
        }

        cookies = {
            'bm_sz': '445D91B3FEC3FB62E3952A2A9D7DBE8D',
            '_d_id': '5d238330-44c2-44e9-8b16-1d1a435c5755',
            'mynt-eupv': '1',
            '_abck': 'F3A5E0C006909B891022CDC36CB20133',
            'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpka016RXdZekV0WVRCaFlTMHhNV1ZoTFdJd1pHVXRNREF3WkROaFpqSTRZbVprSWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTURZeE9UZzFOamNzSW1semN5STZJa2xFUlVFaWZRLldIRDBFXzdpTmxJUHlfdkZCRWpVRnBOOHprLTJ4R3ZSdW5SVUhRUnhGcW8',
            'xid': 'b7d310c1-a0aa-11ea-b0de-000d3af28bfd',
            'utm_track_1': 'a%3A7%3A%7Bs%3A10%3A%22utm_source%22%3Bs%3A6%3A%22direct%22%3Bs%3A10%3A%22utm_medium%22%3Bs%3A6%3A%22direct%22%3Bs%3A12%3A%22utm_campaign%22%3BN%3Bs%3A11%3A%22campaign_id%22%3BN%3Bs%3A12%3A%22octane_email%22%3BN%3Bs%3A10%3A%22trackstart%22%3Bi%3A1590646567%3Bs%3A8%3A%22trackend%22%3Bi%3A1591251367%3B%7D',
            'utrid': 'uuid-15906465677277',
            'G_ENABLED_IDPS': 'google',
            'AKA_A2': 'A',
            'ak_bmsc': '483D844FE93AE06250D6FF0B6174220B312C725477200000D38BCF5E39DC341B~plPBTNWXozENjWpWSuvEyH+5MG/X+VN+L2Ulh6m1iAWoV9WEhjFCxJS7gwZ1r61sSkJ3QIxfHAmw863i0bRlvxUWm1gFXnK8iZLYk2mRLwOjbwgH97Uhv/+PBzgIPleo6iur3JGM9g836KtF1d/JXqzyQflEYvm6JFfuxB4Z89jzD9EvhmcWdZRhikTnwC6IwQjabDQAQQ0sEzRwpW6eDC42EjNCa+TjDywsVKW2adRwc=',
            '_mxab_': 'config.bucket%3Dregular%3Bweb.xceleratorTags%3Denabled%3Bcheckout.cartmerge%3Ddisabled%3Btest-mobile-signup-newest%3DVariantA%3Bmobileonlylogin.recoverysetupsignup%3Dnotmandatory',
            '_pv': 'regular',
            'dp': 'd',
            'microsessid': '990',
            'lt_timeout': '1',
            'lt_session': '1',
            'bm_mi': '0564F4FA26867CF4334D703A91AE3415',
            'bc': 'true',
            '_xsrf': 'viLYFHWSa6aOQ36l1mJ394KAx4mhmt24',
            'user_session': 'rXzY0ECsT20gTqXpt9mwbg',
            'bm_sv': '9A241E5F4D3A5DD0884984C326D2D412',
            'akaas_myntra_SegmentationLabel': '1593252059~rv=58~id=5ede7a11b0e14998977c33aad71e66f8~rn=PWA'
        }

        super().__init__('https://www.myntra.com/auth/login/v1/auth/getotp', cookies, headers)

    def set_num(self, cc: int, num: int):
        if cc != 91:
            print("Myntra: international numbers not supported!")
            return
        self.data["phoneNumber"] = num

    def send(self, cc: int, num: int):
        return super().send(cc, num)
