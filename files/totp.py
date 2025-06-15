#!/usr/bin/env python3

import pyotp

token=pyotp.random_base32()
totp=pyotp.TOTP(token)
print("Secret:", token)
print("Current OTP:", totp.now())
