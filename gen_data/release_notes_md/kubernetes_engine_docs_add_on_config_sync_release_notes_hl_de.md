#  Versionshinweise

Auf dieser Seite werden Produktionsupdates für Config Sync dokumentiert. Hier
finden Sie regelmäßig Hinweise zu neuen oder aktualisierten Funktionen,
Fehlerkorrekturen, bekannten Problemen und verworfenen Funktionen.

Für neueste Produktaktualisierungen können Sie die URL dieser Seite in einen [
Feedreader ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
einfügen oder die Feed-URL direkt hinzufügen: `
https://cloud.google.com/feeds/kubernetes-engine-add-on-config-sync-release-
notes.xml `

##  1.2.0

Config Sync Version 1.2.0 ist allgemein für den produktiven Einsatz verfügbar.
Das ist die erste Version des Produkts.

###  Bekannte Probleme

**ISSUE:**

Wenn ein [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) in das Repository verschoben wird, führt dies dazu,
dass Config Sync nicht ordnungsgemäß ausgeführt wird und folgende
Fehlermeldung ausgegeben wird: "[KNV2002](/kubernetes-engine/docs/add-
on/config-sync/reference/errors#knv2002): failed to get server resources:
unable to retrieve the complete list of server APIs." (Serverressourcen nicht
abrufbar: die komplette Liste der Server-APIs konnte nicht abgerufen werden.)
Dieses Problem betrifft sowohl neue als auch bestehende Cluster, die aus
diesem Repository synchronisiert werden. So beheben Sie das Problem:

* Finden Sie mithilfe von ` kubectl get pods -n config-management-system ` die Namen der Pods ` git-importer ` und ` syncer ` heraus. 
* Kopieren Sie diese Namen und starten Sie die Pods mit ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` neu. 
* Diese Schritte müssen für jeden Cluster einmal ausgeführt werden. 
Sobald die Pods für einen Cluster neu gestartet wurden, funktioniert die
Synchronisierung wieder normal.

**ISSUE:**

Unter Umständen kann ` nomos view ` keine benutzerdefinierten
Ressourcendefinitionen (Custom Resource Definitions, CRDs) verarbeiten, die im
lokalen Klon des Repositories vorhanden sind, aber noch nicht mit einem
Cluster synchronisiert wurden.

Zum Umgehen dieses Problems können Sie [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=de#hydrate) statt ` nomos view ` verwenden.

