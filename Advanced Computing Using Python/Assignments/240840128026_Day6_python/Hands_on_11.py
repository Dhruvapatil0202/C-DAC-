"""
Regular expression for extracting URLs form text
"""
import re

SAMPLE_TEXT = """
http://example.com/product/123/details
https://example.org/products/category/456
http://example.com/articles/789/reviews
https://blog.example.com/2023/09
http://shop.example.net/sale/2023
https://store.example.com/us/ny
http://example.com/services/it/support
https://example.org/portfolio/design/web
http://example.com/news/2023/09/08
https://news.example.com/technology/latest
http://example.com/profile/user123/settings
https://user.example.com/profile/settings/preferences
http://example.com/settings/account/security
https://settings.example.org/preferences
http://example.com/help/contact/form
https://help.example.com/support/tickets/new
http://example.org/support/faqs
https://support.example.net/articles/how-to
http://example.com/docs/api/v1
https://docs.example.org/api/v2
http://example.com/api/v1/resources
https://api.example.com/v2/endpoints
http://example.org/status/uptime
https://status.example.com/reports
http://example.com/privacy/policy
https://privacy.example.org/terms
http://example.com/terms-of-service
https://terms.example.com/service-agreement
http://example.org/legal/notices
https://legal.example.net/disclaimer
http://example.com/faq/general
https://faq.example.com/troubleshooting
http://example.org/blog/posts/123
https://blog.example.net/archive/2023
http://example.com/forum/threads/456
https://forum.example.org/categories
http://example.com/download/software/latest
https://download.example.com/files/2023
http://example.org/demo/live
https://demo.example.net/features
http://example.com/product/123/details/specs
https://example.org/products/category/456/features
http://example.com/articles/789/reviews/2023
https://blog.example.com/2023/09/latest
http://shop.example.net/sale/2023/september
https://store.example.com/us/ny/locations
http://example.com/services/it/support/remote
https://example.org/portfolio/design/web/case-studies
http://example.com/news/2023/09/08/headlines
https://news.example.com/technology/latest/innovations
http://example.com/profile/user123/settings/notifications
https://user.example.com/profile/settings/preferences/privacy
http://example.com/settings/account/security/password
https://settings.example.org/preferences/notifications/email
http://example.com/help/contact/form/submit
https://help.example.com/support/tickets/new/priority
http://example.org/support/faqs/common
https://support.example.net/articles/how-to/setup
http://example.com/docs/api/v1/endpoints
https://docs.example.org/api/v2/resources
http://example.com/api/v1/resources/data
https://api.example.com/v2/endpoints/users
http://example.org/status/uptime/reports
https://status.example.com/reports/2023
http://example.com/privacy/policy/details
https://privacy.example.org/terms/conditions
http://example.com/terms-of-service/agreement
https://terms.example.com/service-agreement/details
http://example.org/legal/notices/updates
https://legal.example.net/disclaimer/2023
http://example.com/faq/general/questions
https://faq.example.com/troubleshooting/issues
http://example.org/blog/posts/123/comments
https://blog.example.net/archive/2023/09
http://example.com/forum/threads/456/discussion
https://forum.example.org/categories/topics
http://example.com/download/software/latest/version
https://download.example.com/files/2023/releases
http://example.org/demo/live/session
https://demo.example.net/features/overview
"""

if __name__ == "__main__":
    text_blocks = SAMPLE_TEXT.split("\n")
    exp = r"https:\/\/[a-z\.\/0-9\-]+|http:\/\/[a-z0-9\.\/\-]+"
    for text in text_blocks:
        out_li = re.findall(pattern= exp, string= text)
        if out_li:
            print(out_li)