import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21011056"))
    API_HASH = os.environ.get("API_HASH", "696033b1a9c35f0dc027f8ecfbaa9645")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6856342807:AAEpBJK8zR5tw3yPCYRGj8QghJ4KD5wWeEI")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1841888978")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Bikash")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001970031336"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Anjaliforward_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
