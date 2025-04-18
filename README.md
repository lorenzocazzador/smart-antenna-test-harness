# Smart Antenna Test Harness
[![codecov](https://codecov.io/gh/lorenzocazzador/smart-antenna-test-harness/graph/badge.svg?token=YQTT0FTYTN)](https://codecov.io/gh/lorenzocazzador/smart-antenna-test-harness)

A modular embedded test harness for simulating and validating satellite antenna software. Built for Linux-based environments using Python, C++, Bash, and pyserial. Includes CI/CD, UART testing, and a Flask dashboard.

## Features

- C++ mock hardware simulating antenna behavior
- Python and Bash test scripts
- UART testing with pyserial (real or virtual ports)
- 100% code coverage with coverage.py
- Jenkins and GitHub Actions integration
- Optional Flask dashboard for test results

## Getting Started

```bash
./scripts/deploy_test_env.sh
./scripts/run_all_tests.sh > output.log
./scripts/run_coverage.sh
```

## UART Testing

Test communication with real or virtual UART devices:

```bash
pytest tests/test_uart_integration.py
```

## Flask Dashboard

```bash
cd dashboard
python app.py
```
Visit `http://localhost:5000` to view test results.

## Project Structure

```
hardware_sim/         # C++ mock antenna
tests/                # Python and shell tests
scripts/              # Build and test runners
dashboard/            # Flask test viewer
jenkins/              # Jenkins CI config
```