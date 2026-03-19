"""
Command Line Interface Module
"""
from typing import Dict, Any
from .pack_loader import PackLoader
from .pack_runner import PackRunner
from .xcore_registry import xcore_registry


class XCoreCLI:
    """
    Command line interface for X-Core Platform
    """
    
    def __init__(self):
        self.loader = PackLoader()
        self.runner = PackRunner()
    
    def list_packs(self):
        """List all available packs"""
        packs = self.loader.load_all_packs()
        print("\n=== Available Packs ===")
        for pack_name, pack_data in packs.items():
            config = pack_data.get("config", {})
            print(f"\n{pack_name}")
            print(f"  ID: {config.get('pack_id')}")
            print(f"  Description: {config.get('description')}")
            print(f"  Functions: {', '.join(config.get('core_functions', []))}")
    
    def pack_info(self, pack_name: str):
        """Show detailed information about a pack"""
        try:
            pack_data = self.loader.load_pack(pack_name)
            summary = self.runner.get_pack_summary(pack_data)
            
            print(f"\n=== Pack: {summary['pack_name']} ===")
            print(f"ID: {summary['pack_id']}")
            print(f"Version: {summary['version']}")
            print(f"Description: {summary['description']}")
            print(f"\nAvailable Functions:")
            for func in summary['available_functions']:
                print(f"  - {func}")
        except Exception as e:
            print(f"Error: {e}")
    
    def system_status(self):
        """Show system status"""
        summary = xcore_registry.get_registry_summary()
        
        print("\n=== X-Core Platform Status ===")
        print(f"Total Packs: {summary['total_packs']}")
        print(f"Total GAP Packs: {summary['total_gap_packs']}")
        print(f"Total Deployments: {summary['total_deployments']}")
        
        if summary['packs']:
            print("\nRegistered Packs:")
            for pack in summary['packs']:
                print(f"  - {pack}")


def main():
    """Main CLI entry point"""
    import sys
    
    cli = XCoreCLI()
    
    if len(sys.argv) < 2:
        print("X-Core Platform CLI")
        print("Usage: python -m xcore.cli <command>")
        print("\nCommands:")
        print("  list-packs    List all available packs")
        print("  pack-info <pack_name>  Show pack details")
        print("  status        Show system status")
        return
    
    command = sys.argv[1]
    
    if command == "list-packs":
        cli.list_packs()
    elif command == "pack-info":
        if len(sys.argv) < 3:
            print("Error: Pack name required")
            return
        cli.pack_info(sys.argv[2])
    elif command == "status":
        cli.system_status()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()