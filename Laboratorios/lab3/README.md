# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 3 - Contenedores - Docker -Wordpress - Dominio - SSL
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Crear una máquina virtual  por medio de Google Cloud Platform(GCP) y asignarle una dirección Ip estática.
- Desplegar contenedores a través de Docker y Docker compose para instalar wordpress.
- Iniciar el servidor de wordpresss en docker.
- Utilizar certbot para pedir certificado SSL para todo el dominio (wildcard) permitiendo la navegación segura en el servidor.
- Obtener un dominio valido a través de Freenom [https://www.sochoac.tk/](https://www.sochoac.tk/).


# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **Docker** : Docker es un sistema operativo (o runtime) para contenedores. El motor de Docker se instala en cada servidor en el que desee ejecutar contenedores y proporciona un conjunto sencillo de comandos que puede utilizar para crear, iniciar o detener contenedores.
[![Product Name Screen Shot][docker]]((http://34.207.26.5))

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### detalles del desarrollo técnicos.
- Se utiliza el sistema operativo Ubunutu 20.04.4.
- Se utiliza cerbot y letsencrypt para el certificado SSL.
- Se utililiza el servidor nginx.
- Se utilizo docker.io y docker-compose.

### Paso a paso de laboratorio 3.
1. Crear máquina virtual en GCP.
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
7. Instale certbot.
```
sudo apt update
snap install certbot --classic
sudo apt install letsencrypt -y
sudo apt install nginx -y
```
8. Configurar nginx.conf. Editar este archivo:     
``` sudo vim /etc/nginx/nginx.conf ```  
9. Luego, borrar todo y copiar lo siguiente:   
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
    worker_connections  1024;  ## Default: 1024
}
http {
    server {
        listen  80 default_server;
        server_name _;
        location ~ /\.well-known/acme-challenge/ {
            allow all;
            root /var/www/letsencrypt;
            try_files $uri = 404;
            break;
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
10. Ejecute certbot para pedir certificado **SSL** para registros especificos:
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m sochoac1@eafit.edu.co --agree-tos -d sochoac.tk
```
11. Ejecute certbot para pedir certificado **SSL** para todo el dominio (wildcard):
```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sochoac.tk --manual --preferred-challenges dns-01 certonly
```
**Nota**: Este comando queda pausado indicando que debe crear un registro TXT en su dominio, una vez lo cree y verifique, dele ENTER para Continuar. Debe terminar con éxito. **Debemos en este punto crear el registro TXT**.

[![Product Name Screen Shot][txt]]((http://34.207.26.5))
Con lo subrayado en verde basarse para crear el TXT, una vez creado dar ENTER. Recuerda que se debe crear en DNS GCP.  

12. Cree los archivos de docker-compose.
```
mkdir /home/sochoa16_finca/wordpress
mkdir /home/sochoa16_finca/wordpress/ssl
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
openssl dhparam -out dhparam.pem 512
```
Posteriormente, agregué los siguientes archivos en wordpress:

```
cp /etc/letsencrypt/live/sudominio.com/* /home/sochoa16_finca/wordpress/ssl/

cp /etc/letsencrypt/options-ssl-nginx.conf /home/sochoa16_finca/wordpress/ssl/
cp /etc/letsencrypt/ssl-dhparams.pem /home/sochoa16_finca/wordpress/ssl/
exit
```
Finalmente, corra lo siguiente:
```
DOMAIN='sochoac.tk' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'

    cp /etc/letsencrypt/live/sudominio.com/* /home/gcp-username/wordpress/ssl/

    exit
```  
13. Instalar docker y docker-compose en Ubuntu:22.0.4.    
``` 
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
``` 
14. Copie los archivos del docker al sitio propio e inicie.
``` 
git clone https://github.com/st0263eafit/st0263-2022-2.git

cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/scohoa16_finca/wordpress
sudo cp nginx.conf /home/scohoa16_finca/wordpress
sudo cp ssl.conf /home/scohoa16_finca/wordpress
``` 
15. Inicie el servidor de wordpress en docker.
``` 
ps ax | grep nginx
netstat -an | grep 80

sudo systemctl disable nginx
sudo systemctl stop nginx
``` 
vuelve y se conecta a la máquina para que ese proceso no esté corriendo.
**UNA VEZ DETENIDO:**
``` 
cd /home/gcp-username/wordpress
sudo docker-compose up --build -d
``` 
16. Pruebe desde un browser: [https://www.sochoac.tk/](https://www.sochoac.tk/)

# 4. otra información que considere relevante para esta actividad.
- **Nota**: En el github esta la clave privada para ingresar a la MV.
# referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- https://cloud.google.com/dns?hl=es
- 

#### versión README.md -> 1.0 (2022-agosto)

[docker]: images/arquitectura.png
[instancia]: images/instancia.png
[firewall]: images/https.png
[estatica]: images/estatica.png
[lab3]: images/lab3.png
[ssh]: images/ssh.png
[dns]: images/dns.png
[freenom]: images/freenom.png
[nameservers]: images/nameservers.png
[txt]: images/txt.png
