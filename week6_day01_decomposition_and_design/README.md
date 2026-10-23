# Week 6 Day 1: Codebase Decomposition and Design

## Objective
Separate employee management responsibilities into modules
with typed interfaces and testable business logic.

## Architecture
- employee.py: Employee data model
- employee_repository.py: JSON file storage
- employee_service.py: Business rules and validation
- main.py: Application entry point
- test_employee.py: Automated tests

## Run the application
python main.py

## Run tests
python -m pip install pytest
python -m pytest -v

## Design decisions
The model represents employee data.
The repository handles file operations.
The service handles business rules.
The main module starts the application.

## Known limitations
This is a small demonstration using JSON storage.
It does not include a database, authentication,
concurrent-write protection, or a user interface.