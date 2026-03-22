# FastAPI Verification Service

This project is a FastAPI-based service to verify and validate financial transaction data in real-time.

## Features
- Real-time data validation
- Checks amount, currency, and account number
- Returns success or error response

## Technologies Used
- FastAPI
- Python
- Uvicorn

## How to Run

pip install fastapi uvicorn  
uvicorn main:app --reload  

## API Endpoint

POST /verify

## Sample Input

{
  "transaction_id": 1,
  "amount": 500,
  "currency": "INR",
  "account_number": "1234567890"
}

## Output

Valid → Success  
Invalid → Error  

## Conclusion

This system reduces data inaccuracies and ensures compliance in financial systems.
