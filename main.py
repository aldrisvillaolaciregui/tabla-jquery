from fastapi import FastAPI,Request,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,Response
from fastapi.templating import Jinja2Templates



from database import database as conexion


app=FastAPI()


templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.on_event("startup")
def startup():
    if conexion.is_closed():
        conexion.connect()
        print("conexion a la base de datos exitosa")
        
        
@app.get("/")
async def index(request:Request):
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM articulos_empresa")
    articulos=cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request":request, "articulos":articulos})
        
