# Web studying.

The project was founded in order to study and practice web development.

At the moment:
- The main page with a simple greeting created.
- Tests for CI created.
- One of tests checks the main page status of the get-request. It must be equal 200.
- One of tests checks codestyle (pep8).
- Dockerfile created. You can put the docker image on the server and run the container.

## What tools are involved.

 - Python
 - Django
 - CI/CD
 - Docker


## Installation

Clone the repository.
```bash
  git clone https://github.com/GrinBik/web_studying.git
```
Install required libraries for python.
```bash
  pip install -r requirements.txt
```
Run server.
```bash
  python manage.py runserver 0.0.0.0:8000
```
Go to the localhost page with 8000 port.
```bash
  http://localhost:8000/
```
## Docker image creating

Create docker image drom dockerfile.
```bash
  docker build -t <image_name> .
```
Run container.
```bash
  docker run <image_name> -d -p <port_number>:8000
```
Go to the localhost page with <port_number> port.
```bash
  http://localhost:<port_number>/
```
You can do the same by copying the docker image to the server.