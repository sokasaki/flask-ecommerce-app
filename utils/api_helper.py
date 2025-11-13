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
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            # Save to cache
            if use_cache:
                self._save_to_cache(cache_key, data)
            
            logger.info(f"Successfully fetched {len(data)} products")
            return data
            
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
        
        return []
    
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


# Global instance
api_helper = APIHelper()
