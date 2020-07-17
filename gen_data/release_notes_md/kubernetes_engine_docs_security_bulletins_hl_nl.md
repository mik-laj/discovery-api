#  Beveiligingsbulletins

Alle beveiligingsbulletins voor Google Kubernetes Engine (GKE) worden in dit
onderwerp beschreven.

Kwetsbaarheden worden vaak onder embargo gehouden tot de betrokken partijen de
kans hebben gehad om ze aan te pakken. In deze gevallen hebben de [ release-
opmerkingen ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl) van GKE betrekking op 'beveiligingsupdates' totdat het embargo is
opgeheven. Op dat moment worden de opmerkingen geüpdatet met de kwetsbaarheid
die door de patch is verholpen.

**Opmerking:** Lees deze bulletins vooral goed door als u multi-tenant
productietaken op GKE uitvoert, omdat deze kwetsbaarheden vaak meer impact
hebben op dergelijke productietaken. Zie [ Isolatie op verschillende lagen van
de Kubernetes-stack ](https://cloudplatform.googleblog.com/2018/05/Exploring-
container-security-Isolation-at-different-layers-of-the-Kubernetes-stack.html)
voor een technische beschrijving van beveiligingsgrenzen in GKE en hoe deze
van invloed zijn op productietaken.

Voeg de URL van deze pagina aan uw [ feedlezer
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) toe of voeg de
feed-URL rechtstreeks toe om de nieuwste beveiligingsbulletins te ontvangen: `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `

##  GCP-2020-007

**Gepubliceerd:** 01-06-2020  
Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Onlangs is in Kubernetes een kwetsbaarheid van het type Server Side Request
Forgery (SSRF), [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) , ontdekt waardoor bepaalde gemachtigde
gebruikers tot 500 bytes aan gevoelige informatie kunnen lekken van het
hostnetwerk van het besturingsvlak. Het GKE-besturingsvlak (Google Kubernetes
Engine) gebruikt controllers van Kubernetes en is dus getroffen door deze
kwetsbaarheid. We raden u aan het besturingsvlak te [ upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=nl) naar de nieuwste patchversie, zoals hieronder wordt
beschreven. Een node-upgrade is niet vereist.  

####  Wat moet ik doen?

De meeste klanten hoeven verder niets te doen. Het merendeel van de clusters
heeft al een gepatchte versie. De volgende GKE-versies of nieuwer bevatten de
oplossing voor deze kwetsbaarheid:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Clusters met [ releasekanalen ](https://cloud.google.com/kubernetes-
engine/docs/concepts/release-channels?hl=nl) voeren al besturingsvlakversies
met de oplossing uit.

####  Welke kwetsbaarheid wordt door deze patch verholpen?

Deze patches pakken de kwetsbaarheid CVE-2020-8555 aan. Dit wordt beoordeeld
als een gemiddelde kwetsbaarheid voor GKE, omdat het moeilijk te misbruiken
was vanwege de verschillende versterkingsmaatregelen voor het besturingsvlak.

Een aanvaller met toestemming om een pod met bepaalde ingebouwde volumetypen
(GlusterFS, Quobyte, StorageFS, ScaleIO) of een StorageClass te maken, kan `
kube-controller-manager ` ` GET ` -verzoeken of ` POST ` -verzoeken laten
uitvoeren _zonder_ een door de aanvaller gecontroleerd tekstgedeelte van het
verzoek van het hostnetwerk van de hoofdinstantie. Deze volumetypen worden
zelden gebruikt op GKE, dus nieuw gebruik van deze volumetypen kan een nuttig
detectiesignaal zijn.

In combinatie met de mogelijkheid om de resultaten van de ` GET/POST ` terug
naar de aanvaller te lekken, bijvoorbeeld via logboeken, kan dit leiden tot
openbaarmaking van gevoelige informatie. We hebben de desbetreffende
opslagdrivers geüpdatet om het potentiële risico op dergelijke lekken weg te
nemen.

|

