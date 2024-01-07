from fastapi import FastAPI, status, HTTPException
from models import DataPY

from pinterest.organic.pins import Pin

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Pinterest API"
    pinterest_access_token: str = 'your token'
    board_id: str = 'your board id'

settings = Settings()
app = FastAPI()


@app.post('/', status_code=status.HTTP_201_CREATED)
def Publish(data: DataPY):
    if data is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='data is missing')
    try:
        pin_create = Pin.create(
            board_id=BOARD_ID,
            title="Testing Upload",
            description="Testing",
            media_source={
                "source_type": 'image',
                "content_type": "image/jpeg",
                "data": data.caption,
                'url': data.media_url
                }
            )
    except Exception as e:
        return {'message':'pin creation failed',
                'error':str(e)}

    return {'message':'data recieved'}
    

    