<# Example PowerShell `CurrentUserAllHost` Profile #>

$OutputEncoding = [Console]::InputEncoding `
   = [Console]::OutputEncoding `
   = [Text.Encoding]::UTF8
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

$PSStyle.OutputRendering = [Management.Automation.OutputRendering]::Host
$PSStyle.FileInfo.Directory = "`e[96;1m"

Remove-Alias cp,rm,ls,cat,echo,cpp,tee `
   -Force -ErrorAction SilentlyContinue

# if you want a `touch` equivalent on PowerShell:
function touch {
    param (
        [string]$path
    )
    if (Test-Path $path) {
        (Get-Item $path).LastWriteTime = Get-Date
    } else {
        New-Item -Path $path -ItemType File
    }
}
