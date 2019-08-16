from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
import uvicorn

from trafiklab import get_trips

templates = Jinja2Templates(directory="templates")
app = Starlette(debug=True)


@app.route("/api/trips")
def trips(request):
    data = get_trips()

    return JSONResponse(data)


@app.route("/")
async def index(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
