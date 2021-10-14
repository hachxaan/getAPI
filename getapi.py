import re
import sys
import json
import requests # Linea 1
from typing import Any, Dict, AnyStr
from requests.exceptions import HTTPError


patternURL = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"


def validaURL(url: AnyStr) -> bool:
    """ 
        Valida URL, metodo regex
    """

    return re.compile(patternURL).search(url) != None # Linea 1


def getJsonFromApi(urlAPI: AnyStr) -> Any:
    """ 
        Obtiene JSON Object a partir de la url de una API
    """

    if validaURL(urlAPI):
        return requestToApi(urlAPI)
    else:
        print(f"La url \"{urlAPI}\" no es válida.")
        return None


def requestToApi(urlAPI: AnyStr) -> Dict:
    """" 
        Requests API
    """
    jsonResponse = None
    try:
        response = requests.get(urlAPI) # Linea 2
        response.raise_for_status()
        jsonResponse = response.json() # Linea 3

    except HTTPError as err:
        print(f'HTTP error: {err}')
    except Exception as err:
        print(f'Otro error: {err}')

    return jsonResponse # Linea 4


if __name__ == '__main__':

    url = None
    try:
        url = sys.argv[1]
    except:
        pass

    if url:
        jsonVariable = getJsonFromApi( str(sys.argv[1].rstrip()) )
    else:
        print("Ingresa API url")
        print(" > ", end="")
        jsonVariable = None
        while not jsonVariable:
            jsonVariable = getJsonFromApi( str(input().rstrip()) )
            if not jsonVariable:
                print("Ingresa una url válida")
                print(" > ", end="")
    
    print(json.dumps(jsonVariable, indent=4))
