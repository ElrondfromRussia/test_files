#from bas_agent.utils.os_platf_utils import is_windows
import platform

def is_windows():
    return platform.system().find("Windows") >= 0

if is_windows():
    import win32com.client as win32
else:
    import os
    import pyautogui


class MailSender:
    def __init__(self):
        pass

    if is_windows():
        @staticmethod
        def send_email(dest_email, subj="", msg="", file_path=None):
            try:
                outlook = win32.Dispatch('outlook.application')
                mail = outlook.CreateItem(0)
                mail.To = dest_email
                mail.Subject = subj
                mail.Body = msg
                #mail.HTMLBody = '<h2>HTML Message</h2>'
                if file_path:
                    attachment = file_path
                    mail.Attachments.Add(attachment)
                mail.Send()
            except BaseException as ex:
                print("OUTLOOK WINDOWS ERROR: ", ex)
    else:
        @staticmethod
        def send_email(dest_email, subj="", msg="", file_path=None):
            try:
                thp = "thunderbird"
                # for root, dirs, files in os.walk(r'/'):


                #     for name in files:
                #         if name == "thunderbird":
                #             thp = os.path.abspath(os.path.join(root, name))
                thunder_str = thp + " -compose to={dest},subject={subj},body={msg}"\
                                .format(dest=dest_email, subj=subj, msg=msg)
                if file_path:
                    thunder_str += ",attachment={path}".format(path=file_path)
                #thunder_str += " | "
                os.system(thunder_str)

                #os.system("xdotool search --name 'Mozilla Thunderbird' key --window %1 shift+F5")
                pass
            except BaseException as ex:
                print("EMAIL LINUX ERROR: ", ex)

import time
sender = MailSender()
sender.send_email("v.demchenko@angaratech.ru", "Test", "Test!")
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')
pyautogui.press('enter')
                os.system(thunder_str)
                pass
            except BaseException as ex:
                print("EMAIL LINUX ERROR: ", ex)


sender = MailSender()
sender.send_email("v.demchenko@angaratech.ru", "Test", "Test!")
