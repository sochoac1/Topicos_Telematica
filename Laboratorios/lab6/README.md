# ST0263_3832_2266 Tópicos Especiales en Telemática
## Estudiante(s): Santiago Ochoa Castaño, sochoac1@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 6 - Wordcount en Apache Spark en AWS EMR 6.3.1 - 
#
# 1. Breve descripción de la actividad

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Creación de un clúster EMR donde se activa el servicio HUE.
- Utilizar HIVE y SparkSQL para la gestión de datos vía SQL.
- Se utilizo pyspark para ejecutar el wordcount de forma interactiva con datos en HDFS y S3 respectivamente.
- Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en s3.
- Replicar, ejecutar y entender el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- **AWS BUCKET** :Un bucket es un contenedor de objetos. Para almacenar sus datos en Amazon S3, primero debe crear un depósito y especificar un nombre de depósito y una región de AWS. Luego, carga sus datos en ese depósito como objetos en Amazon S3. Cada objeto tiene una clave (o nombre de clave), que es el identificador único del objeto dentro del depósito.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Guía de conexión al cluster en Amazon EMR y cargar los datasets al hdfs:
1. Entramos por ssh al master EMR (especificar donde se encuentra el .pem).
    ```
    ssh -i final.pem hadoop@ec2-54-227-78-19.compute-1.amazonaws.com
    ```
    [![Product Name Screen Shot][master]]()

2. Cargamos los datasets en nuestro master EMR utilizando scp desde donde tenemos los archivos.
    ```
    scp -r -i final.pem st0263-2022-2-main/bigdata/datasets/ hadoop@ec2-54-227-78-19.compute-1.amazonaws.com:
    ```
    [![Product Name Screen Shot][datasets]]()
3. Creamos en el master EMR la siguiente carpetas dentro del hdfs.
    ```
    hdfs dfs -mkdir /user/hadoop/datasets
    ```
    [![Product Name Screen Shot][hadoop]]()
4. Realizamos copia recursiva del dataset al hdfs desde el master EMR.
    ```
    hdfs dfs -copyFromLocal datasets/* /user/hadoop/datasets
    ```
    [![Product Name Screen Shot][recursiva]]()
## Parte 1:
### Ejecutar el wordcount por linea de comando 'pyspark' Interactivo en EMR con datos en HDFS vía ssh en el nodo master.
**Nota**: En el punto anterior se explico como llevar los datos del datasets en HDFS.
1. En el nodo master ejecutamos los comandos a continuación.
    ```
    $ pyspark
    >>> files_rdd = sc.textFile("hdfs:///user/hadoop/datasets/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout1")
    ```
    [![Product Name Screen Shot][pyspark1]]()
2. Observamos el archivo que se salvo en **/tmp/wcout1**.
    [![Product Name Screen Shot][wcout1]]()

### Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.
1. Creamos un bucket s3 con los datos a utilizar.
    [![Product Name Screen Shot][notebook]]()
2. En el nodo master ejecutamos los comandos a continuación.
     ```
    $ pyspark
    >>> files_rdd = sc.textFile("s3://notebooksochoac/datasets/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> 
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout2")
    ```
    [![Product Name Screen Shot][pyspark2]]()
2. Observamos el archivo que se salvo en **/tmp/wcout2**.
    [![Product Name Screen Shot][wcout2]]()
### Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.
1. Ingreamos a la interfaz de Jupyter Notebooks, creamos un notebook y ejecutamos el wordcount.
    [![Product Name Screen Shot][pyspark3]]()
    **Nota**: Ver el archivo [wordcount-spark.ipynb](jupyter/wordcount-spark.ipynb).

2. Observamos el archivo que se salvo en **/tmp/wcout3**.
    [![Product Name Screen Shot][wcout3]]()
3. Observamos el archivo que se salvo en **s3**.
    [![Product Name Screen Shot][s3]]()

## Parte 2:
### Replique, ejecute y ENTIENDA el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos.
1. Creamos un nuevo notebook en jupyter.  
**Nota**: Ver el archivo [Data_processing_using_PySpark](jupyter/Data_processing_using_PySpark.ipynb).
1. Cambiamos la versión de python.
    [![Product Name Screen Shot][python]]()
2. Ejecutamos los siguientes comandos:
    - Listas columnas
    - Número de columnas
    - Número de registros
    - Forma del dataset
    - Imprimir esquema
    - Primeras 5 filas
    - Seleccionar 2 columnas y 5 registros
    - Información del dataframe
    [![Product Name Screen Shot][col]]()
    [![Product Name Screen Shot][col2]]()
3. Comandos más específicos:
    - Se agrega columna que calcula la edad de las personas dentro de 10 años.
    [![Product Name Screen Shot][edad]]()
    - Se pasa la edad a double.
    [![Product Name Screen Shot][double]]()
    - Filtra los registros cuyo 'mobile' sea 'Vivo'.
    [![Product Name Screen Shot][vivo]]()
    - Filtra los registros cuyo 'mobile' sea 'Vivo' y muestra las columnas 'age', 'ratings', 'mobile'.
    [![Product Name Screen Shot][vivo2]]()
    - Filtra los registros cuyo 'mobile' sea 'Vivo' y 'experiencia' mayor a 10 (Dos formas).
    [![Product Name Screen Shot][vivo3]]()
    - Filtra los valores de una columna sin repetir.
    [![Product Name Screen Shot][unicos]]()
    - Cuenta los valores de una columna sin repetir.
    [![Product Name Screen Shot][unicos2]]()
    - Agrupa registros cuyo valor coincida respecto a una columna, luego cuenta las coincidencias.
    [![Product Name Screen Shot][unicos3]]()
    - Cuenta las coincidencias de un valor de una columna y los agrupa de mayor a menor.
    [![Product Name Screen Shot][unicos4]]()
    - Agrupa los valores de una columna y muestra el promedio en que aparece el valor para cada columna.
    [![Product Name Screen Shot][promedio]]()
    - Agrupa los valores de una columna y muestra la suma en que aparece el valor para cada columna.
    [![Product Name Screen Shot][suma]]()
    - Agrupa los valores de una columna y muestra el maximo en que aparece el valor para cada columna.
    [![Product Name Screen Shot][maximo]]()
    - Agrupa los valores de una columna y muestra el minimo en que aparece el valor para cada columna.
    [![Product Name Screen Shot][minimo]]()
    - Agrupa los valores de una columna y muestra la agregación.
    [![Product Name Screen Shot][agregacion]]()
