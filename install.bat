@echo off
for /f "delims=" %%F in ('dir /s /b /a-d ^|findstr "requirements.txt"') do pip install -r %%F