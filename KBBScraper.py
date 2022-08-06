from lxml import html
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

heading = ["Title", "Price","Milage", "Vin"]

year = [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992]
make = ["Acura","Alfa" "Romeo","Aston Martin","Audi","Bentley","BMW","Buick","Cadillac","Chevrolet","Chrysler","Dodge","Ferrari","FIAT","Ford","Genesis","GMC","Honda","Hyundai","INFINITI","Jaguar","Jeep","Kia","Lamborghini","Land Rover","Lexus","Lincoln","Lucid","Maserati","MAZDA","Mercedes-Benz","MINI","Mitsubishi","Nissan","Polestar","Porsche","Ram","Rivian","Rolls-Royce","Subaru","Tesla","Toyota","Volkswagen","Volvo"]
zipcode = 0

pageURL = "https://www.kbb.com"

def menu():
   print ('1 -- Find vehicle information using KBB URL' )
   print ('2 -- Search for a vehicle using Make, Model, and Year' )
   print ('3 -- Exit')

   option = int(input('Enter your choice: ')) 
   if option == 1:
      add_vehicle_to_monitor()
   elif option == 2:
      vehicle_search()
   elif option == 3:
      exit()
   else:
      print('Invalid option. Please enter a number between 1 and 4.')



def add_vehicle_to_monitor():
   print("Enter the URL(s) link from https://www.kbb.com/ for the vehicle you would like to view.")
   input_url = input()
   custom_vehicle_info(input_url)



def vehicle_search():
   print("Please enter your zipcode.")
   zipInput = input()
   zipcode = zipInput

   for element in make:
    print(f"{element}")
   print("Please type the Make of the car you want to view.")
   inputMake = input()
   print("Please type the Model of the", inputMake, "that you want to view.")
   inputModel = input()
   print("Please type the Year(2000 - 2022) of the", inputMake, "that you want to view.")
   inputYear = input()

   urlbuilder = "https://www.kbb.com/cars-for-sale/used/" + inputYear +"/" + inputMake + "/" + "/new-hyde-park-ny-"+zipcode+"?dma=&keywordPhrases=" + inputModel.replace(" ", "_") + "&searchRadius=50"
   print("Link to search: " + urlbuilder)
   print("")
   urlPull(urlbuilder)



def custom_vehicle_info(url):
   URL = url
   page = requests.get(URL, headers=headers)
   soup = BeautifulSoup(page.content, 'html.parser')
   title = soup.find(class_="text-bold text-size-400 text-size-sm-700 col-xs-12 col-sm-7 col-md-8").get_text()
   price = soup.find(class_="first-price first-price-lg text-size-700").get_text()
   mileage = soup.find(class_="col-xs-10 margin-bottom-0").get_text()
   vin = soup.find(class_="text-size-400 text-size-sm-500").get_text()
   print(vin)
   vehicle_list(title,price,mileage)



def openUrls():
   with open('URL.txt') as f:
      for line in f:
         custom_vehicle_info(pageURL + line)


def urlPull(urlINPUT):

   # will filter out the extra links picked up by soup
   checker = "/cars-for-sale/vehicledetails.xhtml"
   urls = urlINPUT
   grab = requests.get(urls)
   soup = BeautifulSoup(grab.text, 'html.parser')
 
   # opening a file in write mode
   f = open("URL.txt", "w")
   # traverse paragraphs from soup
   for link in soup.find_all("a"):
      data = link.get('href')
      if checker in data:
         f.write(data)
         f.write("\n")

   f.close()
   openUrls()
   vehicle_format()


vehicles = []
def vehicle_list(car, price, milage):
   vehicles.append([car, price, milage])

def vehicle_format():
   print(tabulate(vehicles, headers=["Title", "Price", "Milage", "Vin"]))


menu()
#custom_vehicle_info("https://www.kbb.com/cars-for-sale/vehicledetails.xhtml/?listingId=644285474&listingTypes=USED&zip=11040&state=NY&city=New%20Hyde%20Park&dma=&searchRadius=25&isNewSearch=false&referrer=%2Fcars-for-sale%2Fused%3F&clickType=alpha")

#add_vehicle_to_monitor()
#urlPull()







    
