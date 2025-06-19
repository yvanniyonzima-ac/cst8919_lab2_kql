# Azure Web App Logging & Detection Lab

## 🧠 What I Learned

In this lab, I learned how to:

- Link an **Azure Web App** to a **Log Analytics Workspace** to capture logs from different sources (HTTP logs, App Service logs, console output).
- Create and run **KQL (Kusto Query Language)** queries to detect unusual activity or failed login attempts.
- Set up an **alert rule** that sends aggregated log data to an email when specific conditions are met (e.g., spikes in failed logins or application errors).

## ⚠️ Challenges

I did not face any major challenges, but initially:

- I deployed the app using **Azure Static Web Apps**, which are intended for static front-end apps (like React or Vue). I later learned that **Static Web Apps do not support Python** backends like Flask, so I had to switch to using **Azure App Service** for proper support of my Flask app.

## 🔍 Detection Logic (KQL Query)

```kusto
AppServiceHTTPLogs
| where Result has "CallerError"
| project TimeGenerated, CsMethod, UserAgent, Result, ScStatus
| order by TimeGenerated desc
```

### 📖 Explanation:

- `AppServiceHTTPLogs`: The table containing HTTP request logs for App Service.
- `where Result has "CallerError"`: Filters requests that encountered caller-related errors (e.g., invalid requests or client errors).
- `project`: Selects relevant columns:
  - `TimeGenerated`: Timestamp of the request
  - `CsMethod`: HTTP method used (e.g., POST, GET)
  - `UserAgent`: Info about the client's browser/tool
  - `Result`: The outcome or status detail
  - `ScStatus`: HTTP status code (e.g., 401, 500)
- `order by TimeGenerated desc`: Sorts logs with most recent at the top

## 🚀 Real-World Improvements

In a real-world environment, to improve detection logic I would:

- Track **login attempts by IP address** and **username**, then create alerts for:
  - Brute force attempts (e.g., >5 failures from the same IP in 1 min)
  - Logins from **unusual geographies**
- Enable **Application Insights** with structured logging (e.g., `logging.warning("FAILED login", extra={...})`)

## 🎥 5-Minute Demo Video

▶️ Watch the video demo on YouTube: [https://youtu.be/xkR3R2xpGH4](https://youtu.be/xkR3R2xpGH4)