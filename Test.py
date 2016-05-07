top = [
    {
        "name": "Vasya",
        "score": 1000
    },
    {
        "name": "Petya",
        "score": 450
    },
    {
        "name": "Kolya",
        "score": 100
    }]

print(sorted(top, key=lambda x: x["score"], reverse=True)[:9])
