import re

import html2text
import requests
from bs4 import BeautifulSoup, Tag
from tqdm import tqdm

from discovery_tracker.data_sources.sitemap import fetch_links
from discovery_tracker.utils.filesystem import load_text, save_text
from discovery_tracker.utils.git import create_commit

CLOUD_URL = "https://cloud.google.com/"
CLOUD_SITEMAP_URL = "https://cloud.google.com/sitemap.xml"

RELEASE_NOTES_URL_KEYWORDS = [
    'release-notes', 'security-bulletins', 'permissions-change-log'
]


def fetch_release_note_list():
    all_links = fetch_links(CLOUD_SITEMAP_URL)
    print(f"Found {len(all_links)} links")
    release_notes_links = [
        url
        for url in all_links
        if any((kw in url) for kw in RELEASE_NOTES_URL_KEYWORDS)
    ]
    return release_notes_links


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
    for element in article.select("style, .devsite-article-meta, devsite-page-rating, devsite-feedback"):
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
    release_notes_urls = fetch_release_note_list()
    print(f"Found {len(release_notes_urls)} release notes")
    pbar = tqdm(sorted(release_notes_urls))
    for release_notes_url in pbar:
        pbar.set_description("Processing URL: %s" % release_notes_url)
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
