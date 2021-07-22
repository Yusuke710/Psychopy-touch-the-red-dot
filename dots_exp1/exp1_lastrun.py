#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on July 23, 2021, at 05:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'exp1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Yusuke\\Desktop\\dotsJS\\exp1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "term_and_condition"
term_and_conditionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Monash University \nStudy on visual experience\nInvestigators:\n   Prof. Naotsugu Tsuchiya, Monash University, Australia    (naotsugu.tsuchiya@monash.edu)\n   Dr Ariel Zeleznikow-Johnston, Monash University, Australia    (Ariel.Zeleznikow-Johnston@monash.edu)\n   Mr Yusuke Miyashita, Monash University, Australia    (ymiy0005@student.monash.edu)\nHello! Thank you for your interest in our study.\n\nThis experiment will take approximately 10 minutes of your time. Don't worry! Further instructions will be provided before the experiment starts, and you get three practice trials.\n\nAll data will be kept confidential. If you have any question at this stage, please contact the investigators above.\n\nClick here for a detailed version of the participant information sheet\n1. Your consent\nThis participant information sheet contains detailed information about the research project. Its purpose is to explain to you all the procedures involved in this project before you decide whether or not to take part in it. Please read this carefully. Feel free to ask questions about any information in the document. If you wish to discuss the project with a relative or friend or your local health worker, please do so.\nOnce you understand what the project is about and if you agree to take part in it, you will be asked to read and accept the Consent Form (next page). By accepting the Consent Form, you indicate that you understand the information and that you give your consent to participate in the research project.\n2. Purpose of the study\nThe aim of this study is to examine the spacial experience of human perception.\n3. What will happen to me if I participate in the study?\nYou will complete an online visual perceptual task. During this task, you will be shown images and asked to make responses.\nAll results will be de-identified at the time of examination. Please ensure you understand and accept this before providing informed consent.\n5. Possible risks\nIf you begin to feel fatigued during the study you may take a break and return to the testing a little bit later. If you find the testing too frustrating you may stop that test altogether. You may discontinue your participation in the study at any time. Your personal information will be kept confidential as outlined in Section \n4. Use of data for other projects\nData from this research project may be re-used for other related projects in a de-identified manner. Information identifying you will only be available to the researchers involved in the particular study and will not be identifiable when reported\n9. Results of Project\nIf you would like, the results of the study can be sent to you by newsletter or summary format. It is important to know that results may not be known until well after your participation in the study is completed\n10. Further Information or Any Problems\nIf you require further information or if you have any problems concerning this project, you can contact the researchers above.\n",
    font='Open Sans',
    pos=(0, 0.1), height=0.015, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Ready to start? Please press [space] to begin the experiment.',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Calibration.PNG', mask=None,
    ori=0.0, pos=(0, 0.15), size=(0.65, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press [y] to move to next step',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Calibration step:\nAdjust your head position until you see your thumb has a similar width with the black line at the center of the screen.',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
Inst = visual.ImageStim(
    win=win,
    name='Inst', 
    image='Instruction.PNG', mask=None,
    ori=0.0, pos=(0, 0.15), size=(1.2, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_13 = visual.TextStim(win=win, name='text_13',
    text='You will see an image with dots. Then the screen switches and ask you questions about the image you saw. \nPress [space] to continue\n',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='press [s] to start the prctice trial',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "practice_stimuli"
practice_stimuliClock = core.Clock()
stimuli_prac = visual.ImageStim(
    win=win,
    name='stimuli_prac', 
    image='images/20.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "practice_survey"
practice_surveyClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "start_actual"
start_actualClock = core.Clock()
key_resp_4 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='End of the practice trial.\nPress [s] to start the actual trial',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "NOMemorRep"
NOMemorRepClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='press [0] to move to next',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Please note that we are not interested in your ability to remember or  reproduce the exact location of the dots later. \nWe are interested in your experience at the moment that you were seeing the display. \nNo matter whether you can reproduce the positions of dots or not, or no matter whether you remember the location of the dots or not, please report your own experience of the dots AT THE TIME when the image was presented ',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
stimuli1 = visual.ImageStim(
    win=win,
    name='stimuli1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Survey = keyboard.Keyboard()

# Initialize components for Routine "memory_inst"
memory_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Please note that we are not interested in your ability to reproduce the exact location of the dots later. \nWe are interested in your experience at the moment that you were seeing the display. \nNo matter whether you can reproduce the positions of dots or not, please report your own experience of the dots AT THE TIME when the image was presented ',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='press [1] to move to next experiment',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mem_inst = keyboard.Keyboard()

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
stimuli1 = visual.ImageStim(
    win=win,
    name='stimuli1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Survey = keyboard.Keyboard()

# Initialize components for Routine "NO_inst"
NO_instClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Please report your own experience of the dots AT THE TIME when the image was presented\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='press [2] to move to next step',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
No_inst = keyboard.Keyboard()

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
stimuli1 = visual.ImageStim(
    win=win,
    name='stimuli1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Survey = keyboard.Keyboard()

# Initialize components for Routine "Explicit_Rep"
Explicit_RepClock = core.Clock()
key_resp_8 = keyboard.Keyboard()
text_16 = visual.TextStim(win=win, name='text_16',
    text='press [4] to move next',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Please consider whether you can remember or reproduce the exact locations of the dots you just saw.\nWe are interested in your experience at the moment that you were seeing the display. \nPlease report your own experience of the dots AT THE TIME when the image was presented ',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
stimuli1 = visual.ImageStim(
    win=win,
    name='stimuli1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Survey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "term_and_condition"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
term_and_conditionComponents = [text, key_resp, text_2]
for thisComponent in term_and_conditionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
term_and_conditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "term_and_condition"-------
while continueRoutine:
    # get current time
    t = term_and_conditionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=term_and_conditionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in term_and_conditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "term_and_condition"-------
for thisComponent in term_and_conditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "term_and_condition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
calibrationComponents = [image, text_3, key_resp_2, text_11]
for thisComponent in calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calibration"-------
while continueRoutine:
    # get current time
    t = calibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['y'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration"-------
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instructionComponents = [key_resp_3, Inst, text_13]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Inst* updates
    if Inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst.frameNStart = frameN  # exact frame index
        Inst.tStart = t  # local t and not account for scr refresh
        Inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst, 'tStartRefresh')  # time at next scr refresh
        Inst.setAutoDraw(True)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Inst.started', Inst.tStartRefresh)
thisExp.addData('Inst.stopped', Inst.tStopRefresh)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_trial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
practice_trialComponents = [text_9, key_resp_6]
for thisComponent in practice_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_trial"-------
while continueRoutine:
    # get current time
    t = practice_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_trial"-------
for thisComponent in practice_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_stimuli"-------
continueRoutine = True
routineTimer.add(0.200000)
# update component parameters for each repeat
# keep track of which components have finished
practice_stimuliComponents = [stimuli_prac]
for thisComponent in practice_stimuliComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_stimuli"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice_stimuliClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_stimuliClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stimuli_prac* updates
    if stimuli_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stimuli_prac.frameNStart = frameN  # exact frame index
        stimuli_prac.tStart = t  # local t and not account for scr refresh
        stimuli_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stimuli_prac, 'tStartRefresh')  # time at next scr refresh
        stimuli_prac.setAutoDraw(True)
    if stimuli_prac.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stimuli_prac.tStartRefresh + 0.2-frameTolerance:
            # keep track of stop time/frame for later
            stimuli_prac.tStop = t  # not accounting for scr refresh
            stimuli_prac.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stimuli_prac, 'tStopRefresh')  # time at next scr refresh
            stimuli_prac.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_stimuliComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_stimuli"-------
for thisComponent in practice_stimuliComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stimuli_prac.started', stimuli_prac.tStartRefresh)
thisExp.addData('stimuli_prac.stopped', stimuli_prac.tStopRefresh)

# ------Prepare to start Routine "practice_survey"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
practice_surveyComponents = [key_resp_5, text_12]
for thisComponent in practice_surveyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_survey"-------
while continueRoutine:
    # get current time
    t = practice_surveyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_surveyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['7', '6', '5', '4', '3', '2', '1'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_surveyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_survey"-------
for thisComponent in practice_surveyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "practice_survey" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_actual"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
start_actualComponents = [key_resp_4, text_4]
for thisComponent in start_actualComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_actualClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_actual"-------
while continueRoutine:
    # get current time
    t = start_actualClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_actualClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_actualComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_actual"-------
for thisComponent in start_actualComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start_actual" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_0 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dots_setting.xlsx'),
    seed=None, name='trials_0')
thisExp.addLoop(trials_0)  # add the loop to the experiment
thisTrial_0 = trials_0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_0.rgb)
if thisTrial_0 != None:
    for paramName in thisTrial_0:
        exec('{} = thisTrial_0[paramName]'.format(paramName))

for thisTrial_0 in trials_0:
    currentLoop = trials_0
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_0.rgb)
    if thisTrial_0 != None:
        for paramName in thisTrial_0:
            exec('{} = thisTrial_0[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "NOMemorRep"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    NOMemorRepComponents = [text_14, key_resp_7, text_15]
    for thisComponent in NOMemorRepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NOMemorRepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NOMemorRep"-------
    while continueRoutine:
        # get current time
        t = NOMemorRepClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NOMemorRepClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['0'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            text_15.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NOMemorRepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NOMemorRep"-------
    for thisComponent in NOMemorRepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_0.addData('text_14.started', text_14.tStartRefresh)
    trials_0.addData('text_14.stopped', text_14.tStopRefresh)
    # the Routine "NOMemorRep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stimuli1.setImage(images)
    # keep track of which components have finished
    stimuliComponents = [stimuli1]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli1* updates
        if stimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli1.frameNStart = frameN  # exact frame index
            stimuli1.tStart = t  # local t and not account for scr refresh
            stimuli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli1, 'tStartRefresh')  # time at next scr refresh
            stimuli1.setAutoDraw(True)
        if stimuli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                stimuli1.tStop = t  # not accounting for scr refresh
                stimuli1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli1, 'tStopRefresh')  # time at next scr refresh
                stimuli1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "survey"-------
    continueRoutine = True
    # update component parameters for each repeat
    Survey.keys = []
    Survey.rt = []
    _Survey_allKeys = []
    # keep track of which components have finished
    surveyComponents = [text_10, Survey]
    for thisComponent in surveyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "survey"-------
    while continueRoutine:
        # get current time
        t = surveyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=surveyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *Survey* updates
        waitOnFlip = False
        if Survey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Survey.frameNStart = frameN  # exact frame index
            Survey.tStart = t  # local t and not account for scr refresh
            Survey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Survey, 'tStartRefresh')  # time at next scr refresh
            Survey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Survey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Survey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Survey.status == STARTED and not waitOnFlip:
            theseKeys = Survey.getKeys(keyList=['7', '6', '5', '4', '3', '2', '1'], waitRelease=False)
            _Survey_allKeys.extend(theseKeys)
            if len(_Survey_allKeys):
                Survey.keys = _Survey_allKeys[-1].name  # just the last key pressed
                Survey.rt = _Survey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "survey"-------
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Survey.keys in ['', [], None]:  # No response was made
        Survey.keys = None
    trials_0.addData('Survey.keys',Survey.keys)
    if Survey.keys != None:  # we had a response
        trials_0.addData('Survey.rt', Survey.rt)
    trials_0.addData('Survey.started', Survey.tStartRefresh)
    trials_0.addData('Survey.stopped', Survey.tStopRefresh)
    # the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_0'


# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dots_setting.xlsx'),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "memory_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    mem_inst.keys = []
    mem_inst.rt = []
    _mem_inst_allKeys = []
    # keep track of which components have finished
    memory_instComponents = [text_5, text_6, mem_inst]
    for thisComponent in memory_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    memory_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "memory_inst"-------
    while continueRoutine:
        # get current time
        t = memory_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=memory_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *mem_inst* updates
        waitOnFlip = False
        if mem_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mem_inst.frameNStart = frameN  # exact frame index
            mem_inst.tStart = t  # local t and not account for scr refresh
            mem_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mem_inst, 'tStartRefresh')  # time at next scr refresh
            mem_inst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(mem_inst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(mem_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if mem_inst.status == STARTED and not waitOnFlip:
            theseKeys = mem_inst.getKeys(keyList=['1'], waitRelease=False)
            _mem_inst_allKeys.extend(theseKeys)
            if len(_mem_inst_allKeys):
                mem_inst.keys = _mem_inst_allKeys[-1].name  # just the last key pressed
                mem_inst.rt = _mem_inst_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memory_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "memory_inst"-------
    for thisComponent in memory_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if mem_inst.keys in ['', [], None]:  # No response was made
        mem_inst.keys = None
    trials_1.addData('mem_inst.keys',mem_inst.keys)
    if mem_inst.keys != None:  # we had a response
        trials_1.addData('mem_inst.rt', mem_inst.rt)
    # the Routine "memory_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stimuli1.setImage(images)
    # keep track of which components have finished
    stimuliComponents = [stimuli1]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli1* updates
        if stimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli1.frameNStart = frameN  # exact frame index
            stimuli1.tStart = t  # local t and not account for scr refresh
            stimuli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli1, 'tStartRefresh')  # time at next scr refresh
            stimuli1.setAutoDraw(True)
        if stimuli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                stimuli1.tStop = t  # not accounting for scr refresh
                stimuli1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli1, 'tStopRefresh')  # time at next scr refresh
                stimuli1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "survey"-------
    continueRoutine = True
    # update component parameters for each repeat
    Survey.keys = []
    Survey.rt = []
    _Survey_allKeys = []
    # keep track of which components have finished
    surveyComponents = [text_10, Survey]
    for thisComponent in surveyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "survey"-------
    while continueRoutine:
        # get current time
        t = surveyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=surveyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *Survey* updates
        waitOnFlip = False
        if Survey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Survey.frameNStart = frameN  # exact frame index
            Survey.tStart = t  # local t and not account for scr refresh
            Survey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Survey, 'tStartRefresh')  # time at next scr refresh
            Survey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Survey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Survey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Survey.status == STARTED and not waitOnFlip:
            theseKeys = Survey.getKeys(keyList=['7', '6', '5', '4', '3', '2', '1'], waitRelease=False)
            _Survey_allKeys.extend(theseKeys)
            if len(_Survey_allKeys):
                Survey.keys = _Survey_allKeys[-1].name  # just the last key pressed
                Survey.rt = _Survey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "survey"-------
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Survey.keys in ['', [], None]:  # No response was made
        Survey.keys = None
    trials_1.addData('Survey.keys',Survey.keys)
    if Survey.keys != None:  # we had a response
        trials_1.addData('Survey.rt', Survey.rt)
    trials_1.addData('Survey.started', Survey.tStartRefresh)
    trials_1.addData('Survey.stopped', Survey.tStopRefresh)
    # the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_1'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dots_setting.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "NO_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    No_inst.keys = []
    No_inst.rt = []
    _No_inst_allKeys = []
    # keep track of which components have finished
    NO_instComponents = [text_7, text_8, No_inst]
    for thisComponent in NO_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NO_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NO_inst"-------
    while continueRoutine:
        # get current time
        t = NO_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NO_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *No_inst* updates
        waitOnFlip = False
        if No_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            No_inst.frameNStart = frameN  # exact frame index
            No_inst.tStart = t  # local t and not account for scr refresh
            No_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No_inst, 'tStartRefresh')  # time at next scr refresh
            No_inst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(No_inst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(No_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if No_inst.status == STARTED and not waitOnFlip:
            theseKeys = No_inst.getKeys(keyList=['2'], waitRelease=False)
            _No_inst_allKeys.extend(theseKeys)
            if len(_No_inst_allKeys):
                No_inst.keys = _No_inst_allKeys[-1].name  # just the last key pressed
                No_inst.rt = _No_inst_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NO_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NO_inst"-------
    for thisComponent in NO_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if No_inst.keys in ['', [], None]:  # No response was made
        No_inst.keys = None
    trials_2.addData('No_inst.keys',No_inst.keys)
    if No_inst.keys != None:  # we had a response
        trials_2.addData('No_inst.rt', No_inst.rt)
    # the Routine "NO_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stimuli1.setImage(images)
    # keep track of which components have finished
    stimuliComponents = [stimuli1]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli1* updates
        if stimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli1.frameNStart = frameN  # exact frame index
            stimuli1.tStart = t  # local t and not account for scr refresh
            stimuli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli1, 'tStartRefresh')  # time at next scr refresh
            stimuli1.setAutoDraw(True)
        if stimuli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                stimuli1.tStop = t  # not accounting for scr refresh
                stimuli1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli1, 'tStopRefresh')  # time at next scr refresh
                stimuli1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "survey"-------
    continueRoutine = True
    # update component parameters for each repeat
    Survey.keys = []
    Survey.rt = []
    _Survey_allKeys = []
    # keep track of which components have finished
    surveyComponents = [text_10, Survey]
    for thisComponent in surveyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "survey"-------
    while continueRoutine:
        # get current time
        t = surveyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=surveyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *Survey* updates
        waitOnFlip = False
        if Survey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Survey.frameNStart = frameN  # exact frame index
            Survey.tStart = t  # local t and not account for scr refresh
            Survey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Survey, 'tStartRefresh')  # time at next scr refresh
            Survey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Survey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Survey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Survey.status == STARTED and not waitOnFlip:
            theseKeys = Survey.getKeys(keyList=['7', '6', '5', '4', '3', '2', '1'], waitRelease=False)
            _Survey_allKeys.extend(theseKeys)
            if len(_Survey_allKeys):
                Survey.keys = _Survey_allKeys[-1].name  # just the last key pressed
                Survey.rt = _Survey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "survey"-------
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Survey.keys in ['', [], None]:  # No response was made
        Survey.keys = None
    trials_2.addData('Survey.keys',Survey.keys)
    if Survey.keys != None:  # we had a response
        trials_2.addData('Survey.rt', Survey.rt)
    trials_2.addData('Survey.started', Survey.tStartRefresh)
    trials_2.addData('Survey.stopped', Survey.tStopRefresh)
    # the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dots_setting.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Explicit_Rep"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    Explicit_RepComponents = [key_resp_8, text_16, text_17]
    for thisComponent in Explicit_RepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Explicit_RepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Explicit_Rep"-------
    while continueRoutine:
        # get current time
        t = Explicit_RepClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Explicit_RepClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['4'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Explicit_RepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Explicit_Rep"-------
    for thisComponent in Explicit_RepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Explicit_Rep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stimuli1.setImage(images)
    # keep track of which components have finished
    stimuliComponents = [stimuli1]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli1* updates
        if stimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli1.frameNStart = frameN  # exact frame index
            stimuli1.tStart = t  # local t and not account for scr refresh
            stimuli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli1, 'tStartRefresh')  # time at next scr refresh
            stimuli1.setAutoDraw(True)
        if stimuli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                stimuli1.tStop = t  # not accounting for scr refresh
                stimuli1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli1, 'tStopRefresh')  # time at next scr refresh
                stimuli1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "survey"-------
    continueRoutine = True
    # update component parameters for each repeat
    Survey.keys = []
    Survey.rt = []
    _Survey_allKeys = []
    # keep track of which components have finished
    surveyComponents = [text_10, Survey]
    for thisComponent in surveyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "survey"-------
    while continueRoutine:
        # get current time
        t = surveyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=surveyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *Survey* updates
        waitOnFlip = False
        if Survey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Survey.frameNStart = frameN  # exact frame index
            Survey.tStart = t  # local t and not account for scr refresh
            Survey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Survey, 'tStartRefresh')  # time at next scr refresh
            Survey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Survey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Survey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Survey.status == STARTED and not waitOnFlip:
            theseKeys = Survey.getKeys(keyList=['7', '6', '5', '4', '3', '2', '1'], waitRelease=False)
            _Survey_allKeys.extend(theseKeys)
            if len(_Survey_allKeys):
                Survey.keys = _Survey_allKeys[-1].name  # just the last key pressed
                Survey.rt = _Survey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "survey"-------
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Survey.keys in ['', [], None]:  # No response was made
        Survey.keys = None
    trials_3.addData('Survey.keys',Survey.keys)
    if Survey.keys != None:  # we had a response
        trials_3.addData('Survey.rt', Survey.rt)
    trials_3.addData('Survey.started', Survey.tStartRefresh)
    trials_3.addData('Survey.stopped', Survey.tStopRefresh)
    # the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
