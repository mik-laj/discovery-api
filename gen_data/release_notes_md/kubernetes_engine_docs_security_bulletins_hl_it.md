#  Bollettini sulla sicurezza

In questo argomento vengono descritti tutti i bollettini sulla sicurezza per
Google Kubernetes Engine (GKE).

Le vulnerabilità sono spesso mantenute segrete sotto embargo finché le parti
interessate non hanno avuto la possibilità di affrontarle. In questi casi, le
[ Note di rilascio ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it) di GKE faranno riferimento agli "aggiornamenti della sicurezza"
fino a quando l'embargo non sarà stato revocato. A quel punto le note verranno
aggiornate per riflettere la vulnerabilità affrontata dalla patch.

**Nota:** se esegui carichi di lavoro multi-tenant su GKE, ti preghiamo di
prestare particolare attenzione a questi bollettini. È più probabile che
queste vulnerabilità influiscano sui carichi di lavoro multi-tenant. Per una
descrizione tecnica dei limiti di sicurezza in GKE e del modo in cui questi
influiscono sui carichi di lavoro, consulta il post del blog dedicato all' [
isolamento a livelli differenti dello stack Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Per ricevere gli ultimi bollettini sulla sicurezza, aggiungi l'URL di questa
pagina al tuo [ aggregatore di feed
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) oppure aggiungi
direttamente l'URL del feed: ` https://cloud.google.com/feeds/kubernetes-
engine-security-bulletins.xml `

##  GCP-2020-005

**Pubblicato il:** 07/05/2020  
**Ultimo aggiornamento:** 07/05/2020  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Recentemente è stata scoperta una vulnerabilità nel kernel Linux, descritta in
[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) , che consente di uscire dai limiti del
container per ottenere privilegi di utente root sul nodo host.

I nodi di Google Kubernetes Engine (GKE) Ubuntu che eseguono GKE 1.16 o 1.17
sono interessati da questa vulnerabilità e consigliamo di eseguire l'upgrade
alla versione più recente della patch il prima possibile, come descritto di
seguito.

I nodi che eseguono Container-Optimized OS non sono interessati. I nodi che
eseguono GKE on-prem non sono interessati.

####  Che cosa devo fare?

**Per la maggior parte dei clienti non sono necessari ulteriori interventi.
Solo i nodi che eseguono Ubuntu nelle versioni 1.16 o 1.17 di GKE sono
interessati.**

Per eseguire l'upgrade dei nodi, devi prima eseguire l'upgrade del master alla
versione più recente. Questa patch sarà disponibile in Kubernetes
1.16.8-gke.12, 1.17.4-gke.10 e release successive. Traccia la disponibilità di
queste patch nelle [ note di rilascio ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=it) .

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) descrive una vulnerabilità nelle versioni
kernel Linux 5.5.0 e successive che permette a un container dannoso di leggere
e scrivere (con minima interazione dell'utente sotto forma di file eseguibile)
la memoria del kernel, ottenendo così la possibilità di eseguire codice a
livello di utente root sul nodo host. Questa è classificata come vulnerabilità
di gravità "Alta".

|

Alta

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Pubblicato il:** 31/03/2020  
**Ultimo aggiornamento:** 31/03/2020  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Di recente è stata scoperta una vulnerabilità in Kubernetes, descritta in [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , che consente a qualsiasi utente
autorizzato a inviare richieste POST di eseguire un attacco denial of service
remoto contro un server API Kubernetes. Il Kubernetes Product Security
Committee (PSC) ha pubblicato ulteriori informazioni su questa vulnerabilità,
disponibili [ qui ](https://groups.google.com/forum/?hl=it#!topic/kubernetes-
security-announce/wuwEwZigXBc) .

I cluster GKE che utilizzano [ reti autorizzate master
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=it) e [ cluster privati senza endpoint pubblico
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=it#private_master) mitigano questa vulnerabilità.

####  Che cosa devo fare?

Ti consigliamo di eseguire l'upgrade del cluster a una versione della patch
che contenga la correzione per questa vulnerabilità.

Di seguito sono elencate le versioni di patch che contengono la correzione:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Quali vulnerabilità vengono affrontate da questa patch?

La patch corregge la seguente vulnerabilità denial of service (DoS):

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

Media

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Pubblicato il:** 23/03/2020  
**Ultimo aggiornamento:** 23/03/2020  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Kubernetes ha divulgato [ due vulnerabilità denial of service
](https://groups.google.com/forum/?hl=it#!topic/kubernetes-security-
announce/2UOlsba2g0s) , una con conseguenze sul server API, l'altra sui
Kubelet. Per ulteriori dettagli, consulta i problemi di Kubernetes: [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) e [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  Che cosa devo fare?

Tutti gli utenti di GKE sono protetti da CVE-2020-8551 a meno che gli utenti
non attendibili non possano inviare richieste nella rete interna del cluster.
L'utilizzo di [ reti autorizzate master ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=it) riduce ulteriormente i rischi di
CVE-2020-8552.

####  Quando verranno applicate le patch?

Le patch per CVE-2020-8551 richiedono un upgrade del nodo. Di seguito sono
elencate le versioni di patch che conterranno la mitigazione:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Nota: le versioni 1.14.x e precedenti non sono interessate da questa
vulnerabilità, di conseguenza non sono richieste patch.

Le patch per CVE-2020-8552 richiedono un upgrade del master. Di seguito sono
elencate le versioni di patch che conterranno la mitigazione:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Media

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 gennaio 2020; ultimo aggiornamento 24 gennaio 2020

**Pubblicato il:** 21/01/2020  
**Ultimo aggiornamento:** 24/01/2020  Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 24-01-2020:** la messa a disposizione di versioni con patch è
già in corso e sarà completata entro il 25 gennaio 2020\.

* * *

Microsoft ha divulgato una vulnerabilità nell'API Windows Crypto e la sua
convalida delle firme a curva ellittica. Per ulteriori informazioni, consulta
la [ divulgazione di Microsoft ](https://portal.msrc.microsoft.com/en-
US/security-guidance/advisory/CVE-2020-0601) .

**Che cosa devo fare?**

**Per la maggior parte dei clienti non sono necessari ulteriori interventi.
Sono interessati solo i nodi in esecuzione su Windows Server.**

Per i clienti che utilizzano i nodi Windows Server, sia questi ultimi che i
carichi di lavoro containerizzati eseguiti su tali nodi devono essere
aggiornati a versioni con patch per mitigare questa vulnerabilità.

**Per aggiornare i container:**

Ricostruisci i tuoi container utilizzando le immagini container di base di
Microsoft più recenti, selezionando un tag [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) o [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) con un LastUpdated
Time pari a 1/14/2020 o successivo.

**Per aggiornare i nodi:**

La messa a disposizione di versioni con patch è già in corso e sarà completata
entro il 24 gennaio 2020.

Puoi attendere fino a quel momento ed eseguire un upgrade del nodo a una
versione GKE con patch, oppure puoi usare Windows Update per eseguire
manualmente il deployment della patch Windows più recente in qualsiasi
momento.

Di seguito sono elencate le versioni di patch che conterranno la mitigazione:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Quali vulnerabilità vengono affrontate da questa patch?**

La patch attenua le seguenti vulnerabilità:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- Questa vulnerabilità è anche nota come
[ vulnerabilità spoofing dell'API Windows Crypto
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) e può essere sfruttata per fare apparire come
attendibili eseguibili dannosi o permettere a un utente malintenzionato di
condurre attacchi man in the middle e decriptare informazioni riservate su
connessioni TLS al software interessato.

|

Punteggio base NVD: 8,1 (Alta)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 novembre 2019

**Pubblicato il:** 14/11/2019  
**Ultimo aggiornamento:** 14/11/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Kubernetes ha divulgato un problema di sicurezza nei file collaterali
kubernetes-csi [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) e [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) che influisce
sulla maggior parte delle versioni dei file collaterali utilizzate nei driver
[ Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) . Per ulteriori dettagli, consulta la [
divulgazione di Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) .

**Che cosa devo fare?**  
**Questa vulnerabilità non influisce sui componenti GKE gestiti** . Potrebbe
riguardarti se gestisci i tuoi driver CSI in [ cluster GKE alpha
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=it) che eseguono GKE versione 1.12 o successiva. Se la
vulnerabilità si applica al tuo caso, chiedi al tuo fornitore di driver CSI le
istruzioni per l'upgrade.

**Quali vulnerabilità vengono affrontate da questa patch?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : questo CVE rappresenta una
vulnerabilità nei file collaterali ` kubernetes-csi ` [ ` external-provisioner
` ](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) e [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) che
può consentire accessi o modifiche non autorizzati ai dati del volume. Questo
influisce sulla maggior parte delle versioni dei file collaterali utilizzate
nei [ driver CSI ](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Media

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 novembre 2019

**Pubblicato il:** 12/11/2019  
**Ultimo aggiornamento:** 12/11/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Intel ha divulgato CVE che consentono potenziali interazioni tra esecuzione
speculativa e stato della microarchitettura per compromettere i dati. Per
ulteriori dettagli, consulta la [ divulgazione di Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

**L'infrastruttura host che esegue Kubernetes Engine isola i carichi di lavoro
dei clienti. A meno che tu non esegua codice non attendibile all'interno dei
tuoi cluster GKE multi-tenant _e_ utilizzi nodi N2, M2 o C2, non sono
necessarie altre azioni. ** Per le istanze GKE sui nodi N1 non sono richieste
ulteriori azioni.

Se esegui Anthos GKE On-Prem, l'esposizione dipende dall'hardware. Confronta
la tua infrastruttura con la [ divulgazione di Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  Che cosa devo fare?

**La vulnerabilità ti riguarda solo se utilizzi pool di nodi con nodi N2, M2 o
C2 _e_ su tali nodi viene eseguito codice non attendibile all'interno dei tuoi
cluster GKE multi-tenant. **

**La patch viene applicata al riavvio dei nodi.** Il modo più semplice per
riavviare tutti i nodi nel pool è utilizzare l'operazione di [ upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=it#upgrade_nodes) per forzare un riavvio di tutti i nodi nel pool
interessato.  

Nota: non è necessario cambiare versioni durante un upgrade. Puoi avviare un
upgrade alla stessa versione nodo con il flag ` cluster-version ` .

####  Quali vulnerabilità vengono affrontate da questa patch?

La patch attenua le seguenti vulnerabilità:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: questo CVE è noto anche come TSX Async Abort (TAA). TAA fornisce un
ulteriore percorso per l'esfiltrazione dei dati utilizzando le stesse
strutture di dati della microarchitettura sfruttate da [ Microarchitectural
Data Sampling (MDS) ](https://cloud.google.com/kubernetes-
engine/docs/security-bulletins?hl=it#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
Questa vulnerabilità denial of service (DoS) influisce sugli host di macchine
virtuali consentendo a un utente guest malintenzionato di provocare l'arresto
anomalo di un host non protetto. Questo CVE è anche noto con il nome "Machine
Check Error on Page Size Change". Non influisce su GKE.

|

Media

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 ottobre 2019

**Pubblicato il:** 22/10/2019  
**Ultimo aggiornamento:** 22/10/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Di recente è stata scoperta una vulnerabilità nel linguaggio di programmazione
Go, descritta in [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . Questa vulnerabilità influisce
potenzialmente sulle configurazioni di Kubernetes che utilizzano un proxy di
autenticazione. Per ulteriori dettagli, consulta la [ divulgazione di
Kubernetes ](https://groups.google.com/forum/?hl=it#!topic/kubernetes-
security-announce/PtsUCqFi4h4) .

Kubernetes Engine non consente la configurazione di un proxy di
autenticazione, pertanto non è interessato da questa vulnerabilità.

|

Nessuna

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 ottobre 2019

**Pubblicato il:** 16/10/2019  
**Ultimo aggiornamento:** 24/10/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 24/10/2019:** le versioni con patch applicata sono ora
disponibili in tutte le zone.

* * *

Di recente è stata scoperta una vulnerabilità in Kubernetes, descritta in [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , che consente a qualsiasi utente
autorizzato a inviare richieste POST di eseguire un attacco denial of service
remoto contro un server API Kubernetes. Il Kubernetes Product Security
Committee (PSC) ha pubblicato ulteriori informazioni su questa vulnerabilità,
disponibili [ qui ](https://groups.google.com/forum/?hl=it#!topic/kubernetes-
security-announce/jk8polzSUxs) .

I cluster GKE che utilizzano [ reti autorizzate master
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=it) e [ i cluster privati senza endpoint pubblico
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=it#private_master) mitigano questa vulnerabilità.

######  Che cosa devo fare?

Consigliamo di eseguire l'upgrade del cluster a una versione patch che
contenga la correzione non appena disponibile. Prevediamo che saranno
disponibili in tutte le zone con la release di GKE pianificata per la
settimana del 14 ottobre.

Di seguito sono elencate le versioni di patch che conterranno la mitigazione:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Quali vulnerabilità vengono affrontate da questa patch?

La patch attenua le seguenti vulnerabilità:

CVE-2019-11253 è una vulnerabilità denial of service (DoS).

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 settembre 2019

**Pubblicato il:** 16/09/2019  
**Ultimo aggiornamento:** 16/10/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Questo bollettino è stato aggiornato dopo la pubblicazione originale.

Di recente sono state scoperte le nuove vulnerabilità di sicurezza del
linguaggio di programmazione Go [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) e [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) , che
rientrano tra le vulnerabilità denial of service (DoS). In GKE, questo
potrebbe consentire a un utente di creare richieste dannose, che consumano
quantità eccessive di CPU nel server API Kubernetes e possono ridurre la
disponibilità del piano di controllo del cluster. Per ulteriori dettagli,
consulta la [ divulgazione relativa al linguaggio di programmazione Go
](https://groups.google.com/forum/?hl=it#!topic/golang-announce/65QixT3tcmg) .

######  Che cosa devo fare?

Consigliamo di eseguire l'upgrade del cluster all'ultima versione di patch,
che contiene la mitigazione di questa vulnerabilità, non appena disponibile.
Prevediamo che saranno disponibili in tutte le zone con la prossima release di
GKE, in base alla [ programmazione di release
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#september_16_2019) .

Di seguito sono elencate le versioni di patch che conterranno la mitigazione:

  * **Aggiornamento 16 ottobre 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua le seguenti vulnerabilità:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) e [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) sono
vulnerabilità denial of service (DoS).

|

Alta

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 settembre 2019

**Pubblicato il:** 05/09/2019  
**Ultimo aggiornamento:** 05/09/2019

Il bollettino per la correzione della vulnerabilità documentata nel bollettino
del  31 maggio 2019  è aggiornato.

##  22 agosto 2019

**Pubblicato il:** 22/08/2019  
**Ultimo aggiornamento:** 22/08/2019

Il bollettino per il  5 agosto 2019  è stato aggiornato. La correzione per la
vulnerabilità documentata nel bollettino precedente è [ disponibile
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#august_22_2019) .

##  8 agosto 2019

**Pubblicato il:** 08/08/2019  
**Ultimo aggiornamento:** 08/08/2019

Il bollettino per il  5 agosto 2019  è stato aggiornato. Prevediamo che la
correzione per la vulnerabilità documentata nel bollettino sarà disponibile
nella prossima release di GKE.

##  5 agosto 2019

**Pubblicato il:** 05/08/2019  
**Ultimo aggiornamento:** 09/08/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
Questo bollettino è stato aggiornato dopo la pubblicazione originale.

Kubernetes di recente ha scoperto la vulnerabilità [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , che
consente di agire su istanze di [ risorse personalizzate
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) con ambito cluster come se fossero oggetti con spazio dei nomi
esistenti in tutti gli spazi dei nomi. Ciò significa che gli account utente e
di servizio con autorizzazioni RBAC solo a livello di spazio dei nomi possono
interagire con le risorse personalizzate con ambito cluster. Per sfruttare
questa vulnerabilità, l'utente malintenzionato deve avere privilegi per
accedere alla risorsa in qualsiasi spazio dei nomi.

######  Che cosa devo fare?

Ti consigliamo di [ eseguire l'upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=it) del cluster alla versione più
recente della patch, che consente di mitigare questa vulnerabilità, non appena
disponibile. Prevediamo la disponibilità in tutte le zone con la prossima
release di GKE. Di seguito sono elencate le versioni di patch che conterranno
la mitigazione:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ canale rapido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=it) ) 

######  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 luglio 2019

**Pubblicato il:** 03/07/2019  
**Ultimo aggiornamento:** 03/07/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
È ora disponibile una versione con patch di ` kubectl ` per risolvere
CVE-2019-11246 con [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=it#kubernetes_engine) .
Consulta il  bollettino sulla sicurezza del 25 giugno 2019  per ulteriori
informazioni.

**Nota:** la patch non è disponibile in ` kubectl ` 1.11.10.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 luglio 2019

**Pubblicato il:** 25/06/2019  
**Ultimo aggiornamento:** 03/07/2019  Descrizione  |  Gravità  |  Note  
---|---|---  
  
######  Aggiornamento 3 luglio 2019

Al momento dell'ultimo aggiornamento non erano ancora disponibili le patch per
le versioni 1.11.9 e 1.11.10. Ora abbiamo pubblicato 1.11.10-gke.5 come target
di upgrade per entrambe le versioni 1.11.

Al momento, la patch è stata applicata ai master GKE e all'infrastruttura
Google che esegue Kubernetes Engine, che è protetta da questa vulnerabilità.

I master 1.11 saranno presto deprecati ed è programmato l'upgrade automatico a
1.12 nella settimana dell'8 luglio 2019. Puoi scegliere una qualsiasi delle
azioni suggerite di seguito per portare i nodi a una versione con patch:

  * Esegui l'upgrade del nodo a 1.11.10-gke.5 entro l'8 luglio 2019. Dopo questa data, inizierà la rimozione delle versioni 1.11 dall'elenco di target disponibili per l'upgrade. 
  * Abilita gli [ upgrade automatici ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=it) sui nodi 1.11 e permetti l'upgrade insieme ai master a 1.12. 
  * [ Esegui manualmente l'upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=it) di master e nodi a una versione 1.12 fissa. 

Di seguito è riportato il bollettino originale del 24 giugno 2019:

* * *

######  Aggiornamento 24 giugno 2019

A partire dal 22/06/2019 21:40 UTC abbiamo reso disponibili le seguenti
versioni di Kubernetes con patch. I master compresi tra le versioni di
Kubernetes 1.11.0 e 1.13.6 saranno automaticamente aggiornati a una versione
con patch. Se la versione che utilizzi non è compatibile con questa patch,
esegui l'upgrade a una versione master compatibile (nell'elenco di seguito)
prima di procedere all'upgrade dei nodi.

**A causa della gravità di queste vulnerabilità, indipendentemente dal fatto
che siano abilitati o meno gli upgrade automatici dei nodi, ti consigliamo di[
eseguire manualmente l'upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=it) di nodi e master a una
di queste versioni il prima possibile. **

Le versioni con patch:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Segue il bollettino originale del 18 giugno 2019:

* * *

Netflix ha recentemente divulgato tre vulnerabilità TCP nei kernel Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Questi CVE vengono denominati collettivamente [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

I kernel Linux senza patch possono essere vulnerabili a un attacco denial of
service scatenato da remoto. **Sono interessati i nodi Google Kubernetes
Engine che inviano o ricevono traffico di rete non attendibile e consigliamo
di seguire la procedura di mitigazione riportata di seguito per proteggere i
tuoi carichi di lavoro.**

######  Master Kubernetes

  * I master Kubernetes che utilizzano [ Reti autorizzate ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=it) per limitare il traffico alle sole reti attendibili non sono interessati. 

  * I master per cluster GKE, gestiti da Google, riceveranno automaticamente la patch nei prossimi giorni. Non sono richieste azioni da parte del cliente. 

######  Nodi Kubernetes

I nodi che limitano il traffico alle sole reti attendibili non sono
interessati. Un esempio è un cluster con le caratteristiche seguenti:

  * Nodi protetti tramite firewall dalle reti non affidabili o privi di IP pubblici ( [ cluster privati ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=it) ) 
  * Cluster senza servizi LoadBalancer pubblici 

Google sta approntando una mitigazione permanente per queste vulnerabilità,
che sarà resa disponibile come nuova versione dei nodi. Aggiorneremo questo
bollettino e invieremo un'email a tutti i clienti GKE quando sarà disponibile
la correzione permanente.

Mentre la correzione permanente non è ancora disponibile, abbiamo creato un
DaemonSet Kubernetes che implementa le mitigazioni modificando la
configurazione ` iptables ` dell'host.

#####  Che cosa devo fare?

Applica il DaemonSet Kubernetes a tutti i nodi nel tuo cluster mediante il
comando seguente. Questo aggiunge una regola ` iptables ` alle regole `
iptables ` esistenti sul nodo per mitigare la vulnerabilità. **Esegui il
comando una volta per cluster per ciascun progetto Google Cloud.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Ipv6 non è supportato in GKE, di conseguenza non sono richieste regole
ip6tables.

Quando sarà disponibile una versione dei nodi con patch e dopo aver eseguito
l'upgrade di tutti i nodi potenzialmente interessati, potrai rimuovere il
DaemonSet mediante il comando seguente. **Esegui il comando una volta per
cluster per ciascun progetto Google Cloud.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Alta  
Media  
Media  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 giugno 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 03/07/2019:** questa patch è disponibile in ` gcloud `
253.0.0, per ` kubectl ` versioni 1.12.9, 1.13.6, 1.14.2 e release successive.

**Nota:** la patch non è disponibile in 1.11.10.

* * *

Kubernetes ha recentemente scoperto la vulnerabilità [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) , che
consente a un utente malintenzionato con accesso a un'operazione ` kubectl cp
` ed esecuzione di codice all'interno di un container di modificare i file
sull'host. Questo exploit ha il potenziale di permettere a un utente
malintenzionato di sostituire o creare un file nel file system dell'host. Per
ulteriori dettagli, consulta la [ divulgazione di Kubernetes
](https://groups.google.com/forum/?hl=it#!topic/kubernetes-security-
announce/NLs2TGbfPdo) .

**Tutte le versioni di Google Kubernetes Engine (GKE)` gcloud ` sono
interessate da questa vulnerabilità e ti consigliamo di eseguire l'upgrade
alla versione della patch più recente di ` gcloud ` non appena disponibile. **
Una versione patch imminente includerà una mitigazione per questa
vulnerabilità.

######  Che cosa devo fare?

Una versione con patch di ` kubectl ` sarà disponibile in un'imminente release
di ` gcloud ` . Puoi anche eseguire l' [ upgrade di ` kubectl ` direttamente
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) .

Traccia la disponibilità di questa patch nelle [ note di rilascio di ` gcloud
` ](https://cloud.google.com/sdk/docs/release-notes?hl=it) .

######  Quale vulnerabilità viene affrontata da questa patch?

La vulnerabilità [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) consente a un utente malintenzionato con
accesso a un'operazione ` kubectl cp ` e all'esecuzione di codice all'interno
di un container di modificare i file sull'host. Questo exploit potrebbe
consentire a un utente malintenzionato di sostituire o creare un file nel file
system dell'host.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 giugno 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Docker ha recentemente scoperto la vulnerabilità [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , che
permette a un utente malintenzionato in grado di eseguire codice all'interno
di un container di assumere il controllo di un'operazione ` docker cp `
avviata dall'esterno. Questo exploit ha il potenziale di permettere a un
utente malintenzionato di cambiare la destinazione di scrittura di un file a
una posizione arbitraria nel file system dell'host.

**Tutti i nodi Google Kubernetes Engine (GKE) che eseguono Docker sono
interessati da questa vulnerabilità e consigliamo di eseguire l'upgrade alla
versione più recente della patch non appena disponibile. Una versione patch
imminente includerà una mitigazione per questa vulnerabilità.**

**Tutti i master Google Kubernetes Engine (GKE) precedenti la versione 1.12.7
eseguono Docker e sono interessati da questa vulnerabilità.** In GKE, gli
utenti non hanno accesso a ` docker cp ` sul master e quindi il rischio di
questa vulnerabilità è limitato per i master GKE.

#####  Che cosa devo fare?

Sono interessati solo i nodi che eseguono Docker e solo quando viene emesso un
comando ` docker cp ` (o equivalente API) che può essere intercettato da un
malintenzionato. Si tratta di uno scenario decisamente insolito in un ambiente
Kubernetes. I nodi che eseguono [ COS con containerd
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=it) non sono interessati.

Per eseguire l'upgrade dei nodi, devi prima eseguire l' [ upgrade del master
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=it#upgrading_the_cluster) alla versione con patch. Quando la patch
è disponibile, puoi avviare un upgrade del master o attendere che venga
avviato automaticamente da Google. La patch sarà disponibile in Docker
18.09.7, incluso in un'imminente patch per GKE. **Questa patch sarà
disponibile solo per GKE versioni 1.13 e successive.**

Eseguiremo automaticamente l'upgrade dei master dei cluster alla versione con
patch secondo la regolare cadenza degli upgrade. Puoi anche avviare un upgrade
del master quando la versione con patch diventa disponibile.

Aggiorneremo questo bollettino con le versioni contenenti una patch appena
disponibili. Traccia la disponibilità di queste patch nelle [ note di rilascio
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=it) .

#####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

La vulnerabilità [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) permette a un utente malintenzionato in
grado di eseguire codice all'interno di un container di assumere il controllo
di un'operazione ` docker cp ` avviata dall'esterno. Questo exploit ha il
potenziale di permettere a un utente malintenzionato di cambiare la
destinazione di scrittura di un file a una posizione arbitraria nel file
system dell'host.

|  Alta  |  
  
##  31 maggio 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Questo bollettino è stato aggiornato dopo la pubblicazione originale.

######  Aggiornamento 2 agosto 2019

Al momento della pubblicazione del bollettino originale, solo le versioni da
1.13.6-gke.0 a 1.13.6-gke.5 compresa erano interessate. A causa di una
regressione, ora sono interessate tutte le versioni 1.13.6.x. Se esegui la
versione 1.13.6, esegui l'upgrade a 1.13.7 il prima possibile.

Il progetto Kubernetes ha divulgato il [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) in kubelet
v1.13.6 e v1.14.2, in grado di far sì che i container vengano eseguiti come
UID 0 (tipicamente mappato all'utente ` root ` ), anche se nell'immagine
container è specificato un utente diverso. **Se i tuoi container vengono
eseguiti come utenti non-root e la versione nodo in uso è compresa tra
1.13.6-gke.0 e 1.13.6-gke.6, ti consigliamo di impostare` RunAsUser ` su tutti
i pod nel cluster i cui container non devono essere eseguiti come UID 0. **

Se viene specificato un valore ` USER ` non-root (ad esempio impostando il
valore di ` USER ` in un Dockerfile), si verifica un comportamento imprevisto.
Alla prima esecuzione su un nodo, un container rispetta correttamente lo UID
specificato. Tuttavia, a causa di questo difetto, alla seconda esecuzione (e
successive) il container viene eseguito come UID 0 a prescindere dallo UID
specificato. Questo di norma è un aumento dei privilegi indesiderato e può
portare a un comportamento imprevisto delle applicazioni.

#####  Come faccio a sapere se la versione che eseguo è interessata?

Esegui questo comando per elencare tutti i nodi e la relativa versione
kubelet:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

I tuoi nodi sono interessati se nell'output sono elencate le versioni kubelet
riportate di seguito:

  * v1.13.6 
  * v1.14.2 

#####  Come faccio a sapere se la mia configurazione specifica è interessata?

Se i tuoi container vengono eseguiti come utenti non-root e la versione nodo
in uso è compresa tra 1.13.6-gke.0 e 1.13.6-gke.6, la tua configurazione è
interessata, eccetto che nei casi seguenti:

  * I pod che specificano un valore non-root valido per PodSecurityContext di ` runAsUser ` non sono interessati e continuano a funzionare come previsto. 
  * PodSecurityPolicies che prevedono l'applicazione forzata di un'impostazione di ` runAsUser ` non sono interessate e continuano a funzionare come previsto. 
  * I pod che specificano che ` mustRunAsNonRoot:true ` non viene avviato come UID 0 non verranno avviati quando interessati da questo problema. 

#####  Che cosa devo fare?

Imposta il [ contesto di sicurezza RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) su tutti i pod nel cluster che
non devono essere eseguiti come UID 0. Puoi applicare questa configurazione
utilizzando una [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) .

|  Media  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 maggio 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 11/06/2019:** la patch è disponibile in 1.11.10-gke.4,
1.12.8-gke.6 e 1.13.6-gke.5 rilasciati nella settimana del 28/05/2019 e nelle
release successive.

Intel ha divulgato i seguenti CVE:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Questi CVE vengono denominati collettivamente Microarchitectural Data Sampling
(MDS). Queste vulnerabilità possono determinare un'esposizione dei dati
attraverso l'interazione dell'esecuzione speculativa con lo stato della
microarchitettura. Per ulteriori dettagli, consulta la [ divulgazione di Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

**L'infrastruttura host che esegue Kubernetes Engine isola i carichi di lavoro
dei clienti l'uno dall'altro. A meno che tu non esegua codice non attendibile
all'interno dei tuoi cluster GKE multi-tenant, queste vulnerabilità non si
applicano al tuo caso.**

**Per i clienti che eseguono codice non attendibile nei propri servizi multi-
tenant all'interno di Kubernetes Engine, si tratta di una vulnerabilità
particolarmente grave.** Per mitigarla in Kubernetes Engine, disabilita Hyper-
Threading nei tuoi nodi. Queste vulnerabilità interessano solo i nodi Google
Kubernetes Engine (GKE) che utilizzano CPU multiple. Nota che le VM
n1-standard-1 (l'impostazione predefinita per GKE), g1-small e f1-micro
espongono solo 1 vCPU all'ambiente guest, pertanto non è necessario
disabilitare Hyper-Threading.

Ulteriori protezioni per abilitare la funzionalità di svuotamento saranno
incluse in una imminente [ versione della patch
](https://cloud.google.com/kubernetes-engine/release-notes?hl=it) . Eseguiremo
automaticamente l'upgrade di master e nodi alla versione con patch nelle
prossime settimane, in base alla regolare cadenza degli upgrade. **La patch da
sola non è sufficiente per mitigare l'esposizione a questa vulnerabilità. Di
seguito sono riportate le azioni consigliate.**

Se esegui GKE On-Prem, l'impatto dipende dall'hardware in uso. Consulta la [
divulgazione di Intel ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) .

####  Che cosa devo fare?

**A meno che tu non esegua codice non attendibile all'interno dei tuoi cluster
GKE multi-tenant, queste vulnerabilità non si applicano al tuo caso.**

**Per i nodi in Kubernetes Engine, crea nuovi pool di nodi con Hyper-Threading
disabilitato e riprogramma i tuoi carichi di lavoro sui nuovi nodi.**

Nota che le VM n1-standard-1, g1-small e f1-micro espongono solo 1 vCPU
all'ambiente guest e quindi non è necessario disabilitare Hyper-Threading.

**Avviso:**

  * la disabilitazione di Hyper-Threading può avere un grave impatto sulle prestazioni dei cluster e dell'applicazione. Verifica che sia accettabile prima del deployment ai cluster di produzione. 
  * Puoi disabilitare Hyper-threading a livello di pool di nodi GKE con il deployment di un DaemonSet. Tuttavia, il deployment di questo DaemonSet provoca il riavvio simultaneo di tutti i nodi nel pool. Di conseguenza, consigliamo di creare un nuovo pool di nodi nel cluster, eseguire il deployment del DaemonSet per disabilitare Hyper-Threading in tale pool di nodi, quindi eseguire la migrazione dei carichi di lavoro al nuovo pool di nodi. 

Per creare un nuovo pool di nodi con Hyper-Threading disabilitato:

  1. Crea un nuovo pool di nodi nel tuo cluster con l'etichetta nodo ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Esegui il deployment del DaemonSet su questo nuovo pool di nodi. Il DaemonSet viene eseguito solo sui nodi con l'etichetta ` cloud.google.com/gke-smt-disabled=true ` . Disabilita Hyper-Threading e quindi riavvia il nodo. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Verifica che i pod del DaemonSet siano in esecuzione. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Dovresti ricevere una risposta analoga a:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Controlla che nei log dei pod sia presente la dicitura "SMT has been disabled". 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Nota: le opzioni di avvio non possono essere modificate se il nodo ha la
funzione [Avvio protetto](/kubernetes-engine/docs/how-to/shielded-gke-
nodes#secure_boot) attiva. Se la funzione Avvio protetto è attiva, deve essere
[disattivata](/kubernetes-engine/docs/how-to/shielded-gke-nodes#disabling)
prima della creazione del DaemonSet.

Devi mantenere il DaemonSet in esecuzione sui pool di nodi per consentire
l'applicazione automatica delle modifiche ai nuovi nodi creati nel pool. Le
creazioni di nodi possono essere avviate dalla riparazione automatica dei
nodi, dall'upgrade manuale o automatico e dalla scalabilità automatica.

Per riabilitare Hyper-Threading, dovrai ricreare il pool di nodi senza
eseguire il deployment del DaemonSet fornito ed eseguire la migrazione dei
carichi di lavoro al nuovo pool di nodi.

Ti consigliamo inoltre di eseguire manualmente l'upgrade dei nodi non appena
la patch diventa disponibile. Per poterlo fare, devi prima [ eseguire
l'upgrade del master ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=it#upgrading_the_cluster) alla versione più recente.
L'upgrade dei master GKE verrà eseguito automaticamente secondo la regolare
cadenza degli upgrade.

Aggiorneremo questo bollettino con le versioni contenenti una patch non appena
saranno disponibili.

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua le seguenti vulnerabilità:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Queste vulnerabilità sfruttano l'esecuzione speculativa. Questi CVE vengono
denominati collettivamente Microarchitectural Data Sampling. Queste
vulnerabilità possono determinare un'esposizione dei dati attraverso
l'interazione dell'esecuzione speculativa con lo stato della
microarchitettura.  |  Media  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 aprile 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Di recente sono state scoperte le vulnerabilità di sicurezza [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) e [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
in [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) incorpora Envoy e queste vulnerabilità consentono
in alcuni casi di aggirare il criterio di Istio.

Se hai abilitato Istio su Google Kubernetes Engine (GKE), queste vulnerabilità
potrebbero riguardarti. **Ti consigliamo di eseguire l'upgrade dei cluster
interessati alla versione più recente della patch il prima possibile e di
eseguire l'upgrade dei file collaterali Istio (istruzioni di seguito).**

####  Che cosa devo fare?

**A causa della gravità di queste vulnerabilità, indipendentemente dal fatto
che siano abilitati o meno gli upgrade automatici dei nodi, ti consigliamo
di:**

  1. **[ Eseguire manualmente l'upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=it) del cluster non appena la patch diventa disponibile. **
  2. **Eseguire l'upgrade dei file collaterali secondo la[ documentazione per l'upgrade dei file collaterali ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) . **

Le versioni con patch saranno rese disponibili per tutti i progetti GKE prima
delle 19:00 PDT di oggi.

Questa patch sarà disponibile nelle versioni di GKE elencate di seguito. I
nuovi cluster useranno la versione con patch per impostazione predefinita
quando annunciato sulla pagina dei bollettini sulla sicurezza di GKE
(prevediamo il 15 aprile 2019); se crei un nuovo cluster prima di allora, devi
specificare la versione con patch da utilizzare. Per i clienti di GKE che
hanno abilitato gli [ upgrade automatici dei nodi
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=it) e che non eseguono l'upgrade manuale, l'upgrade dei nodi alle
versioni con patch verrà eseguito automaticamente la settimana prossima.

Versioni con patch:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua le seguenti vulnerabilità:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) e [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Puoi scoprire
di più sul [ blog di Istio. ](https://istio.io/blog/2019/announcing-1.1.2)

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 marzo 2019

Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 22/03/2019:** questa patch è disponibile in Kubernetes
1.11.8-gke.4, 1.13.4-gke.1 e release successive. La patch non è ancora
disponibile in 1.12. Traccia la disponibilità di questa patch nelle [ note di
rilascio ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#march_19_2019) .

Kubernetes ha recentemente scoperto una nuova vulnerabilità denial of service,
[ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , che permette a un utente autorizzato
a eseguire richieste di patch di creare una richiesta "json-patch" dannosa,
che consuma quantità eccessive di CPU e memoria nel server API Kubernetes ed è
in grado di ridurre la disponibilità del piano di controllo del cluster. Per
ulteriori dettagli, consulta la [ divulgazione di Kubernetes
](https://groups.google.com/forum/?hl=it#!topic/kubernetes-
announce/vmUUNkYfG9g) . **Tutti i master Google Kubernetes Engine (GKE) sono
interessati da queste vulnerabilità. Una versione patch imminente includerà
una mitigazione per questa vulnerabilità. Eseguiremo automaticamente l'upgrade
dei master dei cluster alla versione con patch nelle prossime settimane,
secondo la regolare cadenza degli upgrade.**

####  Che cosa devo fare?

**Non è richiesta alcuna azione da parte tua. L'upgrade dei master GKE verrà
eseguito automaticamente secondo la regolare cadenza degli upgrade.** Se vuoi
eseguire l'upgrade del master prima di questo momento, puoi [ avviare
manualmente un upgrade del master ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=it#upgrading_the_cluster) .

Questo bollettino verrà aggiornato con le versioni contenenti una patch. Nota
che la patch sarà disponibile solo nelle versioni 1.11+, non in 1.10.

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

La vulnerabilità [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) permette a un utente di creare una
speciale patch di tipo "json-patch" che consuma quantità eccessive di CPU nel
server API Kubernetes ed è in grado di ridurre la disponibilità del piano di
controllo del cluster.

|  Media  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 febbraio 2019 (runc)

Descrizione  |  Gravità  |  Note  
---|---|---  
  
La Open Containers Initiative (OCI) [ ha recentemente scoperto
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=it#!topic/dev/Tc1ELm-8oDI)
la nuova vulnerabilità di sicurezza [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) in runc, che
consente di uscire dai limiti del container per ottenere privilegi di utente
root sul nodo host.

**I tuoi nodi Google Kubernetes Engine (GKE) Ubuntu sono interessati da queste
vulnerabilità e ti consigliamo di[ eseguire l'upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=it) alla versione più recente della patch il prima possibile, come
descritto di seguito. **

####  Che cosa devo fare?

Per eseguire l'upgrade dei nodi, devi prima eseguire l'upgrade del master alla
versione più recente. Questa patch è disponibile in Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 e release successive. Traccia la
disponibilità di queste patch nelle [ note di rilascio
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#february-11-2019) .

Nota che solo i nodi Ubuntu in GKE sono interessati. I nodi che eseguono COS
non sono interessati.

Nota che la nuova versione di runc ha un maggiore utilizzo della memoria e può
richiedere l'aggiornamento della memoria allocata ai container se hai
impostato limiti di memoria bassi (< 16 MB).

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) descrive una vulnerabilità in runc che
permette a un container dannoso di sovrascrivere (con minima interazione
dell'utente sotto forma di file eseguibile) il file binario runc dell'host,
ottenendo così la possibilità di eseguire codice a livello di utente root sul
nodo host. I container non eseguiti come utente root non sono interessati.
Questa è classificata come vulnerabilità di gravità "Alta".

|  Alta  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 febbraio 2019 (Go)

Descrizione  |  Gravità  |  Note  
---|---|---  
  
**Aggiornamento 25/02/2019:** la patch non è disponibile in 1.11.7-gke.4 come
comunicato in precedenza. Se esegui 1.11.7, puoi: eseguire il downgrade a
1.11.6, eseguire l'upgrade a 1.12 o attendere fino alla prossima patch per
1.11.7, disponibile nella settimana del 4/03/2019.

Nel linguaggio di programmazione Go è stata recentemente scoperta una nuova
vulnerabilità di sicurezza, [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) , una vulnerabilità DoS (denial of
service) nelle implementazioni di crittografia ellittica delle curve
ellittiche P-521 e P-384. In Google Kubernetes Engine (GKE), questo potrebbe
permettere a un utente di creare richieste dannose che consumano quantità
eccessive di CPU nel server API Kubernetes, fino a ridurre la disponibilità
del piano di controllo del cluster. Per ulteriori dettagli, consulta la [
divulgazione sul linguaggio di programmazione Go
](https://groups.google.com/forum/?hl=it#!topic/golang-announce/mVeX35iXuSw) .

**Tutti i master Google Kubernetes Engine (GKE) sono interessati da queste
vulnerabilità. La[ versione più recente della patch
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#february-11-2019) include una mitigazione per questa
vulnerabilità. Eseguiremo automaticamente l'upgrade dei master dei cluster
alla versione con patch nelle prossime settimane, secondo la regolare cadenza
degli upgrade. **

####  Che cosa devo fare?

**Non è richiesta alcuna azione da parte tua. L'upgrade dei master GKE verrà
eseguito automaticamente secondo la regolare cadenza degli upgrade.** Se vuoi
eseguire l'upgrade del master prima di questo momento, puoi [ avviare
manualmente un upgrade del master ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=it#upgrading_the_cluster) .

Questa patch è disponibile in GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 e release successive.

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

CVE-2019-6486 è una vulnerabilità nelle implementazioni di crittografia
ellittica delle curve ellittiche P-521 e P-384. Questo può permettere a un
utente di creare input che consumano quantità eccessive di CPU.

|  Alta  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 dicembre 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Kubernetes ha recentemente scoperto una nuova vulnerabilità della sicurezza [
CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , che consente a un utente con
privilegi relativamente bassi di ignorare l'autorizzazione alle API di
kubelet, offrendo la possibilità di eseguire operazioni arbitrarie per
qualsiasi pod su qualsiasi nodo nel cluster. Per ulteriori dettagli, consulta
la [ divulgazione di Kubernetes
](https://groups.google.com/forum/?hl=it#!topic/kubernetes-
announce/GVllWCg6L88) . **Tutti i master di Google Kubernetes Engine (GKE)
sono stati interessati da queste vulnerabilità e abbiamo già eseguito
l'upgrade dei cluster alle[ versioni patch più recenti
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#november-12-2018) . Non è richiesta alcuna azione da parte tua. **

####  Che cosa devo fare?

**Non è richiesta alcuna azione da parte tua. L'upgrade dei master GKE è già
stato eseguito.**

Questa patch è disponibile in GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, 1.11.2-gke.18 e release successive.

####  Quale vulnerabilità viene affrontata da questa patch?

La patch attenua la seguente vulnerabilità:

La vulnerabilità CVE-2018-1002105 consente a un utente con privilegi
relativamente bassi di ignorare l'autorizzazione alle API di kubelet. Ciò
consente a un utente autorizzato a inoltrare richieste aggiornabili di
riassegnare ed eseguire chiamate arbitrarie all'API di kubelet. Questa è
classificata come vulnerabilità di gravità "Critica" in Kubernetes. Dati
alcuni dettagli nell'implementazione di GKE che hanno impedito il percorso di
escalation non autenticato, questa è classificata come vulnerabilità di
gravità "Alta".

|  Alta  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 novembre 2018

Descrizione  
---  
  
**Aggiornamento 16/11/2018:** la revoca e la rotazione di tutti i token
potenzialmente interessati è completa. Non sono necessarie ulteriori azioni.

Recentemente Google ha rilevato un problema nel plug-in Container Network
Interface (CNI) di Calico che può, in alcune configurazioni, registrare
informazioni sensibili. Questo problema è monitorato dal Tigera Technical
Advisory [ TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/) .

  * Quando si esegue la registrazione a livello di debug, il plug-in CNI di Calico scriverà la configurazione del client API di Kubernetes nei log. 
  * La CNI di Calico scriverà anche il token dell'API di Kubernetes nei log a livello di informazioni se il campo "k8s_auth_token" è impostato sulla configurazione di rete CNI. 
  * Inoltre, quando si esegue la registrazione a livello di debug, se il token dell'account di servizio è impostato in modo esplicito, nel file di configurazione Calico letto da Calico o come variabili di ambiente utilizzate da Calico, i componenti Calico (calico/nodo, felix, CNI) scriveranno queste informazioni nei file di log. 

Questi token hanno le seguenti autorizzazioni:  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
I cluster di Google Kubernetes Engine con criterio per la rete di cluster e
abilitati per Stackdriver Logging, hanno registrato i token dell'account di
servizio Calico in Stackdriver. I cluster senza criterio di rete abilitato non
sono interessati.

Abbiamo eseguito il deployment di una correzione che esegue la migrazione del
plug-in CNI di Calico per accedere solo a livello di avviso e utilizzare un
nuovo account di servizio. Il deployment del codice Calico a cui è stata
applicata la patch sarà eseguito in una versione successiva.

Nel corso della prossima settimana, effettueremo una revoca progressiva di
tutti i token potenzialmente interessati. Questo bollettino verrà aggiornato
al termine della revoca. **Non sono richieste altre operazioni da parte tua.**
(Questa rotazione è stata completata in data 16/11/2018)

Se desideri ruotare immediatamente questi token, puoi eseguire il comando
riportato di seguito, il nuovo secret per l'account di servizio dovrebbe
essere ricreato automaticamente in pochi secondi:  
      
    
    
    kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system
            
  
---  
  
####  Rilevamento

GKE registra tutti gli accessi al server API. Per determinare se un token
Calico è stato utilizzato al di fuori dell'intervallo IP previsto da Google
Cloud, è possibile eseguire la seguente query Stackdriver. Ti preghiamo di
notare che questo restituirà solo i record per le chiamate effettuate dalla
rete esterna di GCP. Dovresti personalizzarlo secondo le necessità del tuo
ambiente specifico.  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  14 agosto 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
[ Intel ha divulgato ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) i seguenti CVE:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (per [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (per sistemi operativi e [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (per virtualizzazione) 

Questi CVE vengono denominati collettivamente "L1 Terminal Fault (L1TF)".

Queste vulnerabilità L1TF sfruttano l'esecuzione speculativa attaccando la
configurazione delle strutture di dati a livello di processore. "L1" si
riferisce alla cache dei dati di livello 1 (L1D), una piccola risorsa on-core
utilizzata per accelerare l'accesso alla memoria.

Leggi il [ post del blog di Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=it) per ulteriori dettagli su queste
vulnerabilità e sulle mitigazioni di Compute Engine.

####  Impatto su Google Kubernetes Engine

L'infrastruttura che esegue Kubernetes Engine e isola i cluster e i nodi dei
clienti l'uno dall'altro è protetta dagli attacchi noti.

I pool di nodi di Kubernetes Engine che utilizzano l'immagine Container-
Optimized OS di Google e che hanno l' [ upgrade automatico
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=it) attivato verranno automaticamente aggiornati alla versione con
patch della nostra immagine COS non appena diventeranno disponibili a partire
dalla settimana del 20/08/2018.

I pool di nodi di Kubernetes Engine che non hanno abilitato l' [ upgrade
automatico ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=it) devono essere [ aggiornati manualmente
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=it) non appena le versioni con patch della nostra
immagine COS diventano disponibili.

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 agosto 2018; ultimo aggiornamento: 5 settembre 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Aggiornamento 05/09/2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) è stato recentemente divulgato. Come con [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
, si tratta di una vulnerabilità di rete a livello di kernel che aumenta
l'efficacia degli attacchi DoS (denial of service) contro i sistemi
vulnerabili. La principale differenza è che CVE-2018-5391 è sfruttabile su
connessioni IP. Abbiamo aggiornato questo bollettino per coprire entrambe le
vulnerabilità.

####  Descrizione

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") descrive una
vulnerabilità di rete a livello di kernel che aumenta l'efficacia degli
attacchi DoS (denial of service) contro i sistemi vulnerabili tramite le
connessioni TCP.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") descrive una
vulnerabilità di rete a livello di kernel che aumenta l'efficacia degli
attacchi DoS (denial of service) contro i sistemi vulnerabili tramite le
connessioni IP.

####  Impatto su Google Kubernetes Engine

A partire dall'11/08/2018, tutti i master di Kubernetes Engine sono protetti
da entrambe le vulnerabilità. Inoltre, anche tutti i cluster di Kubernetes
Engine che sono configurati per l'aggiornamento automatico sono protetti da
entrambe le vulnerabilità. I pool di nodi di Kubernetes Engine che non sono
configurati per l' [ aggiornamento automatico
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=it) e che sono stati aggiornati manualmente prima dell'11/08/2018
sono interessati da entrambe le vulnerabilità.

####  Versioni con patch

A causa della gravità di questa vulnerabilità, si consiglia di [ eseguire
manualmente l'upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=it#upgrading-nodes) dei nodi non appena la patch
sarà disponibile.

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 maggio 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Recentemente è stata scoperta una vulnerabilità in Git che potrebbe consentire
l'escalation dei privilegi in Kubernetes se agli utenti senza privilegi è
consentito creare pod con volumi gitRepo. Il CVE è identificato con il tag [
CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  Mi riguarda?

Questa vulnerabilità influisce su di te se tutte le seguenti condizioni sono
vere:

  * Gli utenti non attendibili possono creare pod (o attivare la creazione di pod). 
  * I pod creati da utenti non attendibili dispongono di restrizioni che impediscono di accedere come utente root all'host (ad esempio tramite [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=it) ). 
  * I pod creati da utenti non attendibili sono autorizzati a utilizzare il tipo di volume gitRepo. 

Tutti i nodi di Kubernetes Engine sono vulnerabili.

####  Che cosa devo fare?

Vieta l'uso del tipo di volume gitRepo. Per vietare volumi gitRepo con
PodSecurityPolicy, ometti ` gitRepo ` dalla whitelist ` volumes ` in
PodSecurityPolicy.

Il comportamento equivalente del volume gitRepo può essere ottenuto clonando
un repository git in un volume EmptyDir da un initContainer:

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  Quale patch affronta questa vulnerabilità?

Una patch verrà inclusa in un'imminente release di Kubernetes Engine. Torna a
controllare questa pagina per ulteriori dettagli.

|  Media  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 maggio 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Diverse vulnerabilità sono state recentemente scoperte nel kernel di Linux;
questo potrebbe consentire l'escalation dei privilegi o il denial of service
(tramite arresto del kernel) da un processo senza privilegi. Questi CVE sono
identificati dai tag [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) e [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
. Tutti i nodi di Kubernetes Engine sono interessati da queste vulnerabilità e
ti consigliamo di [ eseguire l'upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=it) alla versione più
recente della patch, come descritto di seguito.

####  Che cosa devo fare?

Per eseguire l'upgrade, è necessario prima aggiornare il master alla versione
più recente. Questa patch è disponibile in Kubernetes Engine 1.8.12-gke.1,
Kubernetes Engine 1.9.7-gke.1 e Kubernetes Engine 1.10.2-gke.1. Queste release
includono patch sia per Container-Optimized OS sia per immagini Ubuntu.

Se crei un nuovo cluster prima di allora, devi specificare la versione con
patch da utilizzare. I clienti che hanno abilitato gli [ aggiornamenti
automatici dei nodi ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=it) e che non effettuano
l'aggiornamento manuale avranno i loro nodi aggiornati alle versioni con patch
nelle prossime settimane.

####  Quali vulnerabilità vengono affrontate da questa patch?

La patch attenua le seguenti vulnerabilità:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : questa vulnerabilità interessa il
kernel di Linux. Consente a un utente o processo senza privilegi di arrestare
il kernel di sistema, causando un attacco DoS o un'escalation dei privilegi.
Questa è classificata come vulnerabilità di gravità "Alta", con un CVSS di
7,8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : questa vulnerabilità interessa il kernel
di Linux. Consente a un utente o processo senza privilegi di arrestare il
kernel di sistema, causando un attacco DoS. Questa è classificata come
vulnerabilità di gravità "Media", con un CVSS di 6,5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : questa vulnerabilità interessa
l'hypervisor KVM del kernel Linux. Ciò consente a un processo senza privilegi
di arrestare il kernel ospite o potenzialmente di ottenere privilegi. A questa
vulnerabilità viene applicata una patch nell'infrastruttura in cui viene
eseguito Kubernetes Engine, pertanto Kubernetes Engine non è interessato.
Questa è classificata come vulnerabilità di gravità "Alta", con un CVSS di
8,0.

|  Alta  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 marzo 2018

Descrizione  |  Gravità  |  Note  
---|---|---  
  
Il progetto Kubernetes ha [ recentemente divulgato
](https://groups.google.com/forum/?hl=it#!topic/kubernetes-security-
announce/P7lBjbjDKd8) nuove vulnerabilità di sicurezza, [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) e [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , che consentono ai container di accedere
ai file all'esterno del container. Tutti i nodi di Kubernetes Engine sono
interessati da queste vulnerabilità e ti consigliamo di eseguire
l'aggiornamento alla versione più recente della patch il prima possibile, come
descritto di seguito.

####  Che cosa devo fare?

A causa della gravità di queste vulnerabilità, indipendentemente dal fatto che
siano abilitati o meno gli upgrade automatici dei nodi, ti consigliamo di [
eseguire manualmente l'upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=it) dei nodi non appena la
patch diventa disponibile. La patch sarà disponibile per tutti i clienti entro
il 16 marzo, ma potrebbe essere disponibile in anteprima per te in base alla
zona in cui si trova il tuo cluster, secondo la [ programmazione di release
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=it#march-12-2018) .

Per eseguire l'upgrade, è necessario prima aggiornare il master alla versione
più recente. Questa patch sarà disponibile in Kubernetes 1.9.4-gke.1,
Kubernetes 1.8.9-gke.1 e Kubernetes 1.7.14-gke.1. I nuovi cluster useranno la
versione con patch per impostazione predefinita entro il 30 marzo; se crei un
nuovo cluster prima di allora, devi specificare la versione con patch da
utilizzare.

Per i clienti di Kubernetes Engine che hanno abilitato gli [ upgrade
automatici dei nodi ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=it) e che non eseguono l'upgrade
manuale, l'upgrade dei nodi alle versioni con patch verrà eseguito
automaticamente entro il 23 aprile. Tuttavia, a causa della natura della
vulnerabilità, ti consigliamo di [ eseguire manualmente l'upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=it) dei nodi non appena la patch diventa disponibile.

####  Quali vulnerabilità vengono affrontate da questa patch?

La patch attenua le due seguenti vulnerabilità:

La vulnerabilità CVE-2017-1002101 consente ai container che utilizzano i
montaggi di volume del [ sottopercorso
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) di
accedere ai file al di fuori del volume. Ciò significa che se stai bloccando
l'accesso del container ai volumi hostpath con PodSecurityPolicy, un utente
malintenzionato con la possibilità di aggiornare o creare pod può montare
qualsiasi hostpath utilizzando qualsiasi altro tipo di volume.

La vulnerabilità CVE-2017-1002102 consente ai container che utilizzano
determinati tipi di volume, inclusi secret, mappe di configurazione, volumi
previsti o volumi API Downward, di eliminare file al di fuori del volume. Ciò
significa che se un container che utilizza uno di questi tipi di volume è
compromesso, oppure se consenti a utenti non attendibili di creare pod, un
utente malintenzionato potrebbe utilizzare quel container per eliminare file
arbitrari sull'host.

Per saperne di più sulla correzione, leggi il [ post del blog Kubernetes
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
.

|  Alta  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