4. Comandos con UDF (Codigo python como si fueran funciones SQL)
    - Función para catalogar las marcas en 'High price', 'Mid Price' y 'Low Price'
    [![Product Name Screen Shot][udf]]()
    - Utilizar funcion lambda para determinar si la persona es joven o adulta.
    [![Product Name Screen Shot][udf2]]()
5. Comandos con Pandas (Excel de Python)
    - Años faltantes para los 100
    [![Product Name Screen Shot][pandas]]()
    - Multiplicar el 'rating' por la 'expetience'
    [![Product Name Screen Shot][pandas2]]()
    - Cuenta valores duplicados y drop a los valores duplicados
    [![Product Name Screen Shot][pandas3]]()
    - Drop a los valores de una columna
    [![Product Name Screen Shot][pandas4]]()
    
6. Guardar un archivo csv
    [![Product Name Screen Shot][csv]]()

## Parte 3
## HIVE y SparkSQL, gestión de datos vía SQL
### Gestión (DDL) y Consultas (DQL)
1. Ir al apartado hive utilizando la interfaz de HUE.
    [![Product Name Screen Shot][hue]]()
2. Crear la tabla HDI en HDFS/beeline:
    ```
    # tabla externa en S3: 
    use usernamedb;
    CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://st0263datasets/onu/hdi/'
    ```
    [![Product Name Screen Shot][hive]]()
3. Hacer consultas y cálculos sobre la tabla HDI:
    - Consultar con gni menor a 200
        ```
        use usernamedb;
        show tables;
        describe hdi;

        select * from hdi;

        select country, gni from hdi where gni > 2000;
        ```
        [![Product Name Screen Shot][hive2]]()
    - Ejecutar un JOIN con HIVE
    1. Crear la tabla EXPO en base a: export-data.csv
    ```
    use usernamedb;
    CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://notebooksochoac/datasets/onu/export/'
    ```
    [![Product Name Screen Shot][hive3]]()
    2. Ejecutar JOIN con las tablas hdi y expo
    ```
    SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;

    ```
    [![Product Name Screen Shot][hive4]]()

4. Wordcount en HIVE:
    - Utilizando HDFS, creamos la tabla
        ```
        use usernamedb;
        CREATE EXTERNAL TABLE docs (line STRING) 
        STORED AS TEXTFILE 
        LOCATION 'hdfs:///user/hadoop/datasets/gutenberg-small/';
        ```
        [![Product Name Screen Shot][hive5]]()
    - Ordenado por palabra
        ```
        SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
        GROUP BY word 
        ORDER BY word DESC LIMIT 10;
        ```
        [![Product Name Screen Shot][hive6]]()
    - Ordenado por frecuencia de menor a mayor
        ``` 
        SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
        GROUP BY word 
        ORDER BY count DESC LIMIT 10;
        ```
        [![Product Name Screen Shot][hive7]]()


# 4. Referencias
[Este es el link al repositorio de la materia donde me base para realizar el lab6.](https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata)

    


#### versión README.md -> 1.0 (2022-agosto)

[master]: Images/1-master.png
[datasets]: Images/2-datasets.png
[hadoop]: Images/3-hadoop.png
[recursiva]: Images/4-recursiva.png
[pyspark1]: Images/5-pyspark1.png
[wcout1]: Images/6-wcout1.png
[notebook]: Images/7-notebook.png
[pyspark2]: Images/8-pyspark2.png
[pyspark3]: Images/9-pyspark3.png
[wcout2]: Images/10-wcout2.png
[wcout3]: Images/11-wcout3.png
[s3]: Images/12-s3wc.png
[python]: Images/13-python.png
[col]: Images/14-col.png
[col2]: Images/15-col2.png
[edad]: Images/16-edad.png
[double]: Images/17-double.png
[vivo]: Images/18-vivo.png
[vivo2]: Images/19-vivo2.png
[vivo3]: Images/20-vivo3.png
[unicos]: Images/21-unico.png
[unicos2]: Images/22-unico2.png
[unicos3]: Images/23-unico3.png
[unicos4]: Images/24-unico4.png
[promedio]: Images/25-promedio.png
[suma]: Images/26-suma.png
[maximo]: Images/27-maximo.png
[minimo]: Images/28-minimo.png
[agregacion]: Images/29-agregacion.png
[udf]: Images/30-udf.png
[udf2]: Images/31-udf2.png
[pandas]: Images/32-pandas.png
[pandas2]: Images/33-pandas2.png
[pandas3]: Images/34-pandas3.png
[pandas4]: Images/35-pandas4.png
[csv]: Images/36-csv.png
[hive]: Images/37-hive.png
[hue]: Images/38-hue.png
[hive2]: Images/39-hive2.png
[hive3]: Images/40-hive3.png
[hive4]: Images/41-hive4.png
[hive5]: Images/42-hive5.png
[hive6]: Images/43-hive6.png
[hive7]: Images/44-hive7.png


