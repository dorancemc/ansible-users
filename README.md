# Ansible role users

Role to manage local Linux users including SSH keys and TOTP

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Role Variables

See [defaults/main.yml](defaults/main.yml) for possible variables.

## Password Management

Generate a new password with the command below. 

```bash
$ openssl passwd -6
Password:
Verifying - Password:
$6$g.9KhoXXg4ewIcwH$mvyGFgpNeYt4QjgFJw7LSZfEfWxSFoKfMtHDmgXbQkKPs.t2L0KUGJG15cwnjtwNR.1CegkL7cVWRwcb9xG/E.
```

## Creating totp token

Create a python virtual env, install the requirements
```bash
python3 -m venv .venv
. .venv/bin/activate  
pip3 install -r files/requirements.txt
```
Run the command `files/totp.py` to create a TOTP token, 
copy it to a secure place.
