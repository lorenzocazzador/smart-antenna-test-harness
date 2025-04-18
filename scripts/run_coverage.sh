#!/bin/bash
echo "[Coverage] Running tests with coverage..."
coverage run -m pytest tests/
coverage report -m
coverage html
coverage xml  # ✅ Generates coverage.xml for Codecov
echo "[Coverage] HTML report at htmlcov/index.html, XML at coverage.xml"
