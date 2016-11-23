from lxml import etree

tree = etree.parse('test.xml')

x1 = tree.xpath('//book[@id = "bk101"]')
x1 = tree.xpath("//book[price = 4.95 and ./genre = 'Horror']")

print(x1)
for e in x1:
    print(e)
    for y in e:
        print(y.text)

