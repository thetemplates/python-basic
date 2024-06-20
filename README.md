<br>

A basic template for Python projects.  These notes are incomplete and a few programs are pending, but the structure and programs are in line with language standards and team norms: in progress.

<br>

_develop_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

_master_<br>
[![Templates](https://github.com/thetemplates/python-basic/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/thetemplates/python-basic/actions/workflows/main.yml)

<br>

### Remote Environment

Building an image for remote development, i.e., development via a container, requires

* Dockerfile
* requirements.txt

Study this project's examples, subsequently build an image using the command

```shell
docker build . --file .devcontainer/Dockerfile -t python-basic
```

Next, print the machine's list of images

```shell
docker images
```

The output should include

| repository   | tag    | image id | created  | size     |
|:-------------|:-------|:---------|:---------|:---------|
| python-basic | latest | $\ldots$ | $\ldots$ | $\ldots$ |

**In progress ...**


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
