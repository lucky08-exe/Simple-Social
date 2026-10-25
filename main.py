import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)

# run a uvicorn API at => app (folder name) . app (filename) : app (=FastAPI())
"""
example src.file:app

go to src folder, file.py insider
object is defined as 'app'
app = FastAPI()
"""