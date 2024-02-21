<br>

A basic template for ...

<br>

### Steps

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
















