from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

# مدل برای دریافت ورودی از body
class NumberInput(BaseModel):
    number: int

# تابع اصلی که اعداد زوج را پیدا کرده و با '*' جدا می‌کند
def exercise1(number: int):
    number_str = str(number)
    even_digits = [digit for digit in number_str if int(digit) % 2 == 0]
    if even_digits:
        return '*'.join(even_digits)
    else:
        return "هیچ رقم زوجی ندارد"

# مسیر GET با استفاده از path parameter و query parameter
@app.get("/exercise1/{number}")
def path_parameter(number: int):
    """
    این مسیر از طریق path و query پارامترها کار می‌کند
    """
    result = exercise1(number)
    return {
        "Type": "path parameter",
        "Result": result
    }


@app.get("/exercise1/")
def query_parameter(number: int):
    """
    این مسیر از طریق path و query پارامترها کار می‌کند
    """
    result = exercise1(number)
    return {
        "Type": "query parameter",
        "Result": result
    }

# مسیر POST برای دریافت داده از body
@app.post("/even-digits/")
def create_even_digits(data: NumberInput):
    """
    این مسیر از طریق body عدد را دریافت می‌کند
    """
    result = exercise1(data.number)
    return {
        "input_number": data.number,
        "even_digits": result
    }

