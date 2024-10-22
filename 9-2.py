from fastapi import FastAPI

app = FastAPI()

# تعریف متغیر گلوبال
s = ""

# تابع برای به روزرسانی متغیر گلوبال
def update_message():
    global s
    s = "I live in Khorram Abad"
    return s

# API برای برگرداندن پیغام
@app.get("/message")
async def get_message():
    """
    برگرداندن پیغام "I live in Khorram Abad".
    """
    msg = update_message()  # به روزرسانی و دریافت پیغام
    return {"message": msg}

# اجرای سرور با Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.post("/message")
async def get_message():
    """
    برگرداندن پیغام "I live in Khorram Abad".
    """
    msg = update_message()  # به روزرسانی و دریافت پیغام
    return {"message": msg}
