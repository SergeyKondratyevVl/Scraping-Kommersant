import datetime
import json
import requests

def get_main_categories(required_list, listtypeid=1):
    full_tags_list = {}
    for category_id in required_list:
        
        idafter =''
        topics =[]
        for _ in range(10):

            url = f'https://www.kommersant.ru/listpage/lazyloaddocs?listtypeid={listtypeid}&listid={category_id}&idafter={idafter}'

            resp = requests.get(url=url).json()
            items = resp.get('Items')
            # print(_, len(items))
            for item in items:
                created_at = datetime.datetime.fromtimestamp(item['DateDoc']).strftime("%d-%m-%Y %H-%M")
                main_tag_type = item['MainTagType']
                main_tag_id = item['MainTagId']
                main_tag_title = item['MainTagTitlle']
                doc_id = item['DocsID']
                title = item['Title']
                doc_url = f'https://www.kommersant.ru/doc/{doc_id}'

                tags = item['Tags']
                tags_list =[]
                for tag in tags:
                    tag_name = tag['Name'] 
                    tag_url = tag['Url'] 
                    tage_type = tag['Type'] 
                    tag_id = tag['Id']
                    tags_list.append({
                        'Name': tag_name,
                        'Url': f'https://www.kommersant.ru{tag_url}',
                        'Type': tage_type,
                        'Id': tag_id,
                    })
                    if tag_id not in full_tags_list.keys():
                        full_tags_list[tag_id] = f'{tag_name}_{tage_type}'
                        # print(f'Tag {tag_id} add!')

                topics.append({
                    "MainTagType": main_tag_type,
                    "MainTagId": main_tag_id,
                    "MainTagTitle": main_tag_title,
                    "DocsId": doc_id,
                    "Title": title,
                    "DateDoc": created_at,
                    "URL": doc_url,
                    "Tags": tags_list,
                })
            
            idafter=doc_id
        
        with open(f'{main_tag_title}.json', 'w', encoding='utf-8') as file:
            json.dump(topics, file, ensure_ascii=False, indent=4)
    
    with open(f'fullTagsList_{len(full_tags_list)}.json', 'w', encoding='utf-8') as file:
        json.dump(full_tags_list, file, indent=4, ensure_ascii=False)


def get_other_categories():

    with open('fullTagsList_279.json', 'r', encoding='utf-8') as file:
        my_parse_tags = json.load(file)

    print(len(my_parse_tags))

    for category_id in my_parse_tags.keys():

        listtypeid=my_parse_tags[category_id]
        idafter =''
        topics =[]
        for _ in range(2):
            url = f'https://www.kommersant.ru/listpage/lazyloaddocs?listtypeid={listtypeid}&listid={category_id}&idafter={idafter}'
            resp = requests.get(url=url).json()
            items = resp.get('Items')

            for item in items:
                created_at = datetime.datetime.fromtimestamp(item['DateDoc']).strftime("%d-%m-%Y %H-%M")
                main_tag_type = item['MainTagType']
                main_tag_id = item['MainTagId']
                main_tag_title = item['MainTagTitlle']
                doc_id = item['DocsID']
                title = item['Title']
                doc_url = f'https://www.kommersant.ru/doc/{doc_id}'
                tags = item['Tags']
                tags_list =[]
                for tag in tags:
                    tag_name = tag['Name'] 
                    tag_url = tag['Url'] 
                    tage_type = tag['Type'] 
                    tag_id = tag['Id']
                    tags_list.append({
                        'Name': tag_name,
                        'Url': f'https://www.kommersant.ru{tag_url}',
                        'Type': tage_type,
                        'Id': tag_id,
                    })
                topics.append({
                    "MainTagType": main_tag_type,
                    "MainTagId": main_tag_id,
                    "MainTagTitle": main_tag_title,
                    "DocsId": doc_id,
                    "Title": title,
                    "DateDoc": created_at,
                    "URL": doc_url,
                    "Tags": tags_list,
                })

            idafter=doc_id
        try:
            with open(f'{main_tag_title}_{len(topics)}.json', 'w', encoding='utf-8') as file:
                json.dump(topics, file, ensure_ascii=False, indent=4)
                print(f'{main_tag_title} is Ok!')
        except:
            with open(f'{main_tag_id}_{len(topics)}.json', 'w', encoding='utf-8') as file:
                json.dump(topics, file, ensure_ascii=False, indent=4)
                print(f'{main_tag_id} is Ok!')

def get_unique_topics(category_id):
    pass

def main():
    get_main_categories(range(2,10))
    # get_other_categories()
    # get_unique_topics()


if __name__ == '__main__':
    main()

