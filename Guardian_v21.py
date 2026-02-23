import time
import datetime
import ctypes
import os
import sys
import threading
import requests
import json
import tkinter as tk
from tkinter import simpledialog
import subprocess

# 快速关机机制 (V21.0)
FORBIDDEN_START_TIME = None  # 记录进入禁止状态的时间
FORBIDDEN_TIMEOUT = 60  # 60秒后强制关机


# =========================================================
# 🔐 V21.0 简单加密模块
# =========================================================
import secrets

def simple_encrypt(text):
    """简单的XOR加密"""
    key = secrets.token_bytes(32)  # 生成随机密钥
    key_bytes = key
    text_bytes = text.encode('utf-8')
    
    # 生成加密后的数据: key + ciphertext
    encrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text_bytes)])
    
    # 将key和密文组合并base64编码
    combined = key + encrypted
    return base64.b64encode(combined).decode('utf-8')

def simple_decrypt(encrypted_text):
    """解密"""
    combined = base64.b64decode(encrypted_text.encode('utf-8'))
    key = combined[:32]  # 前32字节是密钥
    ciphertext = combined[32:]  # 剩余的是密文
    
    # XOR解密
    decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(ciphertext)])
    return decrypted.decode('utf-8')

from queue import Queue
import sqlite3  # V21.0：数据库支持

import logging
from logging.handlers import RotatingFileHandler

# =========================================================
# 📝 依赖与配置 (V18.0)
# =========================================================
def install_dependencies():
    libs = ['ntplib', 'Pillow', 'requests']
    for lib in libs:
        try:
            __import__(lib.split('>')[0].split('=')[0])
        except ImportError:
            print(f"检测到缺少 {lib} 库，正在尝试自动安装...")
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', lib], check=True)
                print(f"{lib} 安装成功！")
            except Exception as e:
                print(f"自动安装 {lib} 失败: {e}")

install_dependencies()

try:
    import ntplib
    from PIL import ImageGrab
    from datetime import timezone, timedelta
except ImportError as e:
    print(f"关键库导入失败: {e}，程序可能无法正常运行。")
    sys.exit(1)

# =========================================================
# ✨ V18.0 专业日志与路径系统 ✨
# =========================================================
# 使用 ProgramData 作为公共“根据地”，解决SYSTEM权限问题
CONFIG_DIR = os.path.join(os.environ['PROGRAMDATA'], "Guardian")
LOG_FILE = os.path.join(CONFIG_DIR, "guardian.log")
CACHE_FILE = os.path.join(CONFIG_DIR, "cached_config.json")
os.makedirs(CONFIG_DIR, exist_ok=True)

# 创建一个专业的、带滚动的日志记录器
logger = logging.getLogger("GuardianLogger")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_FILE, maxBytes=1*1024*1024, backupCount=5, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def write_log(message, level="INFO"):
    """使用专业的日志系统记录日志"""
    level = level.upper()
    if level == "INFO":
        logger.info(message)
    elif level == "WARN":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "FATAL":
        logger.critical(message)
    else:
        logger.debug(message)

REMOTE_URLS = {
    "config": "http://47.109.61.116:86/apk/configpc.json",
    "heartbeat": "http://47.109.61.116:86/heartbeat",
    "log_upload": "http://47.109.61.116:86/upload_log",
    "screenshot_upload": "http://47.109.61.116:86/upload_screenshot",
    "ack": "http://47.109.61.116:86/ack_command"
}

# =========================================================
# 💖 内置时间表 & 密码 (V18.0)
# =========================================================
DEFAULT_TIME_SCHEDULE = {
    "0": [[9, 0, 11, 0], [14, 0, 17, 0], [19, 30, 21, 0]],
    "1": [[9, 0, 11, 0], [14, 0, 17, 0], [19, 30, 21, 0]],
    "2": [[9, 0, 11, 0], [14, 0, 17, 0], [19, 30, 21, 0]],
    "3": [[9, 0, 11, 0], [14, 0, 17, 0], [19, 30, 21, 0]],
    "4": [[9, 0, 11, 0], [14, 0, 17, 0], [19, 30, 21, 0]],
    "5": [[9, 0, 22, 0]],
    "6": [[9, 0, 22, 0]]
}
DEFAULT_SUPER_PASSWORD = "WanerLovesGege520"
REMINDER_SENT = False
IS_RUNNING = True

