Strumento 15 - Validatore semantico
===================================

*Versione 1.0 del 11/09/2024*

15.1 - Anagrafica
-----------------

**Ente:** ISTAT

**Ufficio proponente:** DIRM - Dipartimento per lo sviluppo di metodi e
tecnologie per la produzione e diffusione dell'informazione statistica

**Destinatari:** Tutte le pubbliche amministrazioni

**Capitolo del PT 2024-2026:** Capitolo 5 - Dati e intelligenza
artificiale

**Tematica:** *Open data e data governance*

15.2 - Scenario
---------------

Nell'ambito della realizzazione dell'interoperabilità dei dati della
Pubblica Amministrazione, il progetto "Catalogo Nazionale per
l'interoperabilità semantica dei dati" (NDC), inquadrato tra gli
investimenti PNRR come Misura M1C1-1.3.1, risponde alle raccomandazioni
della Commissione Europea espresse nel *European Interoperability
Framework*, punto di riferimento per diverse altre fonti normative UE, e
anche a livello nazionale da quanto previsto nel CAD su cui si basano
gli atti programmatici come il Piano triennale per l'informatica. Scopo
del catalogo realizzato attraverso il portale
`Schema <http://www.schema.gov.it>`__ è quello di favorire
l'interoperabilità semantica dei dati nello scambio di informazioni tra
pubbliche amministrazioni attraverso l'armonizzazione e la
standardizzazione di codici e nomenclature ricorrenti, realizzate
mediante l'identificazione e la definizione di risorse semantiche
(ontologie, vocabolari controllati e schemi dati). La pubblicazione
delle risorse semantiche attraverso il catalogo richiede la
standardizzazione dei relativi metadati secondo il profilo nazionale di
metadatazione DCAT-AP_IT. Per agevolare i contributori nel processo di
modellazione e valorizzazione dei metadati delle risorse, viene messo a
disposizione il "**Validatore dei metadati delle risorse
semantiche**", che implementa i controlli di validità a supporto della
fase di *pre-harvesting*, segnalando errori o *warnings*, consentendo
quindi di validare la standardizzazione dei metadati descrittori delle
risorse semantiche della PA. La corretta modellazione e valorizzazione
di questi metadati, di cui è responsabile direttamente l'ente
contributore, consentono di attivare il processo di *harvesting* sul
catalogo e la relativa pubblicazione delle risorse semantiche.

15.3 - Presentazione
--------------------

Il Validatore dei metadati è destinato a tutte le PA che contribuiscono
in modo autonomo con le loro risorse semantiche al portale Schema.

Come indicato nella guida al Catalogo, l'ente contributore, individuato
il dominio di pertinenza e scelta la tematica delle proprie risorse da
rendere fruibili, può modellare autonomamente ontologie, vocabolari
controllati e/o schemi dati e richiederne la pubblicazione a catalogo,
seguendo il *workflow* delle attività propedeutiche alla contribuzione
descritte nella sopracitata guida.

Il `Validatore di metadati <https://schema.gov.it/validatore>`__
consente la validazione attraverso il caricamento dei file in formato
*turtle*. I controlli eseguiti dal validatore sono di carattere
sintattico, differenziati sulla base della tipologia della risorsa:

-  Ontologie: regole di metadatazione dell'ontologia *ADMS-AP_IT*

-  Vocabolari controllati: metadatazione *DCAT-AP_IT* e una licenza
   aperta

-  File "index.ttl" degli schemi dati: regole di metadatazione
   dell'ontologia *ADMS-AP_IT*

Nella pagina del Validatore dei metadati è possibile accedere
direttamente alla guida.

La segnalazione di errori effettuata dal Validatore è dettagliata in
modo da favorire l'intervento di correzione da parte degli enti
contributori. La correzione degli errori è imprescindibile per
consentire la procedura di *harvesting* in produzione, mentre i
*warning* segnalano l'assenza o la non corretta compilazione di
informazioni non indispensabili alla standardizzazione delle risorse, e
al corretto funzionamento della pubblicazione, ma fortemente consigliate
per rendere le risorse semantiche armonizzate e consistenti.

15.4 - Quadro di sintesi - elementi chiave
------------------------------------------

Al fine di sviluppare il Validatore, si è reso innanzitutto necessario
individuare i controlli di validazione da implementare, sulla base di
quelli già effettuati dal processo di *harvesting* al Catalogo.
Successivamente, sono state condotte delle sessioni di progettazione,
volte al miglioramento dell'esperienza utente. Infine, lo strumento è
stato testato in un apposito ambiente di test.

15.5 - Risorse utili
--------------------

Link alla documentazione:

-  `Guida al
   Catalogo <https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/index.html>`__

-  `DCAT Application Profile for data portals in
   Europe <https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/11>`__

-  `Indicazioni su modellazione e metadatazione delle risorse
   semantici <https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/docs/manuale-operativo/indicazioni-su-modellazione-e-metadatazione-degli-asset-semantici.html>`__
