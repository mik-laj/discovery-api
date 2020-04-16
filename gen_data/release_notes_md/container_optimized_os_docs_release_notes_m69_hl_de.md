#  Versionshinweise: Meilenstein-Release 69

##  Aktueller Status

Image-Serie  |  cos-69-lts  
---|---  
Veraltet nach  |  11\. Dez. 2019  
Kernel  |  [ 4.14.91+
](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/edb81c460eee7a4a35e2a95ebf6450df0963398e)  
Kubernetes  |  v1.11.1  
docker  |  v17.03.2  
  
##  Änderungs-Log (im Vergleich zu Meilenstein-Release 68)

###  cos-69-10895-172-0

_Datum: 28. Februar 2019_

  * "kernel.softlockup_all_cpu_backtrace" wurde aktiviert. Die Funktion war zuvor deaktiviert, um ein Kernel-Deadlock-Problem zu beseitigen, das jetzt behoben ist. 
  * "docker.service" wurde konfiguriert, indem "RestartSecs=10" so eingestellt wurde, dass Docker immer nach 10 Sekunden neu gestartet wird. 

###  cos-69-10895-138-0

_Datum: 24. Januar 2019_

  * Die Behebung eines Deadlock-Problems in der Kernel-Panic wurde rückportiert. 
  * Ein stabiler Linux-Kernel "v4.14.91" wurde zusammengeführt. 

###  cos-69-10895-123-0

_Datum: 10. Januar 2019_

  * CONFIG_BLK_WBT_MQ=y wurde zur Verbesserung der Leistungsisolierung auf nichtflüchtigen Speichern festgelegt. Dadurch wird ein Fehler behoben, bei dem Schreibvorgänge auf einem nichtflüchtigen SSD-Speicher die Leistung auf einem nichtflüchtigen Standard-Bootlaufwerk beeinträchtigen können. 
  * Ext4-Commits wurden ausgewählt, die sich auf FS-Inkonsistenzen beziehen. Diese wurden unter bestimmten Bedingungen durch Unterbrechungen während des NFS-CREATE-Vorgangs verursacht. 
  * Stabiler Linux-Kernel "v4.14.89" wurde zusammengeführt. 

###  cos-69-10895-102-0

_Datum: 20. Dezember 2018_

  * Die automatische Aktualisierung für abgeschirmte Bilder wurde deaktiviert. Cos-cloud-Images sind von dieser Änderung nicht betroffen. 
  * Die Ext4-Funktion "metadata_csum" auf der zustandsorientierten Partition wurde aktiviert. Dies verbessert auch die Leistung des Größenänderungvorgangs des Bootlaufwerks. 
  * Wenden Sie die IMA-Richtlinie nur an, wenn cloud-audit-setup.service ausgeführt wird. 

###  cos-69-10895-93-0

_Datum: 16. November 2018_

  * Der Kernel wurde auf v4.14.79 aktualisiert. 
  * Der Fehler, dass cloud-init keine gezippten Dateien schreiben kann, wurde behoben. 

###  cos-69-10895-91-0

_Datum: 29. Oktober 2018_

  * Eine Interaktion zwischen IMA und NFS konnte zu einem Deadlock führen. Dieses Problem wurde behoben. 
  * Bei Containern in Compute Engine wurde ein Problem mit "stackdriver-logging.service" festgestellt. Dieses Problem wurde behoben. 
  * PCID ist jetzt standardmäßig aktiviert, wenn sie von der CPU-Plattform unterstützt wird. 

###  cos-69-10895-85-0

_Datum: 11. Oktober 2018_

  * "softlockup_all_cpu_backtrace" wurde auf "0" zurückgesetzt, um unter bestimmten Umständen einen Kernel-Deadlock auf Maschinen mit leistungsfähiger CPU zu vermeiden. 

###  cos-69-10895-71-0

_Datum: 1. Oktober 2018_

  * Die Userspace-Header wurden aus dem Kernel-Header-Artefakt entfernt. 

###  cos-69-10895-62-0

_Datum: 18. September 2018_

  * Das Release wurde auf den Stable-Kanal verschoben. 
  * Eine Fehlerbehebung wurde rückportiert, damit scsi beim Ausführen der Rotationseinheit die Zufälligkeit beeinflusst  . Dies behebt ein Problem, bei dem Docker wegen niedriger Entropie auf nichtflüchtigen Standardspeichern seit dem Zusammenführen bei v4.14.63 langsam gestartet wird. 
  * CONFIG_RANDOM_TRUST_CPU wurde aktiviert, um einem Entropiemangel auf nichtflüchtigen SSD-Bootlaufwerken entgegenzuwirken. 
  * Ein Upgrade von OpenSSL auf 1.0.2p wurde durchgeführt. 
  * Die auf dem Stable-Kanal befindliche Linux-Version v4.14.65 wurde zusammengeführt. 
  * Die Fehlerbehebung für einen Cloud-init-Fehler, bei dem write_files nur mit Asci-Inhalten umgehen können, wurde rückportiert  . 
  * Die Fehlerbehebung für die Kernel-Warnung "WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)" wurde rückportiert. 
  * Eine Fehlerbehebung für den Linux-Kernel CVE-2018-12232 wurde vorgenommen. 
  * Die Behebung des Problems mit L1 Terminal Fault (L1TF) (CVE-2018-3615, CVE-2018-3620 und CVE-2018-3646) wurde rückportiert. 
  * Es wurden Fehlerkorrekturen bei CVE-2018-5391 vorgenommen. 
  * Es wurde ein Softlockup-Problem behoben, das auf einzelnen vCPU-VMs auftrat, wenn FUSE-Dateisysteme verwendet wurden. 
  * Kubernetes wurde auf Version v1.11.1 aktualisiert. 
  * Es wurden Fehlerkorrekturen bei CVE-2018-5390 vorgenommen. 
  * Der Standardwert für "kernel.pid_max" wurde auf 2^22 erhöht. 
  * Die auf dem Stable-Kanal befindliche Linux-Version v4.14.54 wurde im Kernel zusammengeführt. 
  * Die SCSI-CD-ROM-Unterstützung wurde entfernt. Dies löst das Problem "CVE-2018-11506". 
  * Für das integrierte Kubelet wurde ein Upgrade auf Version v1.11.0 durchgeführt. 
  * Docker-credential-gcr wurde auf Version 1.5.0 aktualisiert. 
  * Die BUG_REPORT_URL wurde unter /etc/os-release aktualisiert. 
  * Die NFS-Konfigurationen für die Fehlerbehebung wurden im Kernel aktiviert. 
  * Das Kernelmodul "tcp_bbr" wurde zur TCP-Überlastungssteuerung aktiviert. 
  * Git wurde auf Version 2.16.4 aktualisiert, um das Problem "CVE 2018-11235" zu beheben. 
  * Die Docker-Konfiguration "--disable-legacy-registry" wurde standardmäßig auf "true" gesetzt. 
  * Kubernetes wurde auf Version 1.10.4 aktualisiert. 
  * "Sshd_config" wurde aktualisiert, um CBC-basierte (Cipher Block Chaining) Chiffren zu löschen. 
  * Die CA-Stammzertifikate wurden aktualisiert, damit sie Mozilla NSS 3.36.1 entsprechen. 
  * OpenSSL wurde auf Version 1.0.2o aktualisiert. 

