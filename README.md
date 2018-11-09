How to use:

1. Clone repo.
2. Run "setup.bat". It will download YAML and urllib3 using pip. It will also create mat.bat.
3. Add mat.bat to PATH or put it in your System32 folder so that you can execute the scraper by typing mat in your command line.

Right now it will scrape Nya Etage (http://www.nyaetage.se/veckans-meny) by default.
I have added support for it to scrape Nya Etage and Restaurang Södra Porten. 
By writing "mat porten" it will scrape the Södra Porten menu.
Whatever key:value pair you put in the top of urls.yaml, that one will be scraped by default.

To add support for more websites, add an alias and url in urls.yaml.
Then write your custom parser in htmlParser.py and remember to add the parser to the chooseParser() function.

EXAMPLE OUTPUT:
<p>> mat<br>
----------<br>
DAGENS MAT<br>
----------<br>
* Helstekt fläskfilé Provencale med råstekt potatis, rödvinssås och ört- & vitlöksmör<br>
* Husets fisk- och skaldjurssoppa på torsk, lax, räkor, grönsaker, rostat vitlöksbröd samt aioli<br>
* Spaghetti Bolognese med grana padano<br>
* Veg/Vegan: Vego Bolognese med grana padano<br>
</p>
