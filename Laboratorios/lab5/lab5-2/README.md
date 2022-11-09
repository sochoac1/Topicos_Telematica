# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 5-2 - GESTIÓN DE ARCHIVOS EN HDFS Y S3 PARA BIG DATA - 
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Creación de un clúster EMR donde se activa el servicio HUE.
- Copiar archivos hacia el HDFS vía HUE.
- Copiar archivos hacie el HDFS vía SSH.
- Copiar archivos hacia AWS S3 vía HUW.
- Copiar archivos hacia el AWS S3 vía SSH.



# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **AWS BUCKET** :Un bucket es un contenedor de objetos. Para almacenar sus datos en Amazon S3, primero debe crear un depósito y especificar un nombre de depósito y una región de AWS. Luego, carga sus datos en ese depósito como objetos en Amazon S3. Cada objeto tiene una clave (o nombre de clave), que es el identificador único del objeto dentro del depósito.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### Evidencia de la creación del cluster.

1. Creación del propio directorio de 'datasets' en HDFS
[![Product Name Screen Shot][datasets]]((http://34.207.26.5))
   * Copiar el datasets a traves de scp
   [![Product Name Screen Shot][ssh]]((http://34.207.26.5))
   * Crear una carptea gutenberg-small
   [![Product Name Screen Shot][guten]]((http://34.207.26.5))
   * Archivos locales FS en el emr-master
   [![Product Name Screen Shot][putgu]]((http://34.207.26.5))
   * Creación de dataset en S3 bucket
   [![Product Name Screen Shot][bucket]]((http://34.207.26.5))
   * Archivos en Amazon s3
   [![Product Name Screen Shot][s3]]((http://34.207.26.5))
   * Copia recursiva de datos
   [![Product Name Screen Shot][recursiva]]((http://34.207.26.5))


2. Listar archivos
    * Listar
    [![Product Name Screen Shot][listar]]((http://34.207.26.5))

3. Copiar archivos de HDFS hacia el servidor local (gateway)
    * Archivos HDFS hacia el servidor local
    [![Product Name Screen Shot][copialocal]]((http://34.207.26.5))
    * Otra forma de copiarlos
    [![Product Name Screen Shot][otraforma]]((http://34.207.26.5))
4. Comandos basicos
    * Algunos comandos basicos.
    [![Product Name Screen Shot][comandosbasicos]]((http://34.207.26.5))
    * Comandos de chmod y resto.
    [![Product Name Screen Shot][resto]]((http://34.207.26.5))

5. Gestión de archivos vía HUE en Amazon EMR.
   * Paso a paso
    [![Product Name Screen Shot][onu]]((http://34.207.26.5))
   * Visualizar
   [![Product Name Screen Shot][visualizar]]((http://34.207.26.5))



#### versión README.md -> 1.0 (2022-agosto)

[datasets]: Imagenes/1-carpetadatasets.png
[ssh]: Imagenes/2-datasets.png
[guten]: Imagenes/3-carpetagutenberg.png
[putgu]: Imagenes/4-guterberzip.png
[bucket]: Imagenes/5-datasetsbucket.png
[s3]: Imagenes/6-amazons3.png
[recursiva]: Imagenes/7-recursiva.png
[listar]: Imagenes/8-listar.png
[copiarlocal]: Imagenes/9-copiararchivoshdfslocal.png
[otraforma]: Imagenes/10-otraformadecopiar.png
[comandosbasicos]: Imagenes/11-comandosbasicos.png
[onu]: Imagenes/12-onu.png
[visualizar]: Imagenes/13-visualizardatos.png
[resto]: Imagenes/14-comandosfaltantes.png
