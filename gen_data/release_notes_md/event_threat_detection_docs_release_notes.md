#  Release notes

This page documents production updates to Event Threat Detection. Check this
page for announcements about new or updated features, bug fixes, known issues,
and deprecated functionality.

##  October 31, 2019

**FEATURE:**

Event Threat Detection is now in beta.

**FEATURE:**

Event Threat Detection automatically handles some de-duplication of Findings.
For Findings that are largely identical, like repeated observation of the same
bad connection from the same Compute Engine instance, Event Threat Detection
only produces a finding once per hour.

**FEATURE:**

Event Threat Detection limits the daily number of Findings based on Google-
provided indicators of compromise to 200 per day

