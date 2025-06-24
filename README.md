# Demo Project

## Setup
1. Install Python 3.11 (or later) from [python.org](https://www.python.org/downloads/).
2. Clone the project and open it on the IDE of choice (recommended: [PyCharm](https://www.jetbrains.com/pycharm/download/)).
3. Install Anaconda from [anaconda.com](https://www.anaconda.com/products/distribution#download-section) (for managing dependencies).
4. Create a virtual environment from the environment.yml file:
   - `conda env create -f environment.yml`
5. When using PyCharm, set the interpreter to the virtual environment:
   - Go to `File` > `Settings` > `Project: demo_project` > `Python Interpreter` > `Add Interpreter`.
   - Choose `Existing environment`, select `Conda Environment` and point to the Python executable in your virtual environment (`C:/user/miniconda/envs/demo_project/python.exe` or `C:/user/anaconda/envs/demo_project/python.exe`).

   When using VSCode or the console, activate the environment with
`conda activate demo_project`. This has to be done everytime when starting the project.
6. Run the project:
   - In PyCharm: `Run` > `Edit and add new configuration` > `main.py`.
   - Or manually in the console: 
     `python main.py`

## Update the project
### Receiving changes
1. Pull the changes from the remote branch
2. Update the dependencies:
   - `conda env update -f environment.yml`
3. ...

### Submitting changes
1. Update the environment.yml file with the new dependencies:
   - `conda env export > environment.yml`
2. Push the changes to the remote branch
3. ...

## Project Structure
Note: All subfolders have an empty `__init__.py` file to make them packages.

### main.py
Creates the app, adds all routers and specifies dependencies, host and port.
### routers/
Contains all endpoints.
### models/
Contains all Pydantic models used for request and response validation.

