Title: Broken Access Control (IDOR)

Description
The application exposes user orders through the endpoint:

GET /api/orders/<order_id>

The server does not verify whether the authenticated user owns the requested order.

Impact
An attacker can enumerate order IDs and retrieve sensitive data belonging to other users.

Proof of Concept
1. Access the endpoint:
   /api/orders/1

2. Modify the identifier:
   /api/orders/2

3. The server returns data for another user.

Severity
High

Remediation
Implement proper server-side authorization checks to ensure that users can only access resources they own.