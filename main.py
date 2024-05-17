from fastapi import FastAPI
from prisma import Prisma
from prisma.models import User


app = FastAPI()
    
@app.get('/')
def index():
    return {"hello":"world"}

@app.get('/createuser')
async def main():
    db = Prisma(auto_register=True)
    await db.connect()
    user = await db.user.create(
        data={
            'name': 'Robert',
            'email': 'robert@craigie.dev'
        },
    )
    await db.disconnect()
    
@app.get('/getusers')
async def get():
    db = Prisma(auto_register=True)
    await db.connect()
    u = await db.user.find_many()
    await db.disconnect()
    return {'users':u}