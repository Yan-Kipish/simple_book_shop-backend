# simple_book_shop-backend

## Build Setup

``` bash
# install dependencies
pip install -r requirements.txt

# or
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# init test db
python3 db_init.py

# serve at localhost:8000
uvicorn main:app

```