# =========================================================
# ✨ V18.0 核心功能模块 (终极毕业版) ✨
# =========================================================
class PasswordDialog(tk.Toplevel):
    def __init__(self, parent, title, prompt, timeout):
        super().__init__(parent)
        self.transient(parent)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.prompt_label = tk.Label(self, text=prompt, padx=20, pady=10)
        self.prompt_label.pack()
        self.entry = tk.Entry(self, show="*")
        self.entry.pack(padx=20, pady=5)
        self.entry.focus_set()
        self.ok_button = tk.Button(self, text="确认", command=self.on_ok)
        self.ok_button.pack(pady=10)
        self.result = None
        self.timeout = timeout
        self.parent = parent
        self.center_window()
        self.after(timeout * 1000, self.on_timeout)

    def on_ok(self, event=None):
        self.result = self.entry.get()
        self.destroy()

    def on_close(self):
        self.result = "closed"
        self.destroy()

    def on_timeout(self):
        if self.winfo_exists():
            self.result = "timeout"
            self.destroy()
    
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def get_result(self):
        self.parent.wait_window(self)
        return self.result

def ask_password_securely(title, prompt, timeout=180):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    dialog = PasswordDialog(root, title, prompt, timeout)
    result = dialog.get_result()
    try:
        root.destroy()
    except tk.TclError:
        pass
    return result

def show_msg(title, text, style=0):
    def msg_thread():
        ctypes.windll.user32.MessageBoxW(0, text, title, style | 0x40000)
    threading.Thread(target=msg_thread).start()

