# wetransfer-clone

This repository is for a python application that mimics the basic functionality of WeTransfer.


## Summary

Create a basic version of a file transfer website such as WeTransfer or Firefox Send.

Django should be used for the backend. The frontend can just be basic HTML/CSS – no Javascript should be required.

The look-and-feel is not important, but you may wish to use something like Bootstrap to provide some basic styling.


## User Stories

- As a sending user I want to be able to upload one or more files and obtain a URL link which I can share with other people so they can access those files.
- As a receiving user I want to be able to visit a link I have received from a sending user so I can download the files.



## How to run the application

The application is running in a docker container, to build & run the container use the following command:

`docker-compose up --build -d`

Once the above command has finished running you can go to http://127.0.0.1:8000 in your preferred browser