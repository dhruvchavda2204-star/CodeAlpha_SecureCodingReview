# CodeAlpha_SecureCodingReview
Secure Coding Review - SQL Injection Fix (Python)
# Secure Coding Review – CodeAlpha Internship

## Objective
To identify and fix SQL Injection vulnerability in a Python login system.

## Vulnerability Found
SQL Injection due to direct query construction.

Payload Used:
' OR '1'='1

## Risk Impact
- Authentication Bypass
- Unauthorized Access
- Data Exposure

## Fix Applied
- Parameterized Queries
- Input Validation

## Tools Used
- Python
- SQLite

