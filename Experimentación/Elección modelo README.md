# Encontrar el mejor modelo

Al comenzar nos encontramos bajo la pregunta de que modelo utilizar para transcribir. Es aqui donde empezamos con nuestras pruebas. Contabamos con una serie de audios de adultos y de niños. 

Decidimos utilizar en primer medida el modelo Whisper, de OpenAI. Este modelo cuenta con diferentes versiones dependiendo de su tamaño:

- Tiny
- Small
- Base
- Medium
- Large
- Turbo

Primero que nada, probamos cada uno de ellos con todos los audios de adultos con los que contabamos. 

En la carpeta Audios_adultos encontramos las ocho grabaciones utilizadas durante estas evaluaciones. En la carpeta docs_adultos encontramos un csv que contiene el nombre de los audios y ayuda en el procesamiento de los audios. 

Para evaluar que tan buena había sido su performance, utilizamos 2 métricas conocidas, WER (word error rate) y CER (character error rate). 
 
# Explicar

La librería jiwer nos facilitó el acceso a las métricas. La función que las ejecuta recibe 2 parámetros:

- La transcripción (hipótesis): Lo que expulsó el modelo
- La referencia: Lo que realmente dijo la persona.

Estas métricas tienen el problema de interpretar la misma letra en mayuscula y en minuscula como diferentes. Esto se extiende también a las palabras. Las comas, tildes y signos de puntuación tambien afectan los valores de las métricas. 

Como nuestras referencias se encontraban enteramente en minúscula, sin tildes ni puntuaciones, decidimos, antes de utilizar las métricas, aplicar una serie de transformaciones para que las hipotesis y las referencias se encuentren en el mismo formato.

Las transformaciónes fueron:

- Eliminación de tildes
- Pasaje de mayusculas a minúsculas
- Eliminación de signos de puntuación
- Eliminación de espacios en blanco al comienzo y al final
- Eliminación de doble espaciado
- Conversión de los textos a listas de palabras o caracters. Esto depende de que métrica estemos evaluado (WER o CER).


También utilizamos la librería jiwer para realizar estas transformaciones. La eliminación de tildes debimos implementarlas por nuestra cuenta ya que no se encontraban disponibles

Jiwer tambien nos proporcionó una forma de visualizar cada uno de los errores de las transcripciones de la siguiente manera:

![image.png](https://i.imgur.com/DjiPfIs.png)

Cada asterisco es un error cometido. Esto facilitó mucho la visualización y análisis de la performance del modelo.

La hipotesis, la referencia, las métricas y estas visualizaciónes fueron almacenadas en un diccionario. Este diccionario guardaba todos estos datos para cada audio y para cada modelo, por lo que cada grabación contaba con diferentes resultados expuestos por las diferentes versiones de Whisper.

Con todo esto en nuestras manos, pudimos recorrer el diccionario obteniendo el WER y el CER promedio para cada modelo. 

![cer_6.png](https://i.imgur.com/H282h3G.png)

![alt text](https://i.imgur.com/2AomDHa.png)

Como podemos ver los resultados fueron prometedores. Con esto decidimos quedarnos con el modelo Whisper Turbo, una combinación entre calidad en las transcripciones y buena performance en cuestiones de tiempo.
