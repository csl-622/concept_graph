#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:42:50 2018

@author: descentis
"""
import subprocess

def runScript():
    shellscript = subprocess.Popen(["/home/descentis/research/WikiMeter/concept_network/run.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    st = "yes\n"
    stdout, stderr = shellscript.communicate(st.encode('utf-8'))   # blocks until shellscript is done
    
