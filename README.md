> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Exfil Simulator

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub Stars](https://img.shields.io/github/stars/5h4d0wn1k/exfil-simulator)
![Last Commit](https://img.shields.io/github/last-commit/5h4d0wn1k/exfil-simulator)
![GitHub Issues](https://img.shields.io/github/issues/5h4d0wn1k/exfil-simulator)

> **Data exfiltration simulator for lab environments** — a chunked HTTP POST
> exfiltration engine that teaches detection and network forensics in isolated
> labs. Educational red-team and blue-team tooling; never for real data.

## Why

Data exfiltration is one of the most common post-breach behaviors, yet detection
teams rarely get safe ways to rehearse against it. This simulator encodes dummy
data into base64 JSON and streams it in configurable chunks to a **listener you
control**, giving blue teams a reproducible exfiltration pattern to tune DLP,
egress monitoring, and anomaly detection against — without ever touching real
data, production systems, or third-party infrastructure. The project is
strictly lab-only: point it at your own listener, use dummy files, and keep the
default chunk/delay knobs to mimic slow, low-and-slow data theft.

## Features

- **Chunked HTTP POST exfiltration** — streams any file to a lab listener in
  configurable-sized chunks (`--chunk-size`, default 512 bytes).
- **Base64 + JSON encoding** — each chunk is sent as `{"i": <index>,
  "data": <base64>}` with a JSON content type.
- **Inter-chunk delay** — realistic slow exfiltration pacing (`--delay`,
  default 0.2 s).
- **Stdlib-only core** — built on `urllib`; no build step, works on Python 3.8+.
- **Lab-safe printing** — loud lab-only warning banner on every run.

## Quickstart

```bash
# No external dependencies required (Python 3.8+)
python exfil_simulator.py --help

# Simulate exfiltration to a lab listener you control
python exfil_simulator.py \
  --url http://localhost:8000/receive \
  --file dummy_data.txt

# Larger chunks with a longer delay
python exfil_simulator.py \
  --url http://localhost:8000/receive \
  --file large_file.bin \
  --chunk-size 2048 \
  --delay 1.0
```

`--url` is the only required flag together with `--file`. Receivers decode the
base64 `data` field from each JSON chunk; the classic lab listener (from the
older README) is a small Flask route at `/receive` that base64-decodes and
prints each chunk index.

## Project structure

```
exfil_simulator.py   # CLI + exfiltration engine (stdio)
requirements.txt     # optional deps note; core runs on the stdlib alone
ETHICS.md            # ethics/authorized-use policy (read first)
SCOPE.md             # defined assessment scope
```

## Documentation

- [ETHICS.md](ETHICS.md) — ethical-use policy, read first
- [SCOPE.md](SCOPE.md) — authorized-scope definition
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute
- [SECURITY.md](SECURITY.md) — vulnerability reporting
- [CHANGELOG.md](CHANGELOG.md) — version history

## Contributing

Contributions for lab tooling, better dummy-data generation, and detection
exercises are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md); all changes must
preserve the lab-only guarantees.

## License

MIT — see [LICENSE](LICENSE).