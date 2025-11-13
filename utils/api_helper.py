"""
API Helper module for FakeStore API
Centralized API calls with error handling and caching
"""
import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import logging

logger = logging.getLogger(__name__)

class APIHelper:
    def __init__(self, base_url: str = "https://fakestoreapi.com", timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self._cache = {}
        self._cache_duration = timedelta(minutes=5)
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if cached data is still valid"""
        if key not in self._cache:
            return False
        
        cached_time = self._cache[key].get('timestamp')
        if not cached_time:
            return False
        
        return datetime.now() - cached_time < self._cache_duration
    
    def _get_from_cache(self, key: str) -> Optional[List[Dict]]:
        """Get data from cache if valid"""
        if self._is_cache_valid(key):
            logger.info(f"Cache hit for key: {key}")
            return self._cache[key]['data']
        return None
    
    def _save_to_cache(self, key: str, data: List[Dict]) -> None:
        """Save data to cache"""
        self._cache[key] = {
            'data': data,
            'timestamp': datetime.now()
        }
        logger.info(f"Cached data for key: {key}")
    
    def get_products(self, use_cache: bool = True) -> List[Dict]:
        """
        Fetch all products from FakeStore API
        
        Args:
            use_cache: Whether to use cached data if available
            
        Returns:
            List of product dictionaries, or empty list on error
        """
        cache_key = 'all_products'
        
        # Try cache first
        if use_cache:
            cached_data = self._get_from_cache(cache_key)
            if cached_data is not None:
                return cached_data
        
        try:
            url = f"{self.base_url}/products"
            logger.info(f"Fetching products from {url}")
            
            # Add headers to mimic a browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Referer': 'https://fakestoreapi.com/'
            }
            
            response = requests.get(url, timeout=self.timeout, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            # Save to cache
            if use_cache:
                self._save_to_cache(cache_key, data)
            
            logger.info(f"Successfully fetched {len(data)} products")
            return data
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                logger.warning(f"API returned 403 Forbidden. Using fallback mock data.")
                # Return fallback mock data
                return self._get_fallback_products()
            logger.error(f"HTTP error fetching products: {e}")
        except requests.exceptions.Timeout:
            logger.error(f"Timeout while fetching products from {self.base_url}")
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error while fetching products from {self.base_url}")
        except requests.exceptions.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching products: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
        
        # Return fallback data if all else fails
        return self._get_fallback_products()
    
    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """
        Fetch a single product by ID
        
        Args:
            product_id: The product ID to fetch
            
        Returns:
            Product dictionary or None on error
        """
        try:
            url = f"{self.base_url}/products/{product_id}"
            logger.info(f"Fetching product {product_id} from {url}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Successfully fetched product {product_id}")
            return data
            
        except Exception as e:
            logger.error(f"Error fetching product {product_id}: {e}")
            return None
    
    def clear_cache(self) -> None:
        """Clear all cached data"""
        self._cache.clear()
        logger.info("Cache cleared")
    
    def _get_fallback_products(self) -> List[Dict]:
        """
        Return fallback mock data when API is unavailable
        Uses images from static/final_project folder
        """
        logger.info("Using fallback mock product data")
        return [
            # Men's Clothing
            {
                "id": 1,
                "title": "Men's Hoody - Black",
                "price": 45.99,
                "description": "T-shirt featuring long sleeves, pocket with embroidery and crew neckline. 45% Cotton 50% Polyester 5% Spandex",
                "category": "men's clothing",
                "image": "/static/final_project/Men/hoody/Black/main.jpg",
                "rating": {"rate": 4.5, "count": 120}
            },
            {
                "id": 2,
                "title": "Men's Hoody - White",
                "price": 45.99,
                "description": "T-shirt featuring long sleeves, pocket with embroidery and crew neckline. 45% Cotton 50% Polyester 5% Spandex",
                "category": "men's clothing",
                "image": "/static/final_project/Men/hoody/white/hoody(main).jpg",
                "rating": {"rate": 4.5, "count": 98}
            },
            {
                "id": 3,
                "title": "Men's Hoody - Brown",
                "price": 45.99,
                "description": "T-shirt featuring long sleeves, pocket with embroidery and crew neckline. 45% Cotton 50% Polyester 5% Spandex",
                "category": "men's clothing",
                "image": "/static/final_project/Men/hoody/Brown/hoody(main).jpg",
                "rating": {"rate": 4.6, "count": 87}
            },
            {
                "id": 4,
                "title": "Men's Basketball T-Shirt - Navy Blue",
                "price": 29.99,
                "description": "Regular t-shirt featuring short sleeves, with text embroidery at the front and crew neckline. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Basketbal_T-Shirt_Wit_Print/Navy Blue/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 145}
            },
            {
                "id": 5,
                "title": "Men's Basketball T-Shirt - Red",
                "price": 29.99,
                "description": "Regular t-shirt featuring short sleeves, with text embroidery at the front and crew neckline. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Basketbal_T-Shirt_Wit_Print/Red/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 132}
            },
            {
                "id": 6,
                "title": "Men's T-Shirt - Black",
                "price": 24.99,
                "description": "Regular t-shirt featuring short sleeves, with text embroidery at the front and crew neckline. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/T-Shirt/Black/T-Shirt (main).jpg",
                "rating": {"rate": 4.4, "count": 210}
            },
            {
                "id": 7,
                "title": "Men's T-Shirt - White",
                "price": 24.99,
                "description": "Regular t-shirt featuring short sleeves, with text embroidery at the front and crew neckline. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/T-Shirt/White/T-Shirt (main).jpg",
                "rating": {"rate": 4.4, "count": 198}
            },
            {
                "id": 8,
                "title": "Men's T-Shirt - Dark Gray",
                "price": 24.99,
                "description": "Regular t-shirt featuring short sleeves, with text embroidery at the front and crew neckline. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/T-Shirt/Dark_Gray/T-Shirt (main).jpg",
                "rating": {"rate": 4.4, "count": 175}
            },
            {
                "id": 9,
                "title": "Men's T-Shirt With Print - White",
                "price": 27.99,
                "description": "Stylish t-shirt with modern print design. Perfect for casual wear. 100% Cotton",
                "category": "men's clothing",
                "image": "/static/final_project/Men/T-Shirt_With_Print/White/T-Shirt main.jpg",
                "rating": {"rate": 4.2, "count": 163}
            },
            {
                "id": 10,
                "title": "Men's T-Shirt With Print - Light Green",
                "price": 27.99,
                "description": "Stylish t-shirt with modern print design. Perfect for casual wear. 100% Cotton",
                "category": "men's clothing",
                "image": "/static/final_project/Men/T-Shirt_With_Print/light Green/T-Shirt main.jpg",
                "rating": {"rate": 4.2, "count": 141}
            },
            {
                "id": 11,
                "title": "Men's Tank Top With Print - Navy Blue",
                "price": 22.99,
                "description": "Comfortable tank top with stylish print. Perfect for summer and workouts. 100% Cotton",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Tank_Top_With_ Print/Navy Blue/Tank-Top main.jpg",
                "rating": {"rate": 4.3, "count": 128}
            },
            {
                "id": 12,
                "title": "Men's Tank Top With Print - Black",
                "price": 22.99,
                "description": "Comfortable tank top with stylish print. Perfect for summer and workouts. 100% Cotton",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Tank_Top_With_ Print/Black/Tank-Top main.jpg",
                "rating": {"rate": 4.3, "count": 115}
            },
            {
                "id": 13,
                "title": "Men's Tank Top With Print - Beige",
                "price": 22.99,
                "description": "Comfortable tank top with stylish print. Perfect for summer and workouts. 100% Cotton",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Tank_Top_With_ Print/Beige/Tank-Top main.jpg",
                "rating": {"rate": 4.3, "count": 102}
            },
            {
                "id": 14,
                "title": "Men's Shorts With Print - Black",
                "price": 34.99,
                "description": "Comfortable athletic shorts with modern print. Perfect for sports and casual wear. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Shorts_With_Print/Black/Short main.jpg",
                "rating": {"rate": 4.4, "count": 156}
            },
            {
                "id": 15,
                "title": "Men's Shorts With Print - Beige",
                "price": 34.99,
                "description": "Comfortable athletic shorts with modern print. Perfect for sports and casual wear. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Shorts_With_Print/Beige/Short main.jpg",
                "rating": {"rate": 4.4, "count": 143}
            },
            {
                "id": 16,
                "title": "Men's Shorts With Print - Navy Blue",
                "price": 34.99,
                "description": "Comfortable athletic shorts with modern print. Perfect for sports and casual wear. 100% Polyester",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Shorts_With_Print/navy Blue/Short main.jpg",
                "rating": {"rate": 4.4, "count": 138}
            },
            {
                "id": 17,
                "title": "Men's Straight Fit Shorts - Beige",
                "price": 39.99,
                "description": "Classic straight fit shorts for everyday comfort. Premium quality fabric. 98% Cotton 2% Spandex",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Straight_Fit Shorts/Beige/short main.jpg",
                "rating": {"rate": 4.5, "count": 167}
            },
            {
                "id": 18,
                "title": "Men's Straight Fit Shorts - Dark Green",
                "price": 39.99,
                "description": "Classic straight fit shorts for everyday comfort. Premium quality fabric. 98% Cotton 2% Spandex",
                "category": "men's clothing",
                "image": "/static/final_project/Men/Straight_Fit Shorts/Dark Green/short main.jpg",
                "rating": {"rate": 4.5, "count": 152}
            },
            
            # Women's Clothing
            {
                "id": 19,
                "title": "Women's Cami Mini Dress - Light Blue",
                "price": 49.99,
                "description": "Mini dress featuring cami sleeves, an adjustable shoulder straps and open-back. 100% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cami Mini Dress/Light Blue/Dress main.jpg",
                "rating": {"rate": 4.6, "count": 189}
            },
            {
                "id": 20,
                "title": "Women's Cami Mini Dress - White",
                "price": 49.99,
                "description": "Mini dress featuring cami sleeves, an adjustable shoulder straps and open-back. 100% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cami Mini Dress/white/Dress main.jpg",
                "rating": {"rate": 4.6, "count": 201}
            },
            {
                "id": 21,
                "title": "Women's Midi Dress - Black",
                "price": 59.99,
                "description": "Elegant midi dress perfect for any occasion. Comfortable fit with premium fabric. 95% Polyester 5% Spandex",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Midi Dress/Black/Dress main.jpg",
                "rating": {"rate": 4.7, "count": 223}
            },
            {
                "id": 22,
                "title": "Women's Midi Dress - Pink",
                "price": 59.99,
                "description": "Elegant midi dress perfect for any occasion. Comfortable fit with premium fabric. 95% Polyester 5% Spandex",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Midi Dress/Pink/Dress main.jpg",
                "rating": {"rate": 4.7, "count": 198}
            },
            {
                "id": 23,
                "title": "Women's Crop Sweat Jacket - Black",
                "price": 54.99,
                "description": "Trendy cropped jacket perfect for layering. Comfortable and stylish. 80% Cotton 20% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Crop Sweat Jacket/Black/Jacket main.jpg",
                "rating": {"rate": 4.5, "count": 167}
            },
            {
                "id": 24,
                "title": "Women's Crop Sweat Jacket - White",
                "price": 54.99,
                "description": "Trendy cropped jacket perfect for layering. Comfortable and stylish. 80% Cotton 20% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Crop Sweat Jacket/White/Jacket main.jpg",
                "rating": {"rate": 4.5, "count": 154}
            },
            {
                "id": 25,
                "title": "Women's Cropped T-shirt With Print - Blue Wash",
                "price": 27.99,
                "description": "Stylish cropped t-shirt with modern print. Perfect for casual summer wear. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cropped T-shirt With Print/Blue Wash/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 142}
            },
            {
                "id": 26,
                "title": "Women's Cropped T-shirt With Print - Olive Green",
                "price": 27.99,
                "description": "Stylish cropped t-shirt with modern print. Perfect for casual summer wear. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cropped T-shirt With Print/Olive Green/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 135}
            },
            {
                "id": 27,
                "title": "Women's Cropped T-Shirt With Print - Navy",
                "price": 27.99,
                "description": "Trendy cropped t-shirt with eye-catching print design. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cropped T-Shirt With Print1/navy/T-Shirt main.jpg",
                "rating": {"rate": 4.4, "count": 128}
            },
            {
                "id": 28,
                "title": "Women's Cropped T-Shirt With Print - Red",
                "price": 27.99,
                "description": "Trendy cropped t-shirt with eye-catching print design. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Cropped T-Shirt With Print1/Red/T-Shirt main.jpg",
                "rating": {"rate": 4.4, "count": 119}
            },
            {
                "id": 29,
                "title": "Women's Off Shoulder T-Shirt - Black",
                "price": 32.99,
                "description": "Chic off-shoulder t-shirt for a stylish casual look. Soft and comfortable. 95% Cotton 5% Spandex",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Off Shoulder T-Shirt/Black/T-Shirt main.jpg",
                "rating": {"rate": 4.5, "count": 176}
            },
            {
                "id": 30,
                "title": "Women's Off Shoulder T-Shirt - White",
                "price": 32.99,
                "description": "Chic off-shoulder t-shirt for a stylish casual look. Soft and comfortable. 95% Cotton 5% Spandex",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Off Shoulder T-Shirt/White/T-Shirt main.jpg",
                "rating": {"rate": 4.5, "count": 192}
            },
            {
                "id": 31,
                "title": "Women's T-Shirt With Print - Light Pink",
                "price": 26.99,
                "description": "Comfortable t-shirt with beautiful print. Perfect for everyday wear. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/T-Shirt With Print/Light Pink/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 158}
            },
            {
                "id": 32,
                "title": "Women's T-Shirt With Print - White",
                "price": 26.99,
                "description": "Comfortable t-shirt with beautiful print. Perfect for everyday wear. 100% Cotton",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/T-Shirt With Print/White/T-Shirt main.jpg",
                "rating": {"rate": 4.3, "count": 171}
            },
            {
                "id": 33,
                "title": "Women's Wide Leg Sweatpants - Black",
                "price": 44.99,
                "description": "Comfortable wide leg sweatpants with relaxed fit. Perfect for lounging or casual outings. 80% Cotton 20% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Wide Leg Sweatpants/Black/Trouser (main).jpg",
                "rating": {"rate": 4.6, "count": 204}
            },
            {
                "id": 34,
                "title": "Women's Wide Leg Sweatpants - White",
                "price": 44.99,
                "description": "Comfortable wide leg sweatpants with relaxed fit. Perfect for lounging or casual outings. 80% Cotton 20% Polyester",
                "category": "women's clothing",
                "image": "/static/final_project/Lady/Wide Leg Sweatpants/White/Trouser (main).jpg",
                "rating": {"rate": 4.6, "count": 187}
            }
        ]


# Global instance
api_helper = APIHelper()
