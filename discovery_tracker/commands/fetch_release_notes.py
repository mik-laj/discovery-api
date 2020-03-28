import re

import html2text
import requests
from bs4 import BeautifulSoup, Tag
from tqdm import tqdm

from discovery_tracker.utils.filesystem import load_text, save_text
from discovery_tracker.utils.git import create_commit

CLOUD_URL = "https://cloud.google.com/"

RELEASE_NOTES_URLS = [
    "https://cloud.google.com/access-context-manager/docs/release-notes",
    "https://cloud.google.com/ai-hub/docs/release-notes",
    "https://cloud.google.com/ai-platform/data-labeling/docs/release-notes",
    "https://cloud.google.com/ai-platform/deep-learning-vm/docs/release-notes",
    "https://cloud.google.com/ai-platform/docs/release-notes",
    "https://cloud.google.com/ai-platform/notebooks/docs/release-notes",
    "https://cloud.google.com/anthos-config-management/docs/release-notes",
    "https://cloud.google.com/anthos/docs/release-notes",
    "https://cloud.google.com/anthos/gke/docs/on-prem/release-notes",
    "https://cloud.google.com/anthos/gke/docs/release-notes",
    "https://cloud.google.com/appengine/docs/admin-api/release-notes",
    "https://cloud.google.com/appengine/docs/flexible/custom-runtimes/release-notes",
    "https://cloud.google.com/appengine/docs/flexible/go/release-notes",
    "https://cloud.google.com/appengine/docs/flexible/php/release-notes",
    "https://cloud.google.com/appengine/docs/standard/go/release-notes",
    "https://cloud.google.com/appengine/docs/standard/go111/release-notes",
    "https://cloud.google.com/appengine/docs/standard/java/release-notes",
    "https://cloud.google.com/appengine/docs/standard/java/release-notes",
    "https://cloud.google.com/appengine/docs/standard/java11/release-notes",
    "https://cloud.google.com/appengine/docs/standard/nodejs/release-notes",
    "https://cloud.google.com/appengine/docs/standard/php/release-notes",
    "https://cloud.google.com/appengine/docs/standard/php7/release-notes",
    "https://cloud.google.com/appengine/docs/standard/python/release-notes",
    "https://cloud.google.com/appengine/docs/standard/python3/release-notes",
    "https://cloud.google.com/appengine/docs/standard/ruby/release-notes",
    "https://cloud.google.com/armor/docs/release-notes",
    "https://cloud.google.com/asset-inventory/docs/release-notes",
    "https://cloud.google.com/automl-tables/docs/release-notes",
    "https://cloud.google.com/bi-engine/docs/release-notes",
    "https://cloud.google.com/bigquery-ml/docs/release-notes",
    "https://cloud.google.com/bigquery-transfer/docs/release-notes",
    "https://cloud.google.com/bigquery/docs/release-notes",
    "https://cloud.google.com/billing/docs/release-notes",
    "https://cloud.google.com/binary-authorization/docs/release-notes",
    "https://cloud.google.com/cdn/docs/release-notes",
    "https://cloud.google.com/cloud-build/docs/release-notes",
    "https://cloud.google.com/cloud-build/release-notes",
    "https://cloud.google.com/code/docs/intellij/release-notes",
    "https://cloud.google.com/composer/docs/release-notes",
    "https://cloud.google.com/compute/docs/release-notes",
    "https://cloud.google.com/compute/docs/security-bulletins",
    "https://cloud.google.com/config-connector/docs/release-notes",
    "https://cloud.google.com/container-optimized-os/docs/release-notes",
    "https://cloud.google.com/container-optimized-os/docs/release-notes/m69",
    "https://cloud.google.com/container-optimized-os/docs/release-notes/m73",
    "https://cloud.google.com/container-registry/docs/release-notes",
    "https://cloud.google.com/data-catalog/docs/release-notes",
    "https://cloud.google.com/data-fusion/docs/release-notes",
    "https://cloud.google.com/dataflow/docs/release-notes",
    "https://cloud.google.com/dataflow/docs/release-notes",
    "https://cloud.google.com/dataflow/docs/release-notes",
    "https://cloud.google.com/dataflow/docs/resources/release-notes-java-2",
    "https://cloud.google.com/dataflow/docs/resources/release-notes-python",
    "https://cloud.google.com/dataflow/docs/resources/release-notes-service",
    "https://cloud.google.com/dataflow/release-notes/release-notes-java-1",
    "https://cloud.google.com/dataprep/docs/release-notes",
    "https://cloud.google.com/datastore/docs/release-notes",
    "https://cloud.google.com/datastore/release-notes",
    "https://cloud.google.com/debugger/docs/release-notes",
    "https://cloud.google.com/deployment-manager/docs/release-notes",
    "https://cloud.google.com/dialogflow/docs/release-notes",
    "https://cloud.google.com/dlp/docs/release-notes",
    "https://cloud.google.com/dns/docs/release-notes",
    "https://cloud.google.com/endpoints/docs/release-notes",
    "https://cloud.google.com/error-reporting/docs/release-notes",
    "https://cloud.google.com/event-threat-detection/docs/release-notes",
    "https://cloud.google.com/filestore/docs/release-notes",
    "https://cloud.google.com/firestore/docs/release-notes",
    "https://cloud.google.com/functions/docs/release-notes",
    "https://cloud.google.com/gke-on-prem/docs/archive/1.0/release-notes",
    "https://cloud.google.com/healthcare/docs/release-notes",
    "https://cloud.google.com/iam/docs/permissions-change-log",
    "https://cloud.google.com/iam/docs/release-notes",
    "https://cloud.google.com/iap/docs/release-notes",
    "https://cloud.google.com/identity-platform/docs/release-notes",
    "https://cloud.google.com/interconnect/docs/release-notes",
    "https://cloud.google.com/iot/docs/release-notes",
    "https://cloud.google.com/istio/docs/istio-on-gke/release-notes",
    "https://cloud.google.com/kms/docs/release-notes",
    "https://cloud.google.com/kubernetes-engine/docs/release-notes",
    "https://cloud.google.com/kubernetes-engine/docs/release-notes-rapid",
    "https://cloud.google.com/kubernetes-engine/docs/release-notes-regular",
    "https://cloud.google.com/kubernetes-engine/docs/release-notes-stable",
    "https://cloud.google.com/kubernetes-engine/docs/security-bulletins",
    "https://cloud.google.com/load-balancing/docs/release-notes",
    "https://cloud.google.com/logging/docs/release-notes",
    "https://cloud.google.com/managed-microsoft-ad/docs/release-notes",
    "https://cloud.google.com/marketplace/docs/partners/release-notes",
    "https://cloud.google.com/marketplace/docs/release-notes",
    "https://cloud.google.com/memorystore/docs/redis/release-notes",
    "https://cloud.google.com/migrate/compute-engine/docs/4.8/release-notes",
    "https://cloud.google.com/monitoring/docs/release-notes",
    "https://cloud.google.com/nat/docs/release-notes",
    "https://cloud.google.com/natural-language/automl/docs/release-notes",
    "https://cloud.google.com/network-intelligence-center/docs/release-notes",
    "https://cloud.google.com/network-tiers/docs/release-notes",
    "https://cloud.google.com/products/operations/docs/release-notes",
    "https://cloud.google.com/profiler/docs/release-notes",
    "https://cloud.google.com/pubsub/docs/release-notes",
    "https://cloud.google.com/recommendations-ai/docs/release-notes",
    "https://cloud.google.com/release-notes",
    "https://cloud.google.com/resource-manager/docs/release-notes",
    "https://cloud.google.com/router/docs/release-notes",
    "https://cloud.google.com/run/docs/gke/release-notes",
    "https://cloud.google.com/run/docs/release-notes",
    "https://cloud.google.com/scheduler/docs/release-notes",
    "https://cloud.google.com/sdk/docs/release-notes",
    "https://cloud.google.com/secret-manager/docs/release-notes",
    "https://cloud.google.com/security-command-center/docs/release-notes",
    "https://cloud.google.com/security-scanner/docs/release-notes",
    "https://cloud.google.com/service-infrastructure/docs/release-notes",
    "https://cloud.google.com/service-mesh/docs/release-notes",
    "https://cloud.google.com/service-usage/docs/release-notes",
    "https://cloud.google.com/source-repositories/docs/release-notes",
    "https://cloud.google.com/spanner/docs/release-notes",
    "https://cloud.google.com/sql/docs/mysql/release-notes",
    "https://cloud.google.com/sql/docs/postgres/release-notes",
    "https://cloud.google.com/sql/docs/release-notes",
    "https://cloud.google.com/sql/docs/sqlserver/release-notes",
    "https://cloud.google.com/stackdriver/docs/release-notes",
    "https://cloud.google.com/storage-transfer/docs/release-notes",
    "https://cloud.google.com/storage/docs/release-notes",
    "https://cloud.google.com/tasks/docs/release-notes",
    "https://cloud.google.com/tools/powershell/docs/release-notes",
    "https://cloud.google.com/tools/visual-studio/docs/release-notes",
    "https://cloud.google.com/trace/docs/release-notes",
    "https://cloud.google.com/traffic-director/docs/release-notes",
    "https://cloud.google.com/translate/automl/docs/release-notes",
    "https://cloud.google.com/translate/docs/release-notes",
    "https://cloud.google.com/velostrata/docs/release-notes",
    "https://cloud.google.com/video-intelligence/automl/docs/release-notes",
    "https://cloud.google.com/video-intelligence/automl/object-tracking/docs/release-notes",
    "https://cloud.google.com/video-intelligence/docs/release-notes",
    "https://cloud.google.com/vision/automl/docs/release-notes",
    "https://cloud.google.com/vision/automl/object-detection/docs/release-notes",
    "https://cloud.google.com/vision/docs/release-notes",
    "https://cloud.google.com/vision/product-search/docs/release-notes",
    "https://cloud.google.com/vpc-service-controls/docs/release-notes",
    "https://cloud.google.com/vpc/docs/networking-release-notes",
    "https://cloud.google.com/vpc/docs/release-notes",
    "https://cloud.google.com/vpn/docs/release-notes",
]


