import os

def create_folders_and_files():
    # C:\FA_Antivira
    folder_path = r'C:\FA_Antivira'
    os.makedirs(folder_path, exist_ok=True)
    
    # C:\FA_Antivira\FApyHlp
    sub_folder_path_1 = os.path.join(folder_path, 'FApyHlp')
    os.makedirs(sub_folder_path_1, exist_ok=True)
    
    # C:\FA_Antivira\FASecLogsTxT
    sub_folder_path_2 = os.path.join(folder_path, 'FASecLogsTxT')
    os.makedirs(sub_folder_path_2, exist_ok=True)
    
    # C:\FA_Antivira\FAvbs
    sub_folder_path_3 = os.path.join(folder_path, 'FAvbs')
    os.makedirs(sub_folder_path_3, exist_ok=True)
    
    # C:\FA_Antivira\Python
    sub_folder_path_4 = os.path.join(folder_path, 'Python')
    os.makedirs(sub_folder_path_4, exist_ok=True)
    
    # Erstelle und schreibe in die Datei 
    with open(os.path.join(folder_path, 'Fabi_Antivira_Securety.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
color 0E
start "" "C:\FA_Antivira\FAwlc.vbs"
start "" "C:\FA_Antivira\FASecLogsTxT\FAupLOG.bat"
start "" "C:\FA_Antivira\FAvbs\FAbuttenUser.vbs"
start "" "C:\FA_Antivira\Python\FAMsh.py"
start "" "C:\FA_Antivira\FAcmd.bat"
''')
    
    # C:\FA_Antivira\FAvbs\FAstartmenu.vbs
    with open(os.path.join(sub_folder_path_3, 'FAstartmenu.vbs'), 'w') as file:
        file.write('''Set objShell = CreateObject("WScript.Shell")
Sub OpenFile(filePath)
    objShell.Run Chr(34) & filePath & Chr(34), 1, False
End Sub
Sub Main()
    Dim buttonClicked
    buttonClicked = InputBox("Please Choose an Option:" & vbCrLf & _
                            "1. Info" & vbCrLf & _
                            "2. Shutdown" & vbCrLf & _
                            "3. Restart", "FA_Antivira Start Menu")
    Select Case buttonClicked
        Case "1"
            OpenFile "C:\FA_Antivira\FApyHlp\FAstartmenuinfo.txt"
        Case "2"
            OpenFile "C:\FA_Antivira\FApyHlp\\FAshutdown.bat"
        Case "3"
            OpenFile "C:\FA_Antivira\FApyHlp\FArestart.bat"
        Case Else
            MsgBox "Invalid input please type in a number from 1 to 3"
    End Select
End Sub
Main
''')

    # C:\FA_Antivira\FApyHlp\FAscaninfo.txt
    with open(os.path.join(sub_folder_path_1, 'FAscaninfo.txt'), 'w') as file:
        file.write('''these are scan methodes
''')
    
    # C:\FA_Antivira\FAvbs\FAscanmenu.vbs
    with open(os.path.join(sub_folder_path_3, 'FAstartmenu.vbs'), 'w') as file:
        file.write('''Set objShell = CreateObject("WScript.Shell")
Sub OpenFile(filePath)
    objShell.Run Chr(34) & filePath & Chr(34), 1, False
End Sub
Sub Main()
    Dim buttonClicked
    buttonClicked = InputBox("Please Choose an Option:" & vbCrLf & _
                            "1. Quick Scan" & vbCrLf & _
                            "2. Desktop Scan" & vbCrLf & _
                            "3. File Scan", "FA_Antivira Start Menu")
    Select Case buttonClicked
        Case "1"
            OpenFile "C:\FA_Antivira\FAquickscan.bat"
        Case "2"
            OpenFile "C:\FA_Antivira\FASystemScan.bat"
        Case "3"
            OpenFile "C:\FA_Antivira\FAfilescan.bat"
        Case Else
            MsgBox "Invalid input please type in a number from 1 to 3"
    End Select
End Sub
Main
''')

    # C:\FA_Antivira\FAhelp.txt
    with open(os.path.join(folder_path, 'FAhelp.txt'), 'w') as file:
        file.write('''Here is Some helpfull advice to keep your pc save
-create backups on your computer
-Use Strong Passwords
-Be carefull when downloading things or clicking on links
-Use a Safe Browser like Tor the safest browser int the world
-Avoid Fake Programs only download trusted programs and only download them from the real websides
-dont use usb sticks you dont know
-dont keep FAPasswords.docx on your pc use a usb stick to save it and if u need to save a password you edit FAPasswords.docx and save it on the usb again
''')

    # C:\FA_Antivira\FAinfo.txt
    with open(os.path.join(folder_path, 'FAinfo.txt'), 'w') as file:
        file.write('''this is a Antivirus addon made by the python / batch / vbs / html coder @fabischau
''')

    # C:\FA_Antivira\StardMenu.bat
    with open(os.path.join(folder_path, 'StardMenu.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
color 0E
start "" "C:\FA_Antivira\FAvbs\FAstartmenu.vbs"
start "" "C:\FA_Antivira\FApyHlp\FAstartmenu.py"
start "" "C:\FA_Antivira\FAcmd.bat"
''')

    # C:\FA_Antivira\FAdmgsysscan.bat
    with open(os.path.join(folder_path, 'FAdmgsysscan.bat'), 'w') as file:
        file.write('''@echo off
color 0E
echo please press search in windows for cmd and open it as administrator.
echo then type in the command sfc /scannow
color 04
echo WARNING this will take some time
echo WARNING DONT CLOSE THE WINDOW WHILE SCANS
color 0E
echo tipp you should have no other Programs open while its scanning
pause
''')

    # C:\FA_Antivira\FAquickscan.bat
    with open(os.path.join(folder_path, 'FAquickscan.bat'), 'w') as file:
        file.write('''@echo off
color 0E
echo Starting Quickscan...
"C:\Program Files\Windows Defender\MpCmdRun.exe" -Scan -ScanType 1
echo Quickscan abgeschlossen
echo QuickScaning...
start "" "C:\Program Files\Windows Defender\MSASCui.exe"
pause
''')

    # C:\FA_Antivira\FAvbs\FAscanmenu.vbs
    with open(os.path.join(sub_folder_path_3, 'FAscanmenu.vbs'), 'w') as file:
        file.write('''Set objShell = CreateObject("WScript.Shell")
Sub OpenFile(filePath)
    objShell.Run Chr(34) & filePath & Chr(34), 1, False
End Sub
Sub Main()
    Dim buttonClicked
    buttonClicked = InputBox("Please Choose an Option:" & vbCrLf & _
                            "1. Quick Scan" & vbCrLf & _
                            "2. Desktop Scan" & vbCrLf & _
                            "3. File Scan", "FA_Antivira Start Menu")
    Select Case buttonClicked
        Case "1"
            OpenFile "C:\FA_Antivira\FAquickscan.bat"
        Case "2"
            OpenFile "C:\FA_Antivira\FASystemScan.bat"
        Case "3"
            OpenFile "C:\FA_Antivira\FAfilescan.bat"
        Case Else
            MsgBox "Invalid input please type in a number from 1 to 3"
    End Select
End Sub
Main
''')

    # C:\FA_Antivira\FAPasswordgenerator.bat
    with open(os.path.join(folder_path, 'FAPasswordgenerator.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
color 0E
set "characters=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.<>?~"
set "passwordLength=12"
set "password="
for /l %%i in (1,1,%passwordLength%) do (
    set /a "randomIndex=!random! %% 94"
    call set "char=%%characters:~!randomIndex!,1%%"
    set "password=!password!!char!"
)
echo Your Generated Password Is:"!password!"
pause
''')

    # C:\FA_Antivira\FASuperPassword.bat
    with open(os.path.join(folder_path, 'FASuperPassword.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
color 0E
set "characters=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.<>?~"
set "passwordLength=30"
set "password="
for /l %%i in (1,1,%passwordLength%) do (
    set /a "randomIndex=!random! %% 94"
    call set "char=%%characters:~!randomIndex!,1%%"
    set "password=!password!!char!"
)
echo Your Generated Password Is:"!password!"
pause
''')

    # C:\FA_Antivira\FA_URLscan.bat
    with open(os.path.join(folder_path, 'FA_URLscan.bat'), 'w') as file:
        file.write('''@echo off
color 0E
echo please dont put the https:// or the http:// infront of the link or the scanner will get confused and may not work properly.
set /p userInput="Please type an URL like this example.com: "
findstr /i "%userInput%" "C:\FA_Antivira\FAurlDataBank.txt" > nul
if %errorlevel% equ 0 (
    echo FA DataBank flagged this URL: "%userInput%" as malicious.
) else (
    echo FA DataBank flagged this URL: "%userInput%" as probaly safe.or the data bank doesnt include this url. or you didnt follow the instructions for better instruktions look at info.
)
pause >nul
''')

    # C:\FA_Antivira\FAantivirusopener.bat
    with open(os.path.join(folder_path, 'FAantivirusopener.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
color 0E
start "" "C:\FA_Antivira\FApyHlp\FAMshAvir.py"
start "" "C:\FA_Antivira\FAvbs\FAbuttenAntiVirusUser.vbs"
start "" "C:\FA_Antivira\FAcmd.bat"
''')

    # C:\FA_Antivira\FAshortcutinstallerdesktop.bat
    with open(os.path.join(folder_path, 'FAshortcutinstallerdesktop.bat'), 'w') as file:
        file.write('''@echo off
color 0E
echo installing short cut .
cls
echo installing short cut ..
cls
echo installing short cut ...
cls
echo installing short cut .
cls
echo installing short cut ..
cls
echo installing short cut ...
cls
setlocal
set "batchPath=C:\FA_Antivira\Fabi_Antivira_Securety.bat"
set "desktopFolder=%USERPROFILE%\Desktop"
set "shortcutName=FA Security.lnk"
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%desktopFolder%\%shortcutName%');$s.TargetPath='%batchPath%';$s.Save()"
echo Installer Shortcut: %desktopFolder%\%shortcutName%
start https://ufile.io/1cs1w93x
start https://ufile.io/3dxhf9ba
pause
''')

    # C:\FA_Antivira\FASecLogsTxT\FAupLOG.bat
    with open(os.path.join(sub_folder_path_2, 'FAupLOG.bat'), 'w') as file:
        file.write('''@echo off
color 0E
set "LogFile=C:\FA_Antivira\FASecLogsTxT\FAupLOGlogFile.txt"
set "TriggerFile=C:\FA_Antivira\Fabi_Antivira_Securety.bat"
:loop
if exist "%TriggerFile%" (
    echo %date% %time% - Fabi AntiVira Securety was opened. >> "%LogFile%"
    rem Hier weitere Aktionen ausführen, z. B. in die Logdatei schreiben.
    timeout /t 5 > nul
    goto loop
) else (
    echo %date% %time% - Fabi AntiVira Securety couldnt be opened. >> "%LogFile%"
)
''')

    # C:\FA_Antivira\FAvbs\FAbuttenAntiVirusUser.vbs
    with open(os.path.join(sub_folder_path_3, 'FAbuttenAntiVirusUser.vbs'), 'w') as file:
        file.write('''Set objShell = CreateObject("WScript.Shell")
Sub OpenFile(filePath)
    objShell.Run Chr(34) & filePath & Chr(34), 1, False
End Sub
Sub Main()
    Dim buttonClicked
    buttonClicked = InputBox("Please Choose an Anti Virus:" & vbCrLf & _
                            "1. Avira" & vbCrLf & _
                            "2. Avast" & vbCrLf & _
                            "3. G Data" & vbCrLf & _
                            "4. Kaspersky" & vbCrLf & _
                            "5. Windows Defender" & vbCrLf & _
                            "6. McAfee" & vbCrLf & _
                            "7. AVG", "FA_Antivira")
    Select Case buttonClicked
        Case "1"
            OpenFile "C:\FA_Antivira\FApyHlp\FAAvira.bat"
        Case "2"
            OpenFile "C:\FA_Antivira\FApyHlp\FAAvast.bat"
        Case "3"
            OpenFile "C:\FA_Antivira\FApyHlp\FAGData.bat"
        Case "4"
            OpenFile "C:\FA_Antivira\FApyHlp\FAKaspersky.bat"
        Case "5"
            OpenFile "C:\FA_Antivira\FApyHlp\FAWindDef.bat"
        Case "6"
            OpenFile "C:\FA_Antivira\FApyHlp\FAMcAfee.bat"
        Case "7"
            OpenFile "C:\FA_Antivira\FApyHlp\FAAVG.bat"
        Case Else
            MsgBox "Invalid input please type in a number from 1 to 9"
    End Select
End Sub
Main
''')

    # C:\FA_Antivira\FAvbs\FAbuttenUser.vbs
    with open(os.path.join(sub_folder_path_3, 'FAbuttenUser.vbs'), 'w') as file:
        file.write('''Set objShell = CreateObject("WScript.Shell")
Sub OpenFile(filePath)
    objShell.Run Chr(34) & filePath & Chr(34), 1, False
End Sub
Sub Main()
    Dim buttonClicked
    buttonClicked = InputBox("Please Choose an Option:" & vbCrLf & _
                            "1. URL Scan" & vbCrLf & _
                            "2. Passwort Generator" & vbCrLf & _
                            "3. Super Passwort Generator" & vbCrLf & _
                            "4. Scan Menu" & vbCrLf & _
                            "5. Open Anti Virus" & vbCrLf & _
                            "6. Help" & vbCrLf & _
                            "7. Scan For Damaged System" & vbCrLf & _
                            "8. Stard Menu" & vbCrLf & _
                            "9. Kill File", "FA_Antivira")
    Select Case buttonClicked
        Case "1"
            OpenFile "C:\FA_Antivira\FA_URLscan.bat"
        Case "2"
            OpenFile "C:\FA_Antivira\FAPasswordgenerator.bat"
        Case "3"
            OpenFile "C:\FA_Antivira\FASuperPassword.bat"
        Case "4"
            OpenFile "C:\FA_Antivira\FApyHlp\FAscanmenu.py"
            OpenFile "C:\FA_Antivira\FAvbs\FAscanmenu.vbs"
        Case "5"
            OpenFile "C:\FA_Antivira\FAantivirusopener.bat"
        Case "6"
            OpenFile "C:\FA_Antivira\FAhelp.txt"
        Case "7"
            OpenFile "C:\FA_Antivira\FAdmgsysscan.bat"
        Case "8"
            OpenFile "C:\FA_Antivira\StardMenu.bat"
        Case "9"
            OpenFile "C:\FA_Antivira\FAmalfiledel.bat"
        Case Else
            MsgBox "Invalid input please type in a number from 1 to 9"
    End Select
End Sub
Main
''')

    # C:\FA_Antivira\FAmalfiledel.bat
    with open(os.path.join(folder_path, 'FAmalfiledel.bat'), 'w') as file:
        file.write('''@echo off
color 0E
set /p filepath="Please Type In The Path Of The File You Want To Kill: "
for /L %%i in (1,1,20000) do (
    echo This File Was Overwritten By FA AntiVira %%i Times > "%filepath%"
)
del /F /Q "%filepath%"
echo File Killed.
echo File Was Permanently Deleted And Overwritten 20000 Times
pause
''')

    # C:\FA_Antivira\FAhashshower.bat
    with open(os.path.join(folder_path, 'FAhashshower.bat'), 'w') as file:
        file.write('''@echo off
setlocal enabledelayedexpansion
set "line=0"
for /f "delims=" %%A in (FAtemp.txt) do (
    set /a line+=1
    call :checkLine %%A
)
exit /b
:checkLine
if %line% equ 2 (
    findstr /i "%~1" "C:\FA_Antivira\FAMalHashDatabase.txt" > nul
	echo The File Hash is: %~1
    call :checkError
)
exit /b
:checkError
if %errorlevel% equ 0 (
    color 04
    echo Malware Detected
	 start "" "C:\FA_Antivira\Python\FAwarnfilescan.py"
 start "" "C:\FA_Antivira\FAquickscan.bat"
 start "" "C:\FA_Antivira\FAvbswarnfile.vbs"
    pause
) else (
    color 0a
    echo No Malware found
 start "" "C:\FA_Antivira\FAquickscan.bat"
    pause
)
exit /b
''')

    # C:\FA_Antivira\FAfilescan.bat
    with open(os.path.join(folder_path, 'FAfilescan.bat'), 'w') as file:
        file.write('''@echo off
setlocal
set /p FILE_PATH=File Path:
if not exist %FILE_PATH% (
    echo File Does Not Ecsist.
	pause
    goto :eof
)
certutil -hashfile %FILE_PATH% SHA256 > FAtemp.txt
	timeout /t 3 >nul
	start "" "C:\FA_Antivira\FAhashshower.bat"
	pause
    goto :next
)
:next
del FAtemp.txt
:end
endlocal
''')

    # C:\FA_Antivira\FAvbswarnfile.vbs
    with open(os.path.join(folder_path, 'FAhashshower.bat'), 'w') as file:
        file.write('''MsgBox "File Detected As Malware", vbExclamation, "Warning"
Antwort = MsgBox("Do You Want To Delete It?", vbExclamation + vbYesNo, "Warning")
If Antwort = vbYes Then
    Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run "C:\FA_Antivira\FAmalfiledel.bat", 0, True
Else
    MsgBox "Ok But Remember The File Might Be Realy Dangerous", vbExclamation, "Warning"
End If
''')

    # C:\FA_Antivira\FASecLogsTxT\FAupLOGlogFile.txt
    with open(os.path.join(sub_folder_path_2, 'FAupLOGlogFile.txt'), 'w') as file:
        file.write('''FA Antivira Opening History:
''')
#___________________________________________________________________________________
    # C:\FA_Antivira\FApyHlp\FAshutdown.bat
    with open(os.path.join(sub_folder_path_1, 'FAshutdown.bat'), 'w') as file:
        file.write('''Shutdown /s /t 10
''')

    # C:\FA_Antivira\FApyHlp\FArestart.bat
    with open(os.path.join(sub_folder_path_1, 'FArestart.bat'), 'w') as file:
        file.write('''Shutdown /r /t 10
''')

    # C:\FA_Antivira\FApyHlp\FAstartmenuinfo.txt
    with open(os.path.join(sub_folder_path_1, 'FAstartmenuinfo.txt'), 'w') as file:
        file.write('''clicking shutdown will shutdown your pc in 10s and hitting restart will Restart your pc in 10s
''')

    # C:\FA_Antivira\FApyHlp\FAAvira.bat
    with open(os.path.join(sub_folder_path_1, 'FAAvira.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files (x86)\Avira\Security\Avira.Spotlight.UI.Application.exe"
''')

    # C:\FA_Antivira\FApyHlp\FAAvast.bat
    with open(os.path.join(sub_folder_path_1, 'FAAvast.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files\AVAST Software\Avast\AvastUI.exe"
''')

    # C:\FA_Antivira\FApyHlp\FAGData.bat
    with open(os.path.join(sub_folder_path_1, 'FAGData.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files (x86)\G Data\InternetSecurity\AVKTray.exe"
''')

    # C:\FA_Antivira\FApyHlp\FAKaspersky.bat 
    with open(os.path.join(sub_folder_path_1, 'FAKaspersky.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files (x86)\Kaspersky Lab\Kaspersky Internet Security 20.0\avp.exe"
''')

    # C:\FA_Antivira\FApyHlp\FAWindDef.bat
    with open(os.path.join(sub_folder_path_1, 'FAWindDef.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files\Windows Defender\MsMpEng.exe"
''')

    # C:\FA_Antivira\FApyHlp\FAMcAfee.bat
    with open(os.path.join(sub_folder_path_1, 'FAMcAfee.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files\Common Files\McAfee\Platform\McSvcHost"
''')

    # C:\FA_Antivira\FApyHlp\FAAVG.bat
    with open(os.path.join(sub_folder_path_1, 'FAAVG.bat'), 'w') as file:
        file.write('''start "" "C:\Program Files\AVG\Antivirus\AVGUI.exe"
''')

    # C:\FA_Antivira\FAwlc.vbs
    with open(os.path.join(folder_path, 'FAwlc.vbs'), 'w') as file:
        file.write('''MsgBox "Welcome To FA Antivira :D"
''')

    # C:\FA_Antivira\FAcmd.bat
    with open(os.path.join(folder_path, 'FAcmd.bat'), 'w') as file:
        file.write('''taskkill /f /im cmd.exe
''')

    # C:\FA_Antivira\FAurlDataBank.txt
    with open(os.path.join(folder_path, 'FAurlDataBank.txt'), 'w') as file:
        file.write('''echo amongus.io
echo bit.ly
echo short.link
echo unsafe.com
echo tx.gl
echo theannoyingsite.com
echo enderman.ch
echo darknet.org
echo freerobux.org
echo freerobux.com
echo malware.com
echo ransomware.com
echo minecraftfree.com
echo minecraftfree.net
echo Bitcoinfree.io
echo notavirus.com
echo maleware.com
echo torbrowser.com
echo worm.com
echo malware.net
echo notavirus.net
echo asianwallpaper.com
echo spongebobfunpack.com
echo linodeusercontent.com
echo jazzremedy.org
echo admin-ods.insolvency-development.co.uk
echo splendorous-lolly-f0975easd.netlify.app
echo apple-mystore-parter-portal.com
echo education.exploresurface.com
echo bridgechurch.tv
echo www.qch.ge
echo wvntq.blogspot.fi
echo grl.hgs.mybluehost.me
echo preparacion.soostain.com
echo xtu.tak.mybluehost.me
echo c3b6y5z6.xyz
echo flikacbs.com
echo ficohsa.click
echo fi97se.webwave.dev
echo email.promode.se
echo dhl-tracking-au.blogspot.com
echo ff.member.garema.id.vn
echo www.howmuchmoney.buzz
echo 154.3.34.9
echo fakinthefunk.net
echo fakeflix.constantine.dev
echo www.iadewebtecepgirisbilgi.app
echo ekzah-eiaaa-aaaak-qavka-cai.raw.icp0.io
echo sanitoceramics.com
echo ebay-001.com
echo ev6gwa.webwave.dev
echo e-telegram.biz
echo koi-wrk.oh8q.info
echo entertainwap.mywibes.com
echo vnihmamweq.com/jp
echo claim-pancakeswep.web.app
echo www.centauroliquidacaoverao.com
echo quickquestion2024.com
echo renew-domain-aruba.duckdns.org
echo er5e3s21a.page.link/rniX
echo pub-d0ef89baeccc41829f8dec9250e6f9a8.r2.de
echo app-c9974f14-48ed-499e-8411-9319ce15f622.c
echo groupvisecaone.blogspot.com
echo xdt.twj.mybluehost.me/signin.php
echo www.sbbswisspasschcominvest.web.app
echo chauthpaypa-accoulog.servebbs.net
echo www.resgatepntsouro.info
echo sardunya.com
echo 5.182.86.32
echo 79.137.194.188
echo achillharpfestival.ie
echo unwaveringmedia.com
echo 103.147.185.68
echo 91.92.255.79
echo 123.13.21.36:47055
echo 91.92.255.79
echo 204.76.203.131
echo 182.113.39.216:35136
echo 117.235.33.205:51071	
echo 200.59.84.176:38779
echo 117.210.172.22:42357
echo 204.76.203.131/bins
echo 119.186.210.116:40839
echo 59.89.71.250:54468
echo 186.45.134.91:33730
echo 204.76.203.131
echo 204.76.203.131
echo 117.217.38.254:56237
echo 123.10.238.41:41251
echo 204.76.203.131
echo 204.76.203.131
echo 2204.76.203.131
echo 204.76.203.131
echo 222.138.112.221:41853
echo delp-heizungsbau.de
echo 204.76.203.131
echo 110.182.151.77:2497
echo 204.76.203.131
echo transfer.sh
echo 219.157.30.5:46128
echo 123.10.238.41:41251
echo 222.141.63.7:34424
echo 117.235.33.139:52355
echo 204.76.203.131
echo 222.140.180.215:35618
echo transfer.sh
echo 125.47.53.49:54876
echo 204.76.203.131
echo 115.55.99.2:40897
echo 91.92.255.79/GuruITDDoS
echo 125.43.25.106:53895
echo shizk.day.50adayplan.com
echo 182.126.80.193:35560
echo 204.76.203.131
echo 59.182.255.173:44917
echo 204.76.203.131
echo 204.76.203.131
echo 119.186.210.116:40839
echo 91.92.255.79/GuruITDDoS
echo 182.113.18.151:46051/Mozi.m
echo 117.248.28.62:35095/Mozi.m
echo 123.9.98.255:55273/Mozi.m
echo 120.211.70.4:37661/bin.sh
echo 125.70.70.156:53932/i
echo 204.76.203.131/bins/nklspc
echo 115.50.187.223:35210/i
echo 117.192.121.173:59568/Mozi.m
echo 178.124.151.232:34884/Mozi.m
echo 204.76.203.131/bins/zerarm6
echo 204.76.203.131/bins/nklarm5
echo 200.69.52.33:51155/bin.sh
echo 222.141.63.7:34424/bin.sh
echo 61.2.111.165:53598/Mozi.m
echo 204.76.203.131/bins/zermpsl
echo 204.76.203.131/bins/jklarm6
echo 190.109.227.231:53932/i	Online
echo 204.76.203.131/bins/arm7
echo 204.76.203.131/bins/splm68k
echo 204.76.203.131/bins/nabmpsl
echo 125.43.25.106:53895/bin.sh
echo 117.211.218.25:40420/i
echo 204.76.203.131/bins/jklspc
echo 204.76.203.131/bins/persh4
echo 204.76.203.131/bins/zerm68k
echo 204.76.203.131/bins/dlr.x86
echo 204.76.203.131/bins/dlr.arm
echo 204.76.203.131/bins/dlr.arm7
echo 123.4.182.230:53152/Mozi.m
echo 182.113.39.216:35136/bin.sh
echo 204.76.203.131/bins/jklx88
echo 222.139.55.14:32779/Mozi.m
echo 204.76.203.131/bins/dlr.arm5
echo 182.123.208.143:47523/Mozi.m
echo 61.53.254.166:50581/i
echo 59.89.196.228:36991/bin.sh
echo 125.45.65.76:44758/Mozi.m
echo 125.41.2.91:44450/i
echo 59.89.198.155:56104/bin.sh
echo 91.92.255.79/GuruITDDoS/RpcSecurity.mips
echo transfer.sh/get/KFB585VJjT/hfghhfd.exe
echo 204.76.203.131/bins/nklm68k
echo 91.92.255.79/GuruITDDoS/RpcSecurity.arc
echo 204.76.203.131/bins/zerppc
echo 204.76.203.131/bins/splarm6
echo 27.215.83.90:32963/bin.sh
echo 204.76.203.131/bins/perarm7
echo 182.56.91.138:56722/mozi.m
echo 120.86.246.224:49724/Mozi.a
echo 204.76.203.131/bins/dlr.mips
echo 204.76.203.131/bins/nabm68k
echo abc.anti-ddos.io.vn/cundi.ppc
echo 59.92.181.210:36481/Mozi.m
echo 103.47.195.200/cundi.m68k
echo abc.anti-ddos.io.vn/cundi.m68k
echo abc.anti-ddos.io.vn/cundi.mpsl
echo 103.47.195.200/cundi.mpsl
echo 103.47.195.200/cundi.ppc
echo 39.49.100.118:59793/i
echo 223.10.180.144:44499/bin.sh
echo 124.95.106.39:55422/i
echo 117.217.85.35:47830/mozi.m
echo 59.89.0.111:58086/bin.sh
echo 219.155.192.96:43065/i
echo 90.109.228.16:36346/Mozi.m
echo 219.155.192.96:43065/bin.sh
echo 42.239.113.115:55625/bin.sh
echo 125.43.91.75:53424/bin.sh
echo 115.50.209.216:36766/bin.sh
echo 123.129.128.102:50269/bin.sh
echo 222.138.125.23:52633/Mozi.m
echo 124.135.182.185:34077/i
echo 42.224.251.23:46775/i
echo 182.127.71.9:50323/Mozi.a
echo 123.11.0.23:34647/i
echo 39.79.114.49:36719/Mozi.m
echo 110.180.168.249:9726/.i
echo 111.61.93.195:36497/bin.sh
echo 201.211.52.196:44368/i
echo 182.119.60.183:57204/mozi.m
echo 37.13.139.249:58780/Mozi.m
echo 193.233.132.216:38324/alana/nadal.exe
echo 219.155.193.48:44376/Mozi.m
echo 112.248.113.209:59817/i
echo 27.204.253.102:49396/i
echo 115.52.19.122:55788/bin.sh
echo 46.23.184.231:49543/mozi.m
echo 42.232.229.21:36674/i
echo 117.235.24.62:53481/i
echo 201.211.52.196:44368/bin.sh
echo 117.219.93.4:58423/i
echo 112.248.113.209:59817/bin.sh
echo 61.53.140.242:56598/i
echo 27.21.211.111:47479/bin.sh
echo 182.121.88.105:48873/Mozi.m
echo 42.232.229.21:36674/bin.sh
echo 115.59.3.130:36818/i
echo 221.14.162.103:34937/i
echo 36.226.135.181:52976/.i
echo 61.53.1405.242:56598/bin.sh
echo 39.74.80.62:54133/i
echo 27.121.83.224:33259/i
echo 59.93.18.228:60786/Mozi.m
echo 125.44.181.103:34396/mozi.m
echo 115.49.176.120:35664/Mozi.m
echo 117.211.208.123:53511/Mozi.m
echo 115.59.3.130:36818/bin.sh
echo echo 113.239.221.3:56538/Mozi.m
echo 47.99.151.68:132/sky.jsp
echo 43.143.130.124:8000/C4
echo 104.243.32.185/ty.jpg
echo 104.243.32.185/z.jpg
echo 43.143.130.124:8000/cs.exe
echo 47.99.151.68:132/shellasp1.jpg
echo 47.99.151.68:132/shellaspx.jpg
echo 47.99.151.68:132/shellasp.jpg
echo 47.99.151.68:132/shelloffice365.zip
echo 47.99.151.68:132/shell.jsp
echo 43.143.130.124:8000/ns.sh
echo 190.123.44.228:1338/keylogger.py
echo 190.123.44.228:1338/xmrig/
echo 47.99.151.68:132/gslpassashx.jpg
echo 47.99.151.68:132/20230627113722jsp.jpg
echo 47.99.151.68:132/IDocView.html
echo 222.142.221.174:50444/i
echo 37.13.139.249:58780/Mozi.a
echo 112.248.83.181:38421/Mozi.m
echo 125.41.5.2:45653/Mozi.m	Online
echo 221.14.162.103:34937/bin.sh
echo 117.205.63.115:60524/i
echo 115.50.69.14:47089/i
echo 27.121.83.224:33259/bin.sh
echo 115.48.156.197:60771/Mozi.m	
echo 112.248.191.194:51261/Mozi.m
echo 112.248.187.45:60324/i
echo 42.234.52.115:36779/Mozi.m
echo 102.33.71.29:51634/Mozi.m
echo 112.254.50.211:49781/Mozi.m
echo 123.13.141.122:49075/Mozi.m
echo 222.142.221.174:50444/bin.sh
echo 117.216.254.206:42967/Mozi.m
echo 117.199.77.246:44904/i
echo 112.248.187.45:60324/bin.sh
echo 117.205.63.115:60524/bin.sh
echo 42.237.102.169:42969/Mozi.m
echo notmalware.top/socks32.exe
echo 182.113.31.156:39215/i
echo 42.234.143.154:51900/Mozi.m
echo 42.224.121.145:34391/i
echo 42.230.211.84:34074/i
echo 117.254.180.159:46603/i
echo 182.117.50.166:50839/bin.sh
echo 117.216.241.6:34229/i
echo 221.1.227.5:59299/bin.sh
echo 27.215.85.224:42860/i
echo 117.254.180.159:46603/bin.sh
echo 115.61.16.211:56933/bin.sh
echo 115.58.86.187:57045/i
echo 115.49.73.89:35831/i
echo 42.224.121.145:34391/bin.sh
echo 123.12.42.71:44313/Mozi.m
echo 182.115.77.130:32936/i
echo 115.58.86.187:57045/bin.sh
echo 125.44.22.143:34317/Mozi.m
echo 182.117.123.79:44977/i
echo 117.216.241.6:34229/bin.sh
echo 112.246.86.45:46038/i
echo 183.150.85.169:50683/i
echo 42.230.211.84:34074/bin.sh
echo 116.74.159.140:38986/Mozi.m
echo 115.55.230.43:35598/i
echo 78.9.100.212:51415/Mozi.m
echo 117.235.57.110:55712/Mozi.m
echo 42.224.27.147:53966/Mozi.m
echo 27.213.60.39:55006/Mozi.m
echo 115.58.112.122:36907/Mozi.m
echo 42.235.190.208:35254/i
echo 86.42.150.41:51810/Mozi.m
echo 182.115.77.130:32936/bin.sh
echo 115.58.134.41:41550/bin.sh
echo 123.12.9.198:39969/bin.sh
echo 182.117.123.79:44977/bin.sh
echo 112.246.86.45:46038/bin.sh
echo 183.150.85.169:50683/bin.sh
echo 59.89.199.197:40244/bin.sh
echo 115.55.230.43:35598/bin.sh
echo 115.50.54.176:38326/bin.sh
echo 115.49.85.1:60897/i
echo 124.95.106.39:55422/bin.sh
echo 201.209.194.207:43518/bin.sh
echo 60.23.77.88:39534/bin.sh
echo 117.254.176.58:49485/bin.sh
echo mail.isellemails.com/MediaLight/uploads...
echo 123.5.126.75:42944/i
echo 117.208.235.84:51763/i
echo 123.10.224.227:37606/i
echo 125.41.173.28:48363/bin.sh
echo 185.32.4.72:35007/Mozi.m
echo 182.126.127.190:42336/i
echo 117.215.75.117:44547/Mozi.m
echo 117.248.27.69:58485/Mozi.m
echo 117.202.66.138:38447/Mozi.m
echo 121.239.208.155:56146/Mozi.m
echo 147.182.203.234/bins.sh
echo 115.49.85.1:60897/bin.sh
echo 117.199.10.33:60071/i
echo 182.127.152.132:53050/i
echo 115.63.181.64:44532/i
echo 125.44.192.254:57143/Mozi.m
echo 59.99.130.178:49061/Mozi.m
echo 175.31.201.133:37911/Mozi.m
echo 115.60.210.4:36089/i
echo 182.126.80.193:35560/Mozi.m
echo 123.5.126.75:42944/bin.sh
echo 117.208.235.84:51763/bin.sh
echo 112.237.233.72:34302/bin.sh
echo 220.192.249.136:55733/i
echo 182.126.127.190:42336/bin.sh
echo 115.63.181.64:44532/bin.sh
echo 175.167.86.250:39901/i
echo 61.53.125.94:53965/i
echo 125.44.192.254:57143/i
echo 182.127.152.132:53050/bin.sh
echo 190.109.228.16:36346/i
echo 182.121.40.133:44236/Mozi.m
echo 61.53.132.253:51677/Mozi.m
echo 219.157.64.105:40679/Mozi.m
echo 219.155.20.230:54876/i
echo 112.248.245.173:59798/i
echo 115.53.244.185:44925/i
echo mail.isellemails.com/MediaLight/uploads...
echo rango009.github.io/demo/virus.exe
echo 61.168.136.39:34970/i
echo 117.199.10.33:60071/bin.sh
echo 115.50.255.155:47706/bin.sh
echo 46.153.135.135:38705/Mozi.a
echo 93.123.39.166/x-8.6-.Sakura
echo 61.53.125.94:53965/bin.sh
echo 124.131.106.137:56479/i
echo 117.235.32.101:47472/i
echo 61.168.136.39:34970/bin.sh
echo 175.31.201.133:37911/bin.sh
echo 61.3.8.37:41700/i
echo 112.248.245.173:59798/bin.sh
echo 190.109.228.16:36346/bin.sh
echo 113.231.250.78:33319/Mozi.m
echo 117.201.5.80:53808/Mozi.m
echo 123.14.197.143:45212/i
echo 123.11.163.123:58315/i
echo 183.184.71.237:46181/Mozi.m
echo 117.255.80.201:38496/Mozi.m
echo 117.242.235.146:46506/bin.sh
echo 115.48.26.35:56412/Mozi.m
echo 117.206.185.115:54305/Mozi.m
echo 220.143.4.139:43429/Mozi.a
echo 123.14.169.115:56913/Mozi.m
echo 109.108.218.34:37077/Mozi.m
echo 175.148.52.76:53973/i
echo 182.113.42.59:37158/i
echo 59.88.176.209:33414/Mozi.a
echo 61.52.156.234:47742/i
echo 42.232.212.111:50143/i
echo 113.230.245.84:44847/i
echo 61.52.156.234:47742/bin.sh
echo 112.239.113.2:33473/Mozi.a
echo 61.3.10.33:60305/Mozi.m
echo 110.183.50.132:42874/Mozi.m
echo 77.89.201.118:54236/bin.sh
echo 182.113.42.59:37158/bin.sh
echo 41.86.19.131:38852/Mozi.m
echo 5.42.65.102/retail.php
echo 123.7.238.130:57387/i
echo 42.232.212.111:50143/bin.sh
echo 221.14.104.183:40705/i
echo 125.44.212.136:60359/bin.sh
echo 222.137.183.215:55684/bin.sh
echo 113.230.245.84:44847/bin.sh
echo 182.127.100.196:48484/i
echo 222.139.74.133:47028/bin.sh
echo unidasg.top/outh.php
echo 115.63.55.61:33789/i
echo 123.7.238.130:57387/bin.sh
echo 59.88.183.213:46028/Mozi.m
echo 45.227.40.213:58262/Mozi.m
echo 158.255.82.66:55583/Mozi.a
echo 59.88.191.59:43189/i
echo 115.63.55.61:33789/bin.sh
echo 221.14.104.183:40705/bin.sh
echo 182.127.100.196:48484/bin.sh
echo 66.23.130.238:37600/i
echo 46.32.172.195:11881/Mozi.m
echo 117.217.38.117:34660/Mozi.m
echo 112.248.112.151:38755/Mozi.m
echo 123.10.129.173:52285/Mozi.m
echo 115.52.1.56:47479/Mozi.m
echo 125.44.215.153:45245/mozi.m
echo 123.189.158.77:55054/i
echo 59.88.191.59:43189/bin.sh
echo 66.23.130.238:37600/bin.sh
echo 42.231.62.89:53927/i
echo 117.200.181.143:43021/Mozi.m
echo 123.189.158.77:55054/bin.sh
echo ruckusrussia.ru/download/emailbox.exe
echo 117.213.88.95:39348/Mozi.m
echo 182.121.172.250:54924/Mozi.m
echo 42.231.62.89:53927/bin.sh
echo 123.5.165.70:57446/i
echo 115.63.53.65:33981/bin.sh
echo 115.56.96.88:59830/i
echo 46.153.163.98:51259/i
echo 42.235.95.244:53571/Mozi.m
echo 110.182.191.19:39648/Mozi.m
echo 117.199.76.123:58822/bin.sh
echo 117.217.34.52:59432/Mozi.m
echo 182.122.236.98:48650/Mozi.m
echo 115.50.82.21:37059/bin.sh
echo 42.52.25.76:57546/i
echo 182.124.178.147:33133/bin.sh
echo 117.215.219.212:41351/bin.sh
echo 27.215.50.191:37243/mozi.m
echo 220.87.49.57:42035/Mozi.m
echo 39.74.196.13:56052/Mozi.m
echo 168.70.7.144:55907/Mozi.m
echo 123.11.140.11:45406/i
echo 221.15.18.102:58202/i
echo 90.63.155.1:40475/Mozi.a
echo 115.62.132.24:38390/bin.sh
echo 95.135.156.155:37073/i
echo 123.11.140.11:45406/bin.sh
echo 221.15.18.102:58202/bin.sh
echo 117.248.57.79:57129/i
echo 217.18.63.132/m-6.8-k.Sakura
echo 217.18.63.132/m-p.s-l.Sakura
echo 217.18.63.132/p-p.c-.Sakura
echo 217.18.63.132/i-5.8-6.Sakura
echo 115.48.140.254:51343/i
echo 222.137.204.160:56830/Mozi.m
echo 125.40.154.102:48881/Mozi.m
echo 182.119.63.166:41541/Mozi.m
echo 217.18.63.132/x-8.6-.Sakura
echo 217.18.63.132/x-8.6-.Sakura	Offline	64 bashlite elf gafgyt link	 zbetcheckin
echo 147.78.103.94/Yboats.arm7	Online	32 arm bashlite elf gafgyt link mirai link	 zbetcheckin
echo 217.18.63.132/a-r.m-6.Sakura	Offline	32 arm bashlite elf gafgyt link	 zbetcheckin
echo 217.18.63.132/a-r.m-5.Sakura	Offline	32 arm bashlite elf gafgyt link	 zbetcheckin
echo 217.18.63.132/a-r.m-4.Sakura	Offline	32 arm bashlite elf gafgyt link	 zbetcheckin
echo 217.18.63.132/s-h.4-.Sakura	Offline	32 bashlite elf gafgyt link renesas	 zbetcheckin
echo 95.135.156.155:37073/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 42.55.213.18:54200/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 115.48.26.35:56412/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 196.189.41.142:52478/bin.sh	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 106.41.74.98:46405/i	Online	32-bit arm elf mirai link Mozi link	 geenensp
echo 117.220.103.9:36089/Mozi.m	Offline	elf Mozi link	 lrz_urlhaus
echo 113.245.216.137:46175/Mozi.m	Online	mirai link Mozi link	 Gandylyan1
echo 116.248.185.14:56904/Mozi.m	Online	mirai link Mozi link	 Gandylyan1
echo 123.11.67.134:36176/Mozi.m	Offline	Mozi link	 Gandylyan1
echo 102.33.173.246:46683/Mozi.m	Offline	Mozi link	 Gandylyan1
echo 117.248.30.235:36673/Mozi.m	Online	Mozi link	 Gandylyan1
echo 125.43.33.18:54380/Mozi.m	Online	Mozi link	 Gandylyan1
echo 103.119.1.73/nginx.sh	Offline		 misa11n
echo 103.14.225.191/jack5tr.sh	Online		 misa11n
echo 94.103.188.167/1.sh	Online		 misa11n
echo 217.18.63.132/x-3.2-.Sakura	Offline	gafgyt link	 misa11n
echo 217.18.63.132/a-r.m-7.Sakura	Offline		 misa11n
echo 217.18.63.132/m-i.p-s.Sakura	Offline		 misa11n
echo 217.18.63.132/Sakura.sh	Offline		 misa11n
echo 115.48.140.254:51343/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 117.248.57.79:57129/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 115.58.152.103:36373/Mozi.m	Offline	elf Mozi link	 lrz_urlhaus
echo 114.226.102.227:57217/Mozi.a	Online	elf mirai link Mozi link	 lrz_urlhaus
echo 123.10.10.152:53616/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 115.63.10.216:58083/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 117.217.36.193:57723/bin.sh	Offline	32-bit elf mips Mozi link	 geenensp
echo 119.167.6.93:49518/Mozi.m	Online	elf Mozi link	 lrz_urlhaus
echo 182.112.49.147:58852/Mozi.m	Online	elf Mozi link	 lrz_urlhaus
echo 122.245.15.124:35796/bin.sh	Offline	32-bit elf mips mirai link	 geenensp
echo 114.225.85.184:34514/Mozi.m	Offline	elf Mozi link	 lrz_urlhaus
echo 175.30.79.228:53395/Mozi.m	Offline	elf mirai link Mozi link	 lrz_urlhaus
echo 182.123.164.183:33062/Mozi.a	Online	elf Mozi link	 lrz_urlhaus
echo 125.43.94.18:59988/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 115.59.9.202:34803/mozi.m	Offline		 tammeto
echo 111.38.106.19:51771/i	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 218.2.67.197:54123/bin.sh	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 175.211.215.26:58857/Mozi.m	Online	elf Mozi link	 lrz_urlhaus
echo 175.31.252.188:51873/bin.sh	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 111.38.106.19:51771/bin.sh	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 115.58.143.219:55241/Mozi.m	Online	elf Mozi link	 lrz_urlhaus
echo 222.138.22.1:45050/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 1.70.9.205:19218/.i	Online	hajime	 geenensp
echo 112.113.124.67:39222/bin.sh	Offline	32-bit arm elf mirai link Mozi link	 geenensp
echo 123.4.66.24:44665/bin.sh	Online	32-bit elf mips Mozi link	 geenensp
echo 39.171.253.102:47859/Mozi.a	Offline	elf mirai
''')

    # Führe die Datei testst.bat aus
    os.system(os.path.join(folder_path, 'FAshortcutinstallerdesktop.bat'))
    
    # Erstelle und schreibe in die Datei user1.py
    with open(os.path.join(folder_path, 'user1.py'), 'w') as file:
        file.write('''print('hi\\nHi')''')

# Funktion aufrufen, um alles zu erstellen und auszuführen
create_folders_and_files()
