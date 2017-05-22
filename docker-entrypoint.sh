#!/bin/sh
service mysql start
service mongodb start
/usr/local/bin/jupyter-notebook --ip 0.0.0.0 --allow-root --notebook-dir /curso-python
