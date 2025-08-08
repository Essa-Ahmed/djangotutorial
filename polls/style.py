def get_theme(request):
    return request.session.get("theme", "light")

def toggle_theme(request):
    current = get_theme(request)
    request.session["theme"] = "dark" if current == "light" else "light"

