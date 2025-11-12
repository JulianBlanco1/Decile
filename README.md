# Decile

Decile es un proyecto donde buscamos transcribir eficaz y eficientemente los relatos de niños entre 5 a 12 años para el análisis de sus producciónes orales.

## Objetivo

Con Decile queremos facilitarle a las maestras la tarea de evaluar e identificar quienes son aquellos alumnos con mayores dificultades en el habla y, gracias a esta detección temprana, poder darles la atención necesaria. 

La detección hasta este momento es realizada por las maestras escuchando a sus alumnos y, gracias a su preparación, determinando quienes presentan más falencias. Con Decile buscamos automatizar esta tarea para que cueste menos esfuerzo y tiempo por parte de las docentes y las acciones correspondientes puedan ser tomadas a tiempo.

## Procedimientos

A los niños se les mostrará unos videos pidiendoles luego, que expliquen lo que sucedía en el mismo. Esto es lo que se analizará con una serie de métricas. Este trabajo se basó en la transcripción de los audios y en la confección de métricas que rigen la evaluación de las producciónes orales.

## Estructura

    tu-proyecto/
    ├─ evaluate.ipynb
    ├─ data.csv
    ├─ metricas.ipynb
    ├─ audios/
    ├─ Experimentación/
    │  └─ audios_adultos/              
    │  └─ audios_niños/
    │       └─ Audios completos/     
    │       └─ Audios fragmentados/     
    │       └─ Audios reconstruidos/ 
    │  └─ docs_adultos 
    │       └─ data_adultos.csv    
    │  └─ docs_niños/
    │       └─ completos.csv      
    │       └─ fragmentos.csv     
    │       └─ reconstruidos.csv           
    ├─ requirements.txt           
    └─ README.md      

`evaluate.ipynb`: Procesamiento de audios y cálculo de métricas.

`data.csv`: Documento auxiliar para realizar la evaluación de las producciónes orales.

`metricas.ipynb`: Definición e implementación del conjunto completo de metricas utilizadas.

`audios`: Carpeta que almacena el nombre de los archivos de audios a evaluar.

En la carpeta experimentación encontramos:

`eleccion_modelo.ipynb`: Experimentación para encontrar el modelo adecuado.

`evaluacion_niños.ipynb`: Evaluación del modelo elegido en un conjunto de audios de niños.

Las carpetas cuyo nombres comienzan en Audios y docs contienen archivos csv y audios respectivamente que hemos usado durante todos los momentos de experimentación. 

Los archivos `eleccion_modelo.ipynb` y `evaluacion_niños.ipynb` cuentan con un README donde damos detalles de nuestro trabajo

En estos explicamos con más detalle en que momento los utilizamos respectivamente

## Ejecución rápida

Primero que nada, los audios que se desean evaluar deben encontrarse almacenados en la carpeta llamada “audios”. Al ejecutar enteramente el código se obtendrá un excel que almacenará la transcripción realizada y las métricas correspondientes

### 1) Prerrequisitos
- **Python** 3.10–3.12 recomendado.

- **FFmpeg** instalado en el sistema (requerido por Whisper).

#### Instalar FFmpeg
- **macOS (Homebrew)**  
  ```bash
  brew install ffmpeg
  ```

- **Ubuntu/Debian**  
  ```bash
  sudo apt-get update && sudo apt-get install -y ffmpeg
  ```

- **Windows (Chocolatey)**  
  ```bash
  choco install ffmpeg
  ```

Una vez que tengamos todo esto, para ejecutar el código deben instalar todas las dependencias necesarias.

```bash
pip install -r requirements.txt
```

Luego ejecutar el notebook evaluate.ipynb


        
