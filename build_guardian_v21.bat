
REM Guardian V21.0 打包脚本
echo ==============================================
echo Guardian V21.0 打包工具
echo ==============================================

echo.
echo [步骤1] 安装依赖...
pip install ntplib Pillow requests wmi pyinstaller

echo.
echo [步骤2] 打包成exe...
pyinstaller Guardian_v21.spec

echo.
echo [步骤3] 完成！
echo   打包后的exe文件位于: dist\Guardian_V21.exe
echo.
 pause
