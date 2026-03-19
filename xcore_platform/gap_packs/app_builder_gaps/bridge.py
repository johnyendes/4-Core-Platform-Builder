def connect(core, screens, navigation, database, api):
    app_name = core.get("app_name", "Unnamed App")
    blueprint = {
        "app_name": app_name,
        "core": core,
        "screens": screens,
        "navigation": navigation,
        "database": database,
        "api": api
    }
    return {"app_blueprint": blueprint, "status": "ready_for_deployment"}