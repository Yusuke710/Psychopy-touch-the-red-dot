/************* 
 * Exp1 Test *
 *************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.0.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'exp1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(term_and_conditionRoutineBegin());
flowScheduler.add(term_and_conditionRoutineEachFrame());
flowScheduler.add(term_and_conditionRoutineEnd());
flowScheduler.add(calibrationRoutineBegin());
flowScheduler.add(calibrationRoutineEachFrame());
flowScheduler.add(calibrationRoutineEnd());
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
flowScheduler.add(practice_trialRoutineBegin());
flowScheduler.add(practice_trialRoutineEachFrame());
flowScheduler.add(practice_trialRoutineEnd());
flowScheduler.add(practice_stimuliRoutineBegin());
flowScheduler.add(practice_stimuliRoutineEachFrame());
flowScheduler.add(practice_stimuliRoutineEnd());
flowScheduler.add(practice_surveyRoutineBegin());
flowScheduler.add(practice_surveyRoutineEachFrame());
flowScheduler.add(practice_surveyRoutineEnd());
flowScheduler.add(start_actualRoutineBegin());
flowScheduler.add(start_actualRoutineEachFrame());
flowScheduler.add(start_actualRoutineEnd());
const trials_0LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_0LoopBegin(trials_0LoopScheduler));
flowScheduler.add(trials_0LoopScheduler);
flowScheduler.add(trials_0LoopEnd);
const trials_1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_1LoopBegin(trials_1LoopScheduler));
flowScheduler.add(trials_1LoopScheduler);
flowScheduler.add(trials_1LoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'images/8.jpg', 'path': 'images/8.jpg'},
    {'name': 'images/100.jpg', 'path': 'images/100.jpg'},
    {'name': 'images/64.jpg', 'path': 'images/64.jpg'},
    {'name': 'images/128.jpg', 'path': 'images/128.jpg'},
    {'name': 'images/47.jpg', 'path': 'images/47.jpg'},
    {'name': 'images/2.jpg', 'path': 'images/2.jpg'},
    {'name': 'dots_setting.xlsx', 'path': 'dots_setting.xlsx'},
    {'name': 'images/20.jpg', 'path': 'images/20.jpg'},
    {'name': 'images/4.jpg', 'path': 'images/4.jpg'},
    {'name': 'images/55.jpg', 'path': 'images/55.jpg'},
    {'name': 'Instruction.PNG', 'path': 'Instruction.PNG'},
    {'name': 'images/16.jpg', 'path': 'images/16.jpg'},
    {'name': 'images/79.jpg', 'path': 'images/79.jpg'},
    {'name': 'images/38.jpg', 'path': 'images/38.jpg'},
    {'name': 'images/32.jpg', 'path': 'images/32.jpg'},
    {'name': 'Calibration.PNG', 'path': 'Calibration.PNG'},
    {'name': 'images/27.jpg', 'path': 'images/27.jpg'},
    {'name': 'images/87.jpg', 'path': 'images/87.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.0';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var term_and_conditionClock;
var text;
var key_resp;
var text_2;
var calibrationClock;
var image;
var text_3;
var key_resp_2;
var text_11;
var instructionClock;
var key_resp_3;
var Inst;
var text_13;
var practice_trialClock;
var text_9;
var key_resp_6;
var practice_stimuliClock;
var stimuli_prac;
var practice_surveyClock;
var key_resp_5;
var text_12;
var start_actualClock;
var key_resp_4;
var text_4;
var NOMemorRepClock;
var text_14;
var key_resp_7;
var text_15;
var stimuliClock;
var stimuli1;
var surveyClock;
var text_10;
var Survey;
var memory_instClock;
var text_5;
var text_6;
var mem_inst;
var NO_instClock;
var text_7;
var text_8;
var No_inst;
var Explicit_RepClock;
var key_resp_8;
var text_16;
var text_17;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "term_and_condition"
  term_and_conditionClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "Monash University \nStudy on visual experience\nInvestigators:\n   Prof. Naotsugu Tsuchiya, Monash University, Australia    (naotsugu.tsuchiya@monash.edu)\n   Dr Ariel Zeleznikow-Johnston, Monash University, Australia    (Ariel.Zeleznikow-Johnston@monash.edu)\n   Mr Yusuke Miyashita, Monash University, Australia    (ymiy0005@student.monash.edu)\nHello! Thank you for your interest in our study.\n\nThis experiment will take approximately 10 minutes of your time. Don't worry! Further instructions will be provided before the experiment starts, and you get three practice trials.\n\nAll data will be kept confidential. If you have any question at this stage, please contact the investigators above.\n\nClick here for a detailed version of the participant information sheet\n1. Your consent\nThis participant information sheet contains detailed information about the research project. Its purpose is to explain to you all the procedures involved in this project before you decide whether or not to take part in it. Please read this carefully. Feel free to ask questions about any information in the document. If you wish to discuss the project with a relative or friend or your local health worker, please do so.\nOnce you understand what the project is about and if you agree to take part in it, you will be asked to read and accept the Consent Form (next page). By accepting the Consent Form, you indicate that you understand the information and that you give your consent to participate in the research project.\n2. Purpose of the study\nThe aim of this study is to examine the spacial experience of human perception.\n3. What will happen to me if I participate in the study?\nYou will complete an online visual perceptual task. During this task, you will be shown images and asked to make responses.\nAll results will be de-identified at the time of examination. Please ensure you understand and accept this before providing informed consent.\n5. Possible risks\nIf you begin to feel fatigued during the study you may take a break and return to the testing a little bit later. If you find the testing too frustrating you may stop that test altogether. You may discontinue your participation in the study at any time. Your personal information will be kept confidential as outlined in Section \n4. Use of data for other projects\nData from this research project may be re-used for other related projects in a de-identified manner. Information identifying you will only be available to the researchers involved in the particular study and will not be identifiable when reported\n9. Results of Project\nIf you would like, the results of the study can be sent to you by newsletter or summary format. It is important to know that results may not be known until well after your participation in the study is completed\n10. Further Information or Any Problems\nIf you require further information or if you have any problems concerning this project, you can contact the researchers above.\n",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.1], height: 0.015,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Ready to start? Please press [space] to begin the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "calibration"
  calibrationClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'Calibration.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0.15], size : [0.65, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Press [y] to move to next step',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'Calibration step:\nAdjust your head position until you see your thumb has a similar width with the black line at the center of the screen.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Inst = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Inst', units : undefined, 
    image : 'Instruction.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0.15], size : [1.2, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: 'You will see an image with dots. Then the screen switches and ask you questions about the image you saw. \nPress [space] to continue\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "practice_trial"
  practice_trialClock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'press [y] to start the prctice trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_stimuli"
  practice_stimuliClock = new util.Clock();
  stimuli_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stimuli_prac', units : undefined, 
    image : 'images/20.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "practice_survey"
  practice_surveyClock = new util.Clock();
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "start_actual"
  start_actualClock = new util.Clock();
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'End of the practice trial.\nPress [y] to start the actual trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "NOMemorRep"
  NOMemorRepClock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'press [0] to move to next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'Please note that we are not interested in your ability to remember or  reproduce the exact location of the dots later. \nWe are interested in your experience at the moment that you were seeing the display. \nNo matter whether you can reproduce the positions of dots or not, or no matter whether you remember the location of the dots or not, please report your own experience of the dots AT THE TIME when the image was presented ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "stimuli"
  stimuliClock = new util.Clock();
  stimuli1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stimuli1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "survey"
  surveyClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Multiple choice\npress [7]: I definitely saw each dot in a well-defined location \n[6]: I think I saw each dot in a general region, but not necessarily in a definitive location\n[5]: I definitely saw dots but I don’t have a sense of where they were located\n[4]: I probably saw dots but I don’t have a sense of where they were located\n[3]: I am not sure whether I saw dots or not\n[2]: I probably did not see any dots\n[1]: I definitely did not see any dots \n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  Survey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "memory_inst"
  memory_instClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Please note that we are not interested in your ability to reproduce the exact location of the dots later. \nWe are interested in your experience at the moment that you were seeing the display. \nNo matter whether you can reproduce the positions of dots or not, please report your own experience of the dots AT THE TIME when the image was presented ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'press [1] to move to next experiment',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  mem_inst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NO_inst"
  NO_instClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Please report your own experience of the dots AT THE TIME when the image was presented\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'press [2] to move to next step',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  No_inst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Explicit_Rep"
  Explicit_RepClock = new util.Clock();
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: 'press [4] to move next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'Please consider whether you can remember or reproduce the exact locations of the dots you just saw.\nWe are interested in your experience at the moment that you were seeing the display. \nPlease report your own experience of the dots AT THE TIME when the image was presented ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var term_and_conditionComponents;
function term_and_conditionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'term_and_condition'-------
    t = 0;
    term_and_conditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    term_and_conditionComponents = [];
    term_and_conditionComponents.push(text);
    term_and_conditionComponents.push(key_resp);
    term_and_conditionComponents.push(text_2);
    
    for (const thisComponent of term_and_conditionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function term_and_conditionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'term_and_condition'-------
    // get current time
    t = term_and_conditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 2.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_2* updates
    if (t >= 2.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of term_and_conditionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function term_and_conditionRoutineEnd() {
  return async function () {
    //------Ending Routine 'term_and_condition'-------
    for (const thisComponent of term_and_conditionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "term_and_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var calibrationComponents;
function calibrationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'calibration'-------
    t = 0;
    calibrationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    calibrationComponents = [];
    calibrationComponents.push(image);
    calibrationComponents.push(text_3);
    calibrationComponents.push(key_resp_2);
    calibrationComponents.push(text_11);
    
    for (const thisComponent of calibrationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function calibrationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'calibration'-------
    // get current time
    t = calibrationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *text_3* updates
    if (t >= 2.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 2 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['y'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of calibrationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function calibrationRoutineEnd() {
  return async function () {
    //------Ending Routine 'calibration'-------
    for (const thisComponent of calibrationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_2.stop();
    // the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instruction'-------
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(key_resp_3);
    instructionComponents.push(Inst);
    instructionComponents.push(text_13);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instruction'-------
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 1.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Inst* updates
    if (t >= 0.0 && Inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Inst.tStart = t;  // (not accounting for frame time here)
      Inst.frameNStart = frameN;  // exact frame index
      
      Inst.setAutoDraw(true);
    }

    
    // *text_13* updates
    if (t >= 1 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd() {
  return async function () {
    //------Ending Routine 'instruction'-------
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_3.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var practice_trialComponents;
function practice_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_trial'-------
    t = 0;
    practice_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    practice_trialComponents = [];
    practice_trialComponents.push(text_9);
    practice_trialComponents.push(key_resp_6);
    
    for (const thisComponent of practice_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_trial'-------
    // get current time
    t = practice_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['y'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_trial'-------
    for (const thisComponent of practice_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_6.stop();
    // the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice_stimuliComponents;
function practice_stimuliRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_stimuli'-------
    t = 0;
    practice_stimuliClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    practice_stimuliComponents = [];
    practice_stimuliComponents.push(stimuli_prac);
    
    for (const thisComponent of practice_stimuliComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practice_stimuliRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_stimuli'-------
    // get current time
    t = practice_stimuliClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli_prac* updates
    if (t >= 0.0 && stimuli_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_prac.tStart = t;  // (not accounting for frame time here)
      stimuli_prac.frameNStart = frameN;  // exact frame index
      
      stimuli_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stimuli_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli_prac.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_stimuliComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_stimuliRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_stimuli'-------
    for (const thisComponent of practice_stimuliComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var practice_surveyComponents;
function practice_surveyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_survey'-------
    t = 0;
    practice_surveyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    practice_surveyComponents = [];
    practice_surveyComponents.push(key_resp_5);
    practice_surveyComponents.push(text_12);
    
    for (const thisComponent of practice_surveyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_surveyRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_survey'-------
    // get current time
    t = practice_surveyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['7', '6', '5', '4', '3', '2', '1'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_12* updates
    if (t >= 0.0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_12.tStart = t;  // (not accounting for frame time here)
      text_12.frameNStart = frameN;  // exact frame index
      
      text_12.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_surveyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_surveyRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_survey'-------
    for (const thisComponent of practice_surveyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "practice_survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var start_actualComponents;
function start_actualRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'start_actual'-------
    t = 0;
    start_actualClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    start_actualComponents = [];
    start_actualComponents.push(key_resp_4);
    start_actualComponents.push(text_4);
    
    for (const thisComponent of start_actualComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function start_actualRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'start_actual'-------
    // get current time
    t = start_actualClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['y'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_actualComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_actualRoutineEnd() {
  return async function () {
    //------Ending Routine 'start_actual'-------
    for (const thisComponent of start_actualComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_4.stop();
    // the Routine "start_actual" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_0;
var currentLoop;
function trials_0LoopBegin(trials_0LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_0 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'dots_setting.xlsx',
      seed: undefined, name: 'trials_0'
    });
    psychoJS.experiment.addLoop(trials_0); // add the loop to the experiment
    currentLoop = trials_0;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_0 of trials_0) {
      const snapshot = trials_0.getSnapshot();
      trials_0LoopScheduler.add(importConditions(snapshot));
      trials_0LoopScheduler.add(NOMemorRepRoutineBegin(snapshot));
      trials_0LoopScheduler.add(NOMemorRepRoutineEachFrame());
      trials_0LoopScheduler.add(NOMemorRepRoutineEnd());
      trials_0LoopScheduler.add(stimuliRoutineBegin(snapshot));
      trials_0LoopScheduler.add(stimuliRoutineEachFrame());
      trials_0LoopScheduler.add(stimuliRoutineEnd());
      trials_0LoopScheduler.add(surveyRoutineBegin(snapshot));
      trials_0LoopScheduler.add(surveyRoutineEachFrame());
      trials_0LoopScheduler.add(surveyRoutineEnd());
      trials_0LoopScheduler.add(endLoopIteration(trials_0LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_0LoopEnd() {
  psychoJS.experiment.removeLoop(trials_0);

  return Scheduler.Event.NEXT;
}


var trials_1;
function trials_1LoopBegin(trials_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'dots_setting.xlsx',
      seed: undefined, name: 'trials_1'
    });
    psychoJS.experiment.addLoop(trials_1); // add the loop to the experiment
    currentLoop = trials_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_1 of trials_1) {
      const snapshot = trials_1.getSnapshot();
      trials_1LoopScheduler.add(importConditions(snapshot));
      trials_1LoopScheduler.add(memory_instRoutineBegin(snapshot));
      trials_1LoopScheduler.add(memory_instRoutineEachFrame());
      trials_1LoopScheduler.add(memory_instRoutineEnd());
      trials_1LoopScheduler.add(stimuliRoutineBegin(snapshot));
      trials_1LoopScheduler.add(stimuliRoutineEachFrame());
      trials_1LoopScheduler.add(stimuliRoutineEnd());
      trials_1LoopScheduler.add(surveyRoutineBegin(snapshot));
      trials_1LoopScheduler.add(surveyRoutineEachFrame());
      trials_1LoopScheduler.add(surveyRoutineEnd());
      trials_1LoopScheduler.add(endLoopIteration(trials_1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_1);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'dots_setting.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      const snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(NO_instRoutineBegin(snapshot));
      trials_2LoopScheduler.add(NO_instRoutineEachFrame());
      trials_2LoopScheduler.add(NO_instRoutineEnd());
      trials_2LoopScheduler.add(stimuliRoutineBegin(snapshot));
      trials_2LoopScheduler.add(stimuliRoutineEachFrame());
      trials_2LoopScheduler.add(stimuliRoutineEnd());
      trials_2LoopScheduler.add(surveyRoutineBegin(snapshot));
      trials_2LoopScheduler.add(surveyRoutineEachFrame());
      trials_2LoopScheduler.add(surveyRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'dots_setting.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      const snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(Explicit_RepRoutineBegin(snapshot));
      trials_3LoopScheduler.add(Explicit_RepRoutineEachFrame());
      trials_3LoopScheduler.add(Explicit_RepRoutineEnd());
      trials_3LoopScheduler.add(stimuliRoutineBegin(snapshot));
      trials_3LoopScheduler.add(stimuliRoutineEachFrame());
      trials_3LoopScheduler.add(stimuliRoutineEnd());
      trials_3LoopScheduler.add(surveyRoutineBegin(snapshot));
      trials_3LoopScheduler.add(surveyRoutineEachFrame());
      trials_3LoopScheduler.add(surveyRoutineEnd());
      trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var _key_resp_7_allKeys;
var NOMemorRepComponents;
function NOMemorRepRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'NOMemorRep'-------
    t = 0;
    NOMemorRepClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    NOMemorRepComponents = [];
    NOMemorRepComponents.push(text_14);
    NOMemorRepComponents.push(key_resp_7);
    NOMemorRepComponents.push(text_15);
    
    for (const thisComponent of NOMemorRepComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NOMemorRepRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'NOMemorRep'-------
    // get current time
    t = NOMemorRepClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_14* updates
    if (t >= 0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['0'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NOMemorRepComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NOMemorRepRoutineEnd() {
  return async function () {
    //------Ending Routine 'NOMemorRep'-------
    for (const thisComponent of NOMemorRepComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_7.stop();
    // the Routine "NOMemorRep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var stimuliComponents;
function stimuliRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'stimuli'-------
    t = 0;
    stimuliClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    stimuli1.setImage(images);
    // keep track of which components have finished
    stimuliComponents = [];
    stimuliComponents.push(stimuli1);
    
    for (const thisComponent of stimuliComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stimuliRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'stimuli'-------
    // get current time
    t = stimuliClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli1* updates
    if (t >= 0.0 && stimuli1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli1.tStart = t;  // (not accounting for frame time here)
      stimuli1.frameNStart = frameN;  // exact frame index
      
      stimuli1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stimuli1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimuliComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimuliRoutineEnd() {
  return async function () {
    //------Ending Routine 'stimuli'-------
    for (const thisComponent of stimuliComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _Survey_allKeys;
var surveyComponents;
function surveyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'survey'-------
    t = 0;
    surveyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Survey.keys = undefined;
    Survey.rt = undefined;
    _Survey_allKeys = [];
    // keep track of which components have finished
    surveyComponents = [];
    surveyComponents.push(text_10);
    surveyComponents.push(Survey);
    
    for (const thisComponent of surveyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function surveyRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'survey'-------
    // get current time
    t = surveyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *Survey* updates
    if (t >= 0.0 && Survey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Survey.tStart = t;  // (not accounting for frame time here)
      Survey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Survey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Survey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Survey.clearEvents(); });
    }

    if (Survey.status === PsychoJS.Status.STARTED) {
      let theseKeys = Survey.getKeys({keyList: ['7', '6', '5', '4', '3', '2', '1'], waitRelease: false});
      _Survey_allKeys = _Survey_allKeys.concat(theseKeys);
      if (_Survey_allKeys.length > 0) {
        Survey.keys = _Survey_allKeys[_Survey_allKeys.length - 1].name;  // just the last key pressed
        Survey.rt = _Survey_allKeys[_Survey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of surveyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function surveyRoutineEnd() {
  return async function () {
    //------Ending Routine 'survey'-------
    for (const thisComponent of surveyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Survey.keys', Survey.keys);
    if (typeof Survey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Survey.rt', Survey.rt);
        routineTimer.reset();
        }
    
    Survey.stop();
    // the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _mem_inst_allKeys;
var memory_instComponents;
function memory_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'memory_inst'-------
    t = 0;
    memory_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    mem_inst.keys = undefined;
    mem_inst.rt = undefined;
    _mem_inst_allKeys = [];
    // keep track of which components have finished
    memory_instComponents = [];
    memory_instComponents.push(text_5);
    memory_instComponents.push(text_6);
    memory_instComponents.push(mem_inst);
    
    for (const thisComponent of memory_instComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function memory_instRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'memory_inst'-------
    // get current time
    t = memory_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *text_6* updates
    if (t >= 0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    
    // *mem_inst* updates
    if (t >= 0 && mem_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mem_inst.tStart = t;  // (not accounting for frame time here)
      mem_inst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { mem_inst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { mem_inst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { mem_inst.clearEvents(); });
    }

    if (mem_inst.status === PsychoJS.Status.STARTED) {
      let theseKeys = mem_inst.getKeys({keyList: ['1'], waitRelease: false});
      _mem_inst_allKeys = _mem_inst_allKeys.concat(theseKeys);
      if (_mem_inst_allKeys.length > 0) {
        mem_inst.keys = _mem_inst_allKeys[_mem_inst_allKeys.length - 1].name;  // just the last key pressed
        mem_inst.rt = _mem_inst_allKeys[_mem_inst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of memory_instComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_instRoutineEnd() {
  return async function () {
    //------Ending Routine 'memory_inst'-------
    for (const thisComponent of memory_instComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('mem_inst.keys', mem_inst.keys);
    if (typeof mem_inst.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('mem_inst.rt', mem_inst.rt);
        routineTimer.reset();
        }
    
    mem_inst.stop();
    // the Routine "memory_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _No_inst_allKeys;
var NO_instComponents;
function NO_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'NO_inst'-------
    t = 0;
    NO_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    No_inst.keys = undefined;
    No_inst.rt = undefined;
    _No_inst_allKeys = [];
    // keep track of which components have finished
    NO_instComponents = [];
    NO_instComponents.push(text_7);
    NO_instComponents.push(text_8);
    NO_instComponents.push(No_inst);
    
    for (const thisComponent of NO_instComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NO_instRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'NO_inst'-------
    // get current time
    t = NO_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *text_8* updates
    if (t >= 0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *No_inst* updates
    if (t >= 0 && No_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      No_inst.tStart = t;  // (not accounting for frame time here)
      No_inst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { No_inst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { No_inst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { No_inst.clearEvents(); });
    }

    if (No_inst.status === PsychoJS.Status.STARTED) {
      let theseKeys = No_inst.getKeys({keyList: ['2'], waitRelease: false});
      _No_inst_allKeys = _No_inst_allKeys.concat(theseKeys);
      if (_No_inst_allKeys.length > 0) {
        No_inst.keys = _No_inst_allKeys[_No_inst_allKeys.length - 1].name;  // just the last key pressed
        No_inst.rt = _No_inst_allKeys[_No_inst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NO_instComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NO_instRoutineEnd() {
  return async function () {
    //------Ending Routine 'NO_inst'-------
    for (const thisComponent of NO_instComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('No_inst.keys', No_inst.keys);
    if (typeof No_inst.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('No_inst.rt', No_inst.rt);
        routineTimer.reset();
        }
    
    No_inst.stop();
    // the Routine "NO_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var Explicit_RepComponents;
function Explicit_RepRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Explicit_Rep'-------
    t = 0;
    Explicit_RepClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    Explicit_RepComponents = [];
    Explicit_RepComponents.push(key_resp_8);
    Explicit_RepComponents.push(text_16);
    Explicit_RepComponents.push(text_17);
    
    for (const thisComponent of Explicit_RepComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Explicit_RepRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Explicit_Rep'-------
    // get current time
    t = Explicit_RepClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_8* updates
    if (t >= 0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['4'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_16* updates
    if (t >= 0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }

    
    // *text_17* updates
    if (t >= 0.0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Explicit_RepComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Explicit_RepRoutineEnd() {
  return async function () {
    //------Ending Routine 'Explicit_Rep'-------
    for (const thisComponent of Explicit_RepComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_8.stop();
    // the Routine "Explicit_Rep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
