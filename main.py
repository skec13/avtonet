import requests as req
from lxml import html

#cmd D:\python\Avtonet\venv\Scripts\python.exe -m pip install requests

znamka = "Audi"
model = ""
url = "https://www.avto.net/Ads/results.asp?znamka={}&model={}&tip=katerikoli%20tip&znamka2=&model2=&tip2=katerikoli%20tip&znamka3=&model3=&tip3=katerikoli%20tip&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1000000120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PSLO=&akcija=&paketgarancije=&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=&arhiv=&presort=&tipsort=&stran=".format(znamka,model)
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }



resp = req.get(url, headers = headers, allow_redirects = True)

tree = html.fromstring(resp.content)

#.........................................................................................................#


first = tree.xpath('//table[@class = "table table-striped table-sm table-borderless font-weight-normal mb-0"]/tbody//text()')[2].strip()
if(first == ""):
    print('jeje')
print(f'first: {first}')
print(type(first))

first_reg = tree.xpath('//td[@class = "w-75 pl-3"]/text()')
miles_fuel_top = tree.xpath('//div[@class = "GO-Results-Top-Data-Top"]/table/tbody/tr/td[@class = "pl-3"]/text()')
miles_fuel = tree.xpath('//table[@class = "table table-striped table-sm table-borderless font-weight-normal mb-0"]/tbody/tr/td[@class = "pl-3"]/text()')
print(f'miles_fuel: {miles_fuel}')



for i in range(0,len(first_reg),1):
    if(first_reg[i] == 'NOVO'):
        miles_fuel_top.insert(i*2, 'NOVO')

print(f'first_reg: {first_reg}')
print(f'miles_fuel_top: {miles_fuel_top}')

miles_top = []
engine_type_top = []
for i in range(0,len(miles_fuel_top),1):
    if(i % 2 == 0):
        miles_top.append(miles_fuel_top[i])
        engine_type_top.append(miles_fuel_top[i + 1])

miles = []
engine_type = []
for i in range(0,len(miles_fuel),1):
    if(miles_fuel[i] == ''):
        print("evotigana")
    if(i % 2 == 0):
        miles.append(miles_fuel[i])
        engine_type.append(miles_fuel[i + 1])


print(f'miles_top: {miles_top}')
print(f'engine_type_top: {engine_type_top}')
print(f'miles: {miles}')
print(f'engine_type: {engine_type}')


transmission_engine = tree.xpath('//div[@class = "GO-Results-Top-Data-Top"]/table/tbody/tr/td[@class = "pl-3 text-truncate"]/text()')
transmission_engine1 = tree.xpath('//td[@class = "pl-3 text-truncate"]/text()')
transmission = []
engine = []
for i in range(0,len(transmission_engine1),1):
    if(i % 3 == 0):
        transmission.append(transmission_engine1[i])
        engine.append(transmission_engine1[i + 1])


print(f'transmission_engine1: {transmission_engine1}')
print(f'transmission: {transmission}')
print(f'engine: {engine}')


#names = tree.xpath('//a/img/@title') izpod slike vzame ime, ta spodi pa iz unga prostora nad podatki
names = tree.xpath('//div[@class = "GO-Results-Naziv bg-dark px-3 py-2 font-weight-bold text-truncate text-white text-decoration-none"]/span/text()')


price_top_deal = tree.xpath('//div[@class = "GO-Results-Top-Price-Mid"]/div[@class = "GO-Results-Top-Price-TXT-Regular" or @class = "GO-Results-Price-TXT-Regular" or @class = "GO-Results-Top-Price-TXT-AkcijaCena"]/text()')
price = tree.xpath('//div[@class = "d-none d-sm-block col-auto px-sm-0 pb-sm-3 GO-Results-PriceLogo"]/div/div/div[@class = "GO-Results-Price-TXT-Regular"]/text()')
price_all = price_top_deal + price

print(f'first_reg: {first_reg}')
print(f'transmission_engine: {transmission_engine}')
print(f'transmission_engine1: {transmission_engine1}')
print(f'names: {names}')
print(f'price_top_deal: {price_top_deal}')
print(f'price: {price}')
print(f'price_all: {price_all}')








