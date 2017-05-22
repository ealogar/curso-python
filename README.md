# Curso python para sysadmins

Browse this course with the [online notebook viewer!](http://nbviewer.jupyter.org/github/ealogar/curso-python/tree/master/)

## Setup
If you use docker, build and run the image:

```sh
$docker build -t curso-python .
$docker run -d --name curso-python -p 8888:8888 curso-python
```

Start the container (not after first run):
After build and start you can simply start or stop your container:

```sh
$docker start curso-python
```

If you are asked by a token to access jupyter notebook:

```sh
$docker logs curso-python
```

And use the url to get access to the notebooks.

You can also run the course locally if you have python already installed (and pip)

```sh
$pip install -r requirements.txt
```


### Install jupyterhub with python3 to share locally with multiple users

See

 https://github.com/jupyterhub/jupyterhub#prerequisites

https://github.com/jupyterhub/jupyterhub/wiki/Installation-of-Jupyterhub-on-remote-server

