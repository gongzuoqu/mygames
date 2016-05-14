set BASEFOLDER=D:\dev
set CWD=%CD%

set PYTHON=%BASEFOLDER%\Python34

IF "%1" == "27" (
set PYTHON=%BASEFOLDER%\Python27
)

set PYTHONPATH=%PYTHON%\Scripts;%BASEFOLDER%\bin\py
set GIT=D:\VFI\tools\Git\bin
set PATH=%PYTHON%;%PYTHONPATH%;%GIT%
