It is a painful reality that we often need to manage different versions of Python and different versions of libraries for different projects. To alleviate some of this pain, [virtual environments][pg-venv] can be created, which contains a version of Python, and required libraries for a project — generally speaking, one virtual environment per project. Read the whole story below, or jump to the [Summary](#virtual-environments).

[pg-venv]:
   https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
   "Python Guide — Installing Packages Using pip and Virtual Environments # Creating a Virtual Environment"


# Environment Management

To create and maintain a virtual environment in Python, it's best to use the built-in [**venv**][pl-venv] module in Python 3. There are other third party options to create and manage virtual en&shy;vi&shy;ron&shy;ments, like [**conda**][w-conda], [**poetry**][poetry-docs], [**virtualenv**][pypa-virtualenv], etc., but **venv** is at least standard. Here we detail the steps to create, activate, and main&shy;tain a virtual environment. 

[pl-venv]:
   https://docs.python.org/3/library/venv.html?highlight=venv#module-venv
   "Python Library — venv — Creation of Virtual Environments"
[w-conda]:
   https://en.wikipedia.org/wiki/Conda_(package_manager)
   "Wikipedia — Conda (package manager)"
[poetry-docs]:
   https://python-poetry.org/docs/
   "Poetry — Documentation"
[pypa-virtualenv]:
   https://virtualenv.pypa.io/en/latest/
   "PyPa — Virtualenv"

## Create Environment

Navigate to your workspace or projects directory in your shell's command-line. For example, assuming you have a direc&shy;tory like:<br>
&nbsp;&nbsp;&nbsp;&nbsp; `$HOME/work/python` on macOS or Linux, or<br>
&nbsp;&nbsp;&nbsp;&nbsp; `$Env:USERPROFILE/work/python` on Windows.

This directory we shall designate as your [workspace]{.stx}. It can be *any* direc&shy;tory, as long as you asso&shy;ciate what&shy;ever you choose with: [workspace]{.stx}.

```sh
$> cd ‹workspace›
```

Run the following command to create a virtual environment named [venv]{.stx}; you can use any name but should follow identi&shy;fier naming rules as good practice (only alphabetic characters, and maybe underscores). Something like `pyenv`, `py310`, `myenv`, `learnenv` will be fine.

```sh
#= sh
$> python3 -m venv ‹venv› 
#= pwsh
$> python -m venv ‹venv›
```

A new directory with the name [venv]{.stx} will be created in the current directory. Run `python -m venv --help` to see other options you may find useful. (Use `python3` on Unix & Linux).

| &#x2139;&#xFE0F; **NOTE** — Python Executable Naming |
|:--------------------------------------|
| On Linux and macOS, you are normally safer running **python3** as the executable name. After you have activated an environment, both **python** and **python3** commands will run the Python executable from that enviroment. This is not an issue on Windows. |

## Activate Environment

To use this new [venv]{.stx} environment, we must *activate* it. This simply means a script is *sourced*, which sets your `PATH`, and some other en&shy;vi&shy;ron&shy;ment variables. To acti&shy;vate the virtual en&shy;vi&shy;ron&shy;ment, run the fol&shy;low&shy;ing command:

```sh
#= sh
$> . venv/bin/activate
#= pwsh
$> . venv\Scripts\Activate.ps1
```

Take note that with **bash** and **zsh**, `.` is an alias for `source`, but the latter is not in the POSIX standard. Use `source` if you only use **bash** or **zsh**. PowerShell also do not have a `source` command, although in the above case, it was not tech&shy;ni&shy;cally necessary to source the `Activate.ps1` script.

The terminal/command prompt should now show the virtual en&shy;vi&shy;ron&shy;ment's name (e.g., `(‹venv›)… `), often in colour, depending on you shell prompt customi&shy;sation. Now you can in&shy;stall packages you need in the acti&shy;vated en&shy;vi&shy;ron&shy;ment.

Useful development package to install are: **yapf**, **black**, **pylint** and **flake8**. You can optionally install **ipython** if you like a more pleasant REPL than the standard Python one. For a learning en&shy;vi&shy;ron&shy;ment, we recommend IPython without reservation.

```sh
$> pip install yapf black pylint flake8 ipython
```

For future use and virtual environment duplication, save the list of in&shy;stal&shy;led packages, by creating a **requirements.txt** file (the name is just a common con&shy;vention). You must do this every time you install new packages, update packages, or remove packages.

```sh
$> pip freeze > requirements.txt
```

## Use Environment

You can use the virtual environment for multiple projects, but probably should not. If you treat this environment as a learning and ex&shy;peri&shy;men&shy;ta&shy;tion environ&shy;ment, that will be fine. If that is the case, create some directory for your scripts, e.g., [workspace]{.stx}**/learn**.

You can install, remove or update packages. You can create, delete, edit and run Python scripts, or use Python in the **python3** (or **python**) REPL.

## Deactivate Environment

At some point, you will want to deactivate the virtual environment, which simply means the values of the original `PATH` variable will be restored, and any variables the acti&shy;vation created, will be removed.

```sh
$> deactivate
```

Your shell prompt should return to normal, indicating that no Python virtual environment is active. Your system Python should now also be first in the `PATH`.

## Maintain Environment

To update packages, install new packages, or remove existing packages, ensure the en&shy;vi&shy;ron&shy;ment is [active](#activate-environment), then use **pip**. You current working directory is not significant.

```sh
$> pip install ‹old-package₁› --upgrade
$› pip install ‹new-package›
$› pip remove ‹old-package₂›
```

You can now use these new or updated packages, as long as the environment is active.

## Duplicate Environment

Due to paths being hard-coded in certain places, mainly by **pip**, we cannot trivially copy a virtual en&shy;vi&shy;ron&shy;ment directory else&shy;where. This is where the `requirements.txt` file comes in handy.

&#x2757; **NB** — [Deactivate](#deactivate-environment) current environment first. 

<!--‼️-->
On a new machine, or different directory, [create](#create-environment) a new empty en&shy;vi&shy;ron&shy;ment. Then [activate](#activate-environment) this new environment. Now we can use **pip** and the original `requirements.txt` file, which should be copied locally.

To recreate the virtual environment, use **pip** to install package from the `requirements.txt` file:

```sh
$> pip install -r requirements.txt
```

If you get errors, re-run the above command a few times. If that does not help, you must retrace your steps or seek more experienced support.

# Docker & Podman

Using [Docker][w-docker] for a project involves creating a `Dockerfile`, building a Docker image, and running the image in a Docker container. Docker helps you create a consistent and reproducible environment across different stages of your project's lifecycle and across different machines.

[w-docker]:
   https://en.wikipedia.org/wiki/Docker_(software)
   "Wikipedia — Docker (Software)"

## Install Docker

Download and install Docker Desktop for your [platform][docker-install] (Windows, macOS). For Linux, follow the [instructions][docker-engine] for your distribution. It is [possible][dev-docker-wsl2] to install Docker inside a WSL2 distribution without using Docker Desktop for Windows.

[docker-install]:
   https://www.docker.com/products/docker-desktop
   "Docker — Docker Desktop"
[docker-engine]:
   https://docs.docker.com/engine/install/
   "Docker — Engine Install"
[dev-docker-wsl2]:
   https://dev.to/felipecrs/simply-run-docker-on-wsl2-3o8
   "Dev.To — Docker on WSL2 without Docker Desktop"

## Create a Dockerfile

In your project directory, create a file named `Dockerfile` (no file extension) The `Dockerfile` is a script that contains instructions to build a Docker image for your project

Specify the base image. Choose an official Python image from Docker Hub (https://hub.docker.com/_/python) that matches your desired Python version. For example, to use Python 3.9, start with:

```dockerfile
FROM python:3.9
```

Set the working directory inside the container:

```dockerfile
WORKDIR /app
```

Copy the `requirements.txt` file from your project into the container and install the required packages:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

Copy the rest of your project files into the container:

```dockerfile
COPY . .
```

Optionally, you can set environment variables or expose a port if your application requires them:

```dockerfile
ENV VARIABLE_NAME=value
EXPOSE 8000
```

Define the default command to run when the container starts (optional):

```dockerfile
    CMD ["python", "‹main›.py"]
```

Build the Docker image. In your terminal/command prompt, navigate to your project directory where the `Dockerfile` is located. Run the following command to build the Docker image, replacing [image-name]{.stx} with a name for your image:

```sh
$> docker build -t ‹image-name› .
```

Run the Docker container. After the image is built, you can run it in a Docker container using the following command, replacing [image-name]{.stx} with the name you used earlier:

```sh
$> docker run -it --rm ‹image-name› 
```

If you need to map ports, use the `-p` flag:

```sh
$> docker run -it --rm -p ‹host-port›:‹container-port› ‹image-name› 
```

## Manage Containers

To list all Docker images on your machine, run:

```sh
$> docker images
```

To remove a Docker image, run:

```sh
$> docker rmi ‹image-name›
```

To list all running Docker containers, run the following. Take note of the con&shy;tainer ID, which you may need for other commands.

```sh
$> docker ps
```

To stop a running Docker container, run:

```
$> docker stop ‹container-id›
```

## Python Container

By following these steps, you can use Docker to create a consistent en&shy;vi&shy;ron&shy;ment for your Python pro&shy;ject and share it with others or deploy it to pro&shy;duct&shy;ion. Here is a complete `Dockerfile` example.

```dockerfile
# Base image
FROM python:3.10-slim-buster

# Install dependencies required for code-server
RUN apt-get update && apt-get install -y \
    curl unzip git sudo

# Create a non-root user with sudo access
RUN useradd -m -s /bin/bash vscode && echo "vscode:vscode" \
    | chpasswd && adduser vscode sudo \ 
    && echo 'vscode ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vscode

USER vscode
WORKDIR /home/vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Install Python packages
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir \
    yapf flake8 black pylint ipython
```

You can put the following in a shell script to start the container and run your appli&shy;cation.

```sh
#!/usr/bin/env sh
#
# Run a docker script with a mapped port.
#
docker build -t ‹image-name› .
docker run -it --rm \
   -p ‹host-ssh-port›:‹container-ssh-port› \
   ‹image-name›
```

The `-it` option makes the container interactive. You can replace that with `-d` to detach it from the terminal instead. You can also give the container a name with `--name`, and map a host directory, to a container directory with `-v`.

```sh
docker run -d --rm --name pywork \
   -p ‹host-ssh›:‹container-ssh› \
   -v ./work:/home/vscode/work \
   pydemo
```

The `-p ‹host-ssh›:‹container-ssh›` option is optional if you do not want to access the container over SSH.

### VSCode Server

You can run VSCode in your browser using [**code-server**][gh-code-server]. You can install it in a Docker container. Here is a `Dockerfile` for Python 3.10 *and* VSCode Server. You can then us it to develop in your browser, inside the Docker container:

[gh-code-server]:
   https://github.com/coder/code-server
   "GitHub — code-server"

```dockerfile
# Base image
FROM python:3.10-slim-buster

# Install dependencies required for code-server
RUN apt-get update && apt-get install -y \
    curl unzip git sudo \
    tree vim openssh-server

COPY docker-entry.sh /tmp/docker-entry.sh

# Set up SSH
RUN mkdir /var/run/sshd \
    && echo 'PermitRootLogin yes' \
       >> /etc/ssh/sshd_config \
    && echo 'PasswordAuthentication yes' \
       >> /etc/ssh/sshd_config \
    && echo 'AllowTcpForwarding yes' \
       >> /etc/ssh/sshd_config

# Create a non-root user with sudo access
RUN useradd -m -s /bin/bash vscode \
    && echo "vscode:vscode" | chpasswd \
    && adduser vscode sudo \ 
    && echo 'vscode ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vscode

USER vscode
WORKDIR /home/vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"
ENV TERM=xterm-256color

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Python extension for VSCode
RUN code-server --install-extension ms-python.python

# Install Python package
RUN python3 -m pip install --upgrade pip && \
    pip install --no-cache-dir yapf flake8 black pylint ipython

# Set the code-server working directory
ENV CODE_SERVER_WORKING_DIRECTORY=/home/vscode/work
RUN mkdir -p ${CODE_SERVER_WORKING_DIRECTORY}

# Expose sshd & code-server ports
EXPOSE 22
EXPOSE 8080

# Start sshd & code-server
ENTRYPOINT ["sh", "/tmp/docker-entry.sh"]
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", \
     "none", "--disable-telemetry", "--disable-update-check" ]
```

The above `Dockerfile` requires a script named `docker-entry.sh` which must be present in the same directory. The script is used to start the SSH server in the background.

```sh
#!/usr/bin/env bash
# See: `ENTRYPOINT ["sh", "/tmp/docker-entry.sh"]` in Dockerfile.
sudo service ssh restart 2>/dev/null
exec "$@"
```

This will give you a setup much like the one you will find at GitHub Codespaces. Meaning, you have a Docker image running VSCode in the browser. You can connect to the container using an `ssh` client:

```sh
#= sh
$> ssh -p 2222 -o StrictHostKeyChecking=no \
··     -o UserKnownHostsFile=/dev/null vscode@localhost
#= pwsh
$> ssh -p 2222 -o StrictHostKeyChecking=no `
$>     -o UserKnownHostsFile=/dev/null vscode@localhost
```

The `-o` options are simply to avoid warnings. This is not a secure setup, but feasible for experimenting with, and learning, Python. The only dependency being Docker.

After running the container, point your browser to http://localhost:8080, which will give you access to VSCode Server inside the container.

```sh
#= sh
$> docker run -d --rm --name pywork -p:8080:8080 -p:2222:22 \
··    -v ./work:/home/vscode/work pydemo
#= pwsh
$> docker run -d --rm --name pywork -p:8080:8080 -p:2222:22 `
··    -v ./work:/home/vscode/work pydemo
```

Note that the `Dockerfile` above uses the `--auth none` flag, which disables auth&shy;enti&shy;ca&shy;tion for `code-server`. This is not re&shy;com&shy;men&shy;ded for pro&shy;duc&shy;tion use. In a real-world scenario, you should set up proper auth&shy;en&shy;ti&shy;ca&shy;tion to pro&shy;tect your develop&shy;ment en&shy;vi&shy;ron&shy;ment.

See the official [code-server documentation][gh-codeserver-readme] for more about code-server con&shy;fi&shy;gu&shy;ra&shy;tion and authentication options.

[gh-codeserver-readme]:
   https://github.com/cdr/code-server/blob/main/docs/README.md
   "GitHub — Code-Server / docs / README.md"

## Podman Alternative

[Podman][podman.io] is an alternative option as a container management tool. Podman is a [daemon][w-daemon]-less, open-source tool that provides a similar command-line interface and functionality as Docker. It is especially useful for systems where running a Docker daemon is not desired or possible. Podman can be used with the above `Dockerfile`s.

[podman.io]:
   https://podman.io/
   "Podman — Home Page"
[w-daemon]:
   https://en.wikipedia.org/wiki/Daemon_(computing)
   "Wikipedia — Daemon (computing)"

### Install Podman

For installation instructions on different Linux distributions, visit the official Podman [installation guide][podman-install]

Latest Podman is supported on Windows and macOS. You can also use a Linux virtual machine or WSL2 with a compatible Linux distribution to run Podman on these platforms.

[podman-install]:
   https://podman.io/getting-started/installation.html
   "podman.io — Getting Started / Installation"

### Build & Run Image

Podman uses a similar command-line interface as Docker, so you can use almost the same commands as before. Replace docker with podman in the commands:

```sh
$> podman build -t ‹image-name› .
$> podman run -it --rm -p 8080:8080 ‹image-name›
```

After running the container, you can access the VSCode Server in your browser at http://localhost:8080.

Using Podman, you can manage containers without a daemon and with a rootless mode, offering better security and isolation. Podman is compatible with Dockerfiles and OCI container images, making it a suitable alternative to Docker in many scenarios.

# Summary

This is all very tedious, but we're afraid that is just the current state of affairs. The sooner you become familiar with virtual en&shy;vi&shy;ron&shy;ments, the more you will benefit. Using **docker** or **podman** requires yet more in&shy;volve&shy;ment, but is a common solution.

## Virtual Environments

Assuming you have a directory in mind, which we shall represent as [workspace]{.stx}. This directory must exist; create it if necessary. In the commands below, replace `‹workspace›` with this directory. The first command will try to create this directory. It is benign.

Examples for [workspace]{.stx}

 * Unix-like OS (including WSL): `$HOME/work`.
 * Windows OS & PowerShell: `$Env:USERPROFILE\work`.
 * Windows OS & Command Prompt: `%USERPROFILE%\work`.

Under this [workspace]{.stx} directory, the following command-lines will create a `learn`  subdirectory, inside which a Python virtual environment directory called `myenv` will be created (this will also create a subdirectory called `myenv`).

A `src` subdirectory under `‹workspace›/learn` is created for Python source files (scripts).

**Linux/macOS**

```sh
#= sh ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
$> mkdir ‹workspace› 2>/dev/null
$> cd ‹workspace› ; mkdir learn ; cd learn
$> pip -m venv myenv
$> . myenv/bin/activate 
$> mkdir src ; cd src
## edit/run scripts, install packages, etc. 
$> deactivate
```

**Windows + PowerShell**

```ps1
#= pwsh ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
$> mkdir ‹workspace› -ErrorAction SilentlyContinue
$> cd ‹workspace› ; mkdir learn ; cd learn
$> pip -m venv myenv
$> . myenv\Scripts\Activate.ps1
$> mkdir src ; cd src
## edit/run scripts, install packages, etc. 
$> deactivate
```

**Windows + Command Prompt**

```sh
#= cmd  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
$> mkdir ‹workspace›
$> cd ‹workspace› ; mkdir learn ; cd learn
$> pip -m venv myenv
$> myenv\Scripts\activate.bat
$> mkdir src ; cd src
## edit/run scripts, install packages, etc. 
$> deactivate
```

## Per Session

Once a Python virtual environment exists, you only have to set your working directory and activate the virtual environment, for every new command-line session. If you use VSCode as an editor, you can point it to this environment. And of course, you only have to deactivate the environment when you are done with it. You can reactivate it any time.

Assuming your Python scripts are stored under `‹workspace›/learn/src`, every time you start a new shell session, execute these commands:

```sh
#= sh
$> cd ‹workspace›/learn/src
$> . ../myenv/bin/activate
#= pwsh
$> cd ‹workspace›\learn
$> . ..\myenv\Scripts\Activate.ps1
#= cmd
$> cd ‹workspace›\learn
$> ..\myenv\Scripts\activate.bat
```

Your current directory will be `‹workspace›/learn/src`, and you can run `code` (the VSCode executable) to start editing or create Python scripts, or run an interactive REPL.
