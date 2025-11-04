#!/bin/bash
# Script to run tests with coverage report

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "Running tests with coverage..."
pytest --cov=app --cov-report=html --cov-report=term-missing tests/

echo ""
echo "Coverage report generated!"
echo "Open htmlcov/index.html to view detailed coverage report"
