import subprocess

def test_boot_sequence():
    result = subprocess.run(["./hardware_sim/mock_radio_module"], capture_output=True, text=True)
    assert "[Radio] Initialization complete." in result.stdout
