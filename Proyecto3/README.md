# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Proyecto 3 - Spark con Notebooks y PySpark - 
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Creación de un clúster EMR donde se activa el servicio HUE.
- Utilizar HIVE y SparkSQL para la gestión de datos vía SQL.
- Se utilizo pyspark para ejecutar el wordcount de forma interactiva con datos en HDFS y S3 respectivamente.
- Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en s3.
- Replicar, ejecutar y entender el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos.
- Almacenar datos en AWS S3 y en google drive.
- Cargar datos desde AWS S3 y desde google drive.
- Analisis exploratorio del dataframe donde cargamos los datos.
- Contestar diferentes preguntas sobre los datos de covid.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **AWS BUCKET** :Un bucket es un contenedor de objetos. Para almacenar sus datos en Amazon S3, primero debe crear un depósito y especificar un nombre de depósito y una región de AWS. Luego, carga sus datos en ese depósito como objetos en Amazon S3. Cada objeto tiene una clave (o nombre de clave), que es el identificador único del objeto dentro del depósito.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## Importante
Antes de comenzar la explicación del proyecto 3 tener encuenta los siguientes archivos y links de s3:
- [PySpark_drive](PySpark_drive.ipynb)
- [PySpark_aws](Pyspark_aws.ipynb)
- s3://notebooksochoacv
## Almacenar datos en AWS S3 y en google drive. (Casos_positivos_de_COVID-19_en_Colombia.csv)
1. Datos en AWS S3.
    [![Product Name Screen Shot][s3]]()
2. Datos en google drive.
    [![Product Name Screen Shot][drive]]()

## Análisis exploratorio del dataframe donde cargamos los datos:
### Para S3 con AWS

0. Ponemos las credenciales de la sesión de AWS.
    [![Product Name Screen Shot][aws]]()
1. Cargamos los datos en google colab desde S3.
    [![Product Name Screen Shot][aws2]]()
1. Columnas en el dataframe.
    [![Product Name Screen Shot][aws3]]()
2. Tipo de datos.
    [![Product Name Screen Shot][aws4]]()
3. Seleccionar algunas columnas.  
    [![Product Name Screen Shot][aws5]]()
4. Renombrar una columna.
    [![Product Name Screen Shot][aws6]]()
5. Agregar columnas.
    [![Product Name Screen Shot][aws7]]()
6. Eliminar columnas.
    [![Product Name Screen Shot][aws8]]()
7. Filtrar datos
    [![Product Name Screen Shot][aws9]]()
8. Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.
    [![Product Name Screen Shot][aws10]]()
### Para google colab
0. Cargamos los datos en google colab desde gdrive.
    [![Product Name Screen Shot][colab]]()
1. Columnas en el dataframe.
    [![Product Name Screen Shot][colab2]]()
2. Tipos de datos.
    [![Product Name Screen Shot][colab3]]()
3. Seleccionar algunas columnas.  
    [![Product Name Screen Shot][colab5]]()
4. Cambiar el nombre de una columna.
    [![Product Name Screen Shot][colab4]]()
5. Agregar columnas.
    [![Product Name Screen Shot][colab6]]()
6. Eliminar columnas.
    [![Product Name Screen Shot][colab7]]()
8. Filtrar datos.
    [![Product Name Screen Shot][colab8]]()
9. Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.
    [![Product Name Screen Shot][colab9]]()

## Contestar las siguientes preguntas
### 3.1 Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.
1. Como un dataframe.
    [![Product Name Screen Shot][preg]]()
2. Como un SparkSQL.
    [![Product Name Screen Shot][preg6]]()
### 3.2 Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor.
1. Como un dataframe.
    [![Product Name Screen Shot][preg2]]()
2. Como un SparkSQL.
    [![Product Name Screen Shot][preg7]]()

### 3.3 Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.
1. Como un dataframe.
    [![Product Name Screen Shot][preg3]]()
2. Como un SparkSQL.
    [![Product Name Screen Shot][preg8]]()

### 3.4 Distribución de casos por edades de covid en Colombia.
1. Como dataframe.
    [![Product Name Screen Shot][preg4]]()
2. Como un SparkSQL.
    [![Product Name Screen Shot][preg9]]()
### 3.5 Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark.
1. Como un dataframe.
    [![Product Name Screen Shot][preg5]]()
2. Como un SparkSQL.
    [![Product Name Screen Shot][preg10]]()
## Salve los datos del numeral 3, en el bucket público de cada estudiante
1. Corremos los siguientes comandos.
    [![Product Name Screen Shot][preg11]]()

# 4. Referencias
[Este es el link al repositorio de la materia donde me base para realizar el lab6.](https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata)




#### versión README.md -> 1.0 (2022-agosto)

[s3]: Images/1-S3.png
[drive]: Images/2-drive.png
[preg]: Images/3-preg1.png
[preg2]: Images/4-preg2.png
[preg3]: Images/6-preg4.png
[preg4]: Images/5-preg3.png
[preg5]: Images/7-preg5.png
[preg6]: Images/8-preg6.png
[preg7]: Images/9-preg7.png
[preg8]: Images/10-preg8.png
[preg9]: Images/11-preg9.png
[preg10]: Images/12-preg10.png
[preg11]: Images/13-preg11.png


[colab]: colab/1-colab.png
[colab2]: colab/2-colab2.png
[colab3]: colab/3-colab3.png
[colab4]: colab/4-colab4.png
[colab5]: colab/5-colab5.png
[colab6]: colab/6-colab6.png
[colab7]: colab/7-colab7.png
[colab8]: colab/8-colab8.png
[colab9]: colab/9-colab9.png

[aws]: aws/1-aws.png
[aws2]: aws/2-aws2.png
[aws3]: aws/3-aws3.png
[aws4]: aws/4-aws4.png
[aws5]: aws/5-aws5.png
[aws6]: aws/6-aws6.png
[aws7]: aws/7-aws7.png
[aws8]: aws/8-aws8.png
[aws9]: aws/9-aws9.png
[aws10]: aws/10-aws10.png






