from typing import Dict, Any, List

def generate_site_core(site_name: str, purpose: str, audience: str) -> Dict[str, Any]:
    return {
        "site_name": site_name,
        "purpose": purpose,
        "audience": audience,
        "summary": f"{site_name} is a website designed to {purpose} for {audience}."
    }


def generate_site_pages(site_name: str, pages: List[str]) -> Dict[str, Any]:
    page_list = []
    for page in pages:
        page_list.append({
            "page_name": page.title(),
            "description": f"The {page.title()} page for {site_name}."
        })
    return {"site_name": site_name, "pages": page_list}


def generate_site_layout(site_name: str, layout_type: str) -> Dict[str, Any]:
    return {
        "site_name": site_name,
        "layout_type": layout_type,
        "description": f"{site_name} uses a {layout_type} layout structure."
    }


def generate_site_navigation(pages: List[str]) -> Dict[str, Any]:
    nav_items = []
    for page in pages:
        nav_items.append({
            "label": page.title(),
            "url": f"/{page.lower()}"
        })
    return {"navigation": nav_items}


def generate_site_seo(site_name: str, keywords: List[str]) -> Dict[str, Any]:
    return {
        "site_name": site_name,
        "meta_title": f"{site_name} - Home",
        "meta_description": f"Welcome to {site_name}. Your destination for quality content and services.",
        "keywords": keywords
    }