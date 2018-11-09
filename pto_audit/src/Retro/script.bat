


@echo off
color 4F

SET PATH=%PATH%;C:\ProgramData\Anaconda3;c:\users\185467545\Documents\R\R-3.5.1\bin



cd C:\Repo\pto_audit\input

PAUSE

REM
REM
REM
REM     #        ###   ###     ### #        ####       #############
REM    ###       ###   ###     ###   ###    ####          #####
REM  #######     ###   ###     ###   ##     ####    	  #####
REM #########     #######      ### #        ####          #####

del /q C:\Repo\pto_audit\logs
sleep 3
del /q C:\Repo\pto_audit\report

color 6A
@echo off
@echo File Started: %date% %time%
python C:\Repo\pto_audit\src\pycontrol.py
REM forfiles  /c "cmd /c python C:\Repo\pto_audit\src\auditreader.py @path"
@echo File Completed: %date% %time%
@echo off


color 6B

sqlldr userid=pto/pto@XE control=C:\Repo\pto_audit\output\data.ctl log=C:\Repo\pto_audit\output\data_load.log DIRECT=TRUE SILENT=ALL

sqlplus  /nolog  @C:\Repo\pto_audit\src\sql\conn.sql


robocopy /MOV /S /E C:\Repo\pto_audit\input C:\Repo\pto_audit\logs /NFL /NDL /NJH /NJS /nc /ns /np

SLEEP 5

robocopy /MOV /S /E C:\Repo\pto_audit\output  C:\Repo\pto_audit\logs /NFL /NDL /NJH /NJS /nc /ns /np

Rscript.exe C:\Repo\pto_audit\src\RptGen.r
color 2F

@echo off
@echo All processing Completed: %date% %time%
REM Processing Completed. Output files are now ready!!!

@echo off



PAUSE