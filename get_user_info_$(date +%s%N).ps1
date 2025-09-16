# PowerShell script to get current user information
# Note: This script is designed for PowerShell on Windows.
# The commands used are native to PowerShell/Windows CLI.

# Get the current username
$currentUser = whoami

# Get detailed user information
$userInfo = net user $currentUser

# Get the user's home directory
$homeDir = $env:USERPROFILE

# Display the information
Write-Output "Current User: $currentUser"
Write-Output "Home Directory: $homeDir"
Write-Output "--------------------------"
Write-Output "$userInfo"