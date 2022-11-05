# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 5 - Crear un Cluster AWS EMR en Amazon para trabajar todos los demás laboratorios.
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Se creo un clúster de Amazon EMR.
- Creación de un bucket de AMAZON S3 para almacenar los datos de entrada o de salida de los programas que ejecute en el cluster.


# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **AWS** : Amazon EMR (anteriormente denominado Amazon Elastic) MapReduce) es una plataforma de clúster administrada que simplifica la ejecución de los marcos de trabajo de Big Data, tales comoApache HadoopyApache Spark, enAWSpara procesar y analizar grandes cantidades de datos. Con estos marcos y proyectos de código abierto relacionados, puede procesar datos con fines de análisis y cargas de trabajo de inteligencia empresarial. Amazon EMR también le permite transformar y mover grandes cantidades de datos desde y hacia otrosAWSalmacenes de datos y bases de datos, como Amazon Simple Storage Service (Amazon S3) y Amazon DynamoDB.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### Evidencia de la creación del cluster.

1. En el paso 1. Software y configuración.
[![Product Name Screen Shot][config]]((http://34.207.26.5))

2. Configuración del bucket.
[![Product Name Screen Shot][bucket]]((http://34.207.26.5))
3. Nodos clusters e instancias.
[![Product Name Screen Shot][clusters]]((http://34.207.26.5))
4. Almacenamiento EBS root volume.
[![Product Name Screen Shot][volume]]((http://34.207.26.5))

5. Opciones generales.
[![Product Name Screen Shot][general]]((http://34.207.26.5))

6. Comenzando cluster.
[![Product Name Screen Shot][comenzando]]((http://34.207.26.5))

7. Notebook creado.
[![Product Name Screen Shot][notebook]]((http://34.207.26.5))

8. Conectar al nodo maestro utilizando SSH.
[![Product Name Screen Shot][masterssh]]((http://34.207.26.5))

9. Configuración completa.
[![Product Name Screen Shot][listo]]((http://34.207.26.5))

10. Links de las apps.
[![Product Name Screen Shot][apps]]((http://34.207.26.5))

11. Grupos de seguridad para utilizar las apps.
[![Product Name Screen Shot][seguridad]]((http://34.207.26.5))

12. Entrando al master.
[![Product Name Screen Shot][master]]((http://34.207.26.5))

13. Entrando a hue.
[![Product Name Screen Shot][hue]]((http://34.207.26.5))

14. Entrando a jupyter.
[![Product Name Screen Shot][jupyter]]((http://34.207.26.5))

15. Entrando a zepelin.
[![Product Name Screen Shot][zepelin]]((http://34.207.26.5))



#### versión README.md -> 1.0 (2022-agosto)

[config]: Imagenes/1-config.png
[bucket]: Imagenes/2-config.png
[clusters]: Imagenes/3-m4large.png
[volume]: Imagenes/4-almacenamiento.png
[general]: Imagenes/5-name.png
[comenzando]: Imagenes/6-clusterCreado.png
[notebook]: Imagenes/7-notebookssochoac1.png
[masterssh]: Imagenes/8-maclinuxmaster.png
[listo]: Imagenes/9-listo.png
[apps]: Imagenes/10-apps.png
[seguridad]: Imagenes/11-gruposseguridad.png
[master]: Imagenes/12-master.png
[hue]: Imagenes/13-hue.png
[jupyter]: Imagenes/14-jupyter.png
[zepelin]: Imagenes/15-zepelin.png
[firewallnfs]: Images/firewallnfs.png
[fstab]: Images/fstab.png
[nfs-server]: Images/nfs-server.png
[mysql]: Images/mysql.png
[schemas]: Images/schemas.png
[db]: Images/db.png
[word]: Images/word.png
