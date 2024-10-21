# FELIZ NAVIDAD DESDE PYTHON
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d/%m/%y")
if date_time == "24/12/2024":
    print("Es nochebuena")

elif date_time == "25/12/2024":
    print("Feliz navidad")

