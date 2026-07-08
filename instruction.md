There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json` with exactly these three fields:

- `total_requests` (integer): the total number of log lines (requests) in the file.
- `unique_ips` (integer): the number of distinct client IP addresses that made requests.
- `top_path` (string): the request path (e.g. `/index.html`) that was requested
  most often. If there is a tie, report the path that appears first in the log.

Example output:

    {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
