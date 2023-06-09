from PIL import Image

import requests

from io import BytesIO


def calcular_aspect_ratio(url):
    # Descargar la imagen desde la URL
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # Obtener las dimensiones de la imagen
    width, height = image.size

    # Calcular el aspect ratio
    aspect_ratio = width / height

    return aspect_ratio

# URL de la imagen
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Calcular el aspect ratio
aspect_ratio = calcular_aspect_ratio(url)
print("Aspect Ratio:", aspect_ratio)
