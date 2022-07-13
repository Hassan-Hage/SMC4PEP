# SMC4PEP

SMC4PEP is a tool for converting business processes expressed in the BPMN language into a Markov Decision Process (MDP) file that can be then analyzed by the PRISM model checker, to verify its properties. The BPMN process can be expressed either as a pool-based process (pBPMN), or with our event-based (eBPMN) format. 

## Getting started
First, we need to make sure that Python 3 is installed in our PC. Then, the packages described in `requirements.txt` need to be installed, for example via pip. The tool should run with all standard operating systems.

After that, we go to `SMC4PEP_v1.0/src/gui_smc4pep.py` and run it. The SMC4PEP GUI will start, and prompt the user to upload a BPMN file. Then, the file will be converted in a PRISM '.mdp' file describing the prism model. The user can save this file in a folder and then open it with the PRISM model checker.

Finally, the program creates an additional excel file along with the prism model. This file contains a table that maps the BPMN process nodes (tasks, events, etc.) with their corresponding prism modules and states. In that way, the user knows the prism state that corresponds to any given BPMN node. This is useful if the user would like to define additional properties into PRISM (apart from the default ones), that can be then verified. 

Apart from the desktop GUI, we provide also a web GUI, located in `SMC4PEP_v1.0/src/web_gui/app.py`. After running this script, the user can open a browser and go to the address: `http://127.0.0.1:5000/`, where the web GUI is displayed. The user can then upload a BPMN file and download the corresponding PRISM file (packed in a zip file, along with the excel file that describes the BPMN and PRISM states correspondence).  
You can also run this web GUI without installation, by going to the following address: `http://smc4pep.pythonanywhere.com/`

## Tool structure
The source code is located in the `src` file inside the main folder of the tool (`SMC4PEP_v1.0`). This contains the GUI, as well as the utilities needed to implement the conversion, which are stored in the `src/utils` folder. Finally, the main folder contains also some example BPMN processes (xml files), where the user can run the tool. We have also included pictures of these process diagrams, so that the user does not need an additional software (e.g. Enterprise Architect, etc.) to view them.

## License
This tool is provided under the GPL v3.0 license.
