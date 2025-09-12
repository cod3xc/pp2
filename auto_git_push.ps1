Set-Location "C:\pp2"
git add .
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "��������������: $timestamp"
git push origin main
