#  リリースノート

このページには、Container Registry
に関する本番環境の更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/container-registry-release-
notes.xml ` を直接追加します。

##  March 16, 2020

**FEATURE:**

Artifact Registry, the evolution of Container Registry, is now available in
beta. It includes support for Docker as well as Maven and npm package formats.

If you currently use Container Registry, see [ Transitioning from Container
Registry ](https://cloud.google.com/artifact-registry/docs/transition-from-
gcr?hl=ja) for more information.

##  September 20, 2019

**FEATURE:**

Container Analysis is now Generally Available.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/container-analysis?hl=ja) for information on how to scan
container images for vulnerabilities as well as how to to store and retrieve
metadata for container images.

##  August 26, 2019

**FEATURE:**

V1 Version of the Container Analysis API is now Generally Available.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/reference/rest/?hl=ja) for details about the API.

##  September 06, 2018

**FEATURE:**

Container Analysis is now available in Beta.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/container-analysis?hl=ja) for information on how to store and
retrieve metadata for container images in Container Registry.

##  November 22, 2017

**FEATURE:**

Container Analysis is now available in Alpha.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/get-image-vulnerabilities?hl=ja) for information on how to get
vulnerability scanning results.

##  October 26, 2017

**FEATURE:**

Pub/Sub notifications feature is now available in Beta. See the [
documentation ](https://cloud.google.com/container-registry/docs/configuring-
notifications?hl=ja) for more information on how to configure notifications.

##  March 01, 2017

**DEPRECATED:**

V1 Version of Docker Registry API is now [ deprecated
](https://cloud.google.com/container-registry/docs/support/deprecation-
notices?hl=ja) .

##  November 29, 2016

**FEATURE:**

Container Registry now supports the Docker [ V2 image manifest, schema version
2 ](https://docs.docker.com/registry/spec/manifest-v2-2/) .

##  August 05, 2016

**CHANGED:**

The Docker client now allows users to specify a _credential store_ , which
acts as a delegate to generate the credentials that are used to authenticate
requests to repositories. The Container Registry credential helper, [ docker-
credential-gcr ](https://github.com/GoogleCloudPlatform/docker-credential-gcr)
, simplifies authentication for all use cases, including working on a
developer machine, working on a VM, and using a service account. This means
you no longer have to use the Cloud SDK with Container Registry.

##  July 31, 2016

**FEATURE:**

Added the Registry API ` catalog ` command. Container Registry now implements
the catalog feature as described by the [ Docker Registry API specification
](https://docs.docker.com/registry/spec/api/) .

##  June 22, 2016

**FEATURE:**

Container Registry now offers a Docker Hub mirror. When a user adds the `
--registry-mirror=https://<us|eu|asia>-mirror.gcr.io ` flag to their Docker
daemon, any attempt to pull an image from Docker Hub results in a call to
Container Registry. If the image is found in the Container Registry mirror, it
is pulled from there, and no call is made to Docker Hub. If the image is not
found, the client gets a 404 result and can then make a call to Docker Hub to
download the image.

##  June 13, 2016

**CHANGED:**

The Container Registry user interface now shows Docker Registry V2 image
formats and V2 image digests.

##  November 13, 2015

**FEATURE:**

Implemented V2 of the Docker Registry API. See [ Docker Registry HTTP API V2
](https://docs.docker.com/registry/spec/api/) .

##  June 22, 2015

**CHANGED:**

Container Registry moved from Beta to GA.

##  November 12, 2014

**FEATURE:**

Container Registry Beta.

Container Registry is a new service that provides private container
repositories for Google Cloud Platform customers to support container
development and deployment workflows. Container Registry is currently in Beta;
it is suitable for experimentation and is intended to provide an early view of
the production service, but customers are strongly encouraged not to run
production workloads on it.

