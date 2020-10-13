#  출시 노트

이 페이지에는 Container Registry의 프로덕션 업데이트가 정리되어 있습니다. 이 페이지에서는 새로운 기능이나 업데이트된 기능,
버그 수정, 알려진 문제, 지원 중단된 기능에 관한 공지 사항을 정기적으로 확인할 수 있습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. ` https://cloud.google.com/feeds/container-
registry-release-notes.xml `

##  March 16, 2020

**FEATURE:**

Artifact Registry, the evolution of Container Registry, is now available in
beta. It includes support for Docker as well as Maven and npm package formats.

If you currently use Container Registry, see [ Transitioning from Container
Registry ](https://cloud.google.com/artifact-registry/docs/transition-from-
gcr?hl=ko) for more information.

##  September 20, 2019

**FEATURE:**

Container Analysis is now Generally Available.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/container-analysis?hl=ko) for information on how to scan
container images for vulnerabilities as well as how to to store and retrieve
metadata for container images.

##  August 26, 2019

**FEATURE:**

V1 Version of the Container Analysis API is now Generally Available.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/reference/rest/?hl=ko) for details about the API.

##  September 06, 2018

**FEATURE:**

Container Analysis is now available in Beta.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/container-analysis?hl=ko) for information on how to store and
retrieve metadata for container images in Container Registry.

##  November 22, 2017

**FEATURE:**

Container Analysis is now available in Alpha.

See the [ documentation ](https://cloud.google.com/container-
registry/docs/get-image-vulnerabilities?hl=ko) for information on how to get
vulnerability scanning results.

##  October 26, 2017

**FEATURE:**

Pub/Sub notifications feature is now available in Beta. See the [
documentation ](https://cloud.google.com/container-registry/docs/configuring-
notifications?hl=ko) for more information on how to configure notifications.

##  March 01, 2017

**DEPRECATED:**

V1 Version of Docker Registry API is now [ deprecated
](https://cloud.google.com/container-registry/docs/support/deprecation-
notices?hl=ko) .

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

