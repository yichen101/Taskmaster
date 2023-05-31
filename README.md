# Taskmaster
Task Master is a tool to help keep track of things to do.


## How to run

1. Create virtual environment:
```
pip install virtualenv
python -m venv myenv
```

2. Then run the command to access virtual environment:
```
.\myenv\Scripts\activate
```

3. Start web server:
```
(env) python app.py
```



## How to create database
1. Open python shell:
```
(env) python
```
2. Inside python shell type the following:
```
>>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()
```

# System information
Platform: Windows-10
