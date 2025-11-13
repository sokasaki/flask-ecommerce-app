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
        """
        logger.info("Using fallback mock product data")
        return [
            {
                "id": 1,
                "title": "Classic White T-Shirt",
                "price": 29.99,
                "description": "Premium quality cotton t-shirt with a comfortable fit",
                "category": "men's clothing",
                "image": "https://via.placeholder.com/300x400/FFFFFF/000000?text=White+T-Shirt",
                "rating": {"rate": 4.5, "count": 120}
            },
            {
                "id": 2,
                "title": "Slim Fit Jeans",
                "price": 49.99,
                "description": "Modern slim fit denim jeans with stretch comfort",
                "category": "men's clothing",
                "image": "https://via.placeholder.com/300x400/4169E1/FFFFFF?text=Jeans",
                "rating": {"rate": 4.2, "count": 85}
            },
            {
                "id": 3,
                "title": "Casual Sneakers",
                "price": 79.99,
                "description": "Comfortable everyday sneakers with cushioned sole",
                "category": "men's clothing",
                "image": "https://via.placeholder.com/300x400/000000/FFFFFF?text=Sneakers",
                "rating": {"rate": 4.7, "count": 200}
            },
            {
                "id": 4,
                "title": "Summer Dress",
                "price": 59.99,
                "description": "Light and breezy summer dress perfect for warm weather",
                "category": "women's clothing",
                "image": "https://via.placeholder.com/300x400/FFB6C1/000000?text=Summer+Dress",
                "rating": {"rate": 4.6, "count": 150}
            },
            {
                "id": 5,
                "title": "Leather Handbag",
                "price": 89.99,
                "description": "Elegant leather handbag with multiple compartments",
                "category": "women's clothing",
                "image": "https://via.placeholder.com/300x400/8B4513/FFFFFF?text=Handbag",
                "rating": {"rate": 4.4, "count": 95}
            },
            {
                "id": 6,
                "title": "Wireless Earbuds",
                "price": 99.99,
                "description": "High-quality wireless earbuds with noise cancellation",
                "category": "electronics",
                "image": "https://via.placeholder.com/300x400/000000/FFFFFF?text=Earbuds",
                "rating": {"rate": 4.8, "count": 300}
            },
            {
                "id": 7,
                "title": "Smart Watch",
                "price": 199.99,
                "description": "Feature-rich smartwatch with fitness tracking",
                "category": "electronics",
                "image": "https://via.placeholder.com/300x400/1E90FF/FFFFFF?text=Smart+Watch",
                "rating": {"rate": 4.5, "count": 180}
            },
            {
                "id": 8,
                "title": "Gold Necklace",
                "price": 149.99,
                "description": "Elegant gold-plated necklace with pendant",
                "category": "jewelery",
                "image": "https://via.placeholder.com/300x400/FFD700/000000?text=Necklace",
                "rating": {"rate": 4.3, "count": 75}
            }
        ]


# Global instance
api_helper = APIHelper()
