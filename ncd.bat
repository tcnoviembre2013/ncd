@ECHO OFF
SET MYVAR=.
if "%2"=="-r" call :rescan
recorredir.py %1%> Output
SET /p MYVAR=<Output
DEL Output
cd "%MYVAR%" 
echo Cambio al directorio %MYVAR%
goto :eof

:rescan
echo vuelvo a escanear
recorredir.py %1 %2
goto :eof