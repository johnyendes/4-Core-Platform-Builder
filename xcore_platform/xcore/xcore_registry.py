"""
X-Core Registry Module
Manages packs, gaps, and deployment registrations
"""
from typing import Dict, List, Any


class XCoreRegistry:
    """
    Central registry for all X-Core components
    """
    
    def __init__(self):
        self.packs = {}
        self.gap_packs = {}
        self.deployment_systems = {}
    
    def register_pack(self, pack_name: str, pack_data: Dict[str, Any]) -> None:
        """Register a pack"""
        self.packs[pack_name] = pack_data
    
    def register_gap_pack(self, gap_name: str, gap_data: Dict[str, Any]) -> None:
        """Register a GAP pack"""
        self.gap_packs[gap_name] = gap_data
    
    def register_deployment(
        self,
        deployment_name: str,
        deployment_data: Dict[str, Any]
    ) -> None:
        """Register a deployment system"""
        self.deployment_systems[deployment_name] = deployment_data
    
    def get_pack(self, pack_name: str) -> Dict[str, Any]:
        """Get a registered pack"""
        return self.packs.get(pack_name)
    
    def get_gap_pack(self, gap_name: str) -> Dict[str, Any]:
        """Get a registered GAP pack"""
        return self.gap_packs.get(gap_name)
    
    def get_deployment(self, deployment_name: str) -> Dict[str, Any]:
        """Get a registered deployment system"""
        return self.deployment_systems.get(deployment_name)
    
    def list_packs(self) -> List[str]:
        """List all registered packs"""
        return list(self.packs.keys())
    
    def list_gap_packs(self) -> List[str]:
        """List all registered GAP packs"""
        return list(self.gap_packs.keys())
    
    def list_deployments(self) -> List[str]:
        """List all registered deployment systems"""
        return list(self.deployment_systems.keys())
    
    def get_registry_summary(self) -> Dict[str, Any]:
        """Get a summary of registry contents"""
        return {
            "total_packs": len(self.packs),
            "total_gap_packs": len(self.gap_packs),
            "total_deployments": len(self.deployment_systems),
            "packs": self.list_packs(),
            "gap_packs": self.list_gap_packs(),
            "deployments": self.list_deployments()
        }


# Global registry instance
xcore_registry = XCoreRegistry()