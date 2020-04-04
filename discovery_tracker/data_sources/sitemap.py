import requests
import xmltodict
from tqdm import tqdm


class SitemapParseException(Exception):
    pass


def parse_sitemap(url):
    request = requests.get(url)

    if request.status_code != 200:
        raise SitemapParseException("Status code != 200 for url=%s" % url)

    main_sitemap_doc = xmltodict.parse(request.content)

    if 'sitemapindex' in main_sitemap_doc:
        main_sitemap_entries = main_sitemap_doc["sitemapindex"]['sitemap']
        sitemap_urls = [
            entry['loc']
            for entry in main_sitemap_entries
            if 'loc' in entry
        ]

        return sitemap_urls, []
    elif 'urlset' in main_sitemap_doc:
        main_url_entries = main_sitemap_doc["urlset"]["url"]
        # When the loc element occurs only once, it is returned directly
        if not isinstance(main_url_entries, list):
            main_url_entries = [main_url_entries]

        child_pages_urls = [
            entry['loc']
            for entry in main_url_entries
            if 'loc' in entry
        ]
        return [], child_pages_urls

    assert False, "Invalid document. It should have sitemapindex or urlset element."


def fetch_links(url):
    sitemap_urls, page_urls = parse_sitemap(url)
    print(f"Found {len(sitemap_urls)} sitemaps")

    assert len(sitemap_urls) != 0, "Not found sitemaps"
    all_links = []
    pbar = tqdm(sorted(sitemap_urls))
    for sitemap_url in pbar:
        pbar.set_description("Processing URL: %s" % sitemap_url)
        try:
            child_sitemap_urls, child_page_urls = parse_sitemap(sitemap_url)
            all_links.extend(child_page_urls)
        except SitemapParseException as e:
            print(e)

    return all_links
