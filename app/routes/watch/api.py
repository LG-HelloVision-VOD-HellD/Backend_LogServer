from fastapi import APIRouter, HTTPException
from .fuc import insert_s3

router = APIRouter(prefix = '/watch')

@router.post('/{user_id}')
async def insert_watch_s3(user_id:int, vod_id:int):
    result = await insert_s3(str(user_id),vod_id)
    return result