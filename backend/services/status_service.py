def get_status_data():
    return {
        "status": "ok",
        "message": "Backend работает",
        "service": "backend-service",
        "items_count": 3
    }
def get_items_data():
    return [
        {
            "id": 1,
            "name": "Компьютер",
            "image": "img/pc.jpg"
        },
        {
            "id": 2,
            "name": "Ноутбук",
            "image": "img/nt.jpg"
        },
        {
            "id": 3,
            "name": "Приставка",
            "image": "img/ps.jpg"
        }
    ]