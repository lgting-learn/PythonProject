@echo off
call activate
c:
call conda activate base
python D:\PythonProject\UIautomation\atstudy\test_run\run.py %*
pause