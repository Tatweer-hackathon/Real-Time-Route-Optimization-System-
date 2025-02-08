  # System design using Mermaid Live Editor 
![Screenshot from 2025-02-08 17-27-43](https://github.com/user-attachments/assets/a5644556-060f-4157-b46f-623c8b626593)

docs for the system : https://docs.google.com/document/d/1TYAKwZyRE6Gn2TBBFkzqz6clljTB4PdDCwDAsbZ0Ovw/edit?usp=sharing


# Dynamic Route Optimization Prototype

## Overview

This project demonstrates a dynamic route optimization system for logistics that leverages real-time traffic data to continuously update and optimize truck routes. The prototype is designed to showcase how advanced technologies can complement traditional ERP systems by providing actionable, real-time insights for route consolidation and load optimization.

## Key Components

- **Real-Time Data Ingestion with Kafka:**  
  Traffic data from IoT sensors and external APIs (e.g., TomTom/Google Traffic) is continuously published to Kafka, ensuring that live events (like congestion or accidents) are captured immediately.

- **Real-Time Database:**  
  Kafka consumers write the live traffic data to a real-time database, which stores both current conditions and historical records. This database serves as the data source for our optimization engine.

- **Route Optimization Engine with Threshold-Based Re-Optimization:**  
  The engine periodically queries the database, computes an optimal route using a heuristic algorithm (e.g., a variant of the Traveling Salesman Problem), and then compares the new route against the current one. A predefined threshold (e.g., a minimum time saving) is used to decide whether to update the route—balancing responsiveness with stability.

- **API Server:**  
  A REST API (built with FastAPI or a similar framework) exposes the latest optimized route and key metrics. This allows for easy integration with front-end applications.


## System Workflow

1. **Data Collection:**  
   - Sensors and external traffic APIs continuously stream live traffic data to Kafka.

2. **Data Storage:**  
   - Kafka consumers store this data in a real-time database.

3. **Route Optimization:**  
   - The optimization engine retrieves the latest data, computes a new route, and applies a threshold check to decide if the new route should replace the current one.

4. **API Serving:**  
   - The API server provides endpoints for retrieving the current optimized route.


## Real-World Example

### Static Routing Example

- **Scenario:**  
  At 10:00 AM, a truck is assigned a route based on historical data. The system computes a route using static conditions:
  - **Planned Route:** Truck is set to take Highway 101.
  - **Assumptions:** Traffic is expected to be light (based on historical averages).
  - **Outcome:** The truck follows the planned route. However, at 10:05 AM, an unexpected accident occurs on Highway 101, causing heavy congestion.  
  - **Result:** The truck gets stuck in traffic because the static system did not adapt to the change, resulting in delays and increased costs.

### Dynamic Routing Example

- **Scenario:**  
  The same truck is initially assigned a route at 10:00 AM. The dynamic system, however, continuously monitors traffic data.
  - **Initial Route:** Similar to the static example, the truck is set to take Highway 101.
  - **Real-Time Update:** At 10:05 AM, Kafka streams an update showing heavy congestion on Highway 101.  
  - **Threshold Check:** The optimization engine calculates an alternative route that saves 15 minutes compared to the current route. Since this improvement exceeds the threshold (e.g., 10 minutes saved), the system updates the route.
  - **Outcome:** The truck is rerouted to take an alternative path (e.g., Highway 105), avoiding the congestion and arriving on time.
  - **Result:** The dynamic system successfully adapts to real-time conditions, reducing delays and fuel costs.
## Purpose

The prototype is not intended to replace existing ERP systems but to act as a decision-support tool. It demonstrates how real-time data can be used to adapt routes dynamically, helping managers:

- **Reduce Costs:** Save on fuel, labor, and vehicle wear by optimizing routes.
- **Improve Efficiency:** Shorten delivery times and enhance overall operational performance.
- **Enhance Responsiveness:** Quickly react to dynamic conditions (e.g., traffic congestion or road incidents) with threshold-based re-optimization.

This proof-of-concept validates the potential of using technologies like Kafka, and threshold-based optimization to enhance logistics operations and lays the foundation for further development in a production environment.


resources : https://medium.com/@mervegamzenar/optimizing-delivery-routes-historical-and-real-time-data-f365d6b717be https://github.com/aurelio-labs/semantic-router/blob/main/docs/06-threshold-optimization.ipynb , https://www.meshiq.com/how-kafka-supports-fleet-management-route-optimization/ , https://kardinal.ai/whats-wrong-with-route-optimization/ , https://dev.to/renukapatil/mastering-apache-kafka-a-complete-guide-to-the-heart-of-real-time-data-streaming-3456 https://yellow.systems/blog/real-time-route-optimization-with-ai , https://www.leadspace.com/blog/10-ways-youre-losing-with-static-data/ https://www.upperinc.com/blog/data-driven-route-optimization/
