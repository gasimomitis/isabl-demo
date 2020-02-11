# Isabl Demo App <img src="./assets/isabl-logo.png" height=28px>

## Presentation

[Slides](https://docs.google.com/presentation/d/1TzVM3pfmu3fYjmZ54iEjKzJWjdlmhfspFL52AevVCuw/edit?usp=sharing)

## Installation

```bash
mkvirtualenv -p python3 isabl
pip install git+https://github.com/isabl-io/cli@v1.0.0#egg=isabl_cli
```

Configure and authenticate

```bash
export ISABL_API_URL=https://isabl.mskcc.org/api/v1
export ISABL_CLIENT_ID=4
isabl login
```

## Usage

Access all commands:

```bash
isabl --help
```

## Documentation

https://docs.isabl.io
