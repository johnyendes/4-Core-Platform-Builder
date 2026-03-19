"""
Pack Loader Module
Dynamic loading of X-Core packs from filesystem
"""
import os
import json
import importlib.util
from typing import Dict, List, Any


class PackLoader:
    """
    Dynamic pack loading system
    """
    
    def __init__(self, packs_directory: str = "packs"):
        self.packs_directory = packs_directory
        self.loaded_packs = {}
    
    def load_pack(self, pack_name: str) -> Dict[str, Any]:
        """Load a pack from the packs directory"""
        pack_path = os.path.join(self.packs_directory, pack_name)
        
        if not os.path.exists(pack_path):
            raise ValueError(f"Pack {pack_name} not found at {pack_path}")
        
        # Load pack configuration
        pack_json_path = os.path.join(pack_path, "pack.json")
        with open(pack_json_path, 'r') as f:
            pack_config = json.load(f)
        
        # Load pack functions
        functions_path = os.path.join(pack_path, "functions.py")
        if os.path.exists(functions_path):
            spec = importlib.util.spec_from_file_location(
                f"{pack_name}.functions", 
                functions_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            pack_functions = {
                name: getattr(module, name) 
                for name in pack_config.get("core_functions", [])
                if hasattr(module, name)
            }
        else:
            pack_functions = {}
        
        pack_data = {
            "config": pack_config,
            "functions": pack_functions,
            "metadata": self._load_metadata(pack_path),
            "path": pack_path
        }
        
        self.loaded_packs[pack_name] = pack_data
        return pack_data
    
    def load_all_packs(self) -> Dict[str, Any]:
        """Load all available packs"""
        packs = {}
        if not os.path.exists(self.packs_directory):
            return packs
        
        for pack_name in os.listdir(self.packs_directory):
            pack_path = os.path.join(self.packs_directory, pack_name)
            if os.path.isdir(pack_path):
                try:
                    packs[pack_name] = self.load_pack(pack_name)
                except Exception as e:
                    print(f"Warning: Failed to load pack {pack_name}: {e}")
        
        return packs
    
    def _load_metadata(self, pack_path: str) -> Dict[str, Any]:
        """Load pack metadata"""
        meta_path = os.path.join(pack_path, "meta.txt")
        if os.path.exists(meta_path):
            with open(meta_path, 'r') as f:
                return {"description": f.read()}
        return {}
    
    def get_pack_info(self, pack_name: str) -> Dict[str, Any]:
        """Get information about a loaded pack"""
        return self.loaded_packs.get(pack_name, {})