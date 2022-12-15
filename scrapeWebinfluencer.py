'''
@author: zhaoyingjie
'''
import csv
import requests
from bs4 import BeautifulSoup

    
URL = "https://blog.feedspot.com/beauty_instagram_influencers/"
URL2 = "https://www.amraandelma.com/top-beauty-influencers-to-follow-in-2020-in-us/"

# if you want to run the code on your computer, please change to your user-agent(you can google for it)"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
page = requests.get(URL, headers=headers)
page2 = requests.get(URL2, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(page2.content, "html.parser")

results = soup.find("div", class_="fsb v4 fsbbr_new")
results2 = soup2.find("div", class_="wpb_wrapper").find_all("h4")[0:3]
results22 = soup2.find("div", class_="wpb_wrapper").find_all("h4")[3:50]
results222 = soup2.find("div", class_="wpb_wrapper").find_all("h4")[50:]
results2bio = soup2.find("span", id="1_Chiara_Ferragni_chiaraferragni_201_-_million_followers").parent.parent.find_all("p")[3:6]
results2bio2 = soup2.find("span", id="1_Chiara_Ferragni_chiaraferragni_201_-_million_followers").parent.parent.find_all("p")[7:56]
results2bio22 = soup2.find("span", id="1_Chiara_Ferragni_chiaraferragni_201_-_million_followers").parent.parent.find_all("p")[55:]
results3 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[:8]
results33 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[7:11]
results333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[11:29]
results3333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[29:30]
results33333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[30:31]
results333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[31:32]
results3333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[32:33]
results33333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[33:38]
results333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[38:43]
results3333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[43:44]
results33333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[44:47]
results333333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[47:49]
results3333333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("h4")[49:]
results3bio = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[1:8]
results3bio3 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[9:14]
results3bio33 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[14:]
results3bio333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[33:]
results3bio3333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[35:]
results3bio33333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[37:]
results3bio333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[38:]
results3bio3333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[40:]
results3bio33333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[46:]
results3bio333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[52:]
results3bio3333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[54:]
results3bio33333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[58:]
results3bio333333333333 = soup2.find("span", id="Top_Beauty_Influencers_-_Micro_Makeup_Influencers").parent.parent.find_all("p",text=True)[61:]
with open('top200.csv', 'w', encoding='utf8') as f:
    
    writer = csv.writer(f)
    header0 = ["", "Top200", ""]
    header = ['Name', 'Handle', 'Followers','Bio']
    writer.writerow(header0)
    writer.writerow(header)
    
    names = results.find_all("h3")               
    infor = results.find_all("p", class_="trow trow-wrap")
    
    for name, information, followers, bios, locations in zip(names, infor, infor, infor, infor):
        nikename = name.find("p").text.replace('\n', '')
        username = information.find("a").text.replace('\n', '')
        numberOfFollowers = followers.find("strong", text="Instagram Followers ").find_next_sibling(text=True).text.strip()
        bio = bios.find("strong").find_next_sibling(text=True).text.strip()
        writer.writerow([nikename, username, numberOfFollowers, bio])
f.close()  
     
with open('top150.csv', 'w', encoding='utf8') as h:
    writer = csv.writer(h)
    header1 = ["", "Top150", ""]
    header2 = ['Name', 'Handle', 'Followers','Bio']
    writer.writerow(header1)
    writer.writerow(header2)
    
    
    
    for name1, bio in zip(results2,results2bio):
        infor0 = name1.find("a").find_previous_sibling(text=True).text.strip()
        infor1 = name1.find("a").text.strip()
        infor2 = name1.find("a").find_next_sibling(text=True).text.strip()
        bios = bio.text
        writer.writerow([infor0, infor1, infor2, bios])
    for name3, bio2 in zip(results22,results2bio2):
        infor6 = name3.find("a").find_previous_sibling(text=True).text.strip()
        infor7 = name3.find("a").text.strip()
        infor8 = name3.find("a").find_next_sibling(text=True).text.strip()
        bios2 = bio2.text
        writer.writerow([infor6, infor7, infor8, bios2]) 
    for name4, bio3 in zip(results222, results2bio22):
        infor9 = name4.find("a").find_previous_sibling(text=True).text.strip()
        infor10 = name4.find("a").text.strip()
        infor11 = name4.find("a").find_next_sibling(text=True).text.strip()
        bios3 = bio3.text
        writer.writerow([infor9, infor10, infor11, bios3])
    for name2, bio4 in zip(results3,results3bio):
        infor3 = name2.find("a").find_previous_sibling(text=True).text.strip()
        infor4 = name2.find("a").text.strip()
        infor5 = name2.find("a").find_next_sibling(text=True).text.strip()
        bios4 = bio4.text
        writer.writerow([infor3, infor4, infor5,bios4])
    for name5, bio5 in zip(results33, results3bio3):
        infor12 = name5.find("a").find_previous_sibling(text=True).text.strip()
        infor13 = name5.find("a").text.strip()
        infor14 = name5.find("a").find_next_sibling(text=True).text.strip()
        bios5 = bio5.text
        writer.writerow([infor12, infor13, infor14,bios5])
    for name6, bio6 in zip(results333, results3bio33):
        infor15 = name6.find("a").find_previous_sibling(text=True).text.strip()
        infor16 = name6.find("a").text.strip()
        infor17 = name6.find("a").find_next_sibling(text=True).text.strip()
        bios6 = bio6.text
        writer.writerow([infor15, infor16, infor17,bios6])
        
    for name7, bio7 in zip(results3333, results3bio333):
        infor18 = name7.find("a").find_previous_sibling(text=True).text.strip()
        infor19 = name7.find("a").text.strip()
        infor20 = name7.find("a").find_next_sibling(text=True).text.strip()
        bios7 = bio7.text
        writer.writerow([infor18, infor19, infor20,bios7])
    for name8, bio8 in zip(results33333, results3bio3333):
        infor21 = name8.find("a").find_previous_sibling(text=True).text.strip()
        infor22 = name8.find("a").text.strip()
        infor23 = name8.find("a").find_next_sibling(text=True).text.strip()
        bios8 = bio8.text
        writer.writerow([infor21, infor22, infor23,bios8])
    for name9, bio9 in zip(results333333, results3bio33333):
        infor24 = name9.find("a").find_previous_sibling(text=True).text.strip()
        infor25 = name9.find("a").text.strip()
        infor26 = name9.find("a").find_next_sibling(text=True).text.strip()
        bios9 = bio9.text
        writer.writerow([infor24, infor25, infor26,bios9])
    for name10, bio10 in zip(results3333333, results3bio333333):
        infor27 = name10.find("a").find_previous_sibling(text=True).text.strip()
        infor28 = name10.find("a").text.strip()
        infor29 = name10.find("a").find_next_sibling(text=True).text.strip()
        bios10 = bio10.text
        writer.writerow([infor27, infor28, infor29,bios10])
    for name11, bio11 in zip(results33333333, results3bio3333333):
        infor30 = name11.find("a").find_previous_sibling(text=True).text.strip()
        infor31 = name11.find("a").text.strip()
        infor32 = name11.find("a").find_next_sibling(text=True).text.strip()
        bios11 = bio11.text
        writer.writerow([infor30, infor31, infor32,bios11])
    for name12, bio12 in zip(results333333333, results3bio33333333):
        infor33 = name12.find("a").find_previous_sibling(text=True).text.strip()
        infor34 = name12.find("a").text.strip()
        infor35 = name12.find("a").find_next_sibling(text=True).text.strip()
        bios12 = bio12.text
        writer.writerow([infor33, infor34, infor35,bios12])
    for name13, bio13 in zip(results3333333333, results3bio333333333):
        infor36 = name13.find("a").find_previous_sibling(text=True).text.strip()
        infor37 = name13.find("a").text.strip()
        infor38 = name13.find("a").find_next_sibling(text=True).text.strip()
        bios13 = bio13.text
        writer.writerow([infor36, infor37, infor38,bios13])  
    for name14, bio14 in zip(results33333333333, results3bio3333333333):
        infor39 = name14.find("a").find_previous_sibling(text=True).text.strip()
        infor40 = name14.find("a").text.strip()
        infor41 = name14.find("a").find_next_sibling(text=True).text.strip()
        bios14 = bio14.text
        writer.writerow([infor39, infor40, infor41,bios14])    
    for name15, bio15 in zip(results333333333333, results3bio33333333333):
        infor42 = name15.find("a").find_previous_sibling(text=True).text.strip()
        infor43 = name15.find("a").text.strip()
        infor44 = name15.find("a").find_next_sibling(text=True).text.strip()
        bios15 = bio15.text
        writer.writerow([infor42, infor43, infor44,bios15])      
    for name16, bio16 in zip(results3333333333333, results3bio333333333333):
        infor45 = name16.find("a").find_previous_sibling(text=True).text.strip()
        infor46 = name16.find("a").text.strip()
        infor47 = name16.find("a").find_next_sibling(text=True).text.strip()
        bios16 = bio16.text
        writer.writerow([infor45, infor46, infor47,bios16])      
    
h.close()

