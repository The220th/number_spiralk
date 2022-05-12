#!/bin/bash 

ffmpeg -f image2 -framerate 1 -i image%d.png demo.gif