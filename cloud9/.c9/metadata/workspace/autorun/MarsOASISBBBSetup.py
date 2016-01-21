{"changed":true,"filter":false,"title":"MarsOASISBBBSetup.py","tooltip":"/autorun/MarsOASISBBBSetup.py","value":" #!/usr/bin/python\n\n\nfrom bbio import *  #need to check this library for how it is setting pin mode, with pinMode() function, when GPIO.setup is not releasing pin control\nimport Adafruit_BBIO.UART as UART\nimport Adafruit_BBIO.GPIO as GPIO\nimport Adafruit_BBIO.PWM as PWM\n\n#set pins 8_3 through 8_10, P9_12, P9_19, P9_20, P9_25, P9_28 as GPIO Inputs for sensors TEMP1-TEMP5 and RH/TEMP1 - RH/TEMP3\npinMode(GPIO1_6, INPUT) #TEMP1\npinMode(GPIO1_7, INPUT) #TEMP2\npinMode(GPIO1_2, INPUT) #TEMP3\npinMode(GPIO1_3, INPUT) #TEMP4\npinMode(GPIO2_2, INPUT) #TEMP5\npinMode(GPIO2_3, INPUT) #RH/TEMP1\npinMode(GPIO2_5, INPUT) #RH/TEMP2\npinMode(GPIO2_4, INPUT) #RH/TEMP3\n\npinMode(GPIO1_28, INPUT)  #3_3VMon\npinMode(GPIO0_13, INPUT)  #LS3_1\npinMode(GPIO0_12, INPUT)  #LS4_1\npinMode(GPIO3_21, INPUT)  #12VMon\npinMode(GPIO3_17, INPUT)  #24VMon\n\n#set GPIO OUTPUT pins, P8_11-P8_12, P8_14-P8_18, P8_20-P8_35, P9_27\npinMode(GPIO1_13, OUTPUT) #HC_En\npinMode(GPIO1_12, OUTPUT) #HC_Sw\npinMode(GPIO0_26, OUTPUT) #OxConEn\npinMode(GPIO1_15, OUTPUT) #LinearActuatorDir\npinMode(GPIO1_14, OUTPUT) #LinearActuatorEn\npinMode(GPIO0_27, OUTPUT) #P01En\npinMode(GPIO2_1, OUTPUT)  #P02En\npinMode(GPIO1_31, OUTPUT) #P03En\npinMode(GPIO1_30, OUTPUT) #P04En\npinMode(GPIO1_5, OUTPUT)  #P05En\npinMode(GPIO1_4, OUTPUT)  #P06En\npinMode(GPIO1_1, OUTPUT)  #P07En\npinMode(GPIO1_0, OUTPUT)  #P08En\npinMode(GPIO1_29, OUTPUT) #P09En\npinMode(GPIO2_22, OUTPUT) #P10En\npinMode(GPIO2_24, OUTPUT) #P11En\npinMode(GPIO2_23, OUTPUT) #P12-DeHumidEn\npinMode(GPIO2_25, OUTPUT) #Sol2En\npinMode(GPIO0_10, OUTPUT) #Sol1En\npinMode(GPIO0_11, OUTPUT) #UVFilterEn\npinMode(GPIO0_9, OUTPUT)  #READY1\npinMode(GPIO2_17, OUTPUT) #SD_DIR_3.3\npinMode(GPIO0_8, OUTPUT)  #SD_ON/OFF_3.3\npinMode(GPIO3_19, OUTPUT)  #READY2\n\n#set UART pins\nUART.setup(\"UART1\")\nUART.setup(\"UART4\")\nUART.setup(\"UART5\")\n\ntry:\n   while True:\n\n        GPIO.setup(\"P9_27\",GPIO.OUT)\n        GPIO.setup(\"P8_33\",GPIO.OUT)\n        #Set READY1 HIGH\n        GPIO.output(\"P8_33\",GPIO.HIGH)\n        #Set READY2 LOW\n        GPIO.output(\"P9_27\",GPIO.LOW)  \n        print(\"READY SIGNALS ENABLED...\")\n \nexcept KeyboardInterrupt:\n    print('Disaabling READY Signals...')\n    UART.cleanup()\n    GPIO.cleanup()\n    PWM.cleanup()\n    GPIO.output(\"P8_33\",Low)\n\n\n\n\n\n\n\n\n","undoManager":{"mark":-1,"position":71,"stack":[[{"group":"doc","deltas":[{"start":{"row":62,"column":0},"end":{"row":67,"column":34},"action":"remove","lines":["  ","UART.cleanup()","GPIO.cleanup()","PWM.cleanup()","GPIO.output(\"P8_33\",Low)","print(\"READY SIGNALS DISABLED...\")"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":0,"column":18},"action":"insert","lines":[" #!/usr/bin/python"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":79,"column":28},"action":"insert","lines":["try:","   while True:","","         //do something"," ","except KeyboardInterrupt:","","        // cleanup","        // get ready to exit"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":79,"column":28},"action":"remove","lines":["try:","   while True:","","         //do something"," ","except KeyboardInterrupt:","","        // cleanup","        // get ready to exit"]}]}],[{"group":"doc","deltas":[{"start":{"row":54,"column":0},"end":{"row":62,"column":28},"action":"insert","lines":["try:","   while True:","","         //do something"," ","except KeyboardInterrupt:","","        // cleanup","        // get ready to exit"]}]}],[{"group":"doc","deltas":[{"start":{"row":65,"column":0},"end":{"row":71,"column":33},"action":"remove","lines":["GPIO.setup(\"P9_27\",GPIO.OUT)","GPIO.setup(\"P8_33\",GPIO.OUT)","#Set READY1 HIGH","GPIO.output(\"P8_33\",GPIO.HIGH)","#Set READY2 LOW","GPIO.output(\"P9_27\",GPIO.LOW)  ","print(\"READY SIGNALS ENABLED...\")"]}]}],[{"group":"doc","deltas":[{"start":{"row":57,"column":8},"end":{"row":57,"column":23},"action":"remove","lines":[" //do something"]},{"start":{"row":57,"column":8},"end":{"row":63,"column":33},"action":"insert","lines":["GPIO.setup(\"P9_27\",GPIO.OUT)","GPIO.setup(\"P8_33\",GPIO.OUT)","#Set READY1 HIGH","GPIO.output(\"P8_33\",GPIO.HIGH)","#Set READY2 LOW","GPIO.output(\"P9_27\",GPIO.LOW)  ","print(\"READY SIGNALS ENABLED...\")"]}]}],[{"group":"doc","deltas":[{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":58,"column":4},"end":{"row":58,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":59,"column":4},"end":{"row":59,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":60,"column":4},"end":{"row":60,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":61,"column":4},"end":{"row":61,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":62,"column":4},"end":{"row":62,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":63,"column":4},"end":{"row":63,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":8},"end":{"row":68,"column":28},"action":"remove","lines":["// cleanup","        // get ready to exit"]}]}],[{"group":"doc","deltas":[{"start":{"row":68,"column":0},"end":{"row":68,"column":33},"action":"remove","lines":["import Adafruit_BBIO.GPIO as GPIO"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":5,"column":33},"action":"insert","lines":["import Adafruit_BBIO.GPIO as GPIO"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":33},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":6,"column":31},"action":"insert","lines":["import Adafruit_BBIO.PWM as PWM"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":0},"end":{"row":71,"column":24},"action":"insert","lines":["print('MarsOASIS is shutting down...')","UART.cleanup()","GPIO.cleanup()","PWM.cleanup()","GPIO.output(\"P8_33\",Low)"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":11},"end":{"row":67,"column":40},"action":"remove","lines":["MarsOASIS is shutting down..."]},{"start":{"row":67,"column":11},"end":{"row":67,"column":12},"action":"insert","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":12},"end":{"row":67,"column":13},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":13},"end":{"row":67,"column":14},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":14},"end":{"row":67,"column":15},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":15},"end":{"row":67,"column":16},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":15},"end":{"row":67,"column":16},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":15},"end":{"row":67,"column":16},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":16},"end":{"row":67,"column":17},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":17},"end":{"row":67,"column":18},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":18},"end":{"row":67,"column":19},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":19},"end":{"row":67,"column":20},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":20},"end":{"row":67,"column":21},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":21},"end":{"row":67,"column":22},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":22},"end":{"row":67,"column":23},"action":"insert","lines":["R"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":23},"end":{"row":67,"column":24},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":24},"end":{"row":67,"column":25},"action":"insert","lines":["A"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":25},"end":{"row":67,"column":26},"action":"insert","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":26},"end":{"row":67,"column":27},"action":"insert","lines":["Y"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":27},"end":{"row":67,"column":28},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"insert","lines":["S"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":32},"end":{"row":67,"column":33},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":34},"end":{"row":67,"column":35},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":35},"end":{"row":67,"column":36},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":36},"end":{"row":67,"column":37},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":67,"column":37},"end":{"row":67,"column":38},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":0},"end":{"row":76,"column":53},"action":"remove","lines":["raw_input(\"Press any key to disable READY signals: \")"]}]}],[{"group":"doc","deltas":[{"start":{"row":75,"column":0},"end":{"row":76,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":74,"column":0},"end":{"row":75,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":73,"column":0},"end":{"row":74,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":8},"end":{"row":73,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":4},"end":{"row":72,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":28},"end":{"row":72,"column":0},"action":"remove","lines":["",""]}]}]]},"ace":{"folds":[],"scrolltop":720,"scrollleft":0,"selection":{"start":{"row":64,"column":15},"end":{"row":64,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"state":"start","mode":"ace/mode/python"}},"timestamp":1425266494000}