# Postmortem Task - Image Compression Service Outage

![Technical Issue Resolution](./postmortem.webp)

## Issue Summary
- Duration: The outage lasted for 2 hours, from 10:00 AM to 12:00 PM  on August 15, 2024.
- Impact: The image compression service within our Django web application was down, leading to a 100% failure rate for all image upload and compression requests. Users were unable to compress images, resulting in a loss of functionality for the core service. Approximately 85% of active users were affected during this period.
- Root Cause: The outage was caused by a misconfigured PostgreSQL database connection pool, which led to a resource exhaustion scenario where no new connections could be established, causing the web application to become unresponsive.

## Timeline
- 10:00 AM: Issue detected by monitoring alerts indicating a spike in HTTP 500 errors for the image compression service.
- 10:05 AM: On-call engineer begins investigating the issue, initially suspecting a problem with the image processing library.
- 10:20 AM: Logs show repeated database connection timeouts; focus shifts to database connectivity.
- 10:30 AM: Assumption made that the database server might be overloaded; system resources are checked, and CPU/memory usage appears normal.
- 10:45 AM: Misleading investigation paths include checking for database corruption or network latency issues.
- 11:00 AM: Incident escalated to the DevOps team for deeper investigation into the database server.
- 11:15 AM: DevOps team identifies that the PostgreSQL connection pool is saturated due to an incorrect configuration.
- 11:30 AM: The configuration is corrected, and the number of allowed connections is increased.
- 11:45 AM: Service gradually recovers as the application begins to re-establish database connections.
- 12:00 PM: Full service is restored, and the issue is marked as resolved.

# Root Cause and Resolution
- Root Cause: The root cause of the outage was a misconfigured connection pool in the PostgreSQL database settings. The pool was set to allow only a limited number of connections (10 connections), which was quickly exhausted during peak usage. Once all connections were in use, the application could no longer establish new connections to the database, leading to HTTP 500 errors and a complete service outage.

- Resolution: The issue was resolved by updating the database configuration to increase the maximum number of allowed connections in the pool. The PostgreSQL configuration was updated to support 50 connections, which is sufficient to handle peak traffic based on our current load tests. After updating the configuration, the application was restarted, and normal operations resumed.

## Corrective and Preventative Measures
- Improvements:
1. Database Connection Pooling: Review and adjust the connection pooling configuration for all environments to ensure they align with expected traffic loads.
2. Monitoring: Enhance monitoring to include alerts for connection pool saturation and database connection failures.
3. Load Testing: Conduct regular load tests to ensure the system can handle peak traffic scenarios without resource exhaustion.

- Tasks:
1. Patch the PostgreSQL server to ensure it's running the latest stable version.
2. Update the database connection pool settings in all environments (development, staging, production).
3. Add monitoring for PostgreSQL connection pool usage and set up alerts for any unusual spikes.
4. Review and document the current database connection settings as part of the standard operating procedures.
5. Conduct a post-outage load test to confirm that the new configuration can handle expected peak loads.
