import sys
import os
sys.path.append('packs/web_builder')
sys.path.append('gap_packs/web_builder_gaps')
sys.path.append('deployment/web_builder_deploy')

from functions import (
    generate_site_core,
    generate_site_pages,
    generate_site_layout,
    generate_site_navigation,
    generate_site_seo
)
from bridge import connect
from deploy import deploy

# Test the complete Web Builder workflow
def test_web_builder_workflow():
    print("=== Testing Web Builder A2 Workflow ===")
    
    # Step 1: Generate site core
    core = generate_site_core(
        site_name="TechHub Pro",
        purpose="showcase technology products and services",
        audience="tech enthusiasts and businesses"
    )
    print(f"✅ Core generated: {core['site_name']}")
    
    # Step 2: Generate site pages
    pages = generate_site_pages(
        site_name="TechHub Pro",
        pages=["home", "about", "services", "portfolio", "contact"]
    )
    print(f"✅ Pages generated: {len(pages['pages'])} pages")
    
    # Step 3: Generate site layout
    layout = generate_site_layout(
        site_name="TechHub Pro",
        layout_type="modern responsive"
    )
    print(f"✅ Layout generated: {layout['layout_type']}")
    
    # Step 4: Generate site navigation
    page_names = ["home", "about", "services", "portfolio", "contact"]
    navigation = generate_site_navigation(page_names)
    print(f"✅ Navigation generated: {len(navigation['navigation'])} items")
    
    # Step 5: Generate site SEO
    seo = generate_site_seo(
        site_name="TechHub Pro",
        keywords=["technology", "software", "web development", "tech solutions"]
    )
    print(f"✅ SEO generated: {len(seo['keywords'])} keywords")
    
    # Step 6: Connect through GAP bridge
    blueprint_wrapper = connect(core, pages, layout, navigation, seo)
    print(f"✅ GAP bridge connected: {blueprint_wrapper['status']}")
    
    # Step 7: Deploy
    deploy(blueprint_wrapper)
    print("✅ Deployment completed")
    
    print("\n=== Web Builder A2 Workflow Test Complete ===")
    print("✅ All components working correctly!")
    
    return blueprint_wrapper

if __name__ == "__main__":
    result = test_web_builder_workflow()