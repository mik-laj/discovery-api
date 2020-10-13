#  リリースノート

このページでは、Speech-to-Text
に関する本番環境の更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/speech-release-notes.xml `
を直接追加します。

##  March 05, 2020

**FEATURE:**

Cloud Speech-to-Text now supports seven new [ languages
](https://cloud.google.com/speech-to-text/docs/languages?hl=ja) : Burmese,
Estonian, Uzbek, Punjabi, Albanian, Macedonian, and Mongolian.

**FEATURE:**

The [ speaker diarization ](https://cloud.google.com/speech-to-
text/docs/multiple-voices?hl=ja) , [ automatic punctuation
](https://cloud.google.com/speech-to-text/docs/automatic-punctuation?hl=ja) ,
[ speech adaptation boost ](https://cloud.google.com/speech-to-
text/docs/boost?hl=ja) , and [ enhanced telephony model
](https://cloud.google.com/speech-to-text/docs/enhanced-models?hl=ja) features
are now available for new languages. See the supported [ languages page
](https://cloud.google.com/speech-to-text/docs/languages?hl=ja) for a complete
list.

**CHANGED:**

[ Class tokens ](https://cloud.google.com/speech-to-text/docs/class-
tokens?hl=ja) are now available for general use. You can use class tokens with
[ speech adaptation ](https://cloud.google.com/speech-to-text/docs/speech-
adaptation?hl=ja#classes) to help the model recognize concepts in your
recorded audio data.

##  November 26, 2019

**CHANGED:**

[ Automatic punctuation ](https://cloud.google.com/speech-to-
text/docs/automatic-punctuation?hl=ja) is now available for general use. Cloud
Speech-to-Text can insert punctuation into transcription results, including
commas, periods, and question marks.

##  July 23, 2019

**FEATURE:**

Cloud Speech-to-Text has several [ endless streaming tutorials
](https://cloud.google.com/speech-to-text/docs/endless-streaming-
tutorial?hl=ja) that demonstrate how to transcribe an infinite audio stream.

**FEATURE:**

You can now use [ speech adaptation ](https://cloud.google.com/speech-to-
text/docs/context-strength?hl=ja) to provide 'hints' to Cloud Speech-to-Text
when it performs speech recognition. This feature is now in beta.

##  June 18, 2019

**FEATURE:**

Cloud Speech-to-Text now has expanded to a 5 minute limit for [ streaming
recognition ](https://cloud.google.com/speech-to-text/docs/streaming-
recognize?hl=ja) . To use streaming recognition with the 5 minute limit, you
must use the [ ` v1p1beta1 ` ](https://cloud.google.com/speech-to-
text/docs/reference/rpc/google.cloud.speech.v1p1beta1?hl=ja#speech) API
version.

**FEATURE:**

Cloud Speech-to-Text now supports transcription of [ MP3 encoded audio data
](https://cloud.google.com/speech-to-text/docs/encoding?hl=ja) . As this
feature is in beta, you must use the [ ` v1p1beta1 `
](https://cloud.google.com/speech-to-
text/docs/reference/rpc/google.cloud.speech.v1p1beta1?hl=ja#speech) API
version.

##  April 04, 2019

**DEPRECATED:**

The ` v1beta ` version of the service is no longer available for use. You must
migrate your solutions to either the [ ` v1 `
](https://cloud.google.com/speech-to-
text/docs/reference/rpc/google.cloud.speech.v1?hl=ja) or [ ` v1p1beta1 `
](https://cloud.google.com/speech-to-
text/docs/reference/rpc/google.cloud.speech.v1p1beta1?hl=ja) version of the
API.

##  February 20, 2019

**FEATURE:**

[ Data logging ](https://cloud.google.com/speech-to-text/docs/data-
logging?hl=ja) is now available for general use. When you enable data logging,
you can reduce the cost of using Cloud Speech-to-Text by allowing Google to
log your data in order to improve the service.

**FEATURE:**

[ Enhanced models ](https://cloud.google.com/speech-to-text/docs/enhanced-
models?hl=ja) are now available for general use. Using enhanced models can
improve audio transcription results.

**CHANGED:**

Using [ enhanced models ](https://cloud.google.com/speech-to-
text/docs/enhanced-models?hl=ja) no longer requires you to opt-in for data
logging. Enhanced models are available for use by any transcription requests
for a different [ price ](https://cloud.google.com/speech-to-
text/pricing?hl=ja) as standard models.

**FEATURE:**

[ Selecting a transcription model ](https://cloud.google.com/speech-to-
text/docs/transcription-model?hl=ja) is now available for general use. You can
select different speech recognition models when you send a request to Cloud
Speech-to-Text, including a model optimized for transcribing audio data from
video files.

**FEATURE:**

Cloud Speech-to-Text can transcribe audio data that includes [ multiple
channels ](https://cloud.google.com/speech-to-text/docs/multi-channel?hl=ja) .
This feature is now available for general use.

**FEATURE:**

You can now include more details about your audio source files in
transcription requests to Cloud Speech-to-Text in the form of [ recognition
metadata ](https://cloud.google.com/speech-to-text/docs/recognition-
metadata?hl=ja) , which can improve the results of the speech recognition.
This feature is now available for general use.

##  July 24, 2018

**FEATURE:**

Cloud Speech-to-Text provides [ word-level confidence
](https://cloud.google.com/speech-to-text/docs/word-confidence?hl=ja)
Developers can use this feature to get the degree of confidence on a word-by-
word level. This feature is in Beta.

**FEATURE:**

Cloud Speech-to-Text can automatically detect the language used in an audio
file. To use this feature, developers must specify [ alternative languages
](https://cloud.google.com/speech-to-text/docs/multiple-languages?hl=ja) in
their transcription request. This feature is in Beta.

**FEATURE:**

Cloud Speech-to-Text can [ identify different speakers
](https://cloud.google.com/speech-to-text/docs/multiple-voices?hl=ja) present
in an audio file. This feature is in Beta.

**FEATURE:**

Cloud Speech-to-Text can transcribe audio data that includes [ multiple
channels ](https://cloud.google.com/speech-to-text/docs/multi-channel?hl=ja) .
This feature is in Beta.

##  April 09, 2018

**FEATURE:**

Cloud Speech-to-Text now provides [ data logging
](https://cloud.google.com/speech-to-text/docs/data-logging?hl=ja) and [
enhanced models ](https://cloud.google.com/speech-to-text/docs/enhanced-
models?hl=ja) . Developers that want to take advantage of the enhanced speech
recognition models can [ opt-in for data logging
](https://cloud.google.com/speech-to-text/docs/data-logging-terms?hl=ja) .
This feature is in Beta.

**FEATURE:**

Cloud Speech-to-Text can insert [ punctuation
](https://cloud.google.com/speech-to-text/docs/automatic-punctuation?hl=ja)
into transcription results, including commas, periods, and question marks.
This feature is in Beta.

**FEATURE:**

You can now select different speech recognition models when you send a request
to Cloud Speech-to-Text, including a model optimized for [ transcribing audio
from video files ](https://cloud.google.com/speech-to-text/docs/video-
model?hl=ja) . This feature is in Beta.

**FEATURE:**

You can now include more details about your audio source files in
transcription requests to Cloud Speech-to-Text in the form of [ recognition
metadata ](https://cloud.google.com/speech-to-text/docs/recognition-
metadata?hl=ja) , which can improve the results of the speech recognition.
This feature is in Beta.

##  January 16, 2018

**FEATURE:**

Support for the ` OGG_OPUS ` audio encoding has been expanded to support 8000
Hz, 12000 Hz, 16000 Hz, 24000 Hz, or 48000 Hz.

##  August 10, 2017

**FEATURE:**

Time offsets (timestamps) are now available. Set the ` enableWordTimeOffsets `
parameter to true in your request configuration and Cloud Speech-to-Text will
include time offset values for the beginning and end of each spoken word that
is recognized in the audio for your request. For more information, see [ Time
offsets (timestamps) ](https://cloud.google.com/speech-to-
text/docs/basics?hl=ja#time-offsets) .

**CHANGED:**

Cloud Speech-to-Text has added recognition support for 30 new languages. For a
complete list of all supported languages, see the [ language support reference
](https://cloud.google.com/speech-to-text/docs/languages?hl=ja) .

**CHANGED:**

The limit on the length of audio that you can send with an asynchronous
recognition request has been increased from ~80 to ~180 minutes. For
information on Cloud Speech-to-Text limits, see the [ quotas & limits
](https://cloud.google.com/speech-to-text/quotas?hl=ja) . For more information
on asynchronous recognition requests, see the [ transcribing long audio files
guide ](https://cloud.google.com/speech-to-text/docs/async-recognize?hl=ja) .

##  April 18, 2017

**FEATURE:**

Release of Cloud Speech-to-Text v1.

**CHANGED:**

The ` v1beta1 ` release of Cloud Speech-to-Text has been deprecated. The `
v1beta1 ` endpoint continues to be available for a period of time as defined
in the [ terms of service ](https://cloud.google.com/terms?hl=ja) . To avoid
being impacted when the ` v1beta1 ` is discontinued, replace references to `
v1beta1 ` in your code with ` v1 ` and update your code with valid ` v1 ` API
names and values.

**CHANGED:**

A ` language_code ` is now required with requests to Cloud Speech-to-Text.
Requests with a missing or invalid ` language_code ` will return an error.
(Pre-release versions of the API used ` en-US ` if the ` language_code ` was
omitted from the request.)

**CHANGED:**

` SyncRecognize ` is renamed to ` Recognize ` . ` v1beta1/speech:syncrecognize
` is renamed to ` v1/speech:recognize ` . The behavior is unchanged.

**CHANGED:**

The ` sample_rate ` field has been renamed to ` sample_rate_hertz ` . The
behavior is unchanged.

**CHANGED:**

The ` EndpointerType ` enum has been renamed to ` SpeechEventType ` .

The following ` SpeechEventType ` enums have been removed.

  * ` START_OF_SPEECH `
  * ` END_OF_SPEECH `
  * ` END_OF_AUDIO `

**CHANGED:**

The ` END_OF_UTTERANCE ` enum has been renamed to ` END_OF_SINGLE_UTTERANCE `
. The behavior is unchanged.

**CHANGED:**

The ` result_index field ` has been removed.

**CHANGED:**

The ` speech_context ` field has been replaced by the ` speech_contexts `
field, which is a repeated field. However, you can specify, at most, one
speech context. The behavior is unchanged.

**CHANGED:**

The ` SPEEX_WITH_HEADER_BYTE ` and ` OGG_OPUS ` codecs have been added to
support audio encoder implementations for legacy applications. We do not
recommend using lossy codes, as they result in a lower-quality speech
transcription. If you must use a low-bitrate encoder, ` OGG_OPUS ` is
preferred.

**CHANGED:**

You are no longer required to specify the encoding and sample rate for WAV or
FLAC files. If omitted, Cloud Speech-to-Text automatically determines the
encoding and sample rate for WAV or FLAC files based on the file header. If
you specify an encoding or sample rate value that does not match the value in
the file header, then Cloud Speech-to-Text will return an error. This change
is backwards-compatible and will not invalidate any currently valid requests.

