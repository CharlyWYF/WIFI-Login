# SUT Wifi 登录工具

一个简单易用的校园网认证登录工具，提供便捷的网络认证体验。

## 📋 功能特性

- ✅ 校园网登录/登出功能
- ✅ 图形化用户界面
- ✅ 系统通知提示
- ✅ 支持自定义默认用户名和密码
- ✅ 多线程操作，避免界面卡顿
- ✅ 深色主题，美观易用

## 🛠️ 技术栈

- **Python 3.x**
- **Tkinter** - 基础 GUI 库
- **CustomTkinter** - 现代化 UI 组件
- **Requests** - 网络请求
- **Plyer** - 系统通知

## 📦 安装说明

### 从源码运行

1. 克隆或下载本项目
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行主脚本：
   ```bash
   python WebLogin.py
   ```


## ⚙️ 配置

### 默认用户名和密码

在 `default_psw.py` 文件中设置默认值：

```python
DEFAULT_USER = "你的用户名"
DEFAULT_PSW = "你的密码"
```

## 📦 打包指南

使用 PyInstaller 打包项目为可执行文件：

1. 安装 PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 执行打包命令：
   ```bash
   pyinstaller --onefile --windowed --icon=app.ico --name="SUT-WIFI" --hidden-import plyer.platforms.win.notification WebLogin.py
   ```

   命令说明：
   - `--onefile`：生成单个可执行文件
   - `--windowed`：无控制台窗口（GUI 程序）
   - `--icon=app.ico`：设置应用图标
   - `--name="SUT-WIFI"`：设置可执行文件名称
   - `--hidden-import plyer.platforms.win.notification`：确保 Windows 平台的通知功能正常工作

3. 打包完成后，可执行文件会生成在 `dist` 目录中


## 📁 项目结构

```
weblogin/
├── WebLogin13.py        # 主脚本
├── default_psw.py        # 默认账号配置
├── requirements.txt      # 依赖项
├── app.ico              # 应用图标
├── dist/                # 打包输出目录
│   └── SUT-WIFI.exe     # 可执行文件
└── README.md            # 项目说明
```

## 📥 依赖项

- requests
- customtkinter
- plyer

