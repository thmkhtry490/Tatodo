# mytodolist

The Simple TodoList app written in django.

(c) by Taha Mokhtari HashemAbad, see License in LICENSE file.

!!!Warning!!! Now This app in development level. You can contribute to this app in Github platform.

## How to install and run it

First you have to clone it(or fork for yourself and next clone it):

```
git clone git@github.com:thmkhtry490/mytodolist # If you fork it swap thmkhtry490 to your username
cd 
```
For next, you can create venv(you can see more in [here](https://docs.python.org/3/library/venv.html) ):

```
python -m venv venv
source venv/bin/activate # It's for Unix Like's Operating Systems. For Windows see https://docs.python.org/3/library/venv.html 
```
Next, Install requirments:

```
pip install -r requirments.txt
```
For next, You Must Create your secret key:

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 📄 Environment Setup Guide

To configure environment variables for this project:

1. **Copy the sample environment file**:

   ```bash
   cp sample.env .env
   ```

2. **Open `.env` in a text editor** and fill in the required values. Here's what each variable means:

   | Variable        | Description                                                                                                                                                         |
   | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `SECRET_KEY`    | Your Django secret key. You can generate one using:<br>`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
   | `DEBUG`         | Set to `True` for development or `False` for production.                                                                                                            |
   | `ALLOWED_HOSTS` | A comma-separated list of allowed hostnames, e.g., `127.0.0.1,localhost`                                                                                            |

3. **Save the file**, and make sure it's **not committed to version control** (already ignored in `.gitignore`).

### run and see it

For run, run here commands for make database migrations and run it:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
and see in localhost:8000 


Do your works funny!