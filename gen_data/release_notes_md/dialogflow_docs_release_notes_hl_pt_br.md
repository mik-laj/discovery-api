#  Notas da versão

Nesta página, você verá as atualizações de produção do Dialogflow.
Recomendamos que os desenvolvedores do Dialogflow consultem esta lista
periodicamente para saber das novidades. As principais mudanças também serão
anunciadas no [ Cloud Blog: IA e aprendizado de máquina
](https://cloud.google.com/blog/products/ai-machine-learning?hl=pt_br) (em
inglês).

**Observação:** é possível ler as [ notas da versão de histórico
](https://cloud.google.com/dialogflow/docs/data/historic-release-
notes.pdf?hl=pt_br) anteriores a 16 de novembro de 2017.

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt_br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/dialogflow-release-
notes.xml `

##  August 10, 2020

**FEATURE:**

Beta launch of [ regionalization and data residency
](https://cloud.google.com/dialogflow/docs/how/region?hl=pt_br) .

##  July 30, 2020

**FEATURE:**

GA (general availability) launch of [ mega agents
](https://cloud.google.com/dialogflow/docs/agents-mega?hl=pt_br) .

**FEATURE:**

Beta launch of the [ Facebook Workplace integration
](https://cloud.google.com/dialogflow/docs/integrations/workplace?hl=pt_br) .

##  July 27, 2020

**FEATURE:**

Beta launch of [ Dialogflow Messenger
](https://cloud.google.com/dialogflow/docs/integrations/dialogflow-
messenger?hl=pt_br) . This new integration provides a customizable chat dialog
for your agent that can be embedded in your website.

##  July 23, 2020

**DEPRECATED:**

Amazon Alexa importer and exporter are no longer supported.

##  July 06, 2020

**FEATURE:**

The Dialogflow Console has been upgraded with an improved [ Analytics page
](https://cloud.google.com/dialogflow/docs/analytics?hl=pt_br) (Beta) that
provides new metrics and data views.

##  June 29, 2020

**DEPRECATED:**

The V1 API is in the process of a gradual shutdown. See the [ November 14,
2019 release note ](https://cloud.google.com/dialogflow/docs/release-
notes?hl=pt_br#November_14_2019) for details.

##  June 01, 2020

**CHANGED:**

The shutdown of 7 integrations [ announced in January
](https://cloud.google.com/dialogflow/docs/release-
notes?hl=pt_br#January_06_2020) is now extended to July 6th, 2020.

##  May 29, 2020

**CHANGED:**

The [ Dialogflow Facebook Messenger integration
](https://cloud.google.com/dialogflow/docs/integrations/facebook?hl=pt_br) has
been updated to to be compliant with newer Facebook Messenger API versions. If
you have an agent that enabled this integration prior to today, you should
have received an email from Dialogflow with upgrade instructions. If you have
not received this email, please [ contact Dialogflow support
](https://cloud.google.com/dialogflow/docs/support/getting-support?hl=pt_br) .

##  May 17, 2020

**CHANGED:**

Old Node.js client library require statements must be updated. Your require
statements should look like this:

` const dialogflow = require('@google-cloud/dialogflow').v2; `

or this:

` const dialogflow = require('@google-cloud/dialogflow').v2beta1; `

Old syntax that does not include ` @google-cloud ` is now deprecated. The old
syntax will continue to work, but you will not receive updates.

##  May 08, 2020

**FEATURE:**

Beta launch of a one-click integration with the [ Voximplant
](https://cloud.google.com/dialogflow/docs/integrations/voximplant?hl=pt_br)
telephony partner:

##  May 05, 2020

**FEATURE:**

GA (general availability) launch of [ auto speech adaptation
](https://cloud.google.com/dialogflow/docs/speech-adaptation?hl=pt_br) .

##  April 30, 2020

**FEATURE:**

Beta launch of a one-click integration with a new telephony partner:

  * [ Avaya ](https://cloud.google.com/dialogflow/docs/integrations/avaya?hl=pt_br)

##  April 25, 2020

**CHANGED:**

In May 2020, the [ Facebook Messenger
](https://cloud.google.com/dialogflow/docs/integrations/facebook?hl=pt_br)
integration will be updated, and you may notice slight changes related to
fulfillment.

To make sure that your Facebook Messenger bot keeps functioning normally,
observe the following recommendations:

  1. To get the Facebook ` sender.id ` value, use the ` originalDetectIntentRequest.payload.data.sender ` field from the Dialogflow ` WebhookRequest ` message. 
  2. To get the ` source ` field value, use the ` originalDetectIntentRequest.source ` field from the Dialogflow ` WebhookRequest ` message. 
  3. To send rich response messages from your webhook to the Facebook Messenger integration, use the ` WebhookResponse.fulfillment_mesages[].payload ` field. 
  4. In your webhook logic, don’t rely on the fields that are not documented in the official [ Facebook Messenger API ](https://developers.facebook.com/docs/messenger-platform/reference/) . 

If you have any questions, reach out to your primary [ support channel
](https://cloud.google.com/dialogflow/docs/support/getting-
support?hl=pt_br#one-on-one) .

##  April 20, 2020

**FEATURE:**

Beta launch of one-click integrations with two telephony partners:

  * [ AudioCodes ](https://cloud.google.com/dialogflow/docs/integrations/audiocodes?hl=pt_br)
  * [ SignalWire ](https://cloud.google.com/dialogflow/docs/integrations/signalwire?hl=pt_br)

##  March 31, 2020

**CHANGED:**

When using fulfillment, the ` WebhookResponse.payload ` field can now only be
used for two cases:

  * Custom data sent from your webhook service to a Dialogflow API caller. 
  * Google Assitant integration custom payload rich response messages. 

For all other [ custom payload rich response messages
](https://cloud.google.com/dialogflow/docs/intents-rich-
messages?hl=pt_br#custom) , you should use the `
WebhookResponse.fulfillment_mesages[].payload ` field.

##  March 27, 2020

**CHANGED:**

The shutdown of the V1 API [ announced in November
](https://cloud.google.com/dialogflow/docs/release-
notes?hl=pt_br#November_14_2019) has been extended to May 31, 2020,

##  March 13, 2020

**CHANGED:**

On March 16, 2020, the [ Inline Editor
](https://cloud.google.com/dialogflow/docs/fulfillment-inline-editor?hl=pt_br)
will use [ Cloud Functions ](https://cloud.google.com/functions/docs?hl=pt_br)
instead of [ Cloud Functions for Firebase
](https://firebase.google.com/docs/functions?hl=pt_br) .

##  March 10, 2020

**CHANGED:**

Event names are now [ limited to 150 characters
](https://cloud.google.com/dialogflow/quotas?hl=pt_br#length_limits) .

##  February 19, 2020

**FEATURE:**

GA (general availability) launch of [ versions and environments
](https://cloud.google.com/dialogflow/docs/agents-versions?hl=pt_br) .

**FEATURE:**

GA (general availability) launch of [ agent validation
](https://cloud.google.com/dialogflow/docs/agents-validation?hl=pt_br) .

**FEATURE:**

You can now update fulfillment settings with the API. For more information,
visit the [ agent reference
](https://cloud.google.com/dialogflow/docs/reference/common-
types?hl=pt_br#agents) and click the link for your protocol or client library
language.

##  January 31, 2020

**FEATURE:**

Beta launch of [ mega agents
](https://cloud.google.com/dialogflow/docs/agents-mega?hl=pt_br) to combine
multiple sub-agents agents into a single mega agent.

##  January 06, 2020

**DEPRECATED:**

The following [ integrations
](https://cloud.google.com/dialogflow/docs/integrations/?hl=pt_br) are now
deprecated and will be shut down on ~~April 6th, 2020~~ ~~May 6th, 2020~~
~~June 6th, 2020~~ July 6th, 2020 :

  * Kik 
  * Skype 
  * Spark 
  * Twilio IP Messaging 
  * Twilio (Text Messaging) 
  * Twitter 
  * Viber 

Your live bots that use these integrations will stop working unless you take
action. The implementations of these integrations have moved to open source.
To continue using these integrations, follow the instructions at the [ GitHub
repository ](https://github.com/GoogleCloudPlatform/dialogflow-integrations) .

##  December 19, 2019

**CHANGED:**

If you use the [ Telegram
](https://cloud.google.com/dialogflow/docs/integrations/telegram?hl=pt_br)
integration, and the bot was created before August 19th, 2019, you must
restart the integration in the Dialogflow console by February 28th, 2020. To
restart it, perform the following steps for all your agents that use Telegram:

  1. Make sure you don't change or delete your current token on the Telegram side. 
  2. Open the agent in the Dialoglow Console. 
  3. In the integration settings, click the **STOP** button. 
  4. Then click the **START** button. 

##  December 04, 2019

**FEATURE:**

You can now use [ Mutual TLS authentication
](https://cloud.google.com/dialogflow/docs/fulfillment-mtls?hl=pt_br) to
ensure that webhook traffic is both secure and trusted.

**DEPRECATED:**

The Cortana exporter has been removed from the console.

##  November 14, 2019

**CHANGED:**

We are extending the V1 API shutdown deadline to ~~March 31st, 2020~~ May
31st, 2020. Migrate to the V2 API as described [ here
](https://dialogflow.com/docs/reference/v1-v2-migration-guide?hl=pt_br) .

If you use Dialogflow exclusively for Actions on Google, you don't need to
migrate your agent to the V2 API. However, note the following changes:

  * The Dialogflow simulator will show responses in the V2 format and the "Copy curl" button will generate requests in the V2 format. This should have no impact on the functionality of the Actions on Google simulator. 
  * You will no longer be able to call API methods for the V1 [ intents ](https://dialogflow.com/docs/reference/agent/intents?hl=pt_br) and [ entities ](https://dialogflow.com/docs/reference/agent/entities?hl=pt_br) resources. You will still be able to modify your agent using the Dialogflow Console. 

##  October 17, 2019

**CHANGED:**

When calling the API to provide an intent priority value, the behavior has
changed to the following:

  * If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the ` Normal ` priority in the console. 
  * If the supplied value is negative, the intent is ignored in runtime detect intent requests. 

Prior to this change, a value of 0 was stored as-is by the service. Any agents
created before this change may still have intent priority values of 0. For
runtime detect intent requests, a value of 0 is treated as -1, and the intent
is ignored.

##  October 01, 2019

**FEATURE:**

You can now [ create session entities with fulfillment
](https://cloud.google.com/dialogflow/docs/entities-session?hl=pt_br) .

**FEATURE:**

You can now disable automatic agent training. See the [ ML settings
](https://cloud.google.com/dialogflow/docs/agents-settings?hl=pt_br#ml) for
details.

##  September 20, 2019

**FEATURE:**

Beta launch of [ Agent Validation
](https://cloud.google.com/dialogflow/docs/agents-validation?hl=pt_br) to
check your agent for quality and correctness.

##  September 19, 2019

**FEATURE:**

You can now use [ System entity extension
](https://cloud.google.com/dialogflow/docs/entities-system-extension?hl=pt_br)
to extend system entities with custom values.

##  September 13, 2019

**FEATURE:**

You can now use [ Regexp entities
](https://cloud.google.com/dialogflow/docs/entities-regexp?hl=pt_br) to
provide regular expressions for matching entities.

**FEATURE:**

You can now use [ Fuzzy matching
](https://cloud.google.com/dialogflow/docs/entities-fuzzy?hl=pt_br) to allow
flexibility with word ordering for multi-word entities.

##  July 23, 2019

**FEATURE:**

Beta launch of [ Auto speech adaptation
](https://cloud.google.com/dialogflow/docs/speech-adaptation?hl=pt_br) to
improve the speech recognition accuracy of your agent.

##  June 13, 2019

**FEATURE:**

You can now create and update agents with the API. See the [ Agents type
reference ](https://cloud.google.com/dialogflow/docs/reference/common-
types?hl=pt_br#agents) .

##  May 23, 2019

**FEATURE:**

GA (general availability) launch of [ Speech response
](https://cloud.google.com/dialogflow/docs/detect-intent-tts?hl=pt_br) .

**FEATURE:**

GA (general availability) launch of [ Sentiment analysis
](https://cloud.google.com/dialogflow/docs/sentiment?hl=pt_br) .

**CHANGED:**

[ Pricing ](https://cloud.google.com/dialogflow/pricing?hl=pt_br) and [ Quotas
](https://cloud.google.com/dialogflow/quotas?hl=pt_br) have been updated for
speech response and sentiment analysis.

**FEATURE:**

All REST command line samples in documentation now include both curl (Linux,
macOS) and PowerShell (Windows) commands.

##  May 15, 2019

**FEATURE:**

Integration with [ Hangouts Chat
](https://cloud.google.com/dialogflow/docs/integrations/hangouts?hl=pt_br) is
now supported.

##  April 18, 2019

**FEATURE:**

The new ` @sys.person ` [ system entity
](https://cloud.google.com/dialogflow/docs/reference/system-entities?hl=pt_br)
has been added to all languages except Portuguese and Ukrainian. It is used
for given names, last names, or their combinations. You should start using `
@sys.person ` instead of the existing ` @sys.given-name ` and ` @sys.last-name
` system entities.

##  January 15, 2019

**FEATURE:**

Added support for Polish, including new [ system entities
](https://cloud.google.com/dialogflow/docs/reference/system-entities?hl=pt_br)
and [ pre-defined follow-up intents
](https://cloud.google.com/dialogflow/docs/reference/follow-up-intent-
expressions?hl=pt_br) .

##  December 18, 2018

**FEATURE:**

Added support for Turkish, including new [ system entities
](https://cloud.google.com/dialogflow/docs/reference/system-entities?hl=pt_br)
and [ pre-defined follow-up intents
](https://cloud.google.com/dialogflow/docs/reference/follow-up-intent-
expressions?hl=pt_br) .

**DEPRECATED:**

You can no longer annotate training phrases with some locale-specific
entities. These entities are marked as deprecated in the [ system entities
](https://cloud.google.com/dialogflow/docs/reference/system-entities?hl=pt_br)
documentation. However, if you already have training phrases annotated with
these entities in your existing agents, they will continue to function
properly.

##  December 04, 2018

**DEPRECATED:**

Template mode has been deprecated. Example mode is the only supported way to
create new training phrases. If you have existing training phrases that you've
created in template mode, those will continue to work. For more information,
see [ Example and template modes
](https://cloud.google.com/dialogflow/docs/intents-training-
phrases?hl=pt_br#example_and_template_modes)

##  September 20, 2018

**FEATURE:**

Added zh-TW machine learning support.

##  August 09, 2018

**FEATURE:**

The Dialogflow Enterprise Edition _Plus_ pricing plan is now available. See [
Editions ](https://cloud.google.com/dialogflow/docs/editions?hl=pt_br) for
details.

##  July 24, 2018

**FEATURE:**

Beta launch of [ Adding Speech Response to Detect Intent Requests
](https://cloud.google.com/dialogflow/docs/detect-intent-tts?hl=pt_br)

**FEATURE:**

Beta launch of [ Adding Sentiment Analysis to Detect Intent Requests
](https://cloud.google.com/dialogflow/docs/sentiment?hl=pt_br)

**FEATURE:**

Beta launch of [ Knowledge Connectors
](https://cloud.google.com/dialogflow/docs/knowledge-connectors?hl=pt_br)

**FEATURE:**

Beta launch of [ Telephony Gateway
](https://cloud.google.com/dialogflow/docs/telephony?hl=pt_br)

**FEATURE:**

Beta launch of [ Data Logging and Enhanced Speech Models
](https://cloud.google.com/dialogflow/docs/concepts/data-logging?hl=pt_br)

**FEATURE:**

Beta launch of [ Automatic Spell Correction
](https://cloud.google.com/dialogflow/docs/agents-
settings?hl=pt_br#ml_settings_machine_learning)

##  May 08, 2018

**FEATURE:**

The [ Versions and Environments
](https://cloudplatform.googleblog.com/2018/05/Dialogflow-adds-versioning-and-
other-new-features-to-help-enterprises-build-vibrant-conversational-
experiences.html) beta feature has launched.

**FEATURE:**

You can now enable and view [ Stackdriver logs
](https://cloud.google.com/dialogflow/docs/history?hl=pt_br#webhook_errors_in_stackdriver_logs)
for your fulfillment.

**FEATURE:**

When a phrase is matched to an intent when it shouldn't be, you can now
designate it as a [ negative example
](https://cloud.google.com/dialogflow/docs/intents-
default?hl=pt_br#default_fallback_intent) and add it to the Default Fallback
Intent.

**FEATURE:**

The following geography system entities have been added to pt-BR, Nl, Ko, Hi,
Id, Th, No, Sv, and Da languages: @sys.geo-country, @sys.geo-city, and
@sys.geo-capital.

##  April 17, 2018

**CHANGED:**

The Dialogflow V2 API is now GA (general availability). See [ the GCP blog
post ](https://cloudplatform.googleblog.com/2018/04/Dialogflow-Enterprise-
Edition-is-now-generally-available.html) for details. Users of the V2beta1 API
are encouraged to migrate to the V2 API. See [ Migrating code from Dialogflow
V2beta1 to V2
](https://cloud.google.com/dialogflow/docs/migrating?hl=pt_br#v2beta1-to-v2)
for instructions. The V2beta1 API will continue to be a beta channel for the
stable V2 API. If you plan to continue using V2beta1, see the migration
instructions which describe how enabling ML will become the default.

##  March 29, 2018

**FEATURE:**

We added additional system entities for the following languages:

  * Hindi (hi) 
  * Thai (th) 
  * Indonesian (id) 
  * Swedish (sv) 
  * Danish (da) 
  * Norwegian (no) 

##  February 22, 2018

**FEATURE:**

We added additional support for these languages:

  * Hindi (hi) 
  * Thai (th) 
  * Indonesian (id) 
  * Swedish (sv) 
  * Danish (da) 
  * Norwegian (no) 

We added ML support for these languages:

  * Brazilian Portuguese (br-PT) 
  * Korean (ko) 
  * Dutch (nl) 

##  December 01, 2017

**FEATURE:**

We added new prebuilt agents: banking, easter egg, mobile account, and online
shopping

**CHANGED:**

We updated these prebuilt agents: flights (added FAQ) and profile bot (renamed
to "Job Interview").

##  November 16, 2017

**FEATURE:**

Dialogflow Beta release.

