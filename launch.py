from app import app
from app.config import BASE_URL

app.run(host=BASE_URL, port= 80, debug= True)