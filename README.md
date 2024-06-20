<br>

A basic template for Python projects.  Incomplete, but the structure and programs are in line with language standards and team norms.

<br>

_develop_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

_master_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

<br>
<br>

## Environments

### Remote Development

For this Python project/template, the remote development environment requires

* [Dockerfile](.devcontainer/Dockerfile)
* [requirements.txt](.devcontainer/requirements.txt)

An image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile -t fundamentals
```

On success, the output of command

```shell
docker images
```

should include

| repository   | tag    | image id | created  | size     |
|:-------------|:-------|:---------|:---------|:---------|
| fundamentals | latest | $\ldots$ | $\ldots$ | $\ldots$ |


<br>

Subsequently, run a container, an instance, of the image `fundamentals` via:

<br>

> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
> &nbsp; &nbsp; type=bind,src="$(pwd)",target=/app fundamentals

<br>

Herein, `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment,
i.e., -w, must be inline with this project's top directory.  Get the name of the running instance of ``fundamentals`` via:

```shell
docker ps --all
```

Note, never deploy a root container, study the production [Dockerfile](Dockerfile); cf. [/.devcontainer/Dockerfile](.devcontainer/Dockerfile)

<br>

### Remote Development & Integrated Development Environments

An IDE (independent development environment) is a helpful remote development tool.  The **IntelliJ
IDEA** instructions are:

> Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** `operating system`
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

**Visual Studio Code** has its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).


<br>
<br>

## Actions

Conduct remote code 

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Analyse a directory via the command

```shell
python -m pylint --rcfile .pylintrc {directory}
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135


<br>


### pytest

Study the programs

* src.algorithms.random
* tests.algorithms.test_random

Subsequently, test the program `src.algorithms.random` via the command

```shell
python -m pytest tests/algorithms/test_random.py
```


<br>


### flake8

For code & complexity analysis.  A directive of the form

```bash
python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics src/data
```

inspects issues in relation to logic (F7), syntax (Python E9, Flake F7), mathematical formulae symbols (F63), undefined variable names (F82).  Additionally

```shell
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics src/data
```

inspects complexity.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
