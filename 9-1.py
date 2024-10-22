from fastapi import FastAPI

app = FastAPI()

# تابع داخلی برای برگرداندن پیغام
def get_message():
    return "I live in Khorramabad"

# API برای برگرداندن پیغام
@app.get("/message")
async def message():
    """
    برگرداندن پیغام "I live in Khorramabad".
    """
    msg = get_message()
    return {"message": msg}

# API برای برگرداندن پیغام
@app.post("/message")
async def message():
    """
    برگرداندن پیغام "I live in Khorramabad".
    """
    msg = get_message()
    return {"message": msg}

