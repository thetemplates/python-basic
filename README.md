<br>

A basic template for Python projects.  These notes are incomplete: in progress.

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

|repository|tag|image id|created|size|
|:---|:---|:---|:---|:---|
|python-basic|latest|$\ldots$|$\ldots$|$\ldots$|

<br>

### Development Notes

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Subsequently, analyse via

```shell
python -m pylint --rcfile .pylintrc ...
```

The `.pylintrc` file of this template project has been amended to adhere to team norms, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135

* And more

<br>

### Testing

An example.  Study the programs

* src.algorithms.random
* tests.algorithms.test_random

Subsequently, test the program `src.algorithms.random` via the command

```shell
python -m pytest tests/algorithms/test_random.py
```

More notes upcoming.


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>














