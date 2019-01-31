#!/bin/bash

sphinx-apidoc -eEM -o source/ ../src/berrymon
make html