def trigger_shutdown_task():
    write_log("正在请求执行关机任务...")
    try:
        subprocess.run(['schtasks', '/run', '/tn', 'GuardianShutdownTask'], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        write_log(f"触发关机任务失败: {e}", "ERROR")
        os.system("shutdown -s -t 60 -c '触发任务失败，尝试直接关机！'")

def get_network_time():
    """获取网络时间 (V18.0 国内高速版)"""
    ntp_servers = [
        'ntp.aliyun.com', 'ntp.tencent.com', 'time1.cloud.tencent.com', 
        'cn.pool.ntp.org', 'ntp.tuna.tsinghua.edu.cn', 'ntp.sjtu.edu.cn'
    ]
    for server in ntp_servers:
        try:
            client = ntplib.NTPClient()
            response = client.request(server, version=3, timeout=3)
            return datetime.datetime.fromtimestamp(response.tx_time, timezone.utc).astimezone(timezone(timedelta(hours=8)))
        except Exception as e:
            write_log(f"从NTP服务器 {server} 获取时间失败: {e}", "WARN")
    
    write_log("所有NTP服务器均无法连接，将使用本地系统时间。", "ERROR")
    return datetime.datetime.now()


def check_reminders(end_time, schedule):
    """检查并触发提醒"""
    global REMINDER_SENT_5MIN, REMINDER_SENT_1MIN
    try:
        now = get_network_time()
        if end_time and end_time > now:
            remaining_minutes = (end_time - now).total_seconds() / 60
            if remaining_minutes > 10:
                REMINDER_SENT_5MIN = False
                REMINDER_SENT_1MIN = False
            if 4.8 <= remaining_minutes <= 5.0 and not REMINDER_SENT_5MIN:
                show_msg("⏰ 温馨提醒", "还有5分钟就要结束辣，快保存好你的作品！")
                write_log("[提醒] 已发送5分钟倒计时提醒")
                REMINDER_SENT_5MIN = True
            elif 0.8 <= remaining_minutes <= 1.0 and not REMINDER_SENT_1MIN:
                show_msg("⏰ 最后1分钟倒计时辣，时间到辣～")
                write_log("[提醒] 已发送1分钟倒计时提醒")
                REMINDER_SENT_1MIN = True
    except Exception as e:
        write_log(f"提醒失败: {e}", "ERROR")

def init_violation_db():
    """初始化违规日志数据库"""
    try:
        conn = sqlite3.connect(STATS_DB_FILE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS violations (id INTEGER PRIMARY KEY, timestamp TEXT, date TEXT, time TEXT, violation_type TEXT, details TEXT)")
        conn.commit()
        conn.close()
        write_log("违规日志数据库初始化完成")
    except Exception as e:
        write_log(f"初始化违规日志数据库失败: {e}", "ERROR")

def log_violation(timestamp, violation_type, details=""):
    """记录违规事件"""
    try:
        conn = sqlite3.connect(STATS_DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO violations (timestamp, date, time, violation_type, details) VALUES (?, ?, ?, ?, ?)",
                      (timestamp.strftime('%Y-%m-%d %H:%M:%S'), timestamp.strftime('%Y-%m-%d'), timestamp.strftime('%H:%M:%S'), violation_type, details))
        conn.commit()
        conn.close()
        write_log(f"[违规日志] 已记录: {violation_type}")
    except Exception as e:
        write_log(f"记录违规失败: {e}", "ERROR")

def init_stats_db():
    """初始化统计数据库"""
    try:
        conn = sqlite3.connect(STATS_DB_FILE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS daily_usage (id INTEGER PRIMARY KEY, date TEXT, mode TEXT, total_duration INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS session_log (id INTEGER PRIMARY KEY, session_start TEXT, mode TEXT, date TEXT, duration INTEGER)")
        conn.commit()
        conn.close()
        write_log("统计数据库初始化完成")
    except Exception as e:
        write_log(f"初始化统计数据库失败: {e}", "ERROR")

def record_session_start(now, mode):
    """记录会话开始"""
    try:
        conn = sqlite3.connect(STATS_DB_FILE)
        cursor = conn.cursor()
        date_str = now.strftime('%Y-%m-%d')
        cursor.execute("SELECT total_duration FROM daily_usage WHERE date=? AND mode=?", (date_str, mode))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE daily_usage SET total_duration=? WHERE date=? AND mode=?", (result[0], date_str, mode))
        else:
            cursor.execute("INSERT INTO daily_usage (date, mode, total_duration) VALUES (?, ?, 0)", (date_str, mode))
        conn.commit()
        conn.close()
    except Exception as e:
        write_log(f"记录会话开始失败: {e}", "ERROR")

def record_session_end(now, mode, duration):
    """记录会话结束"""
    try:
        pass
    except Exception as e:
        pass

def init_screenshot_dir():
    """初始化截图目录"""
    try:
        if not os.path.exists(SCREENSHOT_DIR):
            os.makedirs(SCREENSHOT_DIR)
    except:
        pass

def take_screenshot_auto():
    """自动截图"""
    try:
        screenshot = ImageGrab.grab()
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"screen_{timestamp}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        screenshot.save(filepath)
        write_log(f"[监控] 自动截图: {filename}")
        write_logs = ("[监控] 截图已上传")
        os.remove(filepath)
    except Exception as e:
        write_log(f"自动截图失败: {e}", "ERROR")

def init_bonus_file():
# =========================================================
# 🎁 V21.0 每周五记录函数
# =========================================================
def record_on_time_completion(mode):
    """记录按时完成使用"""
    try:
        with open(BONUS_TIME_FILE, 'r', 'utf-8') as f:
            data = json.load(f)
        
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        tasks = data.get("weekly_completion_tasks", {})
        on_time_list = tasks.get("on_time_completion", [])
        
        # 只记录今日一次，避免重复
        if today not in on_time_list:
            on_time_list.append(today)
            tasks["on_time_completion"] = on_time_list
            data["weekly_completion_tasks"] = tasks
            
            with open(BONUS_TIME_FILE, 'w', 'utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
            
            write_log(f"[奖励] 记录按时完成：{today} ({mode})")
        else:
            write_log(f"[奖励] 今日已记录过按时完成：{today}")
            
    except Exception as e:
        write_log(f"记录按时完成失败: {e}", "ERROR")

def get_bonus_status():
    """获取当前奖励状态"""
    try:
        with open(BONUS_TIME_FILE, 'r', 'utf-8') as f:
            data = json.load(f)
        
        return {
            "当前可用奖励时间(分钟)": data.get("weekly_bonus_minutes", 0),
            "本周累计获得(分钟)": data.get("total_earned_minutes", 0),
            "每周上限(分钟)": data.get("max_bonus_minutes", 60),
            "上次奖励日期": data.get("last_earn_date", "未获得过"),
            "本周完成次数": len(data.get("weekly_completion_tasks", {}).get("on_time_completion", []))
        }
    except:
        return {"错误": "无法读取奖励状态"}



    """初始化奖励文件"""
    try:
        if not os.path.exists(BONUS_TIME_FILE):
            import json
            with open(BONUS_TIME_FILE, 'w', encoding='utf-8') as f:
                # 初始化奖励配置
                json.dump({
                    "weekly_bonus_minutes": 0,          # 当前可用奖励时间
                    "max_bonus_minutes": 60,            # 每周最大奖励限制（60分钟=1小时）
                    "total_earned_minutes": 0,          # 累计获得奖励总时长
                    "last_week_check_date": "",         # 上次检查日期
                    "last_earn_date": "",               # 上次获得奖励日期
                    "weekly_completion_tasks": {}       # 每周完成任务记录
                }, f)
            write_log("奖励配置文件已初始化：每周最大奖励60分钟")
    except Exception as e:
        write_log(f"初始化奖励文件失败: {e}", "ERROR")

def lock_system_time():
    """锁定系统时间"""
    try:
        import wmi
        c = wmi.WMI()
        write_log("系统时间锁定机制已启动")
    except Exception as e:
        write_log(f"锁定系统时间失败: {e}", "WARN")
\ndef check_time(schedule):
    """根据传入的【白名单】时间表检查当前状态 (V21.0 人性化显示版)"""
    global REMINDER_SENT
    if not schedule:
        write_log("白名单时间表为空，默认禁止。", "WARN")
        return "FORBIDDEN", 0

    now = get_network_time()
    weekday_index = str(now.weekday()) # "0" for Monday, "6" for Sunday.
    current_time = now.time()

    # ======================================================
    # ====== 新增：把数字星期，翻译成“人话”！ ======
    # ======================================================
    weekday_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    human_weekday = weekday_map[int(weekday_index)]

    # 在日志里，同时显示“人话”和程序看的“索引”，方便我们对照
    write_log(f"[check_time] 白名单裁决：当前 {human_weekday} (索引 {weekday_index}), 时间 {current_time.strftime('%H:%M:%S')}")

    if weekday_index not in schedule:
        write_log(f"[check_time] 裁决：今天({human_weekday})不在白名单中，禁止使用。")
        return "FORBIDDEN", 0

    for (sh, sm, eh, em) in schedule[weekday_index]:
        try:
            start = datetime.time(sh, sm)
            end = datetime.time(eh, em)

            if start <= current_time < end:
                write_log(f"[check_time] 裁决：命中白名单时段 {start}-{end}，允许使用！")
                
                now_naive = datetime.datetime.combine(datetime.date.today(), now.time())
                end_dt = datetime.datetime.combine(datetime.date.today(), end)
                remaining_minutes = (end_dt - now_naive).total_seconds() / 60

                if 0 < remaining_minutes <= 10 and not REMINDER_SENT:
                    show_msg("💖 婉儿的温馨提示", f"还有 {int(remaining_minutes)} 分钟就要结束啦！", 0x30)
                    REMINDER_SENT = True
                if remaining_minutes > 10:
                    REMINDER_SENT = False

                return "ALLOWED", remaining_minutes
        except Exception as e:
            write_log(f"[check_time] 解析白名单规则时出错: {e}", "ERROR")
            continue
    
    write_log("[check_time] 裁决：未命中任何白名单时段，禁止使用！")
    return "FORBIDDEN", 0

def load_config_from_cloud():
    """从云端加载配置，并暴力破解缓存"""
    try:
        url = f"{REMOTE_URLS['config']}?_t={int(time.time())}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError as e:
                write_log(f"云端响应内容非JSON格式: {e}", "ERROR")
                write_log(f"响应内容: {response.text[:200]}", "ERROR")
                return None
        else:
            write_log(f"云端响应状态码异常: {response.status_code}", "WARN")
            return None
    except Exception as e:
        write_log(f"从云端加载配置失败: {e}", "ERROR")
        return None

def ack_command(command_type):
    try:
        requests.post(REMOTE_URLS["ack"], json={"command_type": command_type}, timeout=5)
        write_log(f"已发送 {command_type} 的执行回执。")
    except Exception as e:
        write_log(f"发送指令回执失败: {e}", "WARN")

def send_heartbeat():
    try:
        requests.get(REMOTE_URLS["heartbeat"], params={"device": "kids_pc"}, timeout=5)
        write_log("心跳发送成功。")
    except Exception as e:
        write_log(f"心跳发送失败: {e}", "WARN")

def upload_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log_content = f.read()
        requests.post(REMOTE_URLS["log_upload"], data=log_content.encode('utf-8'), headers={'Content-Type': 'text/plain'}, timeout=15)
        write_log("日志上传成功。")
    except Exception as e:
        write_log(f"日志上传失败: {e}", "ERROR")

def take_and_upload_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot_path = os.path.join(CONFIG_DIR, "screenshot.png")
        screenshot.save(screenshot_path)
        
        with open(screenshot_path, "rb") as f:
            files = {'screenshot': (os.path.basename(screenshot_path), f, 'image/png')}
            requests.post(REMOTE_URLS["screenshot_upload"], files=files, timeout=30)
        
        os.remove(screenshot_path)
        write_log("截图上传成功。")
    except Exception as e:
        write_log(f"截图上传失败: {e}", "ERROR")

# =========================================================
# 🚀 V18.0 主程序循环 (终极毕业版 - 绝对防卡死) 🚀
# =========================================================
def run_guardian():
    global IS_RUNNING
    write_log("凤凰守护者 V18.0 (终极毕业版) 启动！")
    
    # --- 启动时的三级灾备加载逻辑 ---
    config = load_config_from_cloud()
    if not config:
        write_log("云端加载失败，尝试从本地缓存加载...", "WARN")
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
            write_log("成功从本地缓存加载配置。")
        except Exception as e:
            write_log(f"本地缓存加载失败: {e}，将使用内置配置。", "ERROR")
            config = {}
    
    time_schedule = config.get("time_schedule") or DEFAULT_TIME_SCHEDULE
    super_password = config.get("super_password") or DEFAULT_SUPER_PASSWORD
    
    send_heartbeat()
    
    temp_unlock_until = None
    last_heartbeat_time = time.time()
    last_cloud_read_time = time.time()

    try:
        while IS_RUNNING:
            try:
                # --- 小时级更新逻辑 ---
                if time.time() - last_cloud_read_time > 3600:
                    write_log("已超过1小时，开始尝试更新云端配置...")
                    current_config = load_config_from_cloud()
                    if current_config:
                        time_schedule = current_config.get("time_schedule") or time_schedule
                        super_password = current_config.get("super_password") or super_password
                        last_cloud_read_time = time.time()
                        write_log("云端配置更新成功！")
                        try:
                            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                                json.dump(current_config, f, ensure_ascii=False, indent=4)
                            write_log("新配置已写入缓存。")
                        except Exception as e:
                            write_log(f"新配置写入缓存失败: {e}", "ERROR")
                        
                        command = current_config.get("remote_command")
                        if command:
                            write_log(f"接收到远程指令: {command}")
                            if command == "UNLOCK_1_HOUR":
                                temp_unlock_until = get_network_time() + timedelta(hours=1)
                            elif command == "SHUTDOWN_NOW":
                                trigger_shutdown_task()
                                IS_RUNNING = False
                                continue
                            elif command == "UPLOAD_LOG":
                                upload_log()
                            elif command == "TAKE_SCREENSHOT":
                                take_and_upload_screenshot()
                            ack_command("remote_command")

                        message = current_config.get("message_to_show")
                        if message:
                            show_msg("来自哥哥的远程消息", message)
                            ack_command("message_to_show")
                    else:
                        write_log("本次云端更新失败，将在一小时后重试。", "WARN")
                        last_cloud_read_time = time.time()

                # --- 每分钟的常规检查 ---
                if time.time() - last_heartbeat_time > 900:
                    send_heartbeat()
                    last_heartbeat_time = time.time()

                if temp_unlock_until and get_network_time() < temp_unlock_until:
                    time.sleep(60)
                    continue

                schedule = time_schedule\n            if CURRENT_MODE == "学习模式":\n                schedule = MODE_CONFIGS.get("学习模式", time_schedule)\n            status, _ = check_time(schedule)
                if status == "FORBIDDEN":
                    result_queue = Queue()
                    def ask_password_in_thread():
                        user_input = ask_password_securely("🚨 访问受限 🚨", 
                                                           "已进入休息时段，请在3分钟内输入密码解锁：", 
                                                           timeout=180)
                        result_queue.put(user_input)

                    password_thread = threading.Thread(target=ask_password_in_thread)
                    password_thread.daemon = True
                    password_thread.start()

                    try:
                        user_input_result = result_queue.get(timeout=180)
                    except:
                        user_input_result = "timeout"

                    if user_input_result == super_password:
                        temp_unlock_until = get_network_time() + timedelta(hours=1)
                        show_msg("✅ 解锁成功", "已为您临时解锁1小时！")
                        # 解锁成功后重置禁止时间
                        FORBIDDEN_START_TIME = None
                        continue
                    else:
                        write_log(f"密码输入错误或超时 ({user_input_result})，执行关机。", "WARN")
                        trigger_shutdown_task()
                        IS_RUNNING = False
                        continue
                else:
                    time.sleep(60)
                    
            except Exception as e:
                write_log(f"主循环发生致命错误: {e}", "FATAL")
                import traceback
                write_log(traceback.format_exc(), "FATAL")
                time.sleep(30)
    finally:
        write_log("守护者主循环退出。", "INFO")


if __name__ == "__main__":
    try:
        mutex = ctypes.windll.kernel32.CreateMutexW(None, True, "GuardianPhoenixMutex")
        if ctypes.windll.kernel32.GetLastError() == 183:
            write_log("检测到已有守护者实例在运行，本次启动将退出。", "WARN")
            sys.exit(0)
        
        run_guardian()
    finally:
        if 'mutex' in locals():
            ctypes.windll.kernel32.ReleaseMutex(mutex)