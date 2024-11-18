# Python First — Course Scripts

The scripts here are not all Python scripts, and are used some courses.

### [profile.ps1](./profile.ps1) — Example PowerShell Profile

Ideally, UTF-8 should be the default encoding in PowerShell sessions on Windows. This `profile.ps1` script will set UTF-8 encoding (code page `65001` in Microsoft's terminology). Add this at the top of your [profile][ps1-profiles]. Removing the Unix-like aliases, and the `touch` function, it optional.

You can use the following PowerShell command-line to find the location of `profile.ps1` on your computer:

#### **pwsh** — *Find locations of PowerShell profiles*
```py
> $Profile | Format-List -Force
```

Prefer the `CurrentUserAllHosts` location, if you can.

[ps1-profiles]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles
   "PowerShell — About PowerShell Profiles"

### [circle01.ps1](./circle01.ps1) — Circle Calculator in PowerShell

A simple PowerShell script to introduce some input and output, and to contrast with Python scripts. You can add a [shebang/hash-bang][w-shebang] line, if you use PowerShell on Linux. It should be: `#!/usr/bin/env -S pwsh -NoProfile`. But you will lose access to embedded documentation, if any.

### [circle01.py](./circle01.py) — Circle Calculator in Python

A simple Python script to introduce some input and output, and to contrast with shell scripts. Note the [shebang/hash-bang][w-shebang] line useful in Unix environments, but not on Windows.

### [circle01.sh](./circle01.sh) — Circle Calculator in Shell Script

A simple Unix shell script to introduce some input and output, and to contrast with Python scripts. Note the [shebang/hash-bang][w-shebang] line.

[w-shebang]:
   https://en.wikipedia.org/wiki/Shebang_%28Unix%29
   "Wikipedia — Shebang (Unix)"
