import os
from getpass import getpass, getuser
from typing import Tuple


def export_auth(login_file, login, password):
    with open(login_file, "w") as file:
        file.write(login + "\n")
        file.write(password + "\n")


def import_auth(login_file):
    with open(login_file, "r") as file:
        login, password, *_ = file.readlines()
    return login.strip(), password.strip()


def ask_auth():
    default_login = getuser()
    login = input("Please input your login [default:{}] : ".format(default_login)) or default_login
    password = getpass("Please input your password : ")
    return login, password


def persist_auth(key: str, login_password: Tuple[str, str]):
    login_file = os.path.expanduser("~/{}.auth.txt".format(key))
    if login_password:
        login, password = login_password
        export_auth(login_file, login, password)
        return login, password
    elif os.path.isfile(login_file):
        return import_auth(login_file)
    else:
        login, password = ask_auth()
        export_auth(login_file, login, password)
        return login, password
