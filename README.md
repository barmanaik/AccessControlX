# AccessControlX – Broken Access Control Lab

## Overview
A deliberately vulnerable web application demonstrating Broken Access Control vulnerabilities.

## Vulnerabilities Demonstrated
- IDOR (Insecure Direct Object Reference)
- Forced browsing
- Missing authorization checks

## Installation
pip install -r requirements.txt

## Run the Application
python app/app.py

## Example Exploit
python exploits/idor_exploit.py

## Security Impact
Unauthorized data access through predictable object identifiers.

## Learning Outcome
Understanding how access control flaws occur and how they can be exploited.




Future Improvements

- Implement role-based access control
- Introduce JWT authentication
- Add more Broken Access Control scenarios
- Dockerize the lab environment