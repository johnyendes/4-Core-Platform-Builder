"""
Brain API Integration Module
Central monetization engine for X-Core Platform
"""
import uuid
from typing import Dict, Optional
from datetime import datetime


class BrainAPI:
    """
    Brain API - Central API key management and usage tracking system
    """
    
    def __init__(self):
        self.api_keys = {}
        self.usage_tracking = {}
        self.enabled = True
    
    def generate_api_key(self, user_id: str) -> str:
        """Generate a new API key for a user"""
        key = f"XCORE-{uuid.uuid4()}"
        self.api_keys[key] = {
            "user_id": user_id,
            "created_at": datetime.now().isoformat(),
            "active": True
        }
        self.usage_tracking[key] = 0
        return key
    
    def validate_api_key(self, api_key: str) -> bool:
        """Validate an API key"""
        if not self.enabled:
            return True  # Disabled for testing
        return api_key in self.api_keys and self.api_keys[api_key]["active"]
    
    def track_usage(self, api_key: str) -> None:
        """Track API usage for billing"""
        if api_key in self.usage_tracking:
            self.usage_tracking[api_key] += 1
    
    def get_usage(self, api_key: str) -> int:
        """Get usage count for an API key"""
        return self.usage_tracking.get(api_key, 0)
    
    def deactivate_key(self, api_key: str) -> bool:
        """Deactivate an API key"""
        if api_key in self.api_keys:
            self.api_keys[api_key]["active"] = False
            return True
        return False
    
    def enable(self):
        """Enable Brain API enforcement"""
        self.enabled = True
    
    def disable(self):
        """Disable Brain API enforcement (for testing)"""
        self.enabled = False


# Global Brain API instance
brain_api = BrainAPI()