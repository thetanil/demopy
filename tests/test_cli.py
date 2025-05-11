from demopy import cli
import subprocess

def test_main():
    result = subprocess.run(["demopy"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello from Demopy!"