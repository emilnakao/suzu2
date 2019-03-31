# Instalação em novos ambientes com ansible

- Providenciar uma máquina com Ubuntu 16.04 64bit (não precisa ser o server)
- Instalar no ubuntu openssh-server (sudo apt-get install openssh-server)
- 

- instalar ansible na máquina de onde vão ser feitas as instalações
- rodar comando do ansible:


- vai falhar na task docker_service, informando que o comando docker para python não está instalado. Logar no servidor, e rodar:

```
pip install docker
pip install docker-compose
```

- em seguida, adicionar o usuário do servidor no grupo docker:

```
sudo usermod -aG docker <<USUARIO>>
```
