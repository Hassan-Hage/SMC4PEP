# SMC4PEP

SMC4PEP is a tool for converting business processes expressed in the BPMN language into a Markov Decision Process (MDP) file that can be then analyzed by the PRISM model checker, to verify its properties. The BPMN process can be expressed either as a pool-based process (pBPMN), or with the event-based (eBPMN) modelling approach. 

## Run an example
The results of the Table 2 in row 1 with one abstraction level of the paper `SMC4PEP: A Conversion Tool for an Automated Verification of Product Engineering Processes` can be reproduced based on the file located in `SMC4PEP_v1.1/examples/UC from Journal/Row 2 of Table 2 Abstr. level 2`.

To run the example with the website solution please apply http://smc4pep.pythonanywhere.com/ in your browser (e.g. Google Chrome). Then skip step 1 to 4 and continue with step 5 (see below). 

OR 

To run the example with the web app please apply the following steps:

1. Open a Phyton IDE

2. Open and run the file `app.py` located in `SMC4PEP_v1.1/src/web_gui/app.py`

3. Copy the address `http://127.0.0.1:5000/` displayed in the Console of Phyton

4. Paste the copied adress in a browser (e.g. Google Chrome) and press enter
    -> SMC4PEP web GUI is opend
    
5. Upload the file  `UC_Abstr_level_2.xml` located in  `SMC4PEP_v1.1/examples/UC from Journal/Row 2 of Table2 Abstr. level 2/Process Model (eBPMN Design)` by using the button `Choose File` of SMC4PEP

6. Activate the enginges of SMC4PEP for converting the input fil into an MDP by selecting the green button `Convert to PRISM`
    -> a new file is generated
    
7. Save the output of SMC4PEP in a folder of choice 
    ->now the inital business process model described in BPMN is converted into an MDP. 
    
8. For verifying properties of interest: open PRISM (or another model checker which is able to read PRISM files) and upload the output of SMC4PEP

9. Now properties of interests can be verified (see section Reproducing the results of the paper)


    ### Reproducing the results of the paper 

    1. Building model to obtain the states and transitions of the MDP
    -> right click with the mouse on the window where the MDP is pasted
    -> select Build model (F3)
    -> Result: 1 inital state, 3038 states, 9445 transitions are obtained
    
    2. Verifying property phi_1 of the table
    -> select the sheet Properties in PRISM
    -> right click with the mouse on the area Properties
    -> select +Add
    -> add in the field `Pmin = ? [F "end_state" = true]`
    -> select Okay
    -> the property appears in the area Properties and right click with the mouse on the property
    -> select Verify (F5)
    -> Result: 1.0  ---> probability of reaching always the final state and therefore phi_1 is satisfied
    
    3. Verifying property phi_2 of the table
    -> verification is equal to phi_1 acc. to the satisfaction of the A-SPICE requirements
    
    4. Verifying property phi_3 of the table
    -> since the eBPMN design is used to describe the new process acc. to A-SPICE insense of activities, phi_3 is satisfied from the eBPMN design perspective 
    
    5. Verifying property phi_4 of the table
       -> select the sheet Simulator in PRISM
       -> right click with the mouse on the area Path
       -> select New path
       -> select Simulate in the area Automatic exploration (choose steps of your choice)
       -> the minimum days are obtained manually by simulation!!!
   
     6. Verifying property phi_5 of the table
        -> select the sheet Properties in PRISM
        -> right click with the mouse on the area Properties
        -> select +Add
        -> add in the field `R = ? [F "end_state" = true]`
        -> the property appears in the area Properties and right click with the mouse on the property
        -> select Simulate (F6)
        -> Choose number of samples e.g. 1000
        -> select Okay
        -> Result: 275.52  ---> expected reward 
        -> repeat the simulation again (in total 3 simulations) and calculate the average value rounded down (it can deviate since it is a simulation)
        
    7. Verifying property phi_6 of the table (choose process i and process j of your choice, example here is based on )
        -> select the sheet Properties in PRISM
        -> right click with the mouse on the area Properties
        -> select +Add
        -> add in the field e.g. `Pmin = ? [ !s2_4=12 U s1_0 =13 ]` 
        -> select Okay
        -> the property appears in the area Properties and right click with the mouse on the property
        -> select Simulate (F6)
        -> Choose number of samples e.g. 1000
        -> select Okay
        -> Result: 0.97  ---> probability that process i (last state s1_0=13) ends before process j (last state s2_4=12) which shouldn't be possible in the usual business process flow (can be solved by defining "Master" and "Slave" processes on the process model design)! 
        

        We have included some standard properties in `src/properties/sample_properties.txt`. 


   
