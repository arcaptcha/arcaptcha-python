import json
import requests

class Captcha:

    VERIFY_URL = "https://arcaptcha.co/2/siteverify"

    def __init__(self, site_key, secret_key):

        # Validate arguments
        if not site_key or not secret_key:
            raise ValueError("Arguments cannot be empty")

        # Assign arguments
        self.site_key = site_key
        self.secret_key = secret_key

    # Send HTTP request to verification API url and return the status
    def verify(self, response):
        # Validate argument
        if not response:
            raise ValueError("challenge_id cannot be empty.")

        # Validate argument type
        if not isinstance(response, str):
            raise ValueError("challenge_id must be string.")

        payload = {
          "sitekey": self.site_key,
          "secret": self.secret_key,
          "response": response
        }

        # Send POST request to api
        rsp = requests.post(self.VERIFY_URL, json=payload)
        return self.validate_response(rsp.content)



    # JSON resposne body validator
    def validate_response(self, response):
        parsed = json.loads(response)

        if "success" in parsed:
            return True

        return False



    # Captcha with color
    def displayWithColor(self, color=None):
        if color == None:
            raise ValueError("Captcha should have color")
        return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-color=\"{color}\"></div>"



    # Captcha with language
    def displayWithLang(self, lang="fa"):
        return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-lang=\"{lang}\"></div>"



    # Captcha with theme
    def displayWithTheme(self, theme="light"):
        return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-theme=\"{theme}\"></div>"



    # Captcha with callback
    def displayWithCallBack(self, callback=None):
        if callback == None:
            raise ValueError("Captcha should have callback")        
        return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-callback=\"{callback}\"></div>"



    # Captcha with size
    def displayWithSize(self, size="normal"):
        return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-size=\"{size}\"></div>"
    

    # Captcha with all configs
    def displayCaptcha(self, size="normal", callback=None, theme="light", color=None, lang="fa"):
        if callback != None and color == None:
            return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-size=\"{size}\" data-callback=\"{callback}\" data-theme=\"{theme}\" data-lang=\"{lang}\"></div>"
        elif callback == None and color != None:
            return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-size=\"{size}\" data-color=\"{color}\" data-theme=\"{theme}\" data-lang=\"{lang}\"></div>"
        elif callback != None and color != None:
            return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-size=\"{size}\" data-callback=\"{callback}\" data-color=\"{color}\" data-theme=\"{theme}\" data-lang=\"{lang}\"></div>"
        else:
            return f"<div class=\"arcaptcha\" data-site-key=\"{self.site_key}\" data-size=\"{size}\" data-theme=\"{theme}\" data-lang=\"{lang}\"></div>"



    # Print API script tag
    def display_tag(self):
        return "<script src='https://widget.arcaptcha.co/2/api.js' async defer></script>"
