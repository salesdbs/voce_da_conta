####VOCE_DA_CONTA
```
sudo apt-get update
sudo apt-get remove docker docker-engine docker.io
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo docker images postgres
sudo docker images
sudo docker pull dpage/pgadmin4
sudo docker network create --driver bridge postgres-network
sudo docker run --name teste-postgres --network=postgres-network -e "POSTGRES_PASSWORD=Postgres2018!" -p 5432:5432 -v /home/chaveiro/0-repositorios/docker/postgreSQL:/var/lib/postgresql/data -d postgres
sudo docker run --name teste-pgadmin --network=postgres-network -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=salesdbs@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=PgAdmin2018!" -d dpage/pgadmin4
sudo docker ps -a

sudo docker exec -it teste-postgres sh
apt-get update
apt-get install -y python3-dev python3-setuptools libpq-dev build-essential binutils g++

pacotes python:
pip install PyPDF2
pip3 install response
pip3 install pprint
sudo pip3 install os
sudo pip3 install base64
pip3 install pybase64
pip3 install pprint
pip3 install json
pip install jsonlib-python3
pip3 install jsonlib-python3
pip install facebook-sdk
sudo pip3 install facebook
pip install jupyterlab
sudo pip3 install python3-gpg
sudo pip install python3-gpgme
sudo pip update
sudo pip upgrade
sudo pip search python3-gpgme
pip install gpg
pip install requests
sudo pip install pymongo
pip install scipy
pip install sklearn
pip install matplotlib numpy
pip install numpy
pip install pandas
pip install Py4J
pip install tables
```
