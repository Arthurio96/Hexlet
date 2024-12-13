# Genetic Tests API

This project implements a RESTful API for managing genetic test data for animals.

## Features
- Add new genetic test records
- Retrieve all records or filter by species
- Calculate aggregate statistics for species

## Endpoints
1. `POST /api/tests` - Add a new test record
2. `GET /api/tests` - Retrieve all test records
3. `GET /api/statistics` - Retrieve aggregate statistics

## Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure PostgreSQL in `settings.py`
4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Run the server:
```bash
python manage.py runserver
```
6. Test the API with any HTTP client (e.g., Postman or curl).

## Examples
### Add a Test
```bash
POST /api/tests
Content-Type: application/json
{
  "animal_name": "Буренка",
  "species": "корова",
  "test_date": "2023-11-18",
  "milk_yield": 28.5,
  "health_status": "good"
}
```
### Get All Tests
```bash
GET /api/tests
```
### Get Statistics
```bash
GET /api/statistics
```