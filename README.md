# vulnerable-python-demo
A vulnerable Python/Flask app for demonstrating a DevSecOps CI/CD workflow

To run after cloning:

`docker network create demo-network`

`docker build -t python-devsecops-demo .`

`docker run -it -p 8181:8181 --net demo-network python-devsecops-demo`


Other containers that are to interact with this container, should also be ran with the `--net demo-network` flag.
