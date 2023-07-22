import tkinter as tk
import time

def update_timer():
    # 获取当前时间
    current_time = time.strftime("%H:%M:%S")
    # 更新标签文本
    timer_label.config(text=current_time)
    # 每隔一秒更新一次
    timer_label.after(1000, update_timer)

def start_timer():
    # 获取用户输入的专注时间（分钟）
    focus_time = int(entry.get())
    # 将专注时间转换为秒
    focus_time_seconds = focus_time * 60
    # 禁用开始按钮
    start_button.config(state=tk.DISABLED)
    # 设置专注结束时间
    end_time = time.time() + focus_time_seconds
    # 更新专注时间显示
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        timer_label.config(text=f"剩余时间: {remaining_time // 60:02d}:{remaining_time % 60:02d}")
        root.update()
        time.sleep(1)
    # 恢复开始按钮状态
    start_button.config(state=tk.NORMAL)
    # 提示专注时间结束
    timer_label.config(text="专注时间已结束")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 创建标签用于显示时间
timer_label = tk.Label(root, font=("Helvetica", 48))
timer_label.pack(pady=20)

# 创建输入框获取专注时间
entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(pady=10)

# 创建开始按钮
start_button = tk.Button(root, text="开始专注", font=("Helvetica", 24), command=start_timer)
start_button.pack(pady=10)

# 更新时间
update_timer()

# 启动主循环
root.mainloop()
