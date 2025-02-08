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

- **Online Viewer / Dashboard:**  
  An interactive front end (built with React using react-leaflet, or alternatively with Streamlit for rapid prototyping) displays the optimized route on a map with clear directional arrows and step-by-step markers. It periodically polls the API to show real-time updates.

## System Workflow

1. **Data Collection:**  
   - Sensors and external traffic APIs continuously stream live traffic data to Kafka.

2. **Data Storage:**  
   - Kafka consumers store this data in a real-time database.

3. **Route Optimization:**  
   - The optimization engine retrieves the latest data, computes a new route, and applies a threshold check to decide if the new route should replace the current one.

4. **API Serving:**  
   - The API server provides endpoints for retrieving the current optimized route.

5. **Visualization:**  
   - The online viewer fetches the route data from the API and displays it on an interactive map, updating in real time.

## Deployment & Usage

- **Deployment:**  
  - **Kafka:** Can be hosted on Confluent Cloud or a similar service.
  - **Database:** Use a cloud-hosted solution (e.g., MongoDB Atlas, InfluxDB).
  - **API Server:** Deploy on platforms such as Heroku, AWS Elastic Beanstalk, or via Docker/Kubernetes.
  - **Online Viewer:** Deploy the React app on Vercel or Netlify (or Streamlit on Streamlit Cloud).

- **Usage:**  
  - Follow the installation instructions to set up the environment.
  - Run the backend components and ensure the real-time data pipeline is active.
  - Launch the online viewer to see the dynamic, real-time route optimization in action.

## Purpose

The prototype is not intended to replace existing ERP systems but to act as a decision-support tool. It demonstrates how real-time data can be used to adapt routes dynamically, helping managers:

- **Reduce Costs:** Save on fuel, labor, and vehicle wear by optimizing routes.
- **Improve Efficiency:** Shorten delivery times and enhance overall operational performance.
- **Enhance Responsiveness:** Quickly react to dynamic conditions (e.g., traffic congestion or road incidents) with threshold-based re-optimization.

This proof-of-concept validates the potential of using technologies like Kafka, real-time databases, and threshold-based optimization to enhance logistics operations and lays the foundation for further development in a production environment.


resources : https://medium.com/@mervegamzenar/optimizing-delivery-routes-historical-and-real-time-data-f365d6b717be https://github.com/aurelio-labs/semantic-router/blob/main/docs/06-threshold-optimization.ipynb , https://www.meshiq.com/how-kafka-supports-fleet-management-route-optimization/ , https://kardinal.ai/whats-wrong-with-route-optimization/ , https://dev.to/renukapatil/mastering-apache-kafka-a-complete-guide-to-the-heart-of-real-time-data-streaming-3456 https://yellow.systems/blog/real-time-route-optimization-with-ai , https://www.leadspace.com/blog/10-ways-youre-losing-with-static-data/ https://www.upperinc.com/blog/data-driven-route-optimization/
