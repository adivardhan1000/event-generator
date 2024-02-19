# event-generator
Custom prompt for GPT4 wrapped in flask to generate .ics files event files based on text.


Want to run it locally?

## Managing Environment 
### Create a env:
    python -m venv myenv

### Activate env:
     .\myenv\Scripts\activate

     or 

    source myenv/bin/activate 

### Install all required packages from requirements.txt
    pip install -r requirements.txt

#### Note: Always update requirements.txt if new packages are installed
    pip freeze > requirements.txt

## Running Code
    flask run