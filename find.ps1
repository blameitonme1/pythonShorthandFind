$PSDefaultParameterValues['*:Encoding'] = 'utf8'
$pythonScriptPath = "D:\Project\pyFind\main.py"
$userInput = Read-Host "type 1 for open exe, 2 for set shorthand name"
if($userInput -eq 1){
    python3 $pythonScriptPath 1
}
elseif($userInput -eq 2){
    python3 $pythonScriptPath 2
}
else {
    Write-Host "invalid input"
    # 在这里处理无效选项
}