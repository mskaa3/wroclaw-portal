import os,requests
from bs4 import BeautifulSoup
from googletrans import Translator
import sqlite3

translator = Translator()
page = requests.get('https://przybysz.duw.pl/en/documents-to-download/',verify=False)   
soup = BeautifulSoup(page.text, 'html.parser')


headers=[]
head = soup.find_all('h4', attrs = {'class':''}) 
for elem in head:
    elem_fixed=(elem.text).replace('\n\t\t\t\t','')
    headers.append(elem_fixed.replace('\n\t\t\t',''))
headers.append("Others")
categories = soup.find_all("div", class_="frame frame-default frame-type-uploads frame-layout-0")
categories.pop(0)
result_dict={}
for header,category in zip(headers,categories):
        dict={}
        for row in category.find_all('div', attrs = {'class':''}) :
            doc_title = translator.translate(row.span.text,src='pl',dest='en')
            dict[doc_title.text]='https://przybysz.duw.pl'+row.a['href']
            # dict[row.span.text]='https://przybysz.duw.pl'+row.a['href']
        result_dict[header]=dict
    

with sqlite3.connect('docs_db.db') as conn:
      try:
          cur = conn.cursor()
          for key in result_dict:
                cur.execute(f"SELECT category_id FROM categories WHERE category_name = \"{key}\"")
                data = cur.fetchall()
                if len(data) != 0:
                      msg = "Category already in the database"
                else:
                      cur.execute(f'INSERT INTO categories (category_name) values (\"{key}\")')
                      conn.commit()
                try:
                      for name in result_dict[key]:
                          cur.execute(f"SELECT category_id FROM categories WHERE category_name = \"{key}\"")
                          data = cur.fetchone()
                          cur.execute(f"SELECT document_id FROM documents WHERE document_name =\"{name}\"  AND category_id={data[0]}")
                          doc_data = cur.fetchall()
                          if len(doc_data) != 0:
                              msg = "Document already in the database"
                          else:
                  
                              cur.execute('INSERT INTO documents (document_name,document_link,category_id) values (?,?,?)', (name,result_dict[key][name],data[0]))
                              conn.commit()
                except:
                      msg = "cant add documents to the databse"
      except sqlite3.Error as er:
        print(er)
        msg = "cant add category to the databse"

            
conn.close()
    # for key in big_dict:
    #     cat = Category(category_name=key)
    #     db.session.add(cat)
    #     db.session.commit()
    #     for name in big_dict[key]:
    #         docs=Documents(link=big_dict[key][name],link_name=name,category=cat.id)
    #         db.session.add(docs)
    #         db.session.commit()
