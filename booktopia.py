import requests
from lxml import html
import csv

# Function to scrape book details from a given URL
def scrape_book_details(url,headers):
    # Sending a GET request to the URL and parsing the response
    response = requests.get(url,headers=headers)
    print(f"URL: {url}, Status Code: {response.status_code}") 
    tree = html.fromstring(response.content)
    
    # List to store book details
    books = []

    # Extracting details of each book
    # title = tree.xpath('//div[@class="MuiBox-root mui-style-1ebnygn"]/h1/text()').strip()
    try:
        title = tree.xpath('//div[@class="MuiBox-root mui-style-1ebnygn"]/h1/text()')[0].strip()
    # title2 = tree.xpath('//div[@class="MuiBox-root mui-style-1ebnygn"]/h2/text()')[0].strip()
    # title = title1+title2
        print(title)
    except:
        title = ''
    # authors = tree.xpath('//span[@class="contributors"]/text()')[0].strip()
    try:
        authors = tree.xpath('.//span[@class="MuiTypography-root MuiTypography-body1 mui-style-1plnxgp"]//text()')[0].strip()
        print(authors) 
    except:
        authors = ''
    try:
        book_type = tree.xpath('//div[@class="MuiBox-root mui-style-1ebnygn"]/p[@class="MuiTypography-root MuiTypography-body1 mui-style-tgrox"]/text()')[0].strip()#.replace('eBook | ', '')
        book_type = book_type.split('|')[0].strip()# book_type = tree.xpath('//li[@class="MuiBreadcrumbs-li"][3]/a/p/text()')[0].strip()
        print(book_type)
    except:
        book_type = ''
    # original_price = tree.xpath('//span[@class="retail-price"]/text()')[0].strip().replace('$', '')
    try:
        original_price = tree.xpath('//p[@class="MuiTypography-root MuiTypography-body1 mui-style-vrqid8"]//span//text()')[0].strip().replace('$', '')
        print(original_price)
    except:
        original_price = ''
    try:
        discounted_price = tree.xpath('//p[@class="MuiTypography-root MuiTypography-body1 BuyBox_sale-price__PWbkg mui-style-tgrox"]//text()')[0].strip().replace('$', '')
        print(discounted_price)
    except:
        discounted_price = ''
    # isbn = tree.xpath('//span[@itemprop="isbn"]/text()')[0].strip()
    # print(ISBN-10)
    # published_date = tree.xpath('//span[@itemprop="datePublished"]/text()')[0].strip()
    try:
        published_date = tree.xpath('//div[@class="MuiBox-root mui-style-1ebnygn"]/p[@class="MuiTypography-root MuiTypography-body1 mui-style-tgrox"]/text()')[0].strip().replace('eBook | ', '')
        published_date = published_date.split('|')[-1].strip()
        # print(cleaned_text)
        print(published_date)
    except:
        published_date = ''

    try:
        publisher = tree.xpath('//div[@class="MuiBox-root mui-style-h3npb"]/p[11]/text()')[0].strip()
    # publisher = publisher[0].strip() if publisher else None
        print(publisher)
        try:
            publisher = tree.xpath('//div[@class="MuiBox-root mui-style-h3npb"]/p[9]/text()')[0].strip()

        except:
            publisher = ''
    except:
            publisher = ''

    # pages = tree.xpath('//*[@id="ProductDetails_d-product-info__rehyy"]/div[4]/div/div/div[3]/div/div[1]/text()[2]')[0].strip().replace(' pages', '')
    try:
        pages = tree.xpath('//div[@class="MuiButtonBase-root MuiTab-root MuiTab-labelIcon MuiTab-textColorInherit mui-style-ax6ycu"]//text()[2]')[0].strip().replace(' pages', '')
        print(pages)
    except:
        pages = ''

    # Storing book details in a dictionary and appending to the books list
    books.append({
        'Title': title,
        'Authors': authors,
        'Book Type': book_type,
        'Original Price': original_price,
        'Discounted Price': discounted_price,
        'ISBN-10': isbn_13,
        'Published Date': published_date,
        'Publisher': publisher,
        'No. of Pages': pages,
        'URL':url,
    })

    return books

