from fastapi import FastAPI

app = FastAPI()

# تعریف متغیر گلوبال
s = "I live in Iran."

# تابع برای به‌روزرسانی متغیر
def update_message():
    global s
    s = "I live in Khorram Abad."
    return s

# API برای برگرداندن پیغام
@app.get("/message")
async def get_message():
    """
    برگرداندن پیغام و به‌روزرسانی آن.
    """
    # به روزرسانی پیغام و دریافت آن
    updated_message = update_message()
    return {"message": updated_message}

# اجرای سرور با Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.post("/message")
async def get_message():
    """
    برگرداندن پیغام و به‌روزرسانی آن.
    """
    # به روزرسانی پیغام و دریافت آن
    updated_message = update_message()
    return {"message": updated_message}
