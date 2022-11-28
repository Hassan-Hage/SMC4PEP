# SMC4PEP

SMC4PEP is a tool for converting business processes expressed in the BPMN language into a Markov Decision Process (MDP) file that can be then analyzed by the PRISM model checker, to verify its properties. The BPMN process can be expressed either as a pool-based process (pBPMN), or with the event-based (eBPMN) modelling approach. 

## Getting started
First, we need to make sure that Python 3 is installed on our PC. Then, the packages described in `requirements.txt` need to be installed, for example via pip. The tool should run with all standard operating systems.

After that, we go to `SMC4PEP_v1.1/src/gui_smc4pep.py` and run it Phyton. The SMC4PEP GUI will start, and prompt the user to upload a BPMN process model described in a XML file by selecting the upper button (upload BPMN model XML). Then by selecting the second button (Convert to PRISM), the file will be converted in a PRISM '.mdp' file describing the inital process model in an MDP described in the syntax of PRISM. The user can save the output file in a folder of choice and then open it with the PRISM model checker. 

Finally, the program creates an additional excel file along with the mdp model described in PRISM syntax. This file contains a table that maps the BPMN process nodes (tasks, events, etc.) with their corresponding prism modules and states. In that way, the user knows the prism state that corresponds to any given BPMN node. This is useful if the user would like to define additional properties into PRISM (apart from the default ones), that can be then verified. 

Apart from the desktop GUI, we provide also a web GUI, located in `SMC4PEP_v1.1/src/web_gui/app.py`. After running this script, in the Consol of Phyton the address `http://127.0.0.1:5000/`appears. Then, the user can open a browser (we prefer Google Chrome) and paste the copied address: `http://127.0.0.1:5000/` of the Control into the browser. Finally,the web GUI is displayed. Then the user can upload a BPMN process model described in a XML file with the button `Choose File` and convert the input file into an MDP described in the syntax of PRISM by selecting the button `Convert to PRISM`. Finally, the user can download the corresponding file (packed in a zip file, along with the .dat file that describes the BPMN and PRISM states correspondence).  


## Tool structure
The source code is located in the `src` file inside the main folder of the tool (`SMC4PEP_v1.1`). This contains the GUI, as well as the utilities needed to implement the conversion, which are stored in the `src/utils` folder. Finally, the main folder contains also some example BPMN processes (xml files), where the user can run the tool. We have also included pictures of these process diagrams, so that the user does not need an additional software (e.g. Enterprise Architect, etc.) to view them.

## License
This tool is provided under the GPL v3.0 license.
