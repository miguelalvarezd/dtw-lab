import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from dtw_lab.lab1 import (
    read_csv_from_google_drive ,
    visualize_data,
    calculate_statistic,
    clean_data,
)

# Initialize FastAPI application instance
# This creates our main application object that will handle all routing and middleware
app = FastAPI()

# Server deployment configuration function. We specify on what port we serve, and what IPs we listen to.
def run_server(port: int = 80, reload: bool = False, host:
    str = "127.0.0.1"):
    uvicorn.run("dtw_lab.lab2:app", port=port, reload=reload, host=host)

#Define an entry point to our application.
@app.get("/")
def main_route():
    return {"message": "Hello world"}

@app.get("/statistic/{measure}/{column}")
def get_statistic(measure: str, column: str):
    """Read the CSV data, clean the data, and calculate the statistic."""
    file_id = '1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo'
    df  = read_csv_from_google_drive(file_id)
    df = clean_data(df)

    message = f'The {measure} for the {column} column is {calculate_statistic(measure,df[column])}'

    return {"message": message}

@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):
    """
    Read the CSV data, clean the data, and visualize it.
    This should create 3 files in the graphs folder.
    Based on the graph_type input, return the corresponding image
    HINT: Use FileResponse
    """
    file_id = '1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo'
    df  = read_csv_from_google_drive(file_id)
    df = clean_data(df)
    visualize_data(df)
    route = Path("graphs") / f"{graph_type}.png"
    
    return FileResponse(route)

@app.get("/version")
def get_visualization_version():
    """Using the toml library, get the version field from the "pyproject.toml" file and return it."""
    file = Path(__file__).parent.parent.parent / "pyproject.toml"
    with open(file, "r") as f:
        data = toml.load(f)
        version = data["tool"]["poetry"]["version"]
        
        return {"version": version}
    