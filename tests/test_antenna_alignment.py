import subprocess

def test_alignment():
    result = subprocess.run(["./hardware_sim/mock_radio_module"], capture_output=True, text=True)
    assert "[Radio] Alignment successful." in result.stdout
