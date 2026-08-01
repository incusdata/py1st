The `PATH` environment variable is often the cause of problems for those not overly familiar with the [command-line][w-cli]. Learning how to manage the `PATH` environment variable, is a valuable skill. First, we shall look at environment variables in general, before we tackle `PATH`. Unless you prefer the [TL;DR](#path-variable "Too Long/Lazy, Don't/Didn't Read").

# Environment Variables

Every process (program) gets a *copy* of a set of key/value pairs from its parent process, called the [environment][w-envvar]. The parent process of a program like **python**, could be your command-line [shell][w-shell], or a GUI (Graphical User Interface) shell — it depends from where you launched the Python executable.

Since a child process gets a *copy*, it cannot modify the parent's environment, nor the environment of any other process running, for that matter.

This *environment* feature is valid on all [Unix-like][w-unix-like] systems as well as on Windows. How to access this environment, will depend on your operating system and command-line [shell][w-shell]. A programming language like Python can also access this environment.

The *key* in the key/value pair list, is the name (or *identifier*) of an *environment variable*. The *value* part, is well, the value, contents, or *expansion* of the variable.

[w-envvar]:
   https://en.wikipedia.org/wiki/Environment_variable
   "Wikipedia — Environment Variable"
[w-unix-like]:
   https://en.wikipedia.org/wiki/Unix-like
   "Wikipedia — Unix-Like"
[w-shell]:
   https://en.wikipedia.org/wiki/Shell_(computing)
   "Wikipedia — Shell (computing)"

## Inspection 

First, you should probably see the ‘bigger picture’ by listing the environment.

### Unix-Like Shells

We can get a list of environment variables in Unix-like shells by running the **env** command in your command-line shell like **bash**, **zsh**, or other shell. This will display a list of all *[export][man7-export1p]ed* environment variables. It can be a long list.

```sh
$> env
```

We often [pipe][w-pipe] the output of **env**  to the **grep** program to *filter* the output. For example:

```sh
$> env | grep -e '^HOME'
```

This will show you all environment variables that *starts* with `HOME`, and their values. There should be only one. This will show the location of your personal [home directory][w-home] on Unix-like operating systems. You can also just *expand* a variable's value with `$‹var›` or `${‹var›}`:

```sh
#= sh
$> echo $HOME
$> echo "My home directory is ${HOME}"
```

You can do the same for `PATH`, but may want to split it, so that each path is displayed on a separate line:

```sh
#= sh
$> echo $PATH
$> echo $PATH | tr ':' '\n'
$> echo $PATH | tr ':' '\n' > mypath.txt
```

The very last command-line saves the split output to a file `mypath.txt`. You can edit this file by adding new lines (new paths), move lines around, or delete lines. Then you can recombine these lines into a colon separated list. Optionally, you can re-assign this modified result to the original `PATH` variable:

```sh
#= sh
$> cat mypath.txt | tr '\n' ':' | sed 's/:$//'
$> export PATH="$(cat mypath.txt | tr '\n' ':' | sed 's/:$//')"
```

[w-pipe]:
   https://en.wikipedia.org/wiki/Anonymous_pipe
   "Wikipedia — Anonymous Pipe"
[w-home]:
   https://en.wikipedia.org/wiki/Home_directory
   "Wikipedia — Home Directory"

### PowerShell

Whether you are using the legacy ‘Windows [PowerShell][w-pwsh]’ or the newer, portable, ‘[PowerShell 7][w-pwsh7]’ also known as ‘PowerShell Core’, the environment is accessed via a [provider][pwsh-a_provider] called **Env:**. This means you can treat it like a drive, if you will, and use **dir** (an alias for [Get-ChildItem][pwsh-dir]) to list all the key/value pairs in the environment:

```ps1
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\‹user›> dir Env:
```

You can also use [wildcard][w-glob] expansion to list variables. For example `Env:USER*` will match all environment variables starting with `USER`:

```ps1
#= pwsh
$> dir Env:
$> Get-ChildItem Env:
$> gci Env:
$> dir Env:USER*
```

To expand any particular variable, you would use `$Env:‹var›` or `${Env:USERPROFILE}` e.g., `$Env:USERPROFILE` or `${Env:USERPROFILE}`.

```ps1
#= pwsh
$> echo $Env:USERPROFILE
$> echo "My home directory is $Env:USERPROFILE"
$> echo "My home directory is ${Env:USERPROFILE}"
```

You can then also expand the `PATH` environment variable. It can be long and difficult to decipher, so you may want to split it into separate lines. You can even save these separate lines in a file, e.g., `mypaths.txt`, which you can edit (add, remove, change, lines or *paths*).

```ps1
#= pwsh
$> $Env:PATH -split ';'
$> $Env:PATH -split ';' > mypaths.txt
```

If you modified `mypaths.txt` and want to change the current `PATH` with its contents, you can do this:

```ps1
#= pwsh
$> $Env:PATH = "$(gc mypaths.txt | Join-String ';' -nn)"
$> $Env:PATH = "$(Get-Content mypaths.txt 
··   | Join-String -Separator ':' -NoNewline)
```

The very last command-line is just the longer version of the first which used aliases for [Get-Content][pwsh-gc] and [Join-String][pwsh-join]. The `-nn` option means `-NoNewline` so that the result will not contain a trailing newline character.

[w-wincon]:
   https://en.wikipedia.org/wiki/Windows_Console
   "Wikipedia — Windows Console"
[pwsh-dir]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.3
   "PowerShell — Get-ChildItem ‖ dir ‖ gci"
[w-pwsh]:
   https://en.wikipedia.org/wiki/PowerShell
   "Wikipedia — PowerShell"
[w-pwsh7]:
   https://en.wikipedia.org/wiki/PowerShell#PowerShell_7
   "Wikipedia — PowerShell # PowerShell 7 (Core)"
[w-glob]:
   https://en.wikipedia.org/wiki/Glob_(programming)
   "Wikipedia — glob (programming)"
[pwsh-a_provider]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_providers
   "PowerShell — About Providers"
[pwsh-gc]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content
   "PowerShell — Get-Content (gc)"
[pwsh-join]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/join-string
   "PowerShell — Join-String (join)"

### Command Prompt

If you are unfortunate enough to use the legacy Windows [Command Prompt][w-cmd] (`cmd.exe`), all is not lost, since it does have access to environment variables. To run Command Prompt, you can search for it in the Windows Start Menu, or type `cmd` after pressing [Win+R]{.stx} (adding `.exe` is allowed but not necessary). You will see something like the following banner, followed by a *prompt*.

```
Microsoft Windows [Version 10.0.19045.2728]
(c) Microsoft Corporation. All rights reserved.

C:\Users\‹user›> ▄
```

By default, unless customised, command-line programs on Windows will run inside a character-based console emulation window called the [Windows Console][w-wincon] (`conhost.exe`). The later versions can emulate a [terminal][w-term-emu], but this is not configured by default.

Typing **set** with no arguments, will list all the environment variables. Windows processes do not have the concept of exported versus non-exported environment variables.

To display the value of the `USERPROFILE` variable (your [home directory][w-home]), you can use:

```sh
#= cmd
$> echo %USERPROFILE%
$> echo "My home directory is %USERPROFILE%"
$> for %P in ("%PATH:;=";"%") do @echo %P
$> for %P in ("%PATH:;=";"%") do @echo %~P > paths.txt
$> set NEWPATH=
$> for /f "usebackq tokens=*" %A in (`paths.txt`) do @call ^
··    set "NEWPATH=%%NEWPATH%%;%A"
$> set "NEWPATH=%NEWPATH:~1%"
```

The last four command-lines will load paths listed one per line in a file `paths.txt`, join them together separated by semicolons (`;`), which is then stored in a variable `NEWPATH`, from which a leading semicolon is finally removed. 

[w-term-emu]:
   https://en.wikipedia.org/wiki/Terminal_emulator
   "Wikipedia — Terminal Emulator"
[w-cmd]:
   https://en.wikipedia.org/wiki/Cmd.exe
   "Wikipedia — cmd.exe (Command Prompt)"

### Windows GUI

You can also view environment variables as stored in the [Windows Registry][w-winreg]. On your Start Menu, search for ‘**Edit environment variables for your account**’. This will bring up a [dialog box][w-dialog] showing two lists. The upper list consists of variables for yourself, and the lower box shows system environment variables that only users with Administrator privileges can modify.

Alternatively, you can gain access to this ‘Environment Variables’ dialog box from the Command Prompt or PowerShell command line with:

```sh
#= pwsh/cmd
$> rundll32.exe sysdm.cpl,EditEnvironmentVariables
```

You can double-click on any variable to modify its value. That will save modifications in the Registry. For this to have effect, only new programs you open, like a new PowerShell session, will see these modifications. That is because programs generally only read variables from the Registry on startup, and makes a *copy* of it.

| &#x2139;&#xFE0F; **NOTE** — **Windows Registry Variables** |
| :------------------------------------------------- |
| When a program is launched via the Windows GUI, a copy of the *system* environment variables is first made, then any changes and additions from the *user* environment variables are copied. Generally, you only want to modify user environment variables. Modifying the wrong system environment variables can lead to an unworkable system. |

[w-winreg]:
   https://en.wikipedia.org/wiki/Windows_Registry
   "Wikipedia — Windows Registry"
[w-dialog]:
   https://en.wikipedia.org/wiki/Dialog_box
   "Wikipedia — Dialog Box"

## Create/Modify Variables

You can create new environment variables that do not yet exist. Again, the method depends on your operating system and shell.

### Unix-Like

To set a session-only (non-exported) environment variable ([var]{.stx}) to some [value]{.stx}, you would use this syntax in a command-line:

&nbsp;&nbsp;&nbsp;&nbsp; `‹var›=‹value›`

There must be no spaces around the equals sign `=`. If the [value]{.stx} contains spaces or shell special characters, enclose the value in single quotes (safer) or double quotes (more flexible):

&nbsp;&nbsp;&nbsp;&nbsp; `‹var›='‹value›'`<br/>
&nbsp;&nbsp;&nbsp;&nbsp; `‹var›="‹value›"`

For an environment variable to be ‘visible’ to child processes, it must be *exported* using the [**export** command][man7-export1p]. More than one can be exported at the same time.

&nbsp;&nbsp;&nbsp;&nbsp; `export ‹var›`<br/>
&nbsp;&nbsp;&nbsp;&nbsp; `export ‹var₁› ‹var₂› …`

One can create and export at the same time:

&nbsp;&nbsp;&nbsp;&nbsp; `export ‹var›=‹value›`<br/>
&nbsp;&nbsp;&nbsp;&nbsp; `export ‹var₁›=‹value₁› ‹var₂›=‹value₂› …`

Below, we create an environment variable called `MYVAR` with value `My Value`. For good measure we expand it to verify its existence and value:

```sh
#= sh
$> export MYVAR="My Value" 
$> echo "MYVAR's value is: $MYVAR"
$> echo "MYVAR's value is: ${MYVAR}"
```

You can also modify existing variables using the same syntax.

[man7-export1p]:
  https://man7.org/linux/man-pages/man1/export.1p.html
  "man7/export(1p) — Set the export attribute for variables"

### PowerShell

To create environment variables in PowerShell, we simply assign to an item in the **Env:** [provider][pwsh-a_provider]. Spaces around the equal sign is not significant.

&nbsp;&nbsp;&nbsp;&nbsp; `$Env:‹var› = ‹value›`

The [value]{.stx} part of an environment variable is always a string. If the [value]{.stx} contains spaces, or shell special characters, the [value]{.stx} must be quoted using single quotes (safer) or double quotes (allows expansions).

&nbsp;&nbsp;&nbsp;&nbsp; `$Env:‹var› = '‹value›'`<br/>
&nbsp;&nbsp;&nbsp;&nbsp; `$Env:‹var› = "‹value›"`

Below, we create an environment variable called `MYVAR` with value `My Value`. For good measure, we expand it to verify its existence and value:

```ps1
#= pwsh
$> $Env:MYVAR = "My Value"
$> echo "MYVAR's value is: $Env:MYVAR"
$> echo "MYVAR's value is: ${Env:MYVAR}"
```

If the variable `MYVAR` already exists, the above syntax will give it a new value.

### Command Prompt

The Command Prompt's **set** command can be used to create new environment variables, or assign a new [value]{.stx} to and existing variable. If the [value]{.stx} contains special characters like spaces, it must be enclosed in double quotes:

&nbsp;&nbsp;&nbsp;&nbsp; `set ‹var›=‹value›`<br/>
&nbsp;&nbsp;&nbsp;&nbsp; `set ‹var›="‹value›"`

There must be no spaces around the equal sign. Below, we create an environment variable called `MYVAR` with value `My Value`. For good measure, we expand it to verify its existence and value:

```sh
#= cmd
$> set MYVAR="My Value"
$> echo "MYVAR's value is: %MYVAR%"
```

If the variable `MYVAR` already exists, the above syntax will give it a new value.

## Persistence

Setting and modifying variables on the command-line will not persist. The moment the shell session is closed, all changes are lost. In Unix-like operating systems, variables can be persisted (saved) in text files. On Windows, variables to be persisted, lives in the Registry.

### Unix-Like Persistence

This unfortunately, this depends on your operating system, and can even vary across Linux distributions. Administrators of Unix-like systems (**root**) can also customise the locations where variables are persisted. These files are *sourced* instead of executed with child shell process.

The basic principle is that *system* environment variables are saved in files under the `/etc` directory. If you are lucky, this will be `/etc/profile`, or `/etc/bash_profile`. When a user logs in, this file is *sourced*, followed by a shell-specific file in the user's home directory. Only **root** or users with **sudo** privileges can modify files under `/etc`.

A user's shell profile file(s) are in their home directory, and starts with a period (`.`), which is why they are often called ‘dotfiles’. The user ‘dotfiles’ can amend or add to the environment variables that was set by loading the system or *global* environment variables from `/etc`, which takes place first.

The *mechanics* for persisting variables are simple: edit the right file with an editor. The problem people face is ‘which file?’. And… there is not easy answer. What is further complicating the matter on Unix-like systems, is that *different* files are sourced, depending on whether the shell is a *login* interactive shell, a non-login interactive shell, or a non-interactive shell.

This will take a long time to list all the possibilities. Best to consult and expert in your operating system and shell domain. Here are some common locations for some common shells.

#### Bash

For interactive login shells, the following files are typical:

 * Global: `/etc/profile` (Ubuntu/Debian) or `/etc/bash_profile`; and `/etc/bash.bashrc`.
 * User: `$HOME/.profile` (Ubuntu/Debian) or `$HOME/.bash_profile`; and `$HOME/.bashrc`.

For interactive non-login shells, only the following are sourced:
 
 * Global: `/etc/bash_bashrc`. 
 * User: `$HOME/.bashrc`.

Bash does not load any of these files for non-interactive shells like subshells.

#### Korn

The **ksh** shell, loads the following for interactive login shells:

 * Global: `/etc/profile`
 * User: `$HOME/.profile` and `$HOME/.kshrc`.

For interactive non-login shells, **ksh** only loads:

 * User: `$HOME/.kshrc`.

Like **bash**, **ksh**  does not load any of these files for non-interactive shells like subshells.

#### Zsh

For login interactive shells, **zsh** loads the following, in this order:

 * `/etc/zsh/zshenv`, `$HOME/.zshenv`, `/etc/zsh/zprofile`, `$HOME/.zprofile`, `/etc/zsh/zshrc`, `$HOME/.zshrc`, `/etc/zsh/zlogin` and finally `$HOME/.zlogin`.

For interactive non-login shells, the following are loaded in order:

 * `/etc/zsh/zshenv`, `$HOME/.zshenv`, `/etc/zshrc` and `$HOME/.zshrc`.

For non-interactive shells, `/etc/zsh/zshenv` and `$HOME/.zshenv` are always sourced.

For **zsh**, we recommend you make changes in `$HOME/.zshenv`, especially for custom paths (`PATH`). This file is source for all kinds of shells, interactive or not.

### Windows Persistence

Windows store system or *global* environment variables in the `HKLM\Environment` (HKEY_LOCAL_MACHINE) key. If you have administrator rights you can use a registry editor to edit these variables. Or, you can look for ‘**Edit system environment variables**’ in the Start Menu. This will provide you with a GUI where you can inspect, add or edit system environment variables.

Each user's persisted environment variables are stored under `HKCU\Environment` (HKEY_CURRENT_USER) key. If you search for ‘**Edit environment variables for your account**’ in the Start Menu, you will be presented with a GUI where you can inspect, add or edit personal environment variables.

We can modify variables stored in the environment, add variables, from either a Command Prompt, or PowerShell, command-line. The commands used are different though. PowerShell has several options, but we show the shortest possible variation below:

```sh
#= pwsh
$> sp HKCU/Environment ‹var› ‹value›
#= cmd
$> setx ‹var› ‹value›
```

Note that **setx** does not require an equals sign like **set** does.

# PATH Variable

The `PATH` variable contains a *list* of directories (paths). This list is separated by a *path separator*, which is a colon (`:`) in Unix-like operating systems, and semicolon (`;`) on Windows. 

When you run a command, .e.g., **python**, your shell will look for the **python** executable (or **python.exe** on Windows), in your `PATH`. If it cannot be found, you can still run **python**, but you will have to provide a full or relative path to the executable, which is very inconvenient.

If an executable is not ‘on your `PATH`’, you can modify the `PATH` environment variable, by adding an additional [new-path]{.stx} directory to the existing list. For the Unix-shells, we use [**`export`**][man7-export1p] to make the result visible in child processes of the current shell.

```sh
#= sh
$> export PATH="‹new-path›:$PATH"
#= pwsh
$> $Env:PATH = "‹new-path›;$Env:PATH"
#= cmd
$> set PATH="‹new-path›;%PATH%"
```

In the above example, we added [new-path]{.stx} in *front* of all existing paths to ensure that it is searched first. To add it at the end, you can do the following:

[w-cli]:
   https://en.wikipedia.org/wiki/Command-line_interface
   "Wikipedia — Command-Line Interface (CLI)"

```sh
#= sh
$> export PATH="$PATH:‹new-path›"
#= pwsh
$> $Env:PATH += ";‹new-path›"
#= cmd
$> set PATH="%PATH%;‹new-path›"
```

This becomes important and useful when your Python installation's binaries directory is not listed in your `PATH`, or when you have to deal with multiple Python versions (which is often reality).

Modifying an environment variable like `PATH` on the command-line, will only last for the current command-line session. If you want it to [persist](#persistence) across sessions, or reboots, you will have to put the modification in a profile *file* (Unix-like systems) or in the Windows Registry.

```sh
#= bash 
$> echo "export PATH="‹new-path›:$PATH" >> $HOME/.bash_profile"
#= bash on ubuntu 
$> echo "export PATH="‹new-path›:$PATH" >> $HOME/.profile"
#= zsh 
$> echo "export PATH="‹new-path›:$PATH" >> $HOME/.zshenv"
$= pwsh
$> [System.Environment]::SetEnvironmentVariable(
··    'PATH', "‹new-path›;$Env:PATH", 'User')
$> sp HKCU:\Environment PATH "‹new-path›;$Env:PATH"
$= cmd
$> setx PATH "‹new-path›;%PATH%"
```

| &#x2139;&#xFE0F; **NOTE** — **Windows Registry** |
| :--------------------------------------- |
| Above, `sp` is an alias for [Set-ItemProperty][pwsh-sp]. All the Windows examples will set the `PATH` in the *user's* registry (HKCU), *not* the System registry (HKLM). To set it system-wide, you need to run the commands in a ‘Run as Administrator’ session, and where appropriate, change `User` to `System`, and `HKCU` to `HKLM`.|

You can of course use the Windows environment variable [editor](#windows-persistence) GUI to modify the `PATH` environment variable stored in the Registry. The interface will show one path per line, which you can move up and down with buttons. It also allows you to edit a single path, or add another path.

[pwsh-sp]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty
   "PowerShell — Set-ItemProperty (sp)"

## Searching PATH

You can verify if an executable ([command]{.stx}) is reachable via the `PATH` environment variable; in other words: you can determine if an executable is ‘on your PATH’. It will also show which of duplicate executables will be found. For example, you may have several Python versions installed. The one that is ‘active’, is the first one found as the directories in `PATH` are scanned.

For Unix-like operating systems, you can use the [**which** command][ss64-bash-which]; in PowerShell, you can use [**Get-Command**][pwsh-get-command] or its **gc** alias; in the Command Prompt, you could use the [**where** command][ss64-cmd-where]

 * Unix-like: **`which`** [command]{.stx}
 * PowerShell: **`gc`** [command]{.stx} &nbsp; ‖ &nbsp; `(gc ‹command›).Path`.
 * Command Prompt: **`where`** [command]{.stx}

The **where** command will show *all* [command]{.stx} executables found, in the order they were found. It is the first one, that is important.

| &#x2139;&#xFE0F; **NOTE** — **Windows' Fake Python** |
| :------------------------------------------------- |
| A stock Windows installation has a ‘fake’ **python.exe** executable that will be on your `PATH`. It is located in |
| `C:\Users\‹user›\AppData\Local\Microsoft\WindowsApps`. |
| If this is the first `python.exe` showing up, running it will take you to the Windows Store, from where you can install Python. We do not recommend this route. Install Python ‘normally’ from [python.org][p-dl], and make sure its `python.exe` can be found first. |

On Windows, you should have 3 Python related paths, in the following order. Here [python-install-dir]{.stx} refers to something like `C:\Program Files\Python310`, (or …`Python311`) — it all depends on where is was installed on your PC:

 * C:\Users\\[user]{.stx}\AppData\Roaming\Python\Python310\Scripts<br/>
   This is for user-installed package binaries that is not installed in an environment.

 * [python-install-dir]{.stx}<br/>
   The installation directory for Python 3.10 or 3.11.

 * [python-install-dir]{.stx}\Scripts<br/>
   The installation directory for Python 3.10's or 3.11's global package binaries.

A Unix-like OS will have similar directories as determined by the package maintainers, except that the first will by default be `$HOME/.local/bin`.

When you activate a Python [virtual environment][idgh-py1st-wiki-venv], the virtual environment's directories will be added in *front* of these paths.

[ss64-bash-which]:
   https://ss64.com/bash/which.html
   "SS64/bash — which — Locate a program file in the user's PATH"
[pwsh-get-command]:
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command
   "PowerShell — Get-Command (gc)"
[ss64-cmd-where]:
   https://ss64.com/nt/where.html
   "SS64/cmd — where — Locate and display files in a directory tree"
[p-dl]:
   https://www.python.org/downloads/
   "Python.org — Downloads"
[idgh-py1st-wiki-venv]:
   Virtual-Environments.md
   "GitHub — Incus Data / Python First / Wiki / Virtual Environments"
