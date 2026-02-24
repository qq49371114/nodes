
# Guardian V21.0 打包成 EXE 完整步骤

## 1. 安装依赖

```bash
pip install ntplib Pillow requests wmi pyinstaller
```

或者逐个安装：

```bash
pip install ntplib      # NTP时间同步
pip install Pillow      # 截图功能 ( PIL 模块 )
pip install requests    # HTTP请求
pip install wmi         # Windows系统管理
pip install pyinstaller # 打包工具
```

## 2. 准备文件

将以下文件放在同一目录：
- Guardian_v21.py       # 主程序
- Guardian_v21.spec     # 打包配置（可自动生成）

## 3. 打包命令

### 方法1: 使用 spec 文件打包（推荐）

```bash
pyinstaller Guardian_v21.spec
```

### 方法2: 直接命令行打包

```bash
pyinstaller --onefile --windowed --hidden-import=ntplib --hidden-import=PIL --hidden-import=requests --hidden-import=wmi --hidden-import=sqlite3 --name Guardian_V21 Guardian_v21.py
```

### 方法3: 使用 bat 脚本

双击运行 build_github_v21.bat

## 4. 打包参数说明

| 参数 | 说明 |
|------|------|
| `--onefile` | 打包成单个 exe 文件 |
| `--windowed` | 不显示控制台窗口（GUI模式） |
| `--hidden-import` | 隐式导入的模块 |
| `--name` | 输出的 exe 文件名 |

## 5. 生成文件位置

打包完成后，exe文件位于：
```
dist/Guardian_V21.exe
```

## 6. 注意事项

1. **管理员权限运行**：
   - V21.0 需要 WMI 权限锁定系统时间
   - exe 文件需以管理员身份运行
   - 可以在 exe 右键属性中设置为"以管理员身份运行"

2. **防病毒软件**：
   - 某些杀毒软件可能误报
   - 这是 pyInstaller 打包的常见问题
   - 如果被拦截，需要添加信任白名单

3. **首次运行**：
   - 程序会自动创建必要的目录和文件
   - 位于: C:\ProgramData\Guardian\

4. **依赖完整性**：
   - 确保 Python 3.7+ 已安装
   - 确保所有依赖已正确安装

## 7. 常见问题

### Q: 打包失败，提示缺少模块
A: 先用 pip 安装所需模块，再重新打包

### Q: exe 运行提示缺少 dll
A: 使用 --onefile --windowed 参数，确保所有依赖都打包进去

### Q: 杀毒软件拦截
A: 这是 pyInstaller 打包的误报，添加白名单即可

### Q: exe 文件过大
A: 正常现象，包含 Python 运行时和所有依赖库

## 8. 高级配置（可选）

### 添加程序图标

1. 准备 .ico 图标文件
2. 在 spec 文件中设置：
   icon='guardian.ico'

### 优化 exe 文件大小

使用 UPX 压缩（已默认启用）：

```bash
pyinstaller --upx --onefile Guardian_v21.spec
```

### 添加版本信息

创建 version.txt 文件，然后在 spec 中引用。

## 9. 打包后测试清单

- [ ] exe 文件可以正常启动
- [ ] 时间控制功能正常
- [ ] NTP 时间同步正常
- [ ] 密码解锁功能正常
- [ ] 奖励弹窗显示正常
- [ ] 截图上传功能正常
- [ ] 数据库和日志正常创建
