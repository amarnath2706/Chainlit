echo [$(date)]: "START"
echo [$(date)]: "Creating a conda environement with python version 3.10"
conda create --prefix ./env python=3.10  -y
echo [$(date)]: "Conda environement with python version 3.10 created successfully"
source activate ./env
echo [$(date)]: "Conda environment activated successfully"
echo [$(date)]: "Installation of Requirments"
pip install -r requirements.txt
echo [$(date)]: "Installation of Requirments successfully completed"    
echo [$(date)]: "END"