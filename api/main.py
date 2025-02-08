from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka_producer import produce_traffic_data
from route_optimizer import calculate_optimal_route
from datetime import datetime
app = FastAPI()

class RouteRequest(BaseModel):
    origin: int      # ID of the origin point
    destinations: list[int]  # IDs of destination points

@app.post("/optimize")
async def optimize_route(request: RouteRequest):
    try:
        # Calculate route using real-time data
        optimal_route = calculate_optimal_route(request.origin, request.destinations)
        return {
            "optimal_route": optimal_route,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))