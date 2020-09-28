# csv-webzone
Welcome to the CSV WebZone. This application will power a webserver, allowing you to upload and view CSV files, as well as some statistics and plots about their contents.

# Instructions
You'll need a few pieces of software to start. 
 - Python (I used Python 3.8 to develop this)
 - pip (the Python Package Index)

At the moment, CSV WebZone is only available on the PyPI Test instance. If demand increases we may someday make it to the big leagues. The only difference is that you can't just do "pip install csv-webzone", you have to specify a few things in the command.

To install CSV WebZone, do 'pip install --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple csv-webzone'

To start the application, just do 'flask run' in the 