import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    return json.loads(REPORT_PATH.read_text())


def test_report_exists():
    """instruction.md: 'Save your findings so they can be reviewed' —
    a report file must exist at /app/report.json."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"


def test_total_requests():
    """instruction.md: 'how many requests there were' —
    total_requests must equal the number of log lines."""
    report = _load_report()
    assert report.get("total_requests") == 6, (
        f"expected total_requests=6, got {report.get('total_requests')!r}"
    )


def test_unique_ips():
    """instruction.md: 'the clients involved' —
    unique_ips must equal the number of distinct client IPs in the log."""
    report = _load_report()
    assert report.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {report.get('unique_ips')!r}"
    )


def test_top_path():
    """instruction.md: 'which pages were popular' —
    top_path must be the most frequently requested path."""
    report = _load_report()
    assert report.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {report.get('top_path')!r}"
    )
