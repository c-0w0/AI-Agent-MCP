from typing import Dict, Any, Optional
import httpx
import asyncio
from datetime import datetime

async def get_weather_forecast(location: str) -> Optional[Dict[str, Any]]:
    """
    Get weather 7 days forecast for any location in Malaysia using Data.gov.my API.
    
    Args:
        location: Case-insensitive location name (e.g., "bayan lepas", "kuala lumpur")
                
    Returns:
        Dict with weather data or None if request fails
    """
    try:
        async with httpx.AsyncClient(follow_redirects=True) as client:
            resp = await client.get(f"https://api.data.gov.my/weather/forecast?contains={location}@location__location_name")
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        print(f"Weather API error: {str(e)}")
        return None

# async def main(): # for debugging purpose
#     forecast = await get_weather_forecast('Butterworth')
#     print(forecast)

# if __name__ == "__main__":
#     asyncio.run(main())