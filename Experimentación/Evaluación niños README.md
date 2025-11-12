# Pruebas niños

Con el modelo ya seleccionado nos dispusimos a realizar lo mismo que hicimos en adultos pero ahora enfocándonos en audios y transcripciónes de niños y probando exclusivamente con la versión Turbo de Whisper.

Cada audio de los niños fue representado de 3 maneras diferentes:

- El audio completo sin recortes. Llamado por nosotros Tarea 1
- Recortes aislados de cada audio. Tarea 3
- Recortes concatenados reconstruyendo el audio completo. Tarea 2

La que mejor resultó fue la última de las mencionadas, la Tarea 2. Los audios completos incluían participaciones de la maestra que intentaba orientar y ayudar a los chicos.
Los fragmentos aislados carecían de contexto, algo que Whisper usa para mejorar sus transcripciones. Las reconstrucciones a partir de los recortes solucionaban estas cuestiones: No se contaba con las voces de las maestras pero si con el contexto necesario para obtener buenos resultados.

Probamos con un total de 56 audios obteniendo, en el mejor caso, un WER promedio de … y un CER promedio de… Numeros que, teniendo en cuenta la gran dificultad de la tarea, eran alentadores.

Cabe destacar que, con el objetivo de hacer un análisis más profundo, decidimos comparar entre hipotesis y referencias bajo 2 estados. Normalizados (sin mayusculas ni puntuaciones) y Crudos (tal cual lo expulsa el modelo).

En la carpeta audios_niños encontramos tres carpetas, cada una correspondiente a una de las tareas evaluadas. Allí se ubican las grabaciones utilizadas durante estas evaluaciones. En la carpeta docs_niños encontramos tres archivos csv que contiene el nombre de los audios de cada tarea respectivamente y ayuda en el procesamiento de los audios.

Todo esto fue llevado a una planilla en excel para mejorar la visualización de los resultados.

En la carpeta audios_niños encontrarán todos aquellas grabaciónes que utilizamos para llegar a nuestras conclusiones. 

Al ejecutar el archivo evaluacion_niños.ipynb obtendrán las transcripciones junto a sus alineaciones con la refencia y métricas correspondientes. Toda esta información se guardará en el archivo salida_prueba.xlsx 
