# Procesamiento de Datos con Apache Spark y Kafka

## Descripción
Fase3- Este proyecto presenta una solución de análisis de datos utilizando Apache Spark para procesamiento en batch y Apache Kafka junto con Spark Streaming para procesamiento en tiempo real.

## Tecnologías utilizadas
- Apache Spark
- Apache Kafka
- Python

## Procesamiento en Batch
Se realiza la carga, limpieza, transformación y análisis de datos utilizando DataFrames en Apache Spark, permitiendo identificar patrones y generar estadísticas.

## Procesamiento en Tiempo Real
Se implementa un productor en Kafka que genera datos simulados de sensores y un consumidor con Spark Streaming que procesa estos datos en tiempo real, calculando promedios de temperatura y humedad.

## Archivos del proyecto
- kafka_producer.py → Generador de datos en Kafka
- spark_streaming_consumer.py → Procesamiento en tiempo real
- batch_processing.py → Procesamiento en batch
