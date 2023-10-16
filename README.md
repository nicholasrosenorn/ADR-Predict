# ADR-Predict


To download virtual environment library: 
```commandline
pip install virtualenv
```

To create a virtual environment:
```commandline
python -m venv [name_of_virtual_env] 
```

To activate virtual environment:
```commandline
source [name_of_vitrual_env]/bin/activate
```


To deactivate virtual environment:
```commandline
deactivate
```

Note:
If you name your virtual environment venv or env, 
it should automatically be part of the gitignore file.
If you name it something else, please add the directory to 
the gitignore file.

Downloading required libraries:
```commandline
pip install -r requirements.txt
```

To add to requirements.txt
```commandline
pip freeze > requirements.txt
```