Gemiddeld

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Gepubliceerd:** 01-06-2020  
Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Kubernetes heeft bekendgemaakt dat er een [ kwetsbaarheid
](https://github.com/kubernetes/kubernetes/issues/91507) is waardoor een
gemachtigde container node-verkeer kan omleiden naar een andere container.
Wederzijds TLS/SSH-verkeer, zoals tussen de kubelet en de API-server of
verkeer van apps die mTLS gebruiken, kunnen niet worden gelezen of gewijzigd
door deze aanval. Deze kwetsbaarheid geldt voor alle GKE-nodes (Google
Kubernetes Engine). We raden u aan een [ upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl) uit te voeren naar de nieuwste patchversie, zoals hieronder
beschreven.

####  Wat moet ik doen?

[ Upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-cluster?hl=nl) uw besturingsvlak en vervolgens uw nodes naar een van de
gepatchte versies hieronder om deze kwetsbaarheid op te lossen. Clusters op
releasekanalen voeren al een gepatchte versie op het besturingsvlak en de
nodes uit

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Voor zeer weinig containers is ` CAP_NET_RAW ` vereist. Deze en andere
krachtige functies moeten standaard worden geblokkeerd via [ PodSecurityPolicy
](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-
policies?hl=nl) of [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=nl) :

  * Verwijder de ` CAP_NET_RAW ` -functionaliteit uit containers: 
    * Door het af te dwingen via [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=nl) met: 
        
                
        # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * Of door Anthos Policy Controller/Gatekeeper te gebruiken met deze [ beperkingentemplate ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) en deze toe te passen. bijvoorbeeld: 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * Of door uw pod-specificaties te updaten: 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch verhelpt de volgende kwetsbaarheid:

De kwetsbaarheid beschreven in [ Kubernetes-probleem 91507
](https://github.com/kubernetes/kubernetes/issues/91507) ` CAP_NET_RAW `
-functie (die is inbegrepen in de standaard functieset voor containers) om op
schadelijke wijze de IPv6-stack op de node te configureren en node-verkeer
naar de door de aanvaller beheerde container om te leiden. Hierdoor kan de
aanvaller verkeer van of naar de node onderscheppen/aanpassen. Wederzijds
TLS/SSH-verkeer, zoals tussen de kubelet en de API-server of verkeer van apps
met mTLS, kunnen niet worden gelezen of aangepast door deze aanval.

|

Gemiddeld

|

[ Kubernetes-probleem 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**Gepubliceerd:** 07-05-2020  
**Geüpdatet:** 07-05-2020  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
In de Linux-kernel is onlangs een kwetsbaarheid ontdekt, zoals beschreven in [
CVE-2020-8835 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835)
. Hierdoor kan containerescape rootrechten krijgen op de host-node.

Deze kwetsbaarheid is van toepassing op Ubuntu-nodes in Google Kubernetes
Engine (GKE) die GKE 1.16 of 1.17 uitvoeren. We raden u aan zo snel mogelijk
te upgraden naar de nieuwste patchversie, zoals hieronder beschreven.

Nodes die Container-Optimized OS uitvoeren, worden niet beïnvloed. Nodes die
op GKE On-Prem worden uitgevoerd, worden niet beïnvloed.

####  Wat moet ik doen?

**De meeste klanten hoeven verder niets te doen. Alleen nodes die Ubuntu in
GKE-versie 1.16 of 1.17 uitvoeren, worden beïnvloed.**

Als u uw nodes wilt upgraden, moet u eerst uw hoofdinstantie naar de nieuwste
versie upgraden. Deze patch wordt beschikbaar gesteld in Kubernetes
1.16.8-gke.12, 1.17.4-gke.10 en nieuwere releases. Monitor de beschikbaarheid
van deze patches in de [ release-opmerkingen
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=nl) .

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) beschrijft een kwetsbaarheid in Linux-
kernelversie 5.5.0 en nieuwer waarmee een kwaadaardige container (met minimale
gebruikersinteractie in de vorm van een exec) kernelgeheugen kan lezen en
schrijven en zo code-uitvoering op hoofdniveau op de host-node kan verkrijgen.
Dit wordt beoordeeld als een ernstige kwetsbaarheid.

|

Hoog

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Gepubliceerd:** 31-03-2020  
**Geüpdatet:** 31-03-2020  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Onlangs is in Kubernetes een kwetsbaarheid ontdekt, zoals beschreven in [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , waardoor gebruikers die gemachtigd zijn
om POST-verzoeken in te dienen, op afstand een DoS-aanval (denial of service)
op een Kubernetes API-server kunnen uitvoeren. Het Product Security Committee
(PSC) van Kubernetes heeft aanvullende informatie over deze kwetsbaarheid
vrijgegeven. Deze kunt u [ hier
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/wuwEwZigXBc) vinden.

GKE-clusters die [ gemachtigde hoofdnetwerken
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=nl) en [ privéclusters zonder openbaar eindpunt
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=nl#private_master) gebruiken, hebben geen last van deze
kwetsbaarheid.

####  Wat moet ik doen?

We raden u aan uw cluster te upgraden naar een patchversie met de oplossing
voor deze kwetsbaarheid.

De patchversies die de oplossing bevatten, worden hieronder weergegeven:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Welke kwetsbaarheden worden door deze patch verholpen?

Deze patch bevat de oplossing voor de volgende DoS-kwetsbaarheid (denial of
service):

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Gemiddeld

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Gepubliceerd:** 23-03-2020  
**Geüpdatet:** 23-03-2020  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Kubernetes heeft [ twee DoS-kwetsbaarheden (denial of service)
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/2UOlsba2g0s) bekendgemaakt: een die van toepassing is op de API-
server en een die van toepassing is op Kubelets. Raadpleeg voor meer
informatie de Kubernetes-problemen [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) en [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  Wat moet ik doen?

Alle gebruikers van GKE zijn beschermd tegen CVE-2020-8551, tenzij niet-
vertrouwde gebruikers verzoeken kunnen verzenden binnen het interne netwerk
van het cluster. Het gebruik van [ gemachtigde hoofdnetwerken
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=nl) is ook een oplossing voor CVE-2020-8552.

####  Wanneer worden deze gepatcht?

Patches voor CVE-2020-8551 vereisen een node-upgrade. De patchversies die de
oplossing bevatten, worden hieronder weergegeven:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Opmerking: De kwetsbaarheid geldt niet voor versie 1.14.x en lager. Voor deze
versies zijn dus geen patches vereist.

Patches voor CVE-2020-8552 vereisen een hoofdupgrade. De patchversies die de
oplossing bevatten, worden hieronder weergegeven:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Gemiddeld

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 januari 2020, voor het laatst geüpdatet op 24 januari 2020

**Gepubliceerd:** 21-01-2020  
**Geüpdatet:** 24-01-2020  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update op 24-01-2020:** Het proces om gepatchte versies beschikbaar te
stellen, is gestart en wordt voltooid op 25 januari 2020.

* * *

Microsoft heeft bekendgemaakt dat er een kwetsbaarheid is in de Windows Crypto
API en de bijbehorende validatie van handtekeningen van elliptische curven.
Bekijk de [ kennisgeving van Microsoft ](https://portal.msrc.microsoft.com/en-
US/security-guidance/advisory/CVE-2020-0601) voor meer informatie.

**Wat moet ik doen?**

**De meeste klanten hoeven verder niets te doen. Dit heeft alleen impact op
nodes die op Windows Server worden uitgevoerd.**

Klanten die Windows Server-nodes gebruiken, moeten zowel de nodes als de
containerproductietaken op deze nodes updaten naar gepatchte versies om deze
kwetsbaarheid op te lossen.

**Doe het volgende om de containers te updaten:**

Ontwerp uw containers opnieuw met de nieuwste basiscontainerimages van
Microsoft. Selecteer een [ servercore ](https://hub.docker.com/_/microsoft-
windows-servercore) \- of [ nanoserver ](https://hub.docker.com/_/microsoft-
windows-nanoserver) -tag met een 'LastUpdated Time' van 14-01-2020 of later.

**Doe het volgende om de nodes te updaten:**

Het proces om gepatchte versies beschikbaar te stellen, is al gestart en wordt
voltooid op 24 januari 2020.

U zou tot dan kunnen wachten en vervolgens een node-upgrade uitvoeren naar een
gepatchte GKE-versie of u kunt Windows Update gebruiken om wanneer u maar wilt
de nieuwste Windows-patch handmatig te implementeren.

De patchversies die de oplossing bevatten, worden hieronder weergegeven:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Welke kwetsbaarheden worden door deze patch verholpen?**

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- Deze kwetsbaarheid staat ook wel bekend
als de [ Windows Crypto API Spoofing Vulnerability
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) . Door deze kwetsbaarheid kan een aanvaller
schadelijke uitvoerbare bestanden vertrouwd laten lijken of man-in-the-middle-
aanvallen uitvoeren en vertrouwelijke informatie ontsleutelen op TLS-
verbindingen met de getroffen software.

|

NVD-basisscore: 8,1 (hoog)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 november 2019

**Gepubliceerd:** 14-11-2019  
**Geüpdatet:** 14-11-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Kubernetes heeft een beveiligingsprobleem bekendgemaakt in de kubernetes-csi [
` external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) -, [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) \- en [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer) -sidecars dat van
toepassing is op de meeste versies van de sidecars die zijn gebundeld in [
CSI-stuurprogramma's (Container Storage Interface) ](https://kubernetes-
csi.github.io/docs/drivers.html) . Bekijk de [ kennisgeving van Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) voor meer informatie.

**Wat moet ik doen?**  
**Deze kwetsbaarheid heeft geen invloed op beheerde GKE-componenten** . Het
kan op u van toepassing zijn als u uw eigen CSI-stuurprogramma's beheert in [
GKE-alfaclusters ](https://cloud.google.com/kubernetes-
engine/docs/concepts/alpha-clusters?hl=nl) waarop GKE versie 1.12 of hoger
wordt uitgevoerd. Raadpleeg de leverancier van uw CSI-stuurprogramma voor
upgrade-instructies als dit voor u geldt.

**Welke kwetsbaarheden worden door deze patch verholpen?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : deze CVE is een kwetsbaarheid in de `
kubernetes-csi ` [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) -, [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) \- en [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) -sidecars
waardoor ongeoorloofde gegevenstoegang of -mutatie kan plaatsvinden. Dit is
van toepassing op de meeste versies van de sidecars die zijn gebundeld in [
CSI-stuurprogramma's ](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Gemiddeld

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 november 2019

**Gepubliceerd:** 12-11-2019  
**Geüpdatet:** 12-11-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Intel heeft CVE's bekendgemaakt die mogelijk interacties tussen speculatieve
uitvoering en de microarchitecturale staat toestaan, waardoor gegevens
openbaar gemaakt kunnen worden. Bekijk de [ kennisgeving van Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) voor meer informatie.

**De hostinfrastructuur waarop Kubernetes Engine wordt uitgevoerd, scheidt
productietaken van klanten. U hoeft geen actie te ondernemen, tenzij u niet-
vertrouwde code binnen uw multi-tenant GKE-clusters uitvoert _en_ N2-, M2- of
C2-nodes gebruikt. ** Voor GKE-instanties op N1-nodes is geen nieuwe actie
vereist.

Als u Anthos GKE uitvoert met een implementatie op locatie, is de
openbaarmaking afhankelijk van de hardware. Vergelijk uw infrastructuur met de
[ kennisgeving van Intel ](https://blogs.intel.com/technology/2019/11/ipas-
november-2019-intel-platform-update-ipu/) .

####  Wat moet ik doen?

**Dit is alleen op u van toepassing als u node-pools gebruikt met N2-, M2- of
C2-nodes _en_ als die nodes niet-vertrouwde code binnen uw eigen multi-tenant
GKE-clusters uitvoeren. **

**Start uw nodes opnieuw op om de patch toe te passen.** De gemakkelijkste
manier om alle nodes in uw node-pool opnieuw op te starten is door de [
upgradebewerking ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=nl#upgrade_nodes) te gebruiken om een herstart voor
de getroffen node-pool te forceren.  

Opmerking: U hoeft tijdens een upgrade niet van versie te veranderen. Met de `
cluster-version ` -vlag kunt u een upgrade van dezelfde node-versie starten.

####  Welke kwetsbaarheden worden door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: deze CVE staat ook bekend als TSX Async Abort (TAA). TAA biedt een andere
mogelijkheid voor gegevensonderschepping via dezelfde microarchitecturale
gegevensstructuren waarvan [ Microarchitectural Data Sampling (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=nl#may-14-2019) misbruik heeft gemaakt.

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
Dit is een DoS-kwetsbaarheid (denial of service) die van invloed is op de
hosts van virtuele machines. Door deze kwetsbaarheid kunnen kwaadwillende
outsiders een onbeschermde host laten crashen. Deze CVE staat ook bekend als
'Machine Check Error on Page Size Change'. Dit is niet van toepassing op GKE.

|

Gemiddeld

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 oktober 2019

**Gepubliceerd:** 22-10-2019  
**Geüpdatet:** 22-10-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
In de programmeertaal Go is onlangs een kwetsbaarheid ontdekt, zoals
beschreven in [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . De kwetsbaarheid kan gevolgen hebben
voor Kubernetes-configuraties die gebruikmaken van een Authenticating Proxy.
Bekijk de [ kennisgeving van Kubernetes
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/PtsUCqFi4h4) voor meer informatie.

Kubernetes Engine staat geen configuratie van een Authenticating Proxy toe en
wordt dus niet beïnvloed door deze kwetsbaarheid.

|

Geen

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 oktober 2019

**Gepubliceerd:** 16-10-2019  
**Geüpdatet:** 24-10-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update 24-10-2019:** gepatchte versies zijn nu beschikbaar in alle zones.

* * *

Onlangs is in Kubernetes een kwetsbaarheid ontdekt, zoals beschreven in [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , waardoor gebruikers die gemachtigd zijn
om POST-verzoeken in te dienen, op afstand een DoS-aanval (denial of service)
op een Kubernetes API-server kunnen uitvoeren. Het Kubernetes Product Security
Committee (PSC) heeft aanvullende informatie over deze kwetsbaarheid
vrijgegeven, die [ hier
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/jk8polzSUxs) te vinden is.

GKE-clusters die [ geautoriseerde netwerken met hoofdtoegang
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=nl) gebruiken en [ privéclusters zonder openbaar eindpunt
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=nl#private_master) lossen deze kwetsbaarheid op.

######  Wat moet ik doen?

We raden u aan uw cluster te upgraden naar een patchversie die de oplossing
bevat, zodra deze beschikbaar is. We verwachten dat deze in alle zones
beschikbaar is bij de GKE-release die staat gepland voor de week van 14
oktober.

De patchversies die de oplossing bevatten, worden hieronder weergegeven.

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Welke kwetsbaarheden worden door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

CVE-2019-11253 is een DoS-kwetsbaarheid (denial of service).

|

Hoog

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 september 2019

**Gepubliceerd:** 16-09-2019  
**Geüpdatet:** 16-10-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Dit bulletin is na de oorspronkelijke publicatie geüpdatet.

In de programmeertaal Go zijn onlangs de nieuwe kwetsbaarheden [ CVE-2019-9512
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9512) en [
CVE-2019-9514 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
ontdekt. Dit zijn DoS-kwetsbaarheden (denial of service). Hierdoor kunnen
gebruikers in GKE kwaadwillende verzoeken indienen die buitensporige
hoeveelheden CPU in de Kubernetes API-server verbruiken, waardoor de
beschikbaarheid van het clusterbesturingsvlak mogelijk wordt verminderd.
Bekijk de [ kennisgeving van de programmeertaal Go
](https://groups.google.com/forum/?hl=nl#!topic/golang-announce/65QixT3tcmg)
voor meer informatie.

######  Wat moet ik doen?

We raden u aan uw cluster te upgraden naar de nieuwste patchversie met de
oplossing van deze kwetsbaarheid, zodra deze beschikbaar is. We verwachten dat
deze in alle zones beschikbaar is bij de volgende GKE-release, volgens het [
releaseschema ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#september_16_2019) .

De patchversies die de oplossing bevatten, worden hieronder weergegeven.

  * **Update 16 oktober 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) en [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) zijn DoS-
kwetsbaarheden (denial of service).

|

Hoog

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 september 2019

**Gepubliceerd:** 05-09-2019  
**Geüpdatet:** 05-09-2019

Het bulletin voor de oplossing voor de kwetsbaarheid uit het bulletin van  31
mei 2019  is geüpdatet.

##  22 augustus 2019

**Gepubliceerd:** 22-08-2019  
**Geüpdatet:** 22-08-2019

Het bulletin van  5 augustus 2019  is geüpdatet. De oplossing voor de
kwetsbaarheid die werd beschreven in het eerdere bulletin is [ beschikbaar
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#august_22_2019) .

##  8 augustus 2019

**Gepubliceerd:** 08-08-2019  
**Geüpdatet:** 08-08-2019

Het bulletin van  5 augustus 2019  is geüpdatet. We verwachten dat de
oplossing voor de kwetsbaarheid die in dat bulletin wordt beschreven in de
volgende versie van GKE beschikbaar is.

##  5 augustus 2019

**Gepubliceerd:** 05-08-2019  
**Geüpdatet:** 09-08-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Dit bulletin is na de oorspronkelijke publicatie geüpdatet.

Kubernetes heeft onlangs een kwetsbaarheid ontdekt, [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , waardoor
clustergewijze instanties van [ aangepaste resources
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) kunnen worden benut als naamruimteobjecten die in alle naamruimten
voorkomen. Dit betekent dat alle gebruikers- en serviceaccounts met alleen
RBAC-rechten op naamruimteniveau interactie kunnen hebben met clustergewijze
aangepaste resources. De aanvaller moet de juiste rechten hebben om toegang te
krijgen tot de resource in een naamruimte om deze kwetsbaarheid uit te buiten.

######  Wat moet ik doen?

We raden u aan uw cluster te [ upgraden ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=nl) naar de nieuwste patchversie met
de oplossing van deze kwetsbaarheid, zodra deze beschikbaar is. We verwachten
dat deze in alle zones beschikbaar is bij de volgende GKE-release. De
patchversies die de oplossing bevatten, worden hieronder weergegeven:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ versneld kanaal ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=nl) ) 

######  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch lost de volgende kwetsbaarheid op: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Gemiddeld

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 juli 2019

**Gepubliceerd:** 03-07-2019  
**Geüpdatet:** 03-07-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Een gepatchte versie van ` kubectl ` om CVE-2019-11246 te verhelpen is nu
beschikbaar in [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=nl#kubernetes_engine) .
Bekijk het  beveiligingsbulletin van 25 juni 2019  voor meer informatie.

**Opmerking:** De patch is niet beschikbaar in ` kubectl ` 1.11.10.

|

Hoog

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 juli 2019

**Gepubliceerd:** 25-06-2019  
**Geüpdatet:** 03-07-2019  Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
######  Update 3 juli 2019

Tijdens onze laatste update waren er nog geen patches voor de versies 1.11.9
en 1.11.10 beschikbaar. We hebben nu 1.11.10-gke.5 vrijgegeven als upgrade
voor beide 1.11-versies.

Op dit moment zijn de GKE-hoofdinstanties en de Google-infrastructuur waarop
Kubernetes Engine wordt uitgevoerd, gepatcht en beveiligd tegen deze
kwetsbaarheid.

De 1.11-hoofdinstanties worden binnenkort beëindigd en automatisch geüpgraded
naar 1.12 in de week van 8 juli 2019. U kunt een van de volgende aanbevolen
acties kiezen om nodes op een gepatchte versie te krijgen:

  * Voer de node-upgrade naar 1.11.10-gke.5 vóór 8 juli 2019 uit. Na deze datum worden de 1.11-versies verwijderd uit de beschikbare lijst met upgrades. 
  * Schakel [ automatische upgrades ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=nl) voor 1.11-nodes in en zorg ervoor dat ze worden geüpgraded als de hoofdstinstanties naar 1.12 worden geüpgraded. 
  * [ Upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=nl) de hoofdinstanties en de nodes handmatig naar een 1.12-versie waarin het probleem is verholpen. 

Het oorspronkelijke bulletin van 24 juni 2019 volgt:

* * *

######  Update 24 juni 2019

Op 22-06-2019 21:40 UTC hebben we de volgende gepatchte versie van Kubernetes
vrijgegeven. Hoofdinstanties tussen Kubernetes-versie 1.11.0 en 1.13.6 worden
automatisch geüpdatet naar een gepatchte versie. Upgrade naar een compatibele
hoofdversie (zie hieronder) voordat u uw nodes upgradet, als u een versie
uitvoert die niet is met deze patch.

**Vanwege de ernst van deze kwetsbaarheden raden we aan uw nodes en
hoofdinstanties zo snel mogelijk[ handmatig te upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=nl) , of het automatisch upgraden van nodes nu is
ingeschakeld of niet. **

De gepatchte versies:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Het oorspronkelijke bulletin van 18 juni 2019 volgt:

* * *

Netflix heeft onlangs drie TCP-kwetsbaarheden in Linux-kernels bekendgemaakt:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Deze CVE's worden gezamenlijk [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) genoemd.

Niet-gepatchte Linux-kernels kunnen kwetsbaar zijn voor een op afstand
uitgevoerde DoS-aanval. **Dit geldt voor nodes van Google Kubernetes Engine
die niet-vertrouwd netwerkverkeer verzenden of ontvangen. We raden u aan de
risicobeperkende stappen hieronder te volgen om uw productietaken te
beschermen.**

######  Kubernetes-hoofdinstanties

  * Dit is niet van toepassing op Kubernetes-hoofdinstanties die [ geautoriseerde netwerken ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=nl) gebruiken om het verkeer naar vertrouwde netwerken te beperken. 

  * Hoofdinstanties voor GKE-clusters die door Google worden beheerd, worden in de komende dagen automatisch gepatcht. Er is geen actie van de klant vereist. 

######  Kubernetes-nodes

Dit geldt niet voor nodes die het verkeer naar vertrouwde netwerken beperken.
Dit is een cluster met het volgende:

  * Nodes die via een firewall afkomstig zijn van niet-vertrouwde netwerken of nodes zonder openbaar IP-adres ( [ privéclusters ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=nl) ) 
  * Clusters zonder openbare LoadBalancer Services 

Google is bezig met een permanente oplossing voor deze kwetsbaarheden. Deze
oplossing zal als nieuwe node-versie beschikbaar worden gesteld. We zullen dit
bulletin updaten en een e-mail naar alle GKE-klanten sturen zodra de
permanente oplossing beschikbaar is.

Tot die tijd hebben we een Kubernetes DaemonSet gemaakt die oplossingen
implementeert door de ` iptables ` -hostconfiguratie aan te passen.

#####  Wat moet ik doen?

Pas de Kubernetes DaemonSet toe op alle nodes in uw cluster door de volgende
opdracht uit te voeren. Hiermee voegt u een ` iptables ` -regel toe aan de
bestaande ` iptables ` -regels op de node om de kwetsbaarheid op te lossen.
**Voer de opdracht eenmaal per cluster en per Google Cloud-project uit.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Omdat Ipv6 niet wordt ondersteund op GKE, is er geen ip6tables-regel vereist.

Zodra er een gepatchte versie beschikbaar is en u alle mogelijk getroffen
nodes heeft geüpgraded, kunt u de DaemonSet met de volgende opdracht
verwijderen. **Voer de opdracht eenmaal per cluster en per Google Cloud-
project uit.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Hoog  
Gemiddeld  
Gemiddeld  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 juni 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update 03-07-2019:** Deze patch is beschikbaar in ` gcloud ` 253.0.0, voor `
kubectl ` -versies 1.12.9, 1.13.6, 1.14.2 en nieuwere releases.

**Opmerking:** De patch is niet beschikbaar in 1.11.10.

* * *

Kubernetes heeft onlangs een kwetsbaarheid ontdekt, [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) , waardoor
een aanvaller met toegang tot een ` kubectl cp ` -operatie en code-uitvoering
binnen een container bestanden kan aanpassen op de host. Door dit
beveiligingslek kan een aanvaller mogelijk een bestand in het bestandssysteem
van de host vervangen of maken. Bekijk de [ kennisgeving van Kubernetes
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/NLs2TGbfPdo) voor meer informatie.

**Alle Google Kubernetes Engine (GKE)` gcloud ` -versies worden door deze
kwetsbaarheid beïnvloed. We raden u aan naar de nieuwste patchversie van `
gcloud ` te upgraden, zodra deze beschikbaar is. ** Een aankomende patchversie
bevat een oplossing voor deze kwetsbaarheid.

######  Wat moet ik doen?

Een gepatchte versie van ` kubectl ` wordt in een aankomende ` gcloud `
-release opgenomen. U kunt [ ` kubectl ` ook rechtstreeks zelf upgraden
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) .

Monitor de beschikbaarheid van deze patch in de [ ` gcloud ` -release-
opmerkingen ](https://cloud.google.com/sdk/docs/release-notes?hl=nl) .

######  Welke kwetsbaarheid wordt door deze patch verholpen?

Door de kwetsbaarheid [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) kan een aanvaller met toegang tot een `
kubectl cp ` -bewerking en code-uitvoering binnen een container bestanden
aanpassen op de host. Door dit beveiligingslek kan een aanvaller een bestand
vervangen of maken in het bestandssysteem van de host.

|

Hoog

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 juni 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Docker heeft onlangs de kwetsbaarheid [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) ontdekt
waardoor een aanvaller die code binnen een container kan uitvoeren, een extern
gestarte ` docker cp ` -operatie kan hacken. Door dit beveiligingslek kan een
aanvaller de schrijflocatie van een bestand veranderen in een willekeurige
locatie in het bestandssysteem van de host.

**Deze kwetsbaarheid geldt voor alle GKE-nodes (Google Kubernetes Engine) die
Docker uitvoeren. We raden u aan een upgrade uit te voeren naar de nieuwste
patchversie, zodra deze beschikbaar is. Een aankomende patchversie bevat een
oplossing voor deze kwetsbaarheid.**

**Alle GKE-hoofdinstanties (Google Kubernetes Engine) die ouder zijn dan
versie 1.12.7 draaien op Docker en zijn getroffen door deze kwetsbaarheid.**
Gebruikers op GKE hebben geen toegang tot ` docker cp ` op de hoofdinstantie.
Het risico op deze kwetsbaarheid is dus beperkt voor GKE-hoofdinstanties.

#####  Wat moet ik doen?

Dit is alleen van toepassing op nodes die Docker uitvoeren en een ` docker cp
` -opdracht (of API-equivalent) uitgeven die kan worden gehackt. Dit is naar
verwachting vrij ongebruikelijk in een Kubernetes-omgeving. Nodes die [ COS
met containerd ](https://cloud.google.com/kubernetes-
engine/docs/concepts/using-containerd?hl=nl) uitvoeren, worden niet beïnvloed.

Als u uw nodes wilt upgraden, moet u eerst [ uw hoofdinstantie upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl#upgrading_the_cluster) naar de gepatchte versie. Zodra de patch
beschikbaar is, kunt u een upgrade van de hoofdinstantie uitvoeren of wachten
totdat Google de hoofdinstantie automatisch upgradet. De patch komt
beschikbaar in Docker 18.09.7, als onderdeel van een aankomende GKE-patch.
**Deze patch is alleen beschikbaar voor GKE-versies 1.13 en hoger.**

We upgraden de clusterhoofden volgens de gebruikelijke upgradefrequentie
automatisch naar de gepatchte versie. U kunt ook zelf een upgrade van de
hoofdinstantie uitvoeren zodra de gepatchte versie beschikbaar is.

We zullen dit bulletin updaten met de gepatchte versies zodra deze beschikbaar
zijn. Monitor de beschikbaarheid van deze patches in de [ release-opmerkingen
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=nl) .

#####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

Door de kwetsbaarheid [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) kan een aanvaller die code binnen een
container kan uitvoeren, een extern gestarte ` docker cp ` -bewerking hacken.
Door dit beveiligingslek kan een aanvaller de schrijflocatie van een bestand
veranderen in een willekeurige locatie in het bestandssysteem van de host.

|  Hoog  |  
  
##  31 mei 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Dit bulletin is na de oorspronkelijke publicatie geüpdatet.

######  Update 2 augustus 2019

Ten tijde van het oorspronkelijke bulletin waren alleen 1.13.6-gke.0 tot en
met 1.13.6-gke.5 getroffen. Door een regressie zijn nu alle 1.13.6.x-versies
getroffen. Upgrade zo snel mogelijk naar 1.13.7 als u 1.13.6 uitvoert.

Het Kubernetes-project heeft [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245) in kubelet v1.13.6 en v1.14.2 bekendgemaakt.
Door deze kwetsbaarheid kunnen containers als UID 0 worden uitgevoerd (wordt
meestal aan de ` root ` -gebruiker toegewezen), zelfs als er in de container-
image een andere gebruiker is opgegeven. **Als uw containers als een niet-
root-gebruiker worden uitgevoerd en u node-versie 1.13.6-gke.0 tot en met
1.13.6-gke.6 uitvoert, raden we u aan` RunAsUser ` in te stellen op alle pods
in het cluster waarvan de containers niet als UID 0 moeten worden uitgevoerd.
**

Als er een niet-root ` USER ` -waarde is opgegeven (bijvoorbeeld door de
waarde van ` USER ` in een Dockerfile in te stellen), kan er onverwacht gedrag
optreden. Wordt een container voor de eerste keer op een node uitgevoerd, dan
respecteert deze op de juiste wijze de opgegeven UID. Door dit defect wordt de
container tijdens de tweede uitvoering (en de daaropvolgende uitvoeringen)
echter uitgevoerd als UID 0, ongeacht de opgegeven UID. Dit is meestal een
ongewenste toe-eigening van rechten, wat kan leiden tot onverwacht app-gedrag.

#####  Hoe weet ik of dit defect op mijn versie van toepassing is?

Voer de volgende opdracht uit om alle nodes en hun kubelet-versie weer te
geven:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Als de onderstaande kubelet-versies in de lijst voorkomen, is het defect van
toepassing op uw nodes.

  * v1.13.6 
  * v1.14.2 

#####  Hoe weet ik of dit defect op mijn configuratie van toepassing is?

Als uw containers als een niet-root-gebruiker worden uitgevoerd en u voert
node-versie 1.13.6-gke.0 tot en met 1.13.6-gke.6 uit, is het defect op u van
toepassing, met uitzondering van de volgende gevallen:

  * Pods die een geldige niet-root-waarde voor de ` runAsUser ` -PodSecurityContext opgeven, worden niet beïnvloed en blijven werken zoals verwacht. 
  * PodSecurityPolicies die een ` runAsUser ` -instelling afdwingen, worden ook niet beïnvloed en blijven ook gewoon werken. 
  * Pods die ` mustRunAsNonRoot:true ` opgeven, starten niet als UID 0, maar starten niet als ze door dit probleem worden beïnvloed. 

#####  Wat moet ik doen?

Stel de [ RunAsUser Security Context
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) in op alle pods in het cluster
die niet als UID 0 moeten worden uitgevoerd. U kunt deze configuratie
toepassen met een [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) .

|  Gemiddeld  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 mei 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update 11-06-2019:** de patch is beschikbaar in 1.11.10-gke.4, 1.12.8-gke.6
en 1.13.6-gke.5 die zijn vrijgegeven in de week van 28 mei 2019 en nieuwere
releases.

De volgende CVE's zijn door Intel bekendgemaakt:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Deze CVE's worden gezamenlijk 'Microarchitectural Data Sampling (MDS)'
genoemd. Via deze kwetsbaarheden kunnen gegevens worden blootgelegd via
interactie tussen speculatieve uitvoering en de microarchitecturale staat.
Bekijk de [ kennisgeving van Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) voor meer informatie.

**De hostinfrastructuur waarop Kubernetes Engine wordt uitgevoerd, scheidt
productietaken van klanten van elkaar. Dit is niet op u van toepassing tenzij
u niet-vertrouwde code binnen uw eigen multi-tenant GKE-clusters uitvoert.**

**Voor klanten die niet-vertrouwde code uitvoeren in hun eigen multi-tenant
services binnen Kubernetes-engine, is dit een ernstige kwetsbaarheid.**
Schakel hyperthreading in uw nodes uit om dit in Kubernetes Engine op te
lossen. Deze kwetsbaarheden zijn alleen van toepassing op GKE-nodes (Google
Kubernetes Engine) die meerdere CPU's gebruiken. n1-standard-1 (de GKE-
standaard), g1-small en f1-micro VM's stellen slechts 1 vCPU beschikbaar aan
de gastomgeving. Hyperthreading hoeft dus niet uitgeschakeld te worden.

Aanvullende beveiligingsmaatregelen om flush-functionaliteit in te schakelen,
worden opgenomen in een aankomende [ patchversie
](https://cloud.google.com/kubernetes-engine/release-notes?hl=nl) . We zullen
de hoofdinstanties en nodes in de komende weken automatisch upgraden naar de
gepatchte versie volgens de gebruikelijke upgradefrequentie. **De patch alleen
is niet voldoende om blootstelling aan deze kwetsbaarheid tegen te gaan.
Bekijk hieronder de aanbevolen acties.**

Als u GKE op locatie uitvoert, kan dit op u van toepassing zijn, afhankelijk
van de hardware die u gebruikt. Raadpleeg de [ kennisgeving van Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

####  Wat moet ik doen?

**U hoeft geen actie te ondernemen, tenzij u niet-vertrouwde code binnen uw
eigen multi-tenant GKE-clusters uitvoert.**

**Voor nodes in Kubernetes Engine maakt u nieuwe node-pools waarbij
hyperthreading is uitgeschakeld en plant u uw productietaken opnieuw in op de
nieuwe nodes.**

n1-standard-1, g1-small en f1-micro VM's stellen slechts 1 vCPU beschikbaar
aan de gastomgeving. Hyperthreading hoeft dus niet uitgeschakeld te worden.

**Waarschuwing:**

  * Het uitschakelen van hyperthreading kan ernstige gevolgen hebben voor de prestaties van uw clusters en app. Houd hier rekening mee voordat u dit toepast op uw productieclusters. 
  * Hyperthreading kan worden uitgeschakeld op GKE-node-poolniveau door een DaemonSet te implementeren. Het implementeren van een DaemonSet leidt er echter toe dat alle nodes in uw node-pool tegelijkertijd opnieuw worden opgestart. Daarom raden we u aan een nieuwe node-pool in uw cluster te maken, de DaemonSet te implementeren om hyperthreading in die node-pool uit te schakelen en vervolgens uw productietaken naar de nieuwe node-pool te migreren. 

Een nieuwe node-pool maken waarvoor hyperthreading is uitgeschakeld:

  1. Maak een nieuwe node-pool in uw cluster met het node-label ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Implementeer de DaemonSet naar deze nieuwe node-pool. De DaemonSet wordt alleen uitgevoerd op nodes met het ` cloud.google.com/gke-smt-disabled=true ` -label. Hyperthreading wordt uitgeschakeld en de node wordt opnieuw opgestart. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Zorg ervoor dat de DaemonSet-pods actief zijn. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Als het goed is, krijgt u een reactie als deze:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Controleer of 'SMT is uitgeschakeld' in de logboeken van de pods verschijnt. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Opmerking: Opstartfuncties kunnen niet worden aangepast als de functie [
Veilig opstarten ](https://cloud.google.com/kubernetes-engine/docs/how-
to/shielded-gke-nodes?hl=nl#secure_boot) ingeschakeld is voor de node. Als
'Veilig opstarten' ingeschakeld is, moet deze functie worden [ uitgeschakeld
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=nl#disabling) voordat de DaemonSet wordt gemaakt.

Zorg ervoor dat de DaemonSet actief blijft op de nodes, zodat de wijzigingen
automatisch worden toegepast op de nieuwe nodes in de pool. Het maken van
nodes kan worden geactiveerd door het automatisch herstellen, het handmatig of
automatisch upgraden en het automatisch schalen van nodes.

Als u hyperthreading opnieuw wilt inschakelen, moet u de node-pool opnieuw
maken zonder de DaemonSet te implementeren, en uw productietaken naar de
nieuwe node-pool migreren.

We raden u ook aan uw nodes handmatig te upgraden zodra de patch beschikbaar
is. [ Upgrade eerst uw hoofdinstantie ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=nl#upgrading_the_cluster) naar de
nieuwste versie. GKE-hoofdinstanties worden automatisch geüpgraded volgens de
gebruikelijke upgradefrequentie.

We zullen dit bulletin updaten met de gepatchte versies zodra deze beschikbaar
zijn.

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Deze kwetsbaarheden buiten speculatieve uitvoering uit. Deze CVE's worden
gezamenlijk 'Microarchitectural Data Sampling' genoemd. Via deze
kwetsbaarheden kunnen gegevens openbaar worden gemaakt via interactie tussen
speculatieve uitvoering en de microarchitecturale toestand.  |  Gemiddeld  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 april 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Onlangs zijn de kwetsbaarheden [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) en [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) ontdekt in [
Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) maakt gebruik van Envoy. Deze kwetsbaarheden
zorgen er in sommige gevallen voor dat Istio-beleid omzeild kan worden.

Als u Istio heeft ingeschakeld op Google Kubernetes Engine (GKE), kunnen deze
kwetsbaarheden op u van toepassing zijn. **We raden u aan de getroffen
clusters zo snel mogelijk te upgraden naar de nieuwste patchversie en uw
Istio-sidecars te upgraden (instructies hieronder).**

####  Wat moet ik doen?

**Vanwege de ernst van deze kwetsbaarheden raden we u het volgende aan
(ongeacht of u automatische upgrades voor nodes heeft ingeschakeld):**

  1. **[ Upgrade het cluster handmatig ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=nl) zodra de patch beschikbaar is. **
  2. **Upgrade uw sidecar-bestanden door[ de upgrade-documentatie voor sidecar-bestanden ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) te volgen. **

De gepatchte versies worden vandaag vóór 19:00 uur PDT voor alle GKE-projecten
vrijgegeven.

Deze patch is beschikbaar voor de onderstaande GKE-versies. Nieuwe clusters
zullen standaard de gepatchte versie gebruiken wanneer deze wordt aangekondigd
op de pagina met GKE-beveiligingsbulletins (verwacht op 15 april 2019). Als u
voor die tijd een nieuw cluster maakt, moet u aangeven welke gepatchte versie
gebruikt moet worden. De nodes van GKE-klanten die [ automatische upgrades
voor nodes ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=nl) hebben ingeschakeld en die niet handmatig worden geüpgraded,
worden volgende week automatisch geüpgraded naar gepatchte versies.

Gepatchte versies:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) en [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Bekijk het [
Istio-blog ](https://istio.io/blog/2019/announcing-1.1.2) voor meer
informatie.

|  Hoog  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 maart 2019

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update 22-03-2019:** Deze patch is beschikbaar in Kubernetes 1.11.8-gke.4,
1.13.4-gke.1 en nieuwere releases. De patch is nog niet beschikbaar in 1.12.
Monitor de beschikbaarheid van deze patches in de [ release-opmerkingen
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#march_19_2019) .

Kubernetes heeft onlangs een nieuwe DoS-kwetsbaarheid ontdekt, [
CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , waardoor een gebruiker die
patchverzoeken mag indienen een kwaadaardig 'json-patch'-verzoek kan maken dat
buitensporige hoeveelheden CPU en geheugen in de Kubernetes API-server
verbruikt. Hierdoor wordt de beschikbaarheid van het clusterbesturingsvlak
mogelijk verminderd. Bekijk de [ kennisgeving van Kubernetes
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-
announce/vmUUNkYfG9g) voor meer informatie. **Deze kwetsbaarheden zijn van
toepassing op alle GKE-hoofdinstanties (Google Kubernetes Engine). Een
aankomende patchversie bevat een oplossing voor deze kwetsbaarheid. We zullen
de clusterhoofden in de komende weken automatisch upgraden naar de gepatchte
versie volgens de gebruikelijke upgradefrequentie.**

####  Wat moet ik doen?

**U hoeft niets te doen. GKE-hoofdinstanties worden automatisch geüpgraded
volgens de gebruikelijke upgradefrequentie.** Als u uw hoofdinstantie eerder
wilt upgraden, kunt u [ handmatig een upgrade uitvoeren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl#upgrading_the_cluster) .

We zullen dit bulletin updaten met de gepatchte versies. De patch is alleen
beschikbaar in de versies 1.11+ en niet in 1.10.

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

Door de kwetsbaarheid [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) kan een gebruiker een 'json-
patch'-patch maken die buitensporige hoeveelheden CPU in de Kubernetes API-
server verbruikt. Hierdoor wordt mogelijk de beschikbaarheid van het
clusterbesturingsvlak verminderd.

|  Gemiddeld  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 februari 2019 (runc)

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Het Open Containers Initiative (OCI) heeft onlangs in runc de [ nieuwe
kwetsbaarheid
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=nl#!topic/dev/Tc1ELm-8oDI)
[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) ontdekt, waardoor containerescape
rootrechten kan krijgen op de hostnode.

**Deze kwetsbaarheden zijn van toepassing op uw Ubuntu-nodes in Google
Kubernetes Engine (GKE). We raden u aan zo snel mogelijk te[ upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl) naar de nieuwste patchversie, zoals hieronder beschreven. **

####  Wat moet ik doen?

Als u uw nodes wilt upgraden, moet u eerst uw hoofdinstantie naar de nieuwste
versie upgraden. Deze patch is beschikbaar in Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 en nieuwere releases. Monitor de
beschikbaarheid van deze patches in de [ release-opmerkingen
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#february-11-2019) .

Alleen Ubuntu-nodes in GKE worden beïnvloed. Nodes die COS uitvoeren, worden
niet beïnvloed.

De nieuwe versie van runc heeft het geheugenverbruik verhoogd. Mogelijk moet u
het geheugen dat aan containers is toegewezen updaten als u lage
geheugenlimieten heeft ingesteld (< 16 MB).

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) beschrijft een kwetsbaarheid in runc
waarmee een kwaadaardige container (met minimale gebruikersinteractie in de
vorm van een exec) het binaire bestand van de host-runc kan overschrijven en
zo code-uitvoering op hoofdniveau op de host-node kan verkrijgen. Dit geldt
niet voor containers die niet als root worden uitgevoerd. Dit wordt beoordeeld
als een hoge kwetsbaarheid.

|  Hoog  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 februari 2019 (Go)

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
**Update 25-02-2019:** de patch is niet beschikbaar in 1.11.7-gke.4, zoals
eerder gemeld. Als u 1.11.7 gebruikt, kunt u downgraden naar 1.11.6, upgraden
naar 1.12 of wachten totdat de volgende patch voor 1.11.7 beschikbaar is in de
week van 04-03-2019.

De programmeertaal Go heeft onlangs een nieuwe kwetsbaarheid ontdekt, [
CVE-2019-6486 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6486)
. Dit is een DoS-kwetsbaarheid (denial of service) in de crypto-/elliptische
implementaties van de elliptische krommen P-521 en P-384. Hierdoor kan een
gebruiker in Google Kubernetes Engine (GKE) kwaadaardige verzoeken maken die
buitensporig veel CPU verbruiken in de Kubernetes API-server, waardoor
mogelijk de beschikbaarheid van het clusterbesturingsvlak wordt verminderd.
Bekijk de [ kennisgeving van de programmeertaal Go
](https://groups.google.com/forum/?hl=nl#!topic/golang-announce/mVeX35iXuSw)
voor meer informatie.

**Deze kwetsbaarheden zijn van toepassing op alle GKE-hoofdinstanties (Google
Kubernetes Engine). De[ nieuwste patchversie
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#february-11-2019) bevat een oplossing voor deze kwetsbaarheid. We
upgraden de clusterhoofden in de komende weken automatisch naar de gepatchte
versie volgens de gebruikelijke upgradefrequentie. **

####  Wat moet ik doen?

**U hoeft niets te doen. GKE-hoofdinstanties worden automatisch geüpgraded
volgens de gebruikelijke upgradefrequentie.** Als u uw hoofdinstantie eerder
wilt upgraden, kunt u [ handmatig een upgrade uitvoeren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl#upgrading_the_cluster) .

Deze patch is beschikbaar in GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 en nieuwere releases.

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

CVE-2019-6486 is een kwetsbaarheid in de crypto-/elliptische implementaties
van de elliptische krommen P-521 en P-384. Hierdoor kan een gebruiker invoer
maken die buitensporige hoeveelheden CPU verbruikt.

|  Hoog  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 december 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Kubernetes ontdekte onlangs de nieuwe beveiligingskwetsbaarheid [
CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , waardoor een gebruiker met relatief
weinig rechten de autorisatie voor de API's van de kubelet kan omzeilen.
Daardoor kan deze willekeurige bewerkingen uitvoeren voor elke pod op elke
node in het cluster. Bekijk de [ kennisgeving van Kubernetes
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-
announce/GVllWCg6L88) voor meer informatie. **Deze kwetsbaarheden waren van
toepassing op alle hoofdinstanties van Google Kubernetes Engine (GKE). We
hebben clusters al geüpgraded naar de[ nieuwste patchversies
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#november-12-2018) . U hoeft niets te doen. **

####  Wat moet ik doen?

**U hoeft niets te doen. Hoofdinstanties van GKE zijn al geüpgraded.**

Deze patch is beschikbaar in GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5 en 1.11.2-gke.18 en nieuwere releases.

####  Welke kwetsbaarheid wordt door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheid:

Door de kwetsbaarheid CVE-2018-1002105 kan een gebruiker met relatief weinig
rechten de autorisatie voor de API's van de kubelet omzeilen. Dit geeft een
gebruiker die gemachtigd is om upgradebare verzoeken te doen het recht om uit
te breiden en willekeurige aanroepen te doen naar de API van de kubelet. Dit
wordt beoordeeld als een kritieke kwetsbaarheid in Kubernetes. Vanwege de
aanwezigheid van bepaalde elementen in de implementatie van GKE die de
ongeautoriseerde uitbreiding voorkwamen, wordt dit beoordeeld als een hoge
kwetsbaarheid.

|  Hoog  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 november 2018

Beschrijving  
---  
  
**Update van 16-11-2018:** de intrekking en roulatie van alle mogelijk
beïnvloede tokens is voltooid. U hoeft verder niets te doen.

Google heeft onlangs een probleem ontdekt in de plug-in Calico Container
Network Interface (CNI), die in bepaalde configuraties gevoelige informatie
kan registreren. Dit probleem wordt gemonitord onder Tigera Technical Advisory
[ TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/) .

  * Bij gebruik van logboekregistratie op foutopsporingsniveau schrijft de Calico CNI-plug-in de clientconfiguratie van Kubernetes API in de logboeken. 
  * De Calico CNI schrijft ook het Kubernetes API-token naar de logboeken op het infoniveau als het veld 'k8s_auth_token' is ingesteld op de CNI-netwerkconfiguratie. 
  * Bovendien schrijven Calico-componenten (calico/node, felix, CNI) bij gebruik van logboekregistratie op foutopsporingsniveau het token van het serviceaccount naar de logbestanden wanneer het token expliciet is ingesteld - ofwel in het Calico-configuratiebestand dat door Calico wordt gelezen, ofwel als omgevingsvariabelen die door Calico worden gebruikt. 

Deze tokens hebben de volgende rechten:  
      
    
    
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
  
Google Kubernetes Engine-clusters die een netwerkbeleid voor clusters en
Stackdriver Logging hebben ingeschakeld, registreerden Calico-serviceaccount-
tokens op Stackdriver. Dit is niet van toepassing op clusters waarbij
netwerkbeleid niet is ingeschakeld.

We hebben een oplossing geïmplementeerd die de Calico CNI-plug-in migreert om
alleen op het waarschuwingsniveau logboekregistraties te schrijven en een
nieuw serviceaccount te gebruiken. De gepatchte Calico-code wordt in een
latere release geïmplementeerd.

In de loop van de volgende week zullen we een continue intrekking van alle
mogelijk aangetaste tokens uitvoeren. Dit bulletin wordt geüpdatet wanneer de
intrekking is voltooid. **U hoeft verder niets te doen.** (Deze rotatie werd
voltooid op 16-11-2018)

Als u deze tokens onmiddellijk wilt rouleren, kunt u de volgende opdracht
uitvoeren. Het nieuwe geheim voor het serviceaccount zou binnen enkele
seconden automatisch opnieuw moeten worden gemaakt:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Detectie

GKE registreert alle toegang tot de API-server. Om te bepalen of een Calico-
token van buiten het verwachte IP-bereik van Google Cloud werd gebruikt, kunt
u de volgende Stackdriver-query uitvoeren. Hiermee worden alleen records
geretourneerd voor aanroepen van buiten het GCP-netwerk. Pas dit aan voor uw
specifieke omgeving.  
  
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
  
##  14 augustus 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
De volgende CVE's zijn [ door Intel bekendgemaakt
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (voor [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (voor besturingssystemen en [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (voor virtualisatie) 

Deze CVE's worden gezamenlijk 'L1 Terminal Fault (L1TF)' genoemd.

Deze L1TF-kwetsbaarheden maken gebruik van speculatieve uitvoering door de
configuratie van datastructuren op processorniveau aan te vallen. 'L1'
verwijst naar het Level-1 Data-cachegeheugen (L1D), een kleine resource in de
kern die wordt gebruikt om geheugentoegang te versnellen.

Lees de [ blogpost van Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=nl) voor meer informatie over deze
kwetsbaarheden en de beperkende maatregelen van Compute Engine.

####  Gevolgen voor Google Kubernetes Engine

De infrastructuur waarop Kubernetes Engine wordt uitgevoerd en die
klantclusters en nodes van elkaar isoleert, is beveiligd tegen bekende
aanvallen.

Node-pools op Kubernetes Engine die de voor containers geoptimaliseerde OS-
image van Google gebruiken en [ automatisch upgraden
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=nl) hebben ingeschakeld, worden automatisch geüpdatet naar
gepatchte versies van onze COS-image zodra deze beschikbaar zijn vanaf de week
van 20-08-2018.

Node-pools op Kubernetes Engine waarvoor [ automatisch upgraden
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=nl) niet is ingeschakeld, moeten [ handmatig worden geüpgraded
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=nl) wanneer gepatchte versies van onze COS-image
beschikbaar zijn.

|  Hoog  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 augustus 2018, laatste update op 5 september 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Update op 05-09-2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) is onlangs bekendgemaakt. Net als bij [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
is dit een netwerkkwetsbaarheid op kernel-niveau die de effectiviteit van DoS-
aanvallen (denial of service) op kwetsbare systemen verhoogt. Het
belangrijkste verschil is dat CVE-2018-5391 kan worden gebruikt via IP-
verbindingen. We hebben dit bulletin geüpdatet om beide kwetsbaarheden te
behandelen.

####  Beschrijving

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ('SegmentSmack') beschrijft een
netwerkkwetsbaarheid op kernel-niveau die de effectiviteit van DoS-aanvallen
(denial of service) via TCP-verbindingen op kwetsbare systemen verhoogt.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ('FragmentSmack') beschrijft een
netwerkkwetsbaarheid op kernel-niveau die de effectiviteit van DoS-aanvallen
(denial of service) via IP-verbindingen op kwetsbare systemen verhoogt.

####  Gevolgen voor Google Kubernetes Engine

Vanaf 11-08-2018 zijn alle hoofdinstanties van Kubernetes Engine beschermd
tegen beide kwetsbaarheden. Daarnaast zijn alle Kubernetes Engine-clusters die
zijn geconfigureerd om automatisch te upgraden ook beschermd tegen beide
kwetsbaarheden. Beide kwetsbaarheden zijn van toepassing op node-pools op
Kubernetes Engine die niet zijn geconfigureerd met [ automatisch upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=nl) en als laatste handmatig zijn geüpdatet vóór 11-08-2018.

####  Gepatchte versies

Vanwege de ernst van deze kwetsbaarheid raden we aan om uw nodes [ handmatig
te upgraden ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=nl#upgrading-nodes) zodra de patch beschikbaar is.

|  Hoog  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 mei 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Onlangs werd in Git een kwetsbaarheid ontdekt die uitbreiding van bevoegdheden
in Kubernetes mogelijk maakt als onbevoegde gebruikers pods mogen maken met
gitRepo-volumes. De CVE wordt geïdentificeerd met de tag [ CVE-2018-11235
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235) .

####  Ben ik getroffen?

Deze kwetsbaarheid is op u van toepassing als al het volgende waar is:

  * Niet-vertrouwde gebruikers kunnen pods maken (of hiervoor een trigger activeren). 
  * Pods die zijn gemaakt door niet-vertrouwde gebruikers hebben beperkingen die root-toegang op de host voorkomen (bijvoorbeeld met [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=nl) ). 
  * Pods die zijn gemaakt door niet-vertrouwde gebruikers mogen het gitRepo-volumetype gebruiken. 

Alle Kubernetes Engine-nodes zijn kwetsbaar.

####  Wat moet ik doen?

Verbied het gebruik van het gitRepo-volumetype. Laat ` gitRepo ` weg van de
witte lijst van ` volumes ` in uw PodSecurityPolicy om gitRepo-volumes met
PodSecurityPolicy te verbieden.

Vergelijkbaar gitRepo-volumegedrag kan worden bereikt door een git-
opslagplaats in een EmptyDir-volume te klonen vanuit een initContainer:

    
    
    
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

####  Welke patch lost deze kwetsbaarheid op?

Er wordt een patch opgenomen in een aankomende Kubernetes Engine-release. Kom
later terug voor meer informatie.

|  Gemiddeld  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 mei 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Recentelijk zijn verschillende kwetsbaarheden ontdekt in de Linux-kernel die
een uitbreiding van bevoegdheden of denial of service (via kernel-crash)
vanuit een onbevoegd proces mogelijk zouden kunnen maken. Deze CVE's worden
geïdentificeerd met de tags [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) en [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
. Deze kwetsbaarheden zijn van toepassing op alle Kubernetes Engine-nodes en
we raden u aan om [ een upgrade uit te voeren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=nl) naar de nieuwste patchversie, zoals hieronder wordt
beschreven.

####  Wat moet ik doen?

Upgrade eerst uw hoofdinstantie naar de nieuwste versie. Deze patch is
beschikbaar in Kubernetes Engine 1.8.12-gke.1, Kubernetes Engine 1.9.7-gke.1
en Kubernetes Engine 1.10.2-gke.1. Deze releases bevatten patches voor zowel
Container Optimized OS- als Ubuntu-images.

Als u eerder een nieuw cluster maakt, moet u de gepatchte versie opgeven zodat
deze wordt gebruikt. Voor klanten die [ automatische upgrades voor nodes
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=nl) hebben ingeschakeld en die niet handmatig upgraden, worden hun
nodes in de komende weken geüpgraded naar gepatchte versies.

####  Welke kwetsbaarheden worden door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : Deze kwetsbaarheid treft de Linux-
kernel. Hiermee kan een onbevoegde gebruiker of proces de systeem-kernel laten
crashen, wat leidt tot een DoS-aanval of toe-eigening van rechten. Dit wordt
beoordeeld als een hoge kwetsbaarheid, met een CVSS van 7,8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : Deze kwetsbaarheid treft de Linux-
kernel. Hiermee kan een gebruiker of proces zonder extra rechten de systeem-
kernel laten crashen, wat leidt tot een DoS-aanval. Dit wordt beoordeeld als
een gemiddelde kwetsbaarheid, met een CVSS van 6,5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : Deze kwetsbaarheid treft de KVM-
hypervisor van de Linux-kernel. Hiermee kan een onbevoegd proces de gast-
kernel laten crashen of mogelijk rechten verkrijgen. Deze kwetsbaarheid is
gepatcht in de infrastructuur waarop Kubernetes Engine wordt uitgevoerd, dus
Kubernetes Engine is niet getroffen. Dit wordt beoordeeld als een hoge
kwetsbaarheid, met een CVSS-score van 8,0.

|  Hoog  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 maart 2018

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
Het Kubernetes-project [ publiceerde onlangs
](https://groups.google.com/forum/?hl=nl#!topic/kubernetes-security-
announce/P7lBjbjDKd8) de nieuwe kwetsbaarheden [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) en [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , waardoor containers toegang kunnen
krijgen tot bestanden buiten de container. Alle Kubernetes Engine-nodes zijn
gevoelig voor deze kwetsbaarheden en we raden u aan zo snel mogelijk een
upgrade naar de nieuwste patch-versie uit te voeren, zoals hieronder wordt
beschreven.

####  Wat moet ik doen?

Vanwege de ernst van deze kwetsbaarheden raden we aan om uw nodes [ handmatig
te upgraden ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=nl) zodra de patch beschikbaar is,
ongeacht of u de automatische upgrades voor nodes heeft ingeschakeld. De patch
is vanaf 16 maart voor alle klanten beschikbaar, maar is mogelijk eerder
beschikbaar op basis van de zone waarin uw cluster zich bevindt. Zie het [
releaseschema ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=nl#march-12-2018) .

Upgrade eerst uw hoofdinstantie naar de nieuwste versie. Deze patch is
beschikbaar in Kubernetes 1.9.4-gke.1, Kubernetes 1.8.9-gke.1 en Kubernetes
1.7.14-gke.1. Vanaf 30 maart gebruiken alle nieuwe clusters standaard de
gepatchte versie. Als u eerder een nieuw cluster maakt, moet u de gepatchte
versie opgeven zodat deze wordt gebruikt.

Voor klanten die [ automatische upgrades voor nodes
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=nl) hebben ingeschakeld en die niet handmatig upgraden, worden hun
nodes op 23 april geüpgraded naar gepatchte versies. Vanwege de aard van de
kwetsbaarheid raden we echter aan om uw nodes [ handmatig te upgraden
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=nl) zodra de patch voor u beschikbaar is.

####  Welke kwetsbaarheden worden door deze patch verholpen?

De patch beperkt de volgende kwetsbaarheden:

De kwetsbaarheid CVE-2017-1002101 geeft containers die middels volumeactivatie
een [ subpad ](https://kubernetes.io/docs/concepts/storage/volumes/#using-
subpath) specificeren, toegang tot bestanden buiten het volume. Dit betekent
dat als u containertoegang tot hostpadvolumes blokkeert met PodSecurityPolicy,
een aanvaller met de mogelijkheid om pods te updaten of te maken elk hostpad
kan activeren met elk ander volumetype.

Door de kwetsbaarheid CVE-2017-1002102 kunnen containers met bepaalde
volumetypen (waaronder geheimen, Config Maps, geprojecteerde volumes of
neerwaartse API-volumes) bestanden verwijderen buiten het volume. Als een
container die een van deze volumetypen gebruikt, wordt gehackt of als u niet-
vertrouwde gebruikers de mogelijkheid biedt om pods te maken, kan een
aanvaller die container gebruiken om willekeurige bestanden op de host te
verwijderen.

Lees de [ Kubernetes-blogpost ](https://kubernetes.io/blog/2018/04/04/fixing-
subpath-volume-vulnerability/) voor meer informatie over de oplossing.

|  Hoog  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

