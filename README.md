<h1>
  <img src="https://arcaptcha.ir/_nuxt/023053fecdcdf20e40bdc993c754d487.svg" width="80" />
  Arcaptcha
  
  <!-- Badges -->
  <a href="https://github.com/evokelektrique/arcaptcha-python/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/github/license/evokelektrique/arcaptcha-python?color=blue&style=flat-square">
  </a>
  <a href="https://pypi.org/project/arcaptcha-python/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/arcaptcha-python?style=flat-square">
  </a>
</h1>

Validate and display captcha from Arcaptcha easily in Python. ([PyPI](https://pypi.org/project/arcaptcha-python/))

## Installation
Install using pip:

`pip install arcaptcha-python`

Install manually:

```bash
git clone git@github.com:arcaptcha/arcaptcha-python.git

cd arcaptcha-python

sudo python setup.py install
```

## Usage
Before doing anything, please read the [documentation](https://docs.arcaptcha.ir/).

```python
>>> from arcaptcha_python import Arcaptcha
>>> # Create a new instance of Captcha object
>>> captcha = Arcaptcha.Captcha(site_key = "my_site_key", secret_key = "my_secret_key")
>>> # Verify challenge
>>> captcha.verify(challenge_id = "example_challenge_id")
True
>>> # Display API script tag
>>> captcha.display_tag()
"<script src='https://widget.arcaptcha.co/2/api.js' async defer></script>"
>>> # Display captcha HTML tag
>>> captcha.displayCaptcha()
'<div class="arcaptcha" data-site-key="my_site_key" data-size="normal" data-theme="light" data-lang="fa"></div>'
```

---


### Functions

You can use the following functions with `captcha`:
| Function              | Parameters                                                      | Description                                      |
|-----------------------|-----------------------------------------------------------------|--------------------------------------------------|
| display_tag()         |                                                                 | Display ARCaptcha javascript resource HTML code. |
| displayWithColor()    | color \| Required                                               | Display captcha HTML code with color             |
| displayWithLang()     | lang \| Optional(default: fa)                                   | Display captcha HTML code with language          |
| displayWithTheme()    | theme \| Optional(default: light)                               | Display captcha HTML code with theme             |
| displayWithCallBack() | callback \| Required                                            | Display captcha HTML code with callback          |
| displayWithSize()     | size \| Optional(default: normal)                               | Display captcha HTML code with size              |
| displayCaptcha()      | size, callback(default: None), theme, color(default: None),lang | Display captcha HTML code with all parameter.    |