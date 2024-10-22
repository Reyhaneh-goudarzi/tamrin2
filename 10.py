from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# مدل برای دریافت داده از طریق Body
class FactorialInput(BaseModel):
    number: int

# تابع برای محاسبه فاکتوریل
def factorial(x: int) -> int:
    if x == 1 or x == 0:  # پایه (base case) برای فاکتوریل
        return 1
    else:  # حالت بازگشتی (recursive case)
        return x * factorial(x - 1)

# API برای محاسبه فاکتوریل
@app.post("/factorial")
async def compute_factorial(
    input_data: FactorialInput = Body(...),
):
    """
    محاسبه فاکتوریل یک عدد ورودی.
    """
    number = input_data.number

    # بررسی اینکه آیا عدد غیر منفی است
    if number < 0:
        return {"error": "Please enter a non-negative integer."}

    result = factorial(number)

    # برگرداندن نتیجه
    return {
        "number": number,
        "factorial": result
    }

# اجرای سرور با Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
