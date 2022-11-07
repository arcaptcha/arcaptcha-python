import logging
import unittest

from arcaptcha_python import Arcaptcha

class TestArcaptchaModule(unittest.TestCase):

  def setUp(self):
    # Changing log level to DEBUG
    loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)

    self.site_key = "test_site_key"
    self.secret_key = "test_secret_key"
    self.good_response = "{\"success\": true}"
    self.bad_response = "{\"status\": 404, \"message\": \"Challenge not exist\"}"
    self.captcha = Arcaptcha.Captcha(site_key=self.site_key, secret_key=self.secret_key)
    self.test_site_key = "0000000000"
    self.test_secret_key = "00000000000000000000"
    self.test_response = "000000000000000000000000000000"
    self.test_captcha = Arcaptcha.Captcha(site_key=self.test_site_key, secret_key=self.test_secret_key)

  def test_good_response(self):
    good_response = self.captcha.validate_response(self.good_response)
    self.assertTrue(good_response, "Expected True but got False")

  def test_bad_response(self):
    bad_response = self.captcha.validate_response(self.bad_response)
    self.assertFalse(bad_response, "Expected False but got True")

  def test_display_tag(self):
    script_tag = self.captcha.display_tag()
    self.assertTrue(len(script_tag) > 0)

  def test_display(self):
    captcha = self.captcha.display()
    self.assertTrue(len(captcha) > 0)

  def test_verify(self):
    verified = self.test_captcha.verify(self.test_response)
    self.assertTrue(verified, "Expected True but got Flase")
    
    verified = self.test_captcha.verify("invalid_response")
    self.assertFalse(verified, "Expected False but got True")

if __name__ == '__main__':
    unittest.main()
