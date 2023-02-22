@ECHO OFF
pushd %~dp0
set PROJECT=en
call python -m sphinx -T -E -W --keep-going -b html -d build/doctrees -D language=en docs build/html
popd
