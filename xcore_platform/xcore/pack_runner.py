"""
Pack Runner Module
Execution engine with Brain API integration
"""
from typing import Dict, Any, Callable
from .brain_api import brain_api


class PackRunner:
    """
    Pack execution engine with Brain API enforcement
    """
    
    def __init__(self, enforce_brain_api: bool = True):
        self.enforce_brain_api = enforce_brain_api
    
    def execute_pack_function(
        self, 
        function: Callable, 
        api_key: str = None,
        *args, 
        **kwargs
    ) -> Any:
        """Execute a pack function with Brain API validation"""
        
        # Validate Brain API key if enforcement is enabled
        if self.enforce_brain_api and api_key:
            if not brain_api.validate_api_key(api_key):
                raise ValueError(f"Invalid Brain API key: {api_key}")
            
            # Track usage
            brain_api.track_usage(api_key)
        
        # Execute the function
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as e:
            raise RuntimeError(f"Function execution failed: {str(e)}")
    
    def execute_pack_workflow(
        self,
        pack_data: Dict[str, Any],
        workflow_config: Dict[str, Any],
        api_key: str = None
    ) -> Dict[str, Any]:
        """Execute a complete pack workflow"""
        
        functions = pack_data.get("functions", {})
        results = {}
        
        for step_name, step_config in workflow_config.items():
            function_name = step_config.get("function")
            function_args = step_config.get("args", {})
            
            if function_name not in functions:
                raise ValueError(f"Function {function_name} not found in pack")
            
            # Execute function
            result = self.execute_pack_function(
                functions[function_name],
                api_key,
                **function_args
            )
            
            results[step_name] = result
        
        return results
    
    def validate_pack_requirements(
        self,
        pack_data: Dict[str, Any]
    ) -> bool:
        """Validate that pack has all required components"""
        required_keys = ["config", "functions"]
        for key in required_keys:
            if key not in pack_data:
                return False
        return True
    
    def get_pack_summary(self, pack_data: Dict[str, Any]) -> Dict[str, Any]:
        """Get a summary of pack capabilities"""
        config = pack_data.get("config", {})
        functions = pack_data.get("functions", {})
        
        return {
            "pack_id": config.get("pack_id"),
            "pack_name": config.get("pack_name"),
            "version": config.get("version"),
            "description": config.get("description"),
            "available_functions": list(functions.keys()),
            "total_functions": len(functions),
            "gap_connections": config.get("gap_connections", [])
        }