def slugify(s: str) -> str:
    return re.sub('[^0-9a-zA-Z_]+', '_', s)


def url_to_filename(url: str) -> str:
    assert url.startswith(CLOUD_URL)
    url_path = url[len(CLOUD_URL):]
    return slugify(url_path)


def fetch_doc_article(url):
    html_doc = requests.get(url).content
    soup = BeautifulSoup(html_doc, 'html.parser')
    article = soup.select(".devsite-article")[0].extract()
    return article, soup


def enrich_article(article, soup):
    for element in article.select("style, .devsite-article-meta"):
        element.extract()

    add_item_label(soup, article, "CHANGED:", ".release-changed")
    add_item_label(soup, article, "FIXED:", ".release-fixed")
    add_item_label(soup, article, "ISSUE:", ".release-issue")
    add_item_label(soup, article, "BREAKING:", ".release-breaking")
    add_item_label(soup, article, "DEPRECATED:", ".release-deprecated")
    add_item_label(soup, article, "FEATURE:", ".release-feature")

    for element in article.descendants:
        if isinstance(element, Tag):
            element.smooth()


def add_item_label(soup, article, label_text, selector):
    for element in article.select(selector):
        label = soup.new_tag("strong")
        label.string = label_text
        element.insert(0, label)


def cmd_fetch_release_notes(args):
    output = args.output
    fileformat = args.format
    assert fileformat in ('md', 'html')

    pbar = tqdm(RELEASE_NOTES_URLS)
    for release_notes_url in pbar:
        process_release_note(output, release_notes_url, fileformat=fileformat)


def process_release_note(output, release_notes_url, fileformat):
    file_slug = url_to_filename(release_notes_url)
    output_file = f"{output}/{file_slug}.{fileformat}"

    article, soup = fetch_doc_article(release_notes_url)
    enrich_article(article, soup)
    html_content = article.prettify()
    if fileformat == 'md':
        content = html2text.html2text(html_content)
    else:
        content = html_content

    old_content = load_text(output_file)
    if old_content != content:
        save_text(output_file, content)
        create_commit(
            message=f"Update release note ({fileformat}) - {file_slug}",
            files=[output_file]
        )
