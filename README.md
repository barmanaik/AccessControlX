# AccessControlX – Broken Access Control Lab

## Overview

AccessControlX is a deliberately vulnerable web application designed to demonstrate common **Broken Access Control** vulnerabilities in modern web applications.

The project provides a controlled environment where security researchers, students, and developers can understand how improper authorization logic can allow attackers to access resources beyond their intended permissions.

This lab focuses on vulnerabilities listed in the **OWASP Top 10**, particularly Broken Access Control.

---

## Objectives

The primary goal of this project is to demonstrate:

* How access control vulnerabilities occur
* How attackers exploit authorization flaws
* How security testers identify these issues during penetration testing
* How application logic flaws can lead to privilege escalation

---

## Vulnerabilities Demonstrated

This lab intentionally includes several Broken Access Control scenarios.

### Insecure Direct Object Reference (IDOR)

Users can access other users' orders by modifying object identifiers.

Example endpoint:

```
GET /api/orders/<order_id>
```

Changing the order ID allows unauthorized data access.

---

### Horizontal Privilege Escalation

Users can retrieve profile information of other users.

Example endpoint:

```
GET /api/profile/<user_id>
```

---

### Vertical Privilege Escalation

Administrative functionality is exposed without proper authorization checks.

Example endpoint:

```
GET /admin/all_orders
```

---

### User Enumeration

Predictable user identifiers allow attackers to enumerate user accounts.

---

### JWT Role Manipulation

JWT tokens can be modified to escalate privileges by altering the role value in the payload.

---

## Project Structure

```
AccessControlX
│
├── vulnerable_app
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── routes.py
│
├── exploits
│   ├── idor_exploit.py
│   ├── jwt_privilege_escalation.py
│   ├── user_enumeration.py
│
├── pentest_guide
│   └── testing_steps.md
│
├── docker
│   └── Dockerfile
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/barmanaik/AccessControlX.git
```

Navigate into the project directory:

```
cd AccessControlX
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the vulnerable application:

```
python vulnerable_app/app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

---

## Authentication

Use the following test accounts:

| Username | Password | Role  |
| -------- | -------- | ----- |
| alice    | 123      | user  |
| bob      | 123      | user  |
| admin    | admin    | admin |

Login endpoint:

```
POST /login
```

Example request:

```
{
 "username": "alice",
 "password": "123"
}
```

The response will contain a JWT access token.

---

## Testing the Vulnerabilities

Detailed testing instructions are provided in:

```
pentest_guide/testing_steps.md
```

The guide explains how to reproduce each vulnerability step-by-step.

---

## Exploit Scripts

The repository includes scripts that automate vulnerability exploitation.

Examples:

```
python exploits/idor_exploit.py
python exploits/user_enumeration.py
python exploits/jwt_privilege_escalation.py
```

These scripts demonstrate how attackers may exploit access control flaws.

---

## Security Impact

Broken Access Control vulnerabilities may allow attackers to:

* Access sensitive data belonging to other users
* Perform unauthorized administrative actions
* Enumerate user accounts
* Escalate privileges within the system

These issues are among the most critical security flaws identified in modern web applications.

---

## Tools for Testing

The vulnerabilities can be tested using:

* Burp Suite
* Postman
* curl

Intercepting and modifying requests allows testers to observe unauthorized access behavior.

---

## Future Improvements

Planned improvements include:

* Secure version of the application
* Role-based access control implementation
* Additional access control bypass scenarios
* Automated vulnerability detection scripts
* Expanded security training documentation

---

## Disclaimer

This project is intentionally vulnerable and should be used **only for educational purposes** in controlled environments.

Do not deploy this application in production systems.

---

## Author
    Barma Naik
