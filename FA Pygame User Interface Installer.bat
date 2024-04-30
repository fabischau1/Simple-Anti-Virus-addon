@echo off
setlocal enabledelayedexpansion
:start
color 0E
echo your installing FA Antivira Anti Virus Addon Version: 1.0 at Date: %date% Time: %time%
echo INFO the program you are trying to install uses pygame
echo Do you want to install this program? (Yes/No)
set /p input=
if /i %input%==Yes goto install
if /i %input%==No goto dontinstall
:install
(
echo import pygame
echo import os
echo pygame.init^(^)
echo WIDTH, HEIGHT = 800, 600
echo screen = pygame.display.set_mode^(^(WIDTH, HEIGHT^)^)
echo pygame.display.set_caption^("FA AntiVira Stardup "^)
echo WHITE = ^(42, 42, 42^)
echo BLACK = ^(100, 100, 100^)
echo font = pygame.font.Font^(None, 25^)
echo button_positions = ^[
echo     ^(100, 100^), ^(300, 100^), ^(500, 100^),
echo     ^(100, 300^), ^(300, 300^), ^(500, 300^),
echo     ^(100, 500^), ^(300, 500^), ^(500, 500^)
echo ^]
echo button_texts = ^[
echo     "URL Scan", "Passwort Generator", "Super Passwort Generator",
echo     "Scan Menu", "Open Anti Virus", "Help",
echo     "Scan For Damaged System", "Start Menu", "Kill File"
echo ^]
echo running = True
echo while running:
echo     for event in pygame.event.get^(^):
echo         if event.type == pygame.QUIT:
echo             running = False
echo         elif event.type == pygame.MOUSEBUTTONDOWN:
echo             if event.button == 1:
echo                 for i, pos in enumerate^(button_positions^):
echo                     if pygame.Rect^(pos, ^(200, 50^)^).collidepoint^(event.pos^):
echo                         if i == 0:
echo                             os.system^("start C:\\FA_Antivira\\FA_URLscan.bat"^)
echo                         elif i == 1:
echo                             os.system^("start C:\\FA_Antivira\\FAPasswordgenerator.bat"^)
echo                         elif i == 2:
echo                             os.system^("start C:\\FA_Antivira\\FASuperPassword.bat"^)
echo                         elif i == 3:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAscanmenu.py"^)
echo                         elif i == 4:
echo                             os.system^("start C:\\FA_Antivira\\FAantivirusopener.bat"^)
echo                         elif i == 5:
echo                             os.system^("start notepad C:\\FA_Antivira\\FAhelp.txt"^)
echo                         elif i == 6:
echo                             os.system^("start C:\\FA_Antivira\\FAdmgsysscan.bat"^)
echo                         elif i == 7:
echo                             os.system^("start C:\\FA_Antivira\\StardMenu.bat"^)
echo                         elif i == 8:
echo                             os.system^("start C:\\FA_Antivira\\FAmalfiledel.bat"^)
echo     screen.fill^(WHITE^)
echo     for i, pos in enumerate^(button_positions^):
echo         pygame.draw.rect^(screen, BLACK, ^(*pos, 200, 50^)^)
echo         text_surface = font.render^(button_texts[i], True, WHITE^)
echo         screen.blit^(text_surface, ^(pos^[0^] + 20, pos^[1^] + 10^)^)
echo     pygame.display.flip^(^)
echo pygame.quit^(^)
) > "C:\FA_Antivira\Python\FAMsh.py"
(
echo import pygame
echo import os
echo pygame.init^(^)
echo WIDTH, HEIGHT = 800, 600
echo screen = pygame.display.set_mode^(^(WIDTH, HEIGHT^)^)
echo pygame.display.set_caption^("FA AntiVira Stardup "^)
echo WHITE = ^(42, 42, 42^)
echo BLACK = ^(100, 100, 100^)
echo font = pygame.font.Font^(None, 25^)
echo button_positions = ^[
echo     ^(1000, 1000^), ^(300, 100^), ^(5000, 1000^),
echo     ^(100, 300^), ^(300, 300^), ^(500, 300^),
echo     ^(1000, 5000^), ^(3000, 5000^), ^(5000, 5000^)
echo ^]
echo button_texts = ^[
echo     "URL Scan", "Start Menu", "Super Passwort Generator",
echo     "Shutdown", "info", "Restart",
echo     "Scan For Damaged System", "Start Menu", "Info"
echo ^]
echo running = True
echo while running:
echo     for event in pygame.event.get^(^):
echo         if event.type == pygame.QUIT:
echo             running = False
echo         elif event.type == pygame.MOUSEBUTTONDOWN:
echo             if event.button == 1:
echo                 for i, pos in enumerate^(button_positions^):
echo                     if pygame.Rect^(pos, ^(200, 50^)^).collidepoint^(event.pos^):
echo                         if i == 0:
echo                             print^("StartMenu"^)
echo                         elif i == 1:
echo                             print^("StartMenu"^)
echo                         elif i == 2:
echo                             os.system^("start C:\\FA_Antivira\\FASuperPassword.bat"^)
echo                         elif i == 3:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAshutdown.bat"^)
echo                         elif i == 4:
echo                             os.system^("start notepad C:\\FA_Antivira\\FApyHlp\\FAstartmenuinfo.txt"^)
echo                         elif i == 5:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FArestart.bat"^)
echo                         elif i == 6:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FArestart.bat"^)
echo                         elif i == 7:
echo                             os.system^("start C:\\FA_Antivira\\StardMenu.bat"^)
echo                         elif i == 8:
echo                             os.system^("start C:\\FA_Antivira\\FAinfo.txt"^)
echo     screen.fill^(WHITE^)
echo     for i, pos in enumerate^(button_positions^):
echo         pygame.draw.rect^(screen, BLACK, ^(*pos, 200, 50^)^)
echo         text_surface = font.render^(button_texts[i], True, WHITE^)
echo         screen.blit^(text_surface, ^(pos^[0^] + 20, pos^[1^] + 10^)^)
echo     pygame.display.flip^(^)
echo pygame.quit^(^)
) > "C:\FA_Antivira\FApyHlp\\FAstartmenu.py"
(
echo import pygame
echo import os
echo pygame.init^(^)
echo WIDTH, HEIGHT = 800, 600
echo screen = pygame.display.set_mode^(^(WIDTH, HEIGHT^)^)
echo pygame.display.set_caption^("FA AntiVira Stardup "^)
echo WHITE = ^(42, 42, 42^)
echo BLACK = ^(100, 100, 100^)
echo font = pygame.font.Font^(None, 25^)
echo button_positions = ^[
echo     ^(1000, 1000^), ^(300, 100^), ^(5000, 1000^),
echo     ^(100, 300^), ^(300, 300^), ^(500, 300^),
echo     ^(1000, 5000^), ^(3000, 5000^), ^(5000, 5000^)
echo ^]
echo button_texts = ^[
echo     "URL Scan", "Scan Menu", "Super Passwort Generator",
echo     "Quick Scan", "File Scan", "Desktop Scan",
echo     "Scan For Damaged System", "Start Menu", "Info"
echo ^]
echo running = True
echo while running:
echo     for event in pygame.event.get^(^):
echo         if event.type == pygame.QUIT:
echo             running = False
echo         elif event.type == pygame.MOUSEBUTTONDOWN:
echo             if event.button == 1:
echo                 for i, pos in enumerate^(button_positions^):
echo                     if pygame.Rect^(pos, ^(200, 50^)^).collidepoint^(event.pos^):
echo                         if i == 0:
echo                             print^("Scan Menu"^)
echo                         elif i == 1:
echo                             print^("StartMenu"^)
echo                         elif i == 2:
echo                             os.system^("start C:\\FA_Antivira\\FASuperPassword.bat"^)
echo                         elif i == 3:
echo                             os.system^("start C:\\FA_Antivira\\FAquickscan.bat"^)
echo                         elif i == 4:
echo                             os.system^("start C:\\FA_Antivira\\FAfilescan.bat"^)
echo                         elif i == 5:
echo                             os.system^("start C:\\FA_Antivira\\FASystemScan.bat"^)
echo                         elif i == 6:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FArestart.bat"^)
echo                         elif i == 7:
echo                             os.system^("start C:\\FA_Antivira\\StardMenu.bat"^)
echo                         elif i == 8:
echo                             os.system^("start C:\\FA_Antivira\\FAinfo.txt"^)
echo     screen.fill^(WHITE^)
echo     for i, pos in enumerate^(button_positions^):
echo         pygame.draw.rect^(screen, BLACK, ^(*pos, 200, 50^)^)
echo         text_surface = font.render^(button_texts[i], True, WHITE^)
echo         screen.blit^(text_surface, ^(pos^[0^] + 20, pos^[1^] + 10^)^)
echo     pygame.display.flip^(^)
echo pygame.quit^(^)
) > "C:\FA_Antivira\FApyHlp\FAscanmenu.py"
(
echo import pygame
echo import os
echo pygame.init^(^)
echo WIDTH, HEIGHT = 800, 600
echo screen = pygame.display.set_mode^(^(WIDTH, HEIGHT^)^)
echo pygame.display.set_caption^("FA AntiVira Stardup "^)
echo WHITE = ^(42, 42, 42^)
echo BLACK = ^(100, 100, 100^)
echo font = pygame.font.Font^(None, 25^)
echo button_positions = ^[
echo     ^(100, 100^), ^(300, 100^), ^(500, 100^),
echo     ^(100, 300^), ^(300, 300^), ^(500, 300^),
echo     ^(100, 500^)
echo ^]
echo button_texts = ^[
echo     "Avira", "Avast", "G Data",
echo     "Kaspersky", "Windows Defender", "McAfee",
echo     "AVG"
echo ^]
echo running = True
echo while running:
echo     for event in pygame.event.get^(^):
echo         if event.type == pygame.QUIT:
echo             running = False
echo         elif event.type == pygame.MOUSEBUTTONDOWN:
echo             if event.button == 1:
echo                 for i, pos in enumerate^(button_positions^):
echo                     if pygame.Rect^(pos, ^(200, 50^)^).collidepoint^(event.pos^):
echo                         if i == 0:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAAvira.bat"^)
echo                         elif i == 1:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAAvast.bat"^)
echo                         elif i == 2:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAGData.bat"^)
echo                         elif i == 3:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAKaspersky.bat"^)
echo                         elif i == 4:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAWindDef.bat"^)
echo                         elif i == 5:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAMcAfee.bat"^)
echo                         elif i == 6:
echo                             os.system^("start C:\\FA_Antivira\\FApyHlp\\FAAVG.bat"^)
echo     screen.fill^(WHITE^)
echo     for i, pos in enumerate^(button_positions^):
echo         pygame.draw.rect^(screen, BLACK, ^(*pos, 200, 50^)^)
echo         text_surface = font.render^(button_texts[i], True, WHITE^)
echo         screen.blit^(text_surface, ^(pos^[0^] + 20, pos^[1^] + 10^)^)
echo     pygame.display.flip^(^)
echo pygame.quit^(^)
) > "C:\FA_Antivira\FApyHlp\FAMshAvir.py"
(
echo import pygame
echo import os
echo import sys
echo pygame.init^(^)
echo window = pygame.display.set_mode^(^(800, 600^)^)
echo font = pygame.font.Font^(None, 80^)
echo text = font.render^('File Is Detected as Malware', True, ^(0, 0, 0^), ^(139, 0, 0^)^)
echo button_font = pygame.font.Font^(None, 48^)
echo ignore_button = pygame.Rect^(100, 400, 200, 100^)
echo delete_button = pygame.Rect^(500, 400, 200, 100^)
echo while True:
echo     for event in pygame.event.get^(^):
echo         if event.type == pygame.QUIT:
echo             sys.exit^(^)
echo         if event.type == pygame.MOUSEBUTTONDOWN:
echo             mouse_pos = event.pos
echo             if ignore_button.collidepoint^(mouse_pos^):
echo                 sys.exit^(^)
echo             elif delete_button.collidepoint^(mouse_pos^):
echo                 os.system^("start C:\\FA_Antivira\\FAmalfiledel.bat"^)
echo     window.fill^(^(139, 0, 0^)^)
echo     window.blit^(text, ^(50, 50^)^)
echo     pygame.draw.rect^(window, ^[100, 100, 100^], ignore_button^)
echo     pygame.draw.rect^(window, ^[100, 100, 100^], delete_button^)
echo     window.blit^(button_font.render^('Ignore', True, ^(0, 0, 0^)^), ^(130, 420^)^)
echo     window.blit^(button_font.render^('Delete', True, ^(0, 0, 0^)^), ^(530, 420^)^)
echo     pygame.display.flip^(^)
) > "C:\FA_Antivira\Python\FAwarnfilescan.py"
echo Progress: [----------] 0% 
timeout /t 1 >nul
cls
echo Progress: [=---------] 10% 
timeout /t 1 >nul
cls
echo Progress: [==--------] 20% 
timeout /t 1 >nul
cls
echo Progress: [===-------] 30% 
timeout /t 1 >nul
cls
echo Progress: [====------] 40% 
timeout /t 1 >nul
cls
echo Progress: [=====-----] 50% 
timeout /t 1 >nul
cls
echo Progress: [======----] 60% 
timeout /t 1 >nul
cls
echo Progress: [=======---] 70% 
timeout /t 1 >nul
cls
echo Progress: [========--] 80% 
timeout /t 1 >nul
cls
echo Progress: [=========-] 90% 
timeout /t 1 >nul
cls
echo Progress: [==========] 100% 
timeout /t 1 >nul
cls
echo download complere
echo have a good day
start "" "C:\FA_Antivira\FAwlc.vbs"
timeout /t 60 >nul
goto Start
:dontinstall
echo instalation cancled
timeout /t 60 >nul
goto start