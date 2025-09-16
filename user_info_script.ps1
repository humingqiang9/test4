# PowerShell Script to Get Current User Information
# Note: This script is designed to run in a Linux environment with PowerShell Core installed.

# Get the current username
$username = $env:USER

# Get the user ID and Group ID
$userInfo = id
$uid = ($userInfo -split 'uid=')[1].Split('(')[0]
$gid = ($userInfo -split 'gid=')[1].Split('(')[0]

# Get the home directory
$homeDir = $env:HOME

# Display the information
Write-Host "Username: $username"
Write-Host "User ID (UID): $uid"
Write-Host "Group ID (GID): $gid"
Write-Host "Home Directory: $homeDir"