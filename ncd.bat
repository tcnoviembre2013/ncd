@ECHO OFF
SET MYVAR=.
recorredir.py %1%
recorredir.py %1%> Output
SET /p MYVAR=<Output
DEL Output
cd "%MYVAR%" 
echo Cambio al directorio %MYVAR%
