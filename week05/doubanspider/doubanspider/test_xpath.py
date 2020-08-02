import lxml.etree

path = '/Users/h0rs3/Work/学习/python训练营/Python001-class01/week05/doubanspider/doubanspider/text.html'

with open(path, 'r') as f:
    content = f.read()

html = lxml.etree.HTML(content)
# comment = html.xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()')[0]
# rate = html.xpath(
#     '//*[@id="comments"]/div[1]/div[2]/h3/span[2]/span[2]/@title')
# print(comment, rate)

for i in range(1, 21):
    comment = html.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')[0]
    rate = html.xpath(
        f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@title')[0]
    print(comment, rate)
        
# for selector in html.xpath('//*[@id="comments"]')[:20]:
#     comment = selector.xpath('./div[1]/div[2]/p/span/text()')
#     print(comment)
