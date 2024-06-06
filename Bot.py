print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
❖ › Facebook :- @ahmed.s6yed
❖ › By       :- @lemo
❖ › Xat Bot v1.0      
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                """)

print('\x1b[38;5;208m⇼'*60)
print('\x1b[38;5;22m•'*60)
print('\x1b[38;5;22m•'*60)
print('\x1b[38;5;208m⇼'*60)

import re
from playwright.sync_api import Playwright, sync_playwright, expect
import id
import time

time.sleep(2)
Xat = "https://xat.com/"
element_id = input("[+] Enter the ID: ")
name = input("[+] Enter Your Name: ")
Chat = input("[+] Enter Name Chat: ")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto((Xat)+(Chat))

    # Click On The Guest
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#idvisitors2 > div > div > div.dialogCell.cellWide.noPointer > div:nth-child(1) > p > span > span").click()
    time.sleep(3)

    # Click On The Guest To Change Name
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator(f"#idvisitors{element_id}").click()
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").frame_locator("#actionsFrame").locator("#nameedit").click()
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").frame_locator("#actionsFrame").locator("#nameedit").fill(name)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").frame_locator("#actionsFrame").locator("#act_OK").get_by_text("Save").click()
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").frame_locator("#actionsFrame").locator("#act_OK").get_by_text("Save").click()
    
    return page, context, browser

def get_message():
    message = input("Enter the message you want to send: ")
    return message

def send_message(page, message):
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").click()
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill(message)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")


with sync_playwright() as playwright:
    page, context, browser = run(playwright)
    
    while True:
        another_message = input("[+] Do you want to send message on the chat? (yes/no): ")
        if another_message.lower() != "yes":
            break

        message = get_message()
        send_message(page, message)

    # Close browser if user does not want to send more messages
    context.close()
    browser.close()

