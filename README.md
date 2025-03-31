# Location Metric - Backend

This project serves as the backend API for Location Metric, a system designed to track, analyze, and manage location-based data. Built with FastAPI, it provides a robust set of REST API endpoints for geospatial data handling, user authentication, and analytics.

## Project Structure

```
locationmetric-backend
├── app
│   ├── main.py               # Entry point for the FastAPI application
│   ├── api                   # API route definitions
│   ├── core                  # Core configurations and settings
│   ├── db                    # Database models and connection logic
│   └── schemas               # Pydantic models for request/response validation
├── tests                     # Test suite for the backend
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Installation

Follow these steps to set up the backend:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/locationmetric-fullstack.git
   cd locationmetric-fullstack/locationmetric-backend
   ```

2. Create and activate a virtual environment:
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables by creating a `.env` file:
   ```
   PROJECT_NAME=Location Metric
   VERSION=1.0.0
   DB_SERVER=your_db_server
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_db_name
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

## Running the Application

Start the API server with:
```
uvicorn app.main:app --reload
```

The API documentation is available at `http://127.0.0.1:8000/docs`.

## Features

- **Location Data Management**: Store and retrieve geospatial data.
- **Geospatial Analytics**: Perform location-based calculations and metrics.
- **User Authentication**: Secure access with token-based authentication.
- **Real-Time Updates**: Support for live location tracking.
- **Data Visualization**: Endpoints for visualizing geospatial data.

## Testing

Run tests using:
```
pytest
```

## Contributing

Contributions are welcome! Submit pull requests or open issues to suggest improvements or report bugs.