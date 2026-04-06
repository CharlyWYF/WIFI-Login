from tkinter import font
from unittest.mock import DEFAULT

import requests
import json
import customtkinter as ctk
from threading import Thread
from plyer import notification

# 配置主题
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG_COLOR = "#0f1115"
CARD_COLOR = "#171a21"
CARD_BORDER = "#2a2f3a"
TEXT_PRIMARY = "#f5f7fb"
TEXT_SECONDARY = "#98a2b3"
ACCENT = "#416a83"
ACCENT_HOVER = "#2E405F"
DANGER = "#854371"
DANGER_HOVER = "#552d46"
ENTRY_BG = "#11141b"

DEFAULT_USER = "220408422"
DEFAULT_PSW = "xxx"


def show_message(root, title, message, color="white"):
    # """显示弹出提示框"""
    # popup = ctk.CTkToplevel(root)
    # popup.title(title)
    # popup.geometry("300x120")
    # popup.resizable(False, False)

    # # 居中显示
    # popup.transient(root)
    # popup.grab_set()

    # msg_label = ctk.CTkLabel(popup, text=message, font=("Microsoft YaHei", 20), text_color=color, wraplength=250)
    # msg_label.pack(expand=True, pady=20)

    # ok_btn = ctk.CTkButton(popup, text="确定", command=popup.destroy, width=100)
    # ok_btn.pack(pady=10)

    notification.notify(
        title=title,
        message=message,
        app_name='SUT Wifi',
        timeout=1  # 通知显示秒数
    )


def login(root, username, password):
    """执行登录操作"""
    url = 'http://10.91.200.211/ac_portal/login.php'
    payload = {
        'opr': 'pwdLogin',
        'userName': username,
        'pwd': password
    }


    try:
        with requests.Session() as s:
            p = s.post(url, data=payload, timeout=10)
            data = json.loads(p.text)
            if 'msg' in data:
                data['msg'] = data['msg'].encode('latin-1').decode('utf-8')
            print(data)
            if data['success']:
                show_message(root, "成功", "✓ 登录成功!", "green")
            else:
                show_message(root, "失败", data['msg'], "red")
    except Exception as e:
        show_message(root, "错误", f"✗ 错误: {str(e)}", "red")


def logout(root):
    """执行登出操作"""
    url = 'http://v.sut.edu.cn/homepage/logout'

    try:
        with requests.Session() as s:
            p = s.get(url, timeout=10)
            data = json.loads(p.text)
            if 'msg' in data:
                data['msg'] = data['msg']
            print(data)
            if data['msg']=='success':
                show_message(root, "成功", "✓ 登出成功!", "green")
            else:
                show_message(root, "失败", data['msg'], "red")
    except Exception as e:
        show_message(root, "错误", f"✗ 错误: {str(e)}", "red")


def main():
    app = ctk.CTk()
    app.title("SUT Wifi 登录")
    app.geometry("460x550")
    app.iconbitmap("app.ico")
    app.resizable(False, False)
    app.configure(fg_color=BG_COLOR)

    header_font = ctk.CTkFont(family="Microsoft YaHei", size=32, weight="bold")
    subtitle_font = ctk.CTkFont(family="Microsoft YaHei", size=14)
    section_font = ctk.CTkFont(family="Microsoft YaHei", size=15)
    entry_font = ctk.CTkFont(family="Microsoft YaHei", size=15)
    button_font = ctk.CTkFont(family="Microsoft YaHei", size=15, weight="bold")

    outer_frame = ctk.CTkFrame(app, fg_color="transparent")
    outer_frame.pack(fill="both", expand=True, padx=30, pady=28)

    brand_label = ctk.CTkLabel(
        outer_frame,
        text="SUT Wifi",
        font=header_font,
        text_color=TEXT_PRIMARY,
    )
    brand_label.pack(anchor="w", pady=(0, 8))

    badge = ctk.CTkLabel(
        outer_frame,
        text="校园网认证",
        width=92,
        height=30,
        corner_radius=15,
        fg_color="#222734",
        text_color="#cdd6e5",
        font=section_font,
    )
    badge.pack(anchor="w", pady=(0, 18))

    card = ctk.CTkFrame(
        outer_frame,
        corner_radius=26,
        fg_color=CARD_COLOR,
        border_width=2,
        border_color=CARD_BORDER,
    )
    card.pack(fill="both", expand=True)

    card_inner = ctk.CTkFrame(card, fg_color="transparent")
    card_inner.pack(fill="both", expand=True, padx=26, pady=26)

    username_label = ctk.CTkLabel(card_inner, text="账号", font=section_font, text_color="#d5d9e3")
    username_label.pack(anchor="w", pady=(0, 8))

    username_entry = ctk.CTkEntry(
        card_inner,
        placeholder_text="请输入用户名",
        width=360,
        height=52,
        corner_radius=16,
        border_width=2,
        border_color=CARD_BORDER,
        fg_color=ENTRY_BG,
        text_color=TEXT_PRIMARY,
        placeholder_text_color="#6f7787",
        font=entry_font,
    )
    username_entry.pack(fill="x", pady=(0, 18))
    username_entry.insert(0, DEFAULT_USER)

    password_label = ctk.CTkLabel(card_inner, text="密码", font=section_font, text_color="#d5d9e3")
    password_label.pack(anchor="w", pady=(0, 8))

    password_entry = ctk.CTkEntry(
        card_inner,
        placeholder_text="请输入密码",
        show="*",
        width=360,
        height=52,
        corner_radius=16,
        border_width=2,
        border_color=CARD_BORDER,
        fg_color=ENTRY_BG,
        text_color=TEXT_PRIMARY,
        placeholder_text_color="#6f7787",
        font=entry_font,
    )
    password_entry.insert(0, DEFAULT_PSW)
    password_entry.pack(fill="x", pady=(0, 24))

    # 登录按钮
    def on_login():
        username = username_entry.get()
        password = password_entry.get()
        if not username or not password:
            show_message(app, "提示", "请输入用户名和密码", "orange")
            return
        # 在新线程中执行登录，避免界面卡顿
        Thread(target=login, args=(app, username, password), daemon=True).start()

    login_btn = ctk.CTkButton(
        card_inner,
        text="登 录",
        command=on_login,
        height=50,
        corner_radius=16,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        text_color="#ffffff",
        font=button_font,
    )
    login_btn.pack(fill="x", pady=(0, 14))

    logout_btn = ctk.CTkButton(
        card_inner,
        text="登 出",
        command=lambda: Thread(target=logout, args=(app,), daemon=True).start(),
        height=50,
        corner_radius=16,
        fg_color=DANGER,
        hover_color=DANGER_HOVER,
        text_color="#ffffff",
        font=button_font,
    )
    logout_btn.pack(fill="x")

    app.mainloop()


if __name__ == "__main__":
    main()
