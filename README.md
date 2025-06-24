# Demo Project

## Setup
1. Install Python 3.11 (or later) from [python.org](https://www.python.org/downloads/).
2. Clone the project and open it on the IDE of choice (recommended: [PyCharm](https://www.jetbrains.com/pycharm/download/)).
3. Create a virtual environment:
   - In PyCharm: `File` > `New Project` > `Python Interpreter` > `Add Interpreter` > `Virtual Environment`.
   - Or manually: 
     `python -m venv venv`
     `venv\Scripts\activate`
4. Alternatively use Anaconda (search for tutorial online)
5. Install dependencies:
    `pip install -r requirements.txt`
6. Run the project:
   - In PyCharm: `Run` > `Edit and add new configuration` > `main.py`.
   - Or manually: 
     `python main.py`

## Project Structure
Note: All subfolders have an empty `__init__.py` file to make them packages.

### main.py
Creates the app, adds all routers and specifies dependencies, host and port.
### routers/
Contains all endpoints.
### models/
Contains all Pydantic models used for request and response validation.

