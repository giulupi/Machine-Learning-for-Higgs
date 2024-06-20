
## Motivation and platform choice
Since in my carrer I never had the chance to practice with machine learning, I decided to exploit this project to try to understand the basics of ML.
Having looked around, I found ATLAS Open Data and the related Kaggle's challenges. I hence decided to write a basic Neural Network model to distinguish signal from background in a Higgs search. In the search for the best performances, I encountered a ton of different techniques that could improve my model, therefore I decided to explore some of the most common ones. 
I also decided to use Jupyter Notebooks as they allowed me to quickly visualise the output and run commands on the spot instead of having to launch a script each time.


### Setup
To reproduce the code, three options are available:
1. Run the Notebook on Google Colab (https://colab.research.google.com) 
2. Import the conda environment present in this repository using the following these steps:

   1. Clone the repository to your local machine:
        ```
        git clone **Mettemoce il link**
        ```

   2. Navigate to the repository directory:
        ```
        cd NOME
        ```

   3. Create a new conda environment using the environment.yml file (NB: use environment_mac_m1 if you use apple silicon machines):
        ```
        conda env create -f environment.yml
        ```

        This command will create a new conda environment with the name specified in the environment.yml file.

   4. Activate the newly created environment:
        ```
        conda activate ML (or MLMac if you are on apple silicon)
        ```


   5. Verify that the environment has been successfully created and activated by running:
        ```
        conda env list
        ```

        This command will display a list of all available conda environments, with an asterisk (*) next to the currently active environment.

   6. You can now start working with the imported conda environment and its dependencies.

3. Run the install.ipynb notebook 

Regardless of the platform you choose, try to run the single cell in  `test_setup`. If all the necessary libraries are there, you will not get any error message.

### Input Data
The input data required for this project are too large to be directly included in this repository. Therefore, the data are saved in a separate folder on Google Drive . You can access the data using the following link: 
https://drive.google.com/drive/folders/104SfmJzuUYvtJu7whrJ_2CdiyCmhpH0t?usp=drive_link

Please download the data from the provided link and place it in "input" folder.


### Input Variables
The input provides several variables to classify the events. Since each event has multiple leptons, they were ordered in descending order based on their transverse momentum. Thus, lepton 1 has the highest transverse momentum, lepton 2 the second highest, and so on. <br>
Most of the given variables can be called low-level, because they represent event or object properties, which can be derived directly from the reconstruction in the detector. In contrast to this are high-level variables, which result from the combination of several low-level variables. In the given dataset the only high-level variables are invariant masses of multiple particles:<br>
$m_{inv} = \sqrt{\left(\sum\limits_{i=1}^{n} E_i\right)^2 - \left(\sum\limits_{i=1}^{n} \vec{p}_i\right)^2}$


List of all available variables:<br>
- Scale and event weight
     - The scaling for a dataset is given by the sum of event weights, the cross section, luminosity and a efficiency scale factor
     - Each event has an additional specific event weight
     - To combine simulated events and finally compare them to data each event has to be scaled by the event weight
     - The weight are not used for training
     - Variable name: `totalWeight`
- Number of jets
     - Jets are particle showers which result primarily from quarks and gluons
     - Variable name: `jet_n`
- Invariant four lepton mass
     - The invariant mass $m_{inv}(l_1, l_2, l_3, l_4)$ is the reconstructed invariant mass of the full four lepton event.<br>
     This variable is to be displayed later but not used for training.
     - Variable name: `lep_m_llll`
- Invariant two lepton mass
     - Invariant masses $m_{inv}(l_i, l_j)$ of all combinations of two leptons
     - Variable names: `lep_m_ll_12`, `lep_m_ll_13`, `lep_m_ll_14`, `lep_m_ll_23`, `lep_m_ll_24`, `lep_m_ll_34`
- Transverse momentum $p_T$ of the leptons
     - The momentum in the plane transverse to the beam axis
     - Variable names: `lep1_pt`, `lep2_pt`, `lep3_pt`, `lep4_pt`
- Lepton azimuthal angle
     - The azimuthal angle $\phi$ is measured in the plane transverse to the beam axis
     - Variable name: `lep1_phi`, `lep2_phi`, `lep3_phi`, `lep4_phi`
- Lepton pseudo rapidity
     - The angle $\theta$ is measured between the lepton track and the beam axis.<br>
     Since this angle is not invariant against boosts along the beam axis, the pseudo rapidity $\eta = - \ln{\tan{\frac{\theta}{2}}}$ is primarily used in the ATLAS analyses
     - Variable names: `lep1_eta`, `lep2_eta`, `lep3_eta`, `lep4_eta`
- Lepton energy
     - The energy of the leptons reconstructed from the calorimeter entries
     - Variable name: `lep1_e`, `lep2_e`, `lep3_e`, `lep4_e`
- Lepton PDG-ID
     - The lepton type is classified by a n umber given by the Particle-Data-Group.<br>
     The lepton types are PDG-ID$(e)=11$, PDG-ID$(\mu)=13$ and PDG-ID$(\tau)=15$
     - Variable name: `lep1_pdgId`, `lep2_pdgId`, `lep3_pdgId`, `lep4_pdgId`
- Lepton charge
     - The charge of the given lepton reconstructed by the lepton track
     - Variable name: `lep1_charge`, `lep2_charge`, `lep3_charge`, `lep4_charge`