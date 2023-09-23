# O.dev-test
My test project for O.dev company.

## Installation
For project installation you should enter:

    git clone git@github.com:eeeelya/O.dev-test.git

## Launch
    
    cd O.deve-test
    sudo docker-compose up --build

## Usage 

You can access the application by this url:
    
    http://0.0.0.0:8000/

If you want to know more about API:

    http://0.0.0.0:8000/api/v1/docs 

## Testing 

You can run tests:
    
    sudo docker exec -it odev python -m pytest 
    