# Function to clean the scraped data
# def clean_data(books):
#     for book in books:
#         # Converting Original Price and Discounted Price to float
#         book['Original Price'] = float(book['Original Price'])
#         book['Discounted Price'] = float(book['Discounted Price'])

# Function to export book details to a CSV file
def export_to_csv(books, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Authors', 'Book Type', 'Original Price', 'Discounted Price', 'ISBN-10', 'Published Date', 'Publisher', 'No. of Pages','URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Writing header row
        writer.writeheader()
        # Writing data rows
        for book in books:
            writer.writerow(book)


if __name__ == "__main__":
    # Reading input ISBN-13 from input file
    with open('E:/Mangesh/Techolution/booktopia/input_list.csv', 'r') as file:
        # isbn_13 = file.readline().strip()
        isbn_13_list = file.readlines()

    # Constructing URL with ISBN-13
    # url = f"https://www.booktopia.com.au/star-trek-diane-duane/ebook/{isbn_13}.html"
    
    # print("URL:", url)  # Print the URL to check if it's constructed correctly
    
    # Set user-agent, accept header, and cookies
    headers = {
    'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Cookie': 'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utma=42558518.1965743548.1715077989.1715084282.1715152727.3; __utmc=42558518; __utmb=42558518.1.10.1715152727; _ga_FPB2B22W9V=GS1.3.1715152739.3.0.1715152739.60.0.0; __attentive_ss_referrer=https://www.booktopia.com.au/star-trek-diane-duane/ebook/9780307762528; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; IR_9632=1715152755749%7C0%7C1715152755749%7C%7C; _px3=3fa7881677404fefc70920a80eec380ca8ffeb0113537d97c71d943832f1c459:CqjMcKlyJbVNwLxwkFWT9ZgLlQo/6DGxMDzcfqD9v4Q6dig6ey30gveCMDEV25/pIIv9SsRWTlXTi5XOO/RVrA==:1000:GERfoHCXCXFJCWFNj/f0jZvGD/KIOqFJF5UQ5xlYVa7zL36U81Jsdioohb+9KBvxZdeeTeNwGXH65QdBBpI59hJUSU1yUPu5Qwzcx9SLwAY8PtEDRa8xbpGpziOaB0toSS5BF/3xi9nm0cG0VqXKDyxfWkAlEIlMEFYa3JOvN50Sf3yHlXLaWoxFQs+uXq7bKtykEApOKsfrsQG56RrzCr9Tyi0OjsacIaEpD1AwR70=; _gat=1; AWSALB=HJB1AYarIOZgtlouE5+7ngfXi6vhaliMqtqlJxN8/xqt0hzT6C8xzy0u2iKmdUxwKT29qtvDCma5F920Zv6GRrNQFr6Ns45h9pANkqYtcyff6oPvVmGJI6JagzTY; AWSALBCORS=HJB1AYarIOZgtlouE5+7ngfXi6vhaliMqtqlJxN8/xqt0hzT6C8xzy0u2iKmdUxwKT29qtvDCma5F920Zv6GRrNQFr6Ns45h9pANkqYtcyff6oPvVmGJI6JagzTY; JSESSIONID=nWzgACNcryaCl_kwnVo5qbRdMHBVfQmA_qGErH97.10.0.103.85; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; _ga=GA1.1.1965743548.1715077989; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715154313.0.0.1159643465; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; FPGSID=1.1715152753.1715154317.G-XYG4G317GS.e3yKKNQ8ikAT8BV9ciRbBg; __attentive_pv=4; forterToken=1533d03ceefc4309b10b340ec613eee8_1715154311992__UDF43-m4_6_/+EhIuCKuyU%3D-8429-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715154311992__UDF43-m4_6_/+EhIuCKuyU%3D-8429-v2; _pxde=f3deeecb4fa2b65eb749dd6a9414798a55e51225cf2cc11ebdcaef83ace5fc46:eyJ0aW1lc3RhbXAiOjE3MTUxNTQzMzE1NDF9',
    # 'Cookie':'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utmc=42558518; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; __attentive_ss_referrer=ORGANIC; _gat=1; __utma=42558518.1965743548.1715077989.1715152727.1715156018.4; __utmt=1; JSESSIONID=CCP6WsdobhHvt50sbOtv9G9npxHTn3ONmAVnu2Nx.10.0.103.85; _gat_UA-413837-1=1; FPGSID=1.1715156026.1715156026.G-XYG4G317GS.GwREw3XtFV69i6VcXjP2sg; _gat_enhancedEcommerce=1; _gat_MHEnhancedEcommerce=1; IR_9632=1715156031357%7C1397383%7C1715156031357%7C%7C; __utmb=42558518.2.10.1715156018; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; _ga=GA1.3.1965743548.1715077989; _ga_FPB2B22W9V=GS1.3.1715156026.4.1.1715156035.51.0.0; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156029278__UDF43-mnf-a4_6_DGyz+TYuIk4%3D-6311-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156029278__UDF43-mnf-a4_6_DGyz+TYuIk4%3D-6311-v2; __attentive_pv=7; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715156064.0.0.1159643465; _px3=b6897388b0e058d4036c0d47ce10f11ee39cc1a803d80488270a8ea989be371b:PUYusgal6eJ10iufksFLRYdKkEBCl/s6Ob9xJWTUukveV/JbaEb24lWp0C+0Htjpnvs1SdgfFdp/DmykYuq6XQ==:1000:fIw608K8pgIppIol30Mmi8cIvPhVPZaccKA8jXCHnTd2w1q1dzDpz/GvoBR5azF6jyXPa0Qg7WW7YVG1Q5stq1GYkMpySLZ1M4nFALax1HPl3SdyP6Qg4LGkitmjbXxFJ5uSp0Zo1lL3jWhKAtqtPO+aS6JoQHkdGEjnVa8+TQ3yNbK0iFsfNpNqMhJIF2g9BkLOsXV4AO1ZaYPdobMGiBi5213k/RimhwO7Q9qxA9Q=; _pxde=3eedf9e7c8b30e4dde803851973d2b4698c0ed3721b0c0a9df4822815d0c121e:eyJ0aW1lc3RhbXAiOjE3MTUxNTYwNjk5NTJ9; AWSALB=quH0IBu5HHiBO+Px0YYnf4kcKkqNUUl8jELKK5DglnE3D9EBVX9jZIvFP3lG8+EME6ywYbo6gvFLG8H1IWKl9Ot8z1hL59zWxXe8nEhhEJ2RNn4rC+7itQtfFEg2; AWSALBCORS=quH0IBu5HHiBO+Px0YYnf4kcKkqNUUl8jELKK5DglnE3D9EBVX9jZIvFP3lG8+EME6ywYbo6gvFLG8H1IWKl9Ot8z1hL59zWxXe8nEhhEJ2RNn4rC+7itQtfFEg2',
    # 'Cookie':'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utmc=42558518; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; __attentive_ss_referrer=ORGANIC; __utma=42558518.1965743548.1715077989.1715152727.1715156018.4; __utmt=1; JSESSIONID=CCP6WsdobhHvt50sbOtv9G9npxHTn3ONmAVnu2Nx.10.0.103.85; IR_9632=1715156031357%7C1397383%7C1715156031357%7C%7C; __utmb=42558518.2.10.1715156018; _ga_FPB2B22W9V=GS1.3.1715156026.4.1.1715156035.51.0.0; _gat=1; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; _px3=d5125a78ce2ddc0343bcf54b54ed342a85ef050569d9337a20fd716ed46fbb58:pauwQU+J0ZEMeh/iAU5WbR6OY6OZWK6MpvDn+hysDn/9pMGWkDlKcNj7nFDlPyuESafK1IhbnC8K/O6C19AOtA==:1000:ZU/grK7jwPvwP9csQ3PkuNgkW6xRT+6/6EUVNtrRPSNgDK4WX/8N2U/Ukf/PIz5y2tuxpvh68gIERcHRV1l5Udhz0xPBheSuZNJto70RXhm1jrfszTAByaxFAAInYvBYrkpLOb6v/quS/jTQFWRKxY1Zjo+hoIlCZo/6SBTnC7C9pJfpYO1C/6zXa8EF6oHaehoRcnFZd8zt96rRAJaSg/yjDZddgWmRwmuxZvt+S6U=; FPGSID=1.1715156026.1715156093.G-XYG4G317GS.GwREw3XtFV69i6VcXjP2sg; __attentive_pv=8; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156086964__UDF43-mnf-a4_6_YfaQGYd000I%3D-4479-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156086964__UDF43-mnf-a4_6_YfaQGYd000I%3D-4479-v2; _pxde=cd9104fe4277e99da836639255f8d3b603f8cf5b53e56fc079ec27ddd618c58c:eyJ0aW1lc3RhbXAiOjE3MTUxNTYxMDQ4MjN9; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715156112.0.0.1159643465; _ga=GA1.3.1965743548.1715077989; AWSALB=qz6Gc7tDRd/16LOYpg2Z2vTkjlOThrOTP5Z4fykwaOWtNHqL08MuAeddaG225Wc0MOLV2T7cCqZDCDi3tvgKCXHmsHYDbSDKnFPwgTOq4llqYuuq6tnfenhLa3kZ; AWSALBCORS=qz6Gc7tDRd/16LOYpg2Z2vTkjlOThrOTP5Z4fykwaOWtNHqL08MuAeddaG225Wc0MOLV2T7cCqZDCDi3tvgKCXHmsHYDbSDKnFPwgTOq4llqYuuq6tnfenhLa3kZ',
    # 'Cookie':'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utmc=42558518; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; __attentive_ss_referrer=ORGANIC; __utma=42558518.1965743548.1715077989.1715152727.1715156018.4; __utmt=1; JSESSIONID=CCP6WsdobhHvt50sbOtv9G9npxHTn3ONmAVnu2Nx.10.0.103.85; IR_9632=1715156031357%7C1397383%7C1715156031357%7C%7C; __utmb=42558518.2.10.1715156018; _ga_FPB2B22W9V=GS1.3.1715156026.4.1.1715156035.51.0.0; AWSALB=SSziWZeHe7Coo6ENhu3bzxYSvGbWxowa9vSjkfNr5Z5/MKUoaODxyxf5A1MHGrhf1yDCCMQiVCLVLrENJv1bNixWkS9a7km2Hf8GKoyYfArFDuavM9CFjaa4h1Bt; AWSALBCORS=SSziWZeHe7Coo6ENhu3bzxYSvGbWxowa9vSjkfNr5Z5/MKUoaODxyxf5A1MHGrhf1yDCCMQiVCLVLrENJv1bNixWkS9a7km2Hf8GKoyYfArFDuavM9CFjaa4h1Bt; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; _ga=GA1.1.1965743548.1715077989; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; _px3=52db6c778c5040dec72c16dbe576fef3d0ffd7358a05f0f88b35e501bdf6baaf:6TkkdRL1uYphvyGLVK1+6yExuQ6932IDthiYwMmblDP3oATLWXVLOV5nG9SQRPtR4gwdE4+Cq4th6gFeOyLFjA==:1000:ENo1e0ScgoXdHpgUoFtED7D4ofyVyv+t88ZwqCGbmk3dxx1zdun+8UYqjyjs+jbAJ2NcumIUf8DCsadBR70HrFcxQ224I9MKMV8O/JOoA/7iSIHUFWJHek1Uo5LIiSidc1G+VVHlIKe8mGdism16k3acSUVBNLmMVwS9+cc3tAorCh+OFG2ReSRTt3bAtA8HVuFAw0reG2OtWu0wEPWijMgNxC3mBpd0y3A9zXk+v24=; __attentive_pv=9; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156127852__UDF43-m4_6_9qcuc7HxbBY%3D-12119-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156127852__UDF43-m4_6_9qcuc7HxbBY%3D-12119-v2; _pxde=80e582a74d8ee6e2087982f4f9ac26930bfbc785145c95cda9bd66c7894641bc:eyJ0aW1lc3RhbXAiOjE3MTUxNTYxNDMwOTV9; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715156154.0.0.1159643465; FPGSID=1.1715156026.1715156157.G-XYG4G317GS.GwREw3XtFV69i6VcXjP2sg',
    'Cookie':'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utmc=42558518; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; __utma=42558518.1965743548.1715077989.1715152727.1715156018.4; __utmt=1; JSESSIONID=CCP6WsdobhHvt50sbOtv9G9npxHTn3ONmAVnu2Nx.10.0.103.85; IR_9632=1715156031357%7C1397383%7C1715156031357%7C%7C; __utmb=42558518.2.10.1715156018; _ga_FPB2B22W9V=GS1.3.1715156026.4.1.1715156035.51.0.0; __attentive_pv=13; _px3=a383c98ba643a24525760eda094990133d6bcc11b23e76558903d170a908690e:GcGYA0bmP+V/+G6hAu4Tq7rDFxt7P6ruqoInui5e8ubr9FbDRhapSpZI5i/Nds4yfQagnRyM8QC8TvmZFVcW8Q==:1000:TYIEAoCwac28zzyLpycHY7W63mBEixDhzi26E7Mks3O39meIJfTGYcQLjyx+DdjDscENCHkq2nvI8qi1DQX9UA2SKGcvKqzf3f2FWCXhu55cYNodYXbNyVO7YrK/xSN141em464+7fcBLDshfvQsY2WdBjMR5QtLdy/Z80Oc+WyQkp/VUaOE50DmnFnPrgj1zS57vMCV+eKa2zBfFlh0WAMnalDqaIOf7Yu3KdyzQKY=; _gat=1; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; AWSALB=GbMF5dVC/Cl3PcOlpAFusEpwuQgLBvYKhg8wHKqvMoryEc22AUtK3TE3Cvqkik+85fj0iQrbHVbJomxDSFbwSXYKNa+yXG961RTlqlfkENI+c7OQpHUupOtKYpGs; AWSALBCORS=GbMF5dVC/Cl3PcOlpAFusEpwuQgLBvYKhg8wHKqvMoryEc22AUtK3TE3Cvqkik+85fj0iQrbHVbJomxDSFbwSXYKNa+yXG961RTlqlfkENI+c7OQpHUupOtKYpGs; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; _ga=GA1.1.1965743548.1715077989; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715156603.0.0.1159643465; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156601890__UDF43-m4_6_x46ORstKbyY%3D-1340-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156601890__UDF43-m4_6_x46ORstKbyY%3D-1340-v2; _pxde=11124b8f7fd232628752fd394152cf9942669e82cc1e1f57d022ea81034d8aaf:eyJ0aW1lc3RhbXAiOjE3MTUxNTY2MDY4Njd9; FPGSID=1.1715156026.1715156607.G-XYG4G317GS.GwREw3XtFV69i6VcXjP2sg',
    # 'Cookie':'domainCustomerSessionGuid=CE079B6C-1D1F-52E9-CE7C-F401ABBDD6D7; _gid=GA1.3.1377787162.1715077989; _pxvid=348b05a3-0c5d-11ef-ae8f-a410363617b5; _gcl_au=1.1.395158956.1715077991; ftr_ncd=6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%229TeVrQksk61V5bbABRGV%22%7D; FPID=FPID2.3.M%2FH1ZdBcJPzh8bvRvRD0kmSVMOnZnll3Z7Galq7tq4M%3D.1715077989; __attentive_id=41f421fba12d40f9b0bf45586ca9d299; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1MDc3OTk1ODUyLFwidW9cIjoxNzE1MDc3OTk1ODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQxZjQyMWZiYTEyZDQwZjliMGJmNDU1ODZjYTlkMjk5XCJ9In0=; __attentive_cco=1715077995859; _fbp=fb.2.1715077995952.1360199851; _tt_enable_cookie=1; _ttp=0eEV-LJv45OpTGoBVol4sRygnHs; __attentive_dv=1; __utmz=42558518.1715080092.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IR_PI=be91c581-0c61-11ef-9a6f-0fa1b6a32a61%7C1715080092957; irclickid=%7E1XZQJLHKBDKABIEGFGNUKBCsosija%7E590Z589Z0ZXVNMCrpfa30Q; G_ENABLED_IDPS=google; pxcts=ff61d542-0cfd-11ef-8ebe-9a492fa57242; gaUniqueIdentifier=DE31036F-B003-DFD0-1761-957404FB2087; scarab.visitor=%22219C46A76BF4B378%22; countryCode=IN; isBotUserAgent=false; siteVersion=PC; __utmc=42558518; FPLC=VLSXDN6OpKF5bfGul1eM6pPkWnjqwE8jN9%2FsfcY0BR%2Blq46H7qBk9TrkZ7VI9%2FD0kXAiQGN1CjracW5gITXzpI3bvI4iWvl1um9f4MYc1p9qwNBW%2B3nBjPIbWa%2FBKA%3D%3D; IR_gbd=booktopia.com.au; __attentive_ss_referrer=ORGANIC; __utma=42558518.1965743548.1715077989.1715152727.1715156018.4; __utmt=1; JSESSIONID=CCP6WsdobhHvt50sbOtv9G9npxHTn3ONmAVnu2Nx.10.0.103.85; IR_9632=1715156031357%7C1397383%7C1715156031357%7C%7C; __utmb=42558518.2.10.1715156018; _ga_FPB2B22W9V=GS1.3.1715156026.4.1.1715156035.51.0.0; FPGSID=1.1715156026.1715156157.G-XYG4G317GS.GwREw3XtFV69i6VcXjP2sg; _ga=GA1.1.1965743548.1715077989; AWSALB=h1gpjMPpE6MT3rt+Uyvexx+5WKxNbzjxzGqi+xSLJjMxnznXypyh7uALjCJjG0LDcuADgjhdMMIeXtj8hEabg1R61IYD1z6gtou8iG0Ht3AK0y4NtIIMD4vuGJ/k; AWSALBCORS=h1gpjMPpE6MT3rt+Uyvexx+5WKxNbzjxzGqi+xSLJjMxnznXypyh7uALjCJjG0LDcuADgjhdMMIeXtj8hEabg1R61IYD1z6gtou8iG0Ht3AK0y4NtIIMD4vuGJ/k; _uetsid=3398ab000c5d11ef8c4d15a125ab80d6; _uetvid=3398aee00c5d11efb62a917e23829a10; _ga_XYG4G317GS=GS1.1.1715152727.7.1.1715156203.0.0.1159643465; _rdt_uuid=1715077993460.0f354432-3465-40c9-a1c3-c115c08fab8b; _px3=4376dc9024f275ffca4c72cee9c2fddeefdf1640366ea4773b051630d1d98948:GcGYA0bmP+V/+G6hAu4Tq7rDFxt7P6ruqoInui5e8ubr9FbDRhapSpZI5i/Nds4yfQagnRyM8QC8TvmZFVcW8Q==:1000:aLOn8wxIY2WN9Y1ZzuA94YTPmrJvi3djZLlqUHsd7oemOY6T/GzEPIxeYCCUky0cA9p8s9n4rlbgoRek4WPN/snYznif/7mVA3RCFw0dZJZuqZl/W1KwKFq5FeHXc4mJaNlpCQg+HPYIzDbqbwI1T71R+tE4vLqudePu67+hcN3pdKbJpKMkIubc00E3D4Jtx2jJxrajO+e0kcO0lxcD7UG8aHDI1LbRXRPKeEwXrR8=; __attentive_pv=11; _pxde=9567898cef564d9140925e405fd04d3002f1bee6d7c6c1d5cdf867d97532f549:eyJ0aW1lc3RhbXAiOjE3MTUxNTYyMTMxMjR9; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156201685__UDF43-mnf-a4_6_Wtl/n03s6MM%3D-9557-v2; forterToken=1533d03ceefc4309b10b340ec613eee8_1715156201685__UDF43-mnf-a4_6_Wtl/n03s6MM%3D-9557-v2',

}


    all_books = []
    # Scraping book details from constructed URL
    # books = scrape_book_details(url,headers)
    for isbn_13 in isbn_13_list:
        # Constructing URL with ISBN-13
        url = f"https://www.booktopia.com.au/star-trek-diane-duane/ebook/{isbn_13.strip()}.html"
        # print("URL:", url)
        # Scraping book details from constructed URL
        books = scrape_book_details(url, headers)
        # print("Books:", books)
        # Appending scraped book details to the list
        all_books.extend(books)
        # clean_data(all_books)




    
    # Cleaning scraped data
    # clean_data(all_books)
        # print("Scraped Data:", all_books)

# Exporting data to CSV file
        try:
            export_to_csv(all_books, 'booktopia_books111111111.csv')
            # export_to_csv(all_books, 'booktopia_books.csv')
            print("CSV file created successfully.")
        except Exception as e:
            print("Error occurred while writing to CSV:", e)
        
    # Exporting data to CSV file
    # export_to_csv(all_books, 'booktopia_books.csv')
