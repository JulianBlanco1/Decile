# Uso de LLMs para contar la cantiad de morfemas en una oración

El archivo morfemas_llm.py utiliza modelos de lenguaje obtenidos de la librería `ollama` para realizar un cálculo de morfemas siguiendo una serie de normas previamente especificadas.

El programa recibe: 
- El nombre de modelo a probar. Puede ser cualquiera de este [listado](https://ollama.com/library)
- La oración la cual se desea contar sus morfemas
- Una lista con la cantidad real de cada palabra de la oración a evaluar

Devolverá:
- Una lista con las diferencias entre los morfemas contados y los reales palabra a palabra. Si el valor es 0, quiere decir que el modelo los contó correctamente. Si, en cambio, el valor es negativo, quiere decir el modelo dió una cantidad mayor de morfemas. En caso de ser positivo, habría contado menos de los que debería.

## Quick start

Para poder utilizar el programa. Hay que seguir estos pasos

### Prompt

Escribir las instrucciones que se desea que el modelo siga en el archivo `prompt.txt` ; es muy importante que se aclare que el formato de salida debe ser pura y exclusivamente un valor, un numero, la cantidad de morfemas. No debe incluir ninguna palabra, esto romperá el código. Pueden utilizar algo del estilo:


    REGLA ABSOLUTA DE SALIDA:
    Tu respuesta debe ser exclusivamente un número entero que representa la cantidad total de morfemas del enunciado.
    No podés escribir nada más.
    No podés escribir palabras, explicaciones, segmentaciones, aclaraciones ni comentarios.
    Si intentás escribir cualquier cosa distinta de un número, la salida será inválida.
    Si tenés dudas, igual debés responder únicamente un número.
    No existe ninguna excepción.


Y utilizarlo al principio y al final de las instrucciones

### Descargar los modelos

Se debe instalar la librería ollama con el siguiente comando:

```bash
pip install ollama
```

Luego debemos descargarnos Llama desde esta [página](https://ollama.com/download)

Seguido a esto, debemos bajar el modelo que deseamos probar con el comando:

```bash
ollama pull *nombre del modelo*
```

Si ejecutamos ollama list obtendremos una lista de los modelos descaragdos en nuestra computadora y por ende, utilizables.

Una vez tengamos todo esto, solo debemos ejecutar este comando utilizando los parametros correctos:

```bash
python morfemas_llm.py \
  --model *nombre del modelo* \
  --oracion *oración a evaluar(debe estar entre comillas)* \
  --gold *lista de morfemas palabra a palabra corecto*
```

Por ejemplo:

```bash
python morfemas_llm.py \
  --model mistral \
  --oracion "La casita se ordenó rápidamente" \
  --gold 1 2 1 2 3
```

### Salida esperada

La salida debería ser algo del estilo: Diferencias: [0, 0, 0, 0, 0]