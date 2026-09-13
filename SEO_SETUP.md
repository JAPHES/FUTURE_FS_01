# Search visibility setup for Japhestech

The site now has the technical foundation Google needs: descriptive page titles,
unique descriptions, canonical URLs, crawlable service links, JSON-LD structured
data, a robots file, and an XML sitemap. Complete the account-level steps below
after the new deployment is live.

## 1. Add the site to Google Search Console

1. Open <https://search.google.com/search-console> and sign in with the Google
   account that should own the portfolio property.
2. Choose **Add property**.
3. Select **Domain** and enter `japhes.secora.dev`.
4. Copy Google's TXT verification record into the DNS manager that controls the
   subdomain, then select **Verify** in Search Console.
5. If DNS verification is unavailable, add a **URL-prefix** property for
   `https://japhes.secora.dev/` instead. Search Console will show the alternative
   verification methods.

Keep the verification DNS record in place after verification succeeds.

## 2. Submit the XML sitemap

1. Open the verified property in Search Console.
2. Select **Sitemaps**.
3. Enter `sitemap.xml` and submit it.
4. Confirm that Search Console can read this URL:
   <https://japhes.secora.dev/sitemap.xml>.

The sitemap contains the homepage and the five canonical service pages. Sitemap
submission is a discovery signal, not a guarantee that every page will be indexed.

## 3. Request indexing for the priority pages

Use **URL inspection** in Search Console for each URL below. Run **Test live URL**
and then choose **Request indexing**.

- <https://japhes.secora.dev/>
- <https://japhes.secora.dev/services/web-application-development/>
- <https://japhes.secora.dev/services/ui-ux-design/>
- <https://japhes.secora.dev/services/mentorship-training/>
- <https://japhes.secora.dev/services/backend-api-development/>
- <https://japhes.secora.dev/services/iot-projects/>

Do this once after deployment. Repeated requests do not make crawling faster.

## 4. Validate search markup

1. Test the homepage and one service page with Google's Rich Results Test:
   <https://search.google.com/test/rich-results>.
2. Confirm that the JSON-LD is readable and contains the Person/ProfilePage on the
   homepage and Service/BreadcrumbList on service pages.
3. In Search Console, inspect the rendered page and confirm that its canonical URL
   begins with `https://japhes.secora.dev/`.
4. Confirm that <https://japhes.secora.dev/robots.txt> loads and references the
   canonical sitemap.

## 5. Strengthen identity and authority signals

Use the same public name, role, portrait, and portfolio URL wherever the profile is
listed. Add `https://japhes.secora.dev/` to:

- the GitHub profile website field;
- LinkedIn contact information and Featured section;
- GDG/community speaker or organizer profiles where a website is allowed;
- other genuine professional profiles owned by Japhes Murithi.

Link back only from relevant, real profiles. Do not buy backlinks or place the URL
in unrelated directories.

## 6. Keep building useful content

The next valuable content expansion is one honest case-study page per substantial
project. Each case study should explain the problem, Japhes's role, the technical
decisions, screenshots, and a real outcome. Avoid duplicated service text, invented
testimonials, or location pages with nearly identical content.

## 7. Review Search Console monthly

- Check **Page indexing** for excluded pages and crawl errors.
- Check **Performance** for queries, pages, clicks, impressions, and click-through
  rate. Improve titles only when the query data shows a mismatch.
- Check **Core Web Vitals** and fix persistent mobile problems.
- Resubmit the sitemap only when its URL changes; updates are discovered from the
  same sitemap automatically.

Search visibility grows gradually. Google does not guarantee rankings, and new or
changed pages can take days to several weeks to be crawled and indexed.
