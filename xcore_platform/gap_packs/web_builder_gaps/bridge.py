def connect(core, pages, layout, navigation, seo):
    site_name = core.get("site_name", "Unnamed Site")
    blueprint = {
        "site_name": site_name,
        "core": core,
        "pages": pages,
        "layout": layout,
        "navigation": navigation,
        "seo": seo
    }
    return {"website_blueprint": blueprint, "status": "ready_for_deployment"}