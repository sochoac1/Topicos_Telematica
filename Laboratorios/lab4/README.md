# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 4 -Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Crear una máquinas virtuales  por medio de Google Cloud Platform(GCP) y asignarles una dirección Ip estática.
- Desplegar contenedores a través de Docker y Docker compose para instalar wordpress, nginx y mysql server.
- Iniciar dos instancias de wordpress utilizando docker compose.
- Utilizar certbot para pedir certificado SSL para todo el dominio (wildcard) permitiendo la navegación segura en el servidor.
- Obtener un dominio valido a través de Freenom [https://lab4.sochoac.tk/](https://lab4.sochoac.tk/).
- Realizar un balanceador de cargas de la capa de aplicación del wordpress usando nginx.
- Construir un servidor de base de datos y otros para archivos compartidos con DB en docker y un NFS server respectivamente.


# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **Docker** : Docker es un sistema operativo (o runtime) para contenedores. El motor de Docker se instala en cada servidor en el que desee ejecutar contenedores y proporciona un conjunto sencillo de comandos que puede utilizar para crear, iniciar o detener contenedores.
- **Docker Compose** : Docker Compose es una herramienta para definir y ejecutar aplicaciones de Docker de varios contenedores. En Compose, se usa un archivo YAML para configurar los servicios de la aplicación. Después, con un solo comando, se crean y se inician todos los servicios de la configuración.
[![Product Name Screen Shot][docker]]((http://34.207.26.5))

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### detalles del desarrollo técnicos.
- Se utiliza el sistema operativo Ubunutu 20.04.4.
- Se utiliza cerbot y letsencrypt para el certificado SSL.
- Se utiliza el servidor nginx.
- Se utiliza docker.io y docker-compose.
- Se utiliza NFS para el sistema de archivos compartidos.

### Paso a paso para la creación de las máquinas virtuales en CGP.
**Nota**: Se deben crear las siguientes máquinas virtuales:
- load-balancer
- db-server
- nfs-server
- wordpress-1
- wordpress-2
[![Product Name Screen Shot][maquinas]]((http://34.207.26.5))

1. Crear máquina virtual en GCP. (Repetir los pasos a continuación para cada máquina, cambie solamente el nombre a asignar)
[![Product Name Screen Shot][instancia]]((http://34.207.26.5))
También se habilita los puertos para el tráfico.
[![Product Name Screen Shot][firewall]]((http://34.207.26.5))

2. Asignar dirección estática. Para ello vamos a Red de VPC- Direcciones IP - Direcciones IP externas - Reservar.  
**Nota**: En vez de cambiar te dira reservar, dar click, asignar un nombre y finalmente crear. Recuerda seleccionar la dirección IP externa de la máquina recién creada.
[![Product Name Screen Shot][estatica]]((http://34.207.26.5))
Finalmente la máquina queda así:
[![Product Name Screen Shot][lab3]]((http://34.207.26.5))

3. Generación de claves ssh:  
Generar el par de claves
    - Chequea que no exista el par de claves en tu computador local.
        - ``` cd ~/.ssh ```
        - `ls`
        - Si ves un archivo `id_rsa.pub` , es que ya se generaron el par de claves y no es necesario crear otra nueva.
    - Si no ves `id_rsa.pub` , usa el comando a continuación para generar un par nuevo. Reemplaza tu correo.
        - `ssh-keygen -t rsa -C "sochoac1@eafit.edu.co"`
    - Dale enter para guardar en la ubicación por defecto.
Ahora debe colocar una **copia de su clave pública en cualquier servidor** al que le gustaría usar SSH para conectarse, en lugar de iniciar sesión con un nombre de usuario y una contraseña.
    - Muestre contenido de su nuevo archivo de clave pública con `cat` :
        - `cat ~/.ssh/id_rsa.pub`
    - Copie el contenido de la salida e inicie sesión en el servidor remoto con su nombre de usuario y contraseña a través de GCP dando click a **SSH** iniciar en otra ventana.
    [![Product Name Screen Shot][ssh]]((http://34.207.26.5))
    - Pegue el contenido que copio al final de `~/.ssh/authorized_keys`
        - `sochoac16_finca@lab3:~$ nano ~/.ssh/authorized_keys`
    - Después de agregar el contenido, cierre sesión en la máquina remota e intente iniciar sesión nuevamente. Si configura su clave SSH correctamente, no necesitará escribir su contraseña.
4. Configurar freenom.
[![Product Name Screen Shot][freenom]]((http://34.207.26.5))
5. Crear las entradas en cloud DNS.   
**Nota**: Habilitar la API de GCP **Cloud DNS** (buscar en marketplace), luego crear una zona (En el campo de servidor DNS colocar el dominio de freenom) y añade los resgistros tipo A y CNAME. El TXT se necesitara más adelante entonces no se debe crear todavía.
[![Product Name Screen Shot][dns]]((http://34.207.26.5))
6. Poner los nameservers de GCP en freenom.  
[![Product Name Screen Shot][nameservers]]((http://34.207.26.5))
### Paso a paso para la creación de load balancer con nginx y docker.
1. Instale certbot.
```
sudo apt update
snap install certbot --classic
sudo apt install letsencrypt -y
sudo apt install nginx -y
```
2. Configurar nginx.conf. Editar este archivo:     
``` sudo vim /etc/nginx/nginx.conf ```  
3. Luego, borrar todo y copiar lo siguiente:   
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
events {
  worker_connections  1024;  ## Default: 1024
}
http {
upstream loadbalancer{
server 10.128.0.6:80 weight=5;
server 10.128.0.8:80 weight=5;
}
server {
  listen 80;
  listen [::]:80;
  server_name _;
  rewrite ^ https://$host$request_uri permanent;
}
server {
  listen 443 ssl http2 default_server;
  listen [::]:443 ssl http2 default_server;
  server_name _;
  # enable subfolder method reverse proxy confs
  #include /config/nginx/proxy-confs/*.subfolder.conf;
  # all ssl related config moved to ssl.conf
  include /etc/nginx/ssl.conf;
  client_max_body_size 0;
  location / {
    proxy_pass http://loadbalancer;
    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
}
```
Finalmente corra los comando a continuación:
```
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t

sudo service nginx reload
```
4. Ejecute certbot para pedir certificado **SSL** para registros especificos:
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m sochoac1@eafit.edu.co --agree-tos -d lab4.sochoac.tk
```
5. Ejecute certbot para pedir certificado **SSL** para todo el dominio (wildcard):
```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sochoac.tk --manual --preferred-challenges dns-01 certonly
```
**Nota**: Este comando queda pausado indicando que debe crear un registro TXT en su dominio, una vez lo cree y verifique, dele ENTER para Continuar. Debe terminar con éxito. **Debemos en este punto crear el registro TXT**.

[![Product Name Screen Shot][txt]]((http://34.207.26.5))
Con lo subrayado en verde basarse para crear el TXT, una vez creado dar ENTER. Recuerda que se debe crear en DNS GCP.  

6. Cree los archivos de docker-compose.
```
mkdir /home/sochoa16_finca/nginx-lb
mkdir /home/sochoa16_finca/nginx-lb/ssl
sudo su
```
Luego, crear el archivo de configuración options-ssl-nginx.conf:  
```vim options-ssl-nginx.conf```
```
# This file contains important security parameters. If you modify this file
# manually, Certbot will be unable to automatically provide future security
# updates. Instead, Certbot will print and log an error message with a path to
# the up-to-date file that you will need to refer to when manually updating
# this file.
ssl_session_cache shared:le_nginx_SSL:10m;
ssl_session_timeout 1440m;
ssl_session_tickets off;
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;
ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";
```
Tambien se debe crear el ssh-dhparams.pem:
```
openssl dhparam -out ssl-dhparams.pem 512
```
Posteriormente, agregué los siguientes archivos en wordpress:

```
cp /etc/letsencrypt/live/lab4.sochoac.tk/* /home/sochoa16_finca/nginx/ssl/

cp /etc/letsencrypt/options-ssl-nginx.conf /home/sochoa16_finca/nginx/ssl/
cp /etc/letsencrypt/ssl-dhparams.pem /home/sochoa16_finca/wordpress/ssl/
exit
```
Finalmente, corra lo siguiente:
```
DOMAIN='lab4.sochoac.tk' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'

    cp /etc/letsencrypt/live/sudominio.com/* /home/gcp-username/wordpress/ssl/

    exit
```  
7. Instalar docker y docker-compose en Ubuntu:22.0.4.    
``` 
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
``` 
8. Copie los archivos del docker al sitio propio e inicie.
``` 
git clone https://github.com/st0263eafit/st0263-2022-2.git

cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp ssl.conf /home/scohoa16_finca/nginx
```
Cree un archivo docker-compose.yml y copie lo siguiente
```
version: '3.1'
services:
  nginx:
    container_name: nginx
    image: nginx
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - ./ssl:/etc/nginx/ssl
    - ./ssl.conf:/etc/nginx/ssl.conf
    ports:
    - 80:80
    - 443:443

```
9. Inicie el servidor de nginx en docker.
``` 
ps ax | grep nginx
netstat -an | grep 80

sudo systemctl disable nginx
sudo systemctl stop nginx
``` 
vuelve y se conecta a la máquina para que ese proceso no esté corriendo.
**UNA VEZ DETENIDO:**
``` 
cd /home/scohoa16_finca/nginx
sudo docker-compose up --build -d
``` 
10. Pruebe desde un browser: [https://lab4.sochoac.tk/](https://lab4.sochoac.tk/)

### Paso a paso para la creación de NFS.
1. Se instala nginx a ambos wordpress.
[![Product Name Screen Shot][nginx2]]((http://34.207.26.5))
2. Se instala el servidor nfs dentro de la máquina virtual nfs-server.
[![Product Name Screen Shot][nfs]]((http://34.207.26.5))
3. Se crea la carpeta a compartir y se asignan permisos.
[![Product Name Screen Shot][permisos]]((http://34.207.26.5))
4. Modificamos el archivo exports localizado en /etc/exports. (Se coloca la subred dentro de la cual se encuentran ambas máquinas virtuales que contienen la instancia del wordpress).
[![Product Name Screen Shot][exports]]((http://34.207.26.5))
5. Actualizamos exports y luego se configura el firewall.
[![Product Name Screen Shot][firewallnfs]]((http://34.207.26.5))
6. Configurar fstab dentro de /etc/fstab
[![Product Name Screen Shot][fstab]]((http://34.207.26.5))
7. En cada wordpress cliente repetir los comandos a continuación.  
- Instalar el nfs client: 
``` 
sudo apt install nfs-common
``` 
- Crear el mount point para el cliente:
``` 
sudo mkdir -p /mnt/nfs_clientshare
``` 
- Luego, haga mount del NFS compartido con el servidor nfs-server(10.128.0.7):
``` 
sudo mount 10.128.0.7:/mnt/nfs_share /mnt/nfs_clientshare
``` 
- Finalmente, compruebe que todo este correcto:
[![Product Name Screen Shot][nfs-server]]((http://34.207.26.5))

### Paso a paso para la creación de la base de datos.
1. Se deben habilitar los puertos a utilizar.
[![Product Name Screen Shot][mysql]]((http://34.207.26.5))

2. Crear una carpeta que contiene el contenedor mysql:
[![Product Name Screen Shot][schemas]]((http://34.207.26.5))
- Crear el archivo Dockerfile copiando solo lo siguiente:
``` 
FROM mysql:8.0
``` 
- Crear el archivo docker-compose.yaml copiando lo siguiente:
``` 
version: "3.7"
services:
  mysql:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: dbserver
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "4444"
      MYSQL_DATABASE: "wordpressdb"
    volumes:
      - ./schemas:/var/lib/mysql:rw
volumes:
  schemas: {}
``` 
- Schemas se crea automaticamente al correr el contenedor.
3. Instalar docker y docker-compose:
``` 
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
``` 
3. Corra el contenedor mysql:
``` 
sudo docker-compose up --build -d
``` 
4. Conectese a la base de datos para comprabar que si haya funcionado.
``` 
sudo docker exec -it dbserver mysql  -p
``` 
5. Crear una base de datos y un usuario para que utilicen las instancias de wordpress.
[![Product Name Screen Shot][db]]((http://34.207.26.5))

### Paso a paso para la creación de las instancias de wordpress utilizando docker y docker-compose. (Repita los pasos para cada máquina wordpress creada)
1. Instalar docker y docker-compose.
``` 
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
``` 
2. Detener los servicios de nginx.
``` 
ps ax | grep nginx
netstat -an | grep 80

sudo systemctl disable nginx
sudo systemctl stop nginx
``` 
3. Crear un carpeta wordpress que contendra el contenedor.
[![Product Name Screen Shot][word]]((http://34.207.26.5))
- Crear un archivo docker-compose.yml y colocar lo siguiente:
``` 
version: '3.7'
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    environment:
      WORDPRESS_DB_HOST: 10.128.0.5:3306
      WORDPRESS_DB_USER: wp1
      WORDPRESS_DB_PASSWORD: 4444
      WORDPRESS_DB_NAME: dbwp
    volumes:
      - /var/www/html:/var/www/html
    ports:
      - 80:80
volumes:
  wordpress:
``` 
4. Corra el contenedor de wordpress.
``` 
sudo docker-compose up --build -d
``` 

### Ingrese al sitio web. 
5. Pruebe desde un browser: [https://lab4.sochoac.tk/](https://lab4.sochoac.tk/)

# 4. otra información que considere relevante para esta actividad.
- **Nota**: En el github esta la clave privada para ingresar a la MV.
# referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- https://cloud.google.com/dns?hl=es
- https://linuxhint.com/install-and-configure-nfs-server-ubuntu-22-04/
- https://hub.docker.com/r/bitnami/wordpress-nginx/
- https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee

#### versión README.md -> 1.0 (2022-agosto)

[docker]: Images/arquitectura.png
[maquinas]: Images/maquinas.png
[instancia]: Images/instancia.png
[firewall]: images/https.png
[estatica]: images/estatica.png
[lab3]: images/lab3.png
[ssh]: images/ssh.png
[dns]: images/dns.png
[freenom]: images/freenom.png
[nameservers]: images/nameservers.png
[txt]: images/txt.png
[nginx2]: Images/nginx2.png
[nfs]: Images/nfs.png
[permisos]: Images/permisos.png
[exports]: Images/exports.png
[firewallnfs]: Images/firewallnfs.png
[fstab]: Images/fstab.png
[nfs-server]: Images/nfs-server.png
[mysql]: Images/mysql.png
[schemas]: Images/schemas.png
[db]: Images/db.png
[word]: Images/word.png
