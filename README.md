# csv-webzone
Welcome to the CSV WebZone. This application will power a webserver, allowing you to upload and view CSV files, as well as some statistics and plots about their contents.

# Instructions
You'll need a few pieces of software to start. 
 - Python (I used Python 3.8 to develop this)
 - pip (the Python Package Index)

The easiest way to set everything up is with a python virtual environment. If you have Python 3 already installed, you can make one in your current directory with 'python -m venv venv' and activate it like this:
Unix-based systems: `source venv/bin/activate`
Windows: `./venv/Scripts/activate`

More detailed venv instructions can be found [here](https://docs.python.org/3/library/venv.html).

At the moment, CSV WebZone is only available on the PyPI Test instance. This means that you can't just do "pip install csv-webzone", you have to specify a few things in the command.

To install CSV WebZone, do `pip install --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple csv-webzone`

To start the application, just do `flask run`. The webserver will start in development mode, serving on localhost:5000. 
