# Day 2: Domain Logic and Persistence Boundary

## Objective
Separate employee business logic from file storage using
dependency injection and a repository protocol.

## Architecture
- employee.py: Employee domain model
- protocols.py: Repository interface
- employee_repository.py: JSON persistence
- employee_service.py: Business rules and validation
- main.py: Application entry point
- test_employee_service.py: Automated unit tests

## Run the application
python main.py

## Run unit tests
python -m pip install pytest
python -m pytest -v

## Design decisions
The service receives a repository through dependency injection.
The Protocol defines the required repository methods.
Unit tests use an in-memory fake repository instead of JSON storage.

## Known limitations
The JSON repository is intended for a small demonstration.
Concurrent writes and database transactions are not implemented.