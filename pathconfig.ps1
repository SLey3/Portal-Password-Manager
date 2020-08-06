$PATH = [Environment]::GetEnvironmentVariable("PATH")
$modulePATH = $env:USERPROFILE + "\AppData\Local\Programs\Portal Password Manager\Lib\site-packages"
[Environment]::SetEnvironmentVariable("PATH", "$PATH;$modulePATH")
