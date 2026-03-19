"""
X-Core Platform Startup Module
"""
import os
from typing import Optional


def initialize_platform():
    """Initialize the X-Core platform"""
    print("🚀 Initializing X-Core Platform...")
    print(f"Version: 1.0.0")
    print(f"Python: {os.sys.version}")
    
    # Load environment variables
    brain_api_enabled = os.getenv('BRAIN_API_ENABLED', 'true').lower() == 'true'
    debug_mode = os.getenv('DEBUG', 'false').lower() == 'true'
    
    print(f"\nConfiguration:")
    print(f"  Brain API: {'Enabled' if brain_api_enabled else 'Disabled'}")
    print(f"  Debug Mode: {'Enabled' if debug_mode else 'Disabled'}")
    
    # Initialize components
    from .brain_api import brain_api
    from .license_manager import license_manager
    from .pack_loader import PackLoader
    from .xcore_registry import xcore_registry
    
    if not brain_api_enabled:
        brain_api.disable()
    
    loader = PackLoader()
    packs = loader.load_all_packs()
    
    # Register packs
    for pack_name, pack_data in packs.items():
        xcore_registry.register_pack(pack_name, pack_data)
    
    print(f"\n✅ Platform initialized successfully")
    print(f"📦 Loaded {len(packs)} packs")
    
    return {
        "brain_api": brain_api,
        "license_manager": license_manager,
        "registry": xcore_registry,
        "packs": packs
    }


def run_platform():
    """Run the X-Core platform"""
    try:
        platform = initialize_platform()
        
        # Start CLI or web interface
        import sys
        if len(sys.argv) > 1:
            from .cli import main
            main()
        else:
            print("\nX-Core Platform is ready!")
            print("Use 'python -m xcore.cli list-packs' to see available packs")
    
    except Exception as e:
        print(f"❌ Platform initialization failed: {e}")
        raise


if __name__ == "__main__":
    run_platform()