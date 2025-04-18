#!/bin/bash
echo "[Test] Running Python tests..."
pytest tests/test_boot_sequence.py
pytest tests/test_antenna_alignment.py

echo "[Test] Running Shell test..."
./tests/test_com_loss_recovery.sh
