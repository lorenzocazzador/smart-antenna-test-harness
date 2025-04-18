#!/bin/bash
output=$(./hardware_sim/mock_radio_module loss)
echo "$output" | grep -q "Signal restored"
if [ $? -eq 0 ]; then
  echo "[PASS] Signal recovery test passed"
  exit 0
else
  echo "[FAIL] Signal recovery test failed"
  exit 1
fi
