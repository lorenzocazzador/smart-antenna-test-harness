import subprocess

def test_alignment_success():
    result = subprocess.run(["./hardware_sim/mock_radio_module", "align"], capture_output=True, text=True)
    assert "Alignment successful" in result.stdout

def test_alignment_error():
    result = subprocess.run(["./hardware_sim/mock_radio_module", "align", "error"], capture_output=True, text=True)
    assert "Alignment failed" in result.stderr
