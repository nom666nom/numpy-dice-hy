#!/usr/bin/env python3

from setuptools import setup

setup(
   name='numpy-dice-hy',
   version='1.0',
   description='Dice Roller Using Numpy',
   author='White Rabbit',
   author_email='heathy@gmail.com',
   packages=['numpy-dice-hy'],  #same as name
   #scripts=['numpy-dice-hy.py'],
   install_requires=['numpy'], #external packages as dependencies
)
