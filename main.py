from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn

from trafiklab import get_trips

app = Starlette(debug=True)


@app.route("/api/trips")
def trips(request):
    data = get_trips()

    return JSONResponse(data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
