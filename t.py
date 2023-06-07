import subprocess as sub
import os


username = testUser
passwds = passwordTest

command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwds) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Add-LocalGroupMember -Group "Administrators" -Member $nusnm
Get-LocalUser
"""
print(command)
exec = sub.Popen(["powershell","& {" + command + "}"])