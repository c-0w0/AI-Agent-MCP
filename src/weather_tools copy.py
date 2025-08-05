from typing import Dict, Any, Optional
import httpx
import asyncio
from datetime import datetime

async def get_malaysia_weather_forecast(
    location: str,
    date: str,  # Format: YYYY-MM-DD
    timeout: float = 15.0
) -> Optional[Dict[str, Any]]:
    """
    Get weather forecast for any location in Malaysia using Data.gov.my API.
    
    Args:
        location: Case-insensitive location name (e.g., "bayan lepas", "kuala lumpur")
        date: Forecast date in YYYY-MM-DD format
        timeout: Request timeout in seconds
        
    Returns:
        Dict with weather data or None if request fails
    """
    base_url = "https://api.data.gov.my/weather"
    params = { 
        "location": location.lower().strip(),
        "date": date,
        "category": "forecast"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                base_url,
                params=params,
                headers={
                    "User-Agent": "MalaysiaWeatherForecast/1.0",
                    "Accept": "application/json"
                },
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Weather API error: {str(e)}")
        return None

async def format_weather_forecast(
    location: str,
    date: str
) -> str:
    """
    Get formatted weather forecast string.
    
    Args:
        location: Case-insensitive location name
        date: Forecast date in YYYY-MM-DD format
        
    Returns:
        Formatted string with weather data or error message
    """
    data = await get_malaysia_weather_forecast(location, date)
    
    if not data or not data.get("data"):
        return f"No forecast available for {location.title()} on {date}"
    
    forecast = data["data"][0]
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    
    return (
        f"{location.title()} Weather Forecast ({date_obj.strftime('%d %b %Y')}):\n"
        f"Condition: {forecast.get('weather_condition', 'N/A')}\n"
        f"Temperature: {forecast.get('temperature_min', 'N/A')}°C - {forecast.get('temperature_max', 'N/A')}°C\n"
        f"Humidity: {forecast.get('humidity_min', 'N/A')}% - {forecast.get('humidity_max', 'N/A')}%\n"
        f"Wind: {forecast.get('wind_speed', 'N/A')} km/h {forecast.get('wind_direction', '')}\n"
        f"Rain Probability: {forecast.get('rain_probability', 'N/A')}%\n"
        f"\nSource: Data.gov.my Weather API"
    )

async def main():
    forecast = await format_weather_forecast('Penang', '2025-08-06')
    print(forecast)

if __name__ == '__main__':
    asyncio.run(main())  # Properly run the async function