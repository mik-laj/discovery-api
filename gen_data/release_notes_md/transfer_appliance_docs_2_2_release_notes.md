#  Release notes

This page documents production updates to Transfer Appliance. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/transferappliance-2.2-release-
notes.xml `

##  April 11, 2019

**FEATURE:**

Transfer Appliance documentation provides instructions for [ using NFS to
capture data from HDFS ](https://cloud.google.com/transfer-
appliance/docs/2.0/capturing-data-hdfs-nfs-share) .

##  June 26, 2018

**FEATURE:**

Transfer Appliance Capture Utility now [ preserves file metadata by default
](https://cloud.google.com/transfer-appliance/docs/2.0/capturing-data-
windows#capture-metadata) .

**FEATURE:**

Transfer Appliance Capture Utility provides the option to [ skip symbolic
links to files ](https://cloud.google.com/transfer-
appliance/docs/2.0/capturing-data-windows#skip-links) .

**FEATURE:**

Transfer Appliance allows [ cancellation of data capture jobs
](https://cloud.google.com/transfer-appliance/docs/2.0/canceling-jobs) .

**FEATURE:**

While performing an [ NFS capture ](https://cloud.google.com/transfer-
appliance/docs/2.0/capturing-data-appliance) , Transfer Appliance allows you
to navigate to and select specific folders.

**FEATURE:**

[ NFS share export ](https://cloud.google.com/transfer-
appliance/docs/2.0/exporting-nfs-share) is now a supported data capture
method.

**FEATURE:**

[ Serial data captures using multiple appliances
](https://cloud.google.com/transfer-appliance/docs/2.0/performing-serial-
captures) is now supported, allowing you to continue data captures even if
your data size exceeds the capacity of a single Transfer Appliance.

**FEATURE:**

[ Network usage monitoring ](https://cloud.google.com/transfer-
appliance/docs/2.0/monitoring-capture-jobs#monitor-network-usage) is now
available through the Transfer Appliance Web User Interface.

**FEATURE:**

Disk status indicators are now accessible from the Settings menu in Transfer
Appliance Web User Interface.

**FEATURE:**

[ Rehydrator job status ](https://cloud.google.com/transfer-
appliance/docs/2.0/monitoring-rehydration-jobs) now displays rehydration job
start and end time.

**FEATURE:**

Password for [ Rehydrator SMTP configuration
](https://cloud.google.com/transfer-appliance/docs/2.0/launching-rehydrator)
is now optional.

**FEATURE:**

[ Rehydration job time to completion ](https://cloud.google.com/transfer-
appliance/docs/2.0/monitoring-rehydration-jobs) is now displayed in the
**Pending Jobs** list.

**FEATURE:**

The target path is now configurable while you're [ rehydrating uploaded data
](https://cloud.google.com/transfer-appliance/docs/2.0/rehydrating-
data#rehydrate-data) .

**FEATURE:**

Transfer Appliance software now performs a [ data integrity check
](https://cloud.google.com/transfer-appliance/docs/2.0/rehydrating-
data#verify-rehydrated-data) at every stage of the data migration.

**FEATURE:**

Transfer Appliance now allows you to perform a [ factory reset
](https://cloud.google.com/transfer-appliance/docs/2.0/shipping-
appliance#prepare-for-shipping) after you prepare an appliance for shipment to
the Google upload facility.

**FEATURE:**

Users no longer need to manually create the staging bucket when [ preparing to
ship Transfer Appliance ](https://cloud.google.com/transfer-
appliance/docs/2.0/shipping-appliance) to the Google upload facility.

**FEATURE:**

To avoid early deletion charges, the Rehydrator uses [ regional or multi-
regional ](https://cloud.google.com/storage/docs/bucket-locations#key-
concepts) storage class locations as appropriate when building component
objects to rehydrate files greater than 100GB.

**CHANGED:**

Transfer Appliance Console User Interface now provides most features through
**Data Capture** and **Settings** menus.

**CHANGED:**

[ Password for SMTP configuration ](https://cloud.google.com/transfer-
appliance/docs/2.0/preparing-to-unpack#get-smtp-info) is now optional,
enabling email alerts to be sent via both authenticated and unauthenticated
SMTP servers.

**CHANGED:**

New communications protocol removes the need for connections from Transfer
Appliance to workstations running the Capture Utility. See [ Firewall port
requirements ](https://cloud.google.com/transfer-appliance/docs/2.0/preparing-
data-transfer#firewall-port-requirements) .

