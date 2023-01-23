goto :DOES_PYTHON_EXIST
:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)
goto :EOF
:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
echo Now opeing the download URL.
start "" "https://www.python.org/downloads/windows/"
goto :EOF
:PYTHON_DOES_EXIST
for /f "delims=" %%V in ('python -V') do @set ver=%%V
pip install discord
pip install youtube_dl
pip install BeautifulSoup
pip install bs4
pip install asyncio
pip install youtube-search-python
pip install urllib
pip install colorama
pip install pytube
goto :EOF