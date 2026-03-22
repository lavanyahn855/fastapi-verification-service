from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)

# Data model
class Transaction(BaseModel):
    transaction_id: int
    amount: float
    currency: str
    account_number: str

# Home route
@app.get("/")
def home():
    return {"message": "Verification Service Running"}

# Verification endpoint
@app.post("/verify")
def verify_transaction(txn: Transaction):
    
    # Validation rules
    if txn.amount <= 0:
        logging.error("Invalid amount")
        return {"status": "error", "message": "Amount must be greater than 0"}
    
    if len(txn.account_number) < 10:
        logging.error("Invalid account number")
        return {"status": "error", "message": "Invalid account number"}
    
    if txn.currency not in ["INR", "USD", "EUR"]:
        logging.error("Invalid currency")
        return {"status": "error", "message": "Unsupported currency"}

    logging.info("Transaction is valid")
    return {"status": "success", "message": "Transaction is valid"}
