import ollama
import pandas as pd
import re
import argparse

def contar_morfemas(model:str, oracion:str, gold_std:list[int]) -> list[int]:
    '''
    Cuenta la cantidad de morfemas en una oración palabra a palabra y calcula la diferencia con el gold standar
    Devuelve la diferencia entre la cantidad de morfemas calculada y la real
    '''
    with open("prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    palabras:list[str] = re.findall(r"\w+", oracion.lower())

    result:list[int] = []

    for palabra in palabras:
	# Hacer una consulta
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content':palabra
                }
            ]
        )
        result.append(int(response['message']['content']))
    return [a - b for a, b in zip(gold_std, result)]



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Contar morfemas desde terminal")

    parser.add_argument("--model", required=True, help="Nombre del modelo de Ollama")
    parser.add_argument("--oracion", required=True, help="Oración a analizar")
    parser.add_argument("--gold", nargs="+", type=int, required=True,
                        help="Lista de valores gold standard separados por espacios")

    args = parser.parse_args()

    diferencias = contar_morfemas(args.model, args.oracion, args.gold)

    print("Diferencias:", diferencias)