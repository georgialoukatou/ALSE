
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import datetime
#from psychopy import psychtoolbox as ptb
from psychopy import visual, core, event, sound
#from psychopy.visual import vlc
import time, os
import csv, random
import pyglet

win = visual.Window(fullscr="TRUE")


video="/Users/admin/Documents/artificialLanguageSegmentation/pilot5/new/A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0_2.mov"
mov = visual.MovieStim3(win, video, flipVert=False)
mov.play()
mov.draw()
