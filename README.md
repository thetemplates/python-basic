<br>

A basic template for Python projects.  These notes are incomplete and a few programs are pending, but the structure and programs are in line with language standards and team norms: in progress.

<br>

_develop_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

_master_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

<br>

### Remote Environment

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

> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
> &nbsp; &nbsp; type=bind,src="$(pwd)",target=/app fundamentals

Herein, `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment,
i.e., -w, must be inline with this project's top directory.  Get the name of the running instance of ``fundamentals`` via:

```shell
docker ps --all
```

<br>

### Remote Development via Integrated Development Environment




<br>

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Subsequently, analyse via

```shell
python -m pylint --rcfile .pylintrc ...
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135

* $\ldots$

**In progress ...**

<br>

### pytest

An example.  Study the programs

* src.algorithms.random
* tests.algorithms.test_random

Subsequently, test the program `src.algorithms.random` via the command

```shell
python -m pytest tests/algorithms/test_random.py
```

**In progress ...**


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
