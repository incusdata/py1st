<# Circle Calculator in PowerShell
#>
$radius = Read-Host -Prompt "Radius?"
$circum = 2.0 * [Math]::PI * $radius
$area   = [Math]::PI * [Math]::Pow($radius, 2.0)

Write-Output ("Radius : {0,10:N2}" -f $radius)
Write-Output ("Circum.: {0,10:N2}" -f $circum)
Write-Output ("Area   : {0,10:N2}" -f $area)
