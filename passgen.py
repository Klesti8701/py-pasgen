from fastapi import FastAPI, Query
import random
import string

#create the endpoit
app = FastAPI()

@app.get("/password")
async def generate_password(
    length: int = 8,
    special_characters: bool = 0,
    uppercase: bool = 0,
    numbers: bool = 0
):
    characters = string.ascii_lowercase
    if special_characters:
        characters += string.punctuation
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
        
    password = ''.join(random.choices(characters, k=length))
    return {"password": password}
