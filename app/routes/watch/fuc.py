from datetime import datetime
from app.load_file.get_txt import upload_s3
dic = {}
input_data = ''
i = 0
async def insert_s3(user_id: str, vod_id: int):
    global input_data
    global i
    if user_id not in dic:
        dic[user_id] = {
            'user_id': user_id,
            'vod_id': vod_id,
            'start_time': datetime.now()
        }
    else:
        rtm = datetime.now() - dic[user_id]['start_time']
        rtm_minutes = round(rtm.total_seconds() / 60)  # Convert to minutes and round
        start_time = dic[user_id]['start_time'].strftime("%Y%m%d%H%M%S")
        
        input_data = input_data + f'{user_id},{vod_id},{start_time},{rtm_minutes}\n'
        i += 1
        if i > 100:
            await upload_s3(input_data)
            
        return input_data

# Example usage
# import asyncio
# asyncio.run(insert_s3("user123", 1))
