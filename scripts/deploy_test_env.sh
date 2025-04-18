#!/bin/bash
echo "[Deploy] Setting up environment..."
g++ hardware_sim/mock_radio_module.cpp -o hardware_sim/mock_radio_module
chmod +x tests/test_com_loss_recovery.sh
echo "[Deploy] Build complete."
