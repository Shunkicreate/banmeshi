import requests
import json
def get_datas():
  
  url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
   

  params = {
      "format": "json",
      "applicationId": "1093061721945645180",
      "categoryId":"10",
  }
  # responses = '{"result":{"small":[],"medium":[],"large":[{"categoryName":"人気メニュー","categoryId":"30","categoryUrl":"https://recipe.rakuten.co.jp/category/30/"},{"categoryName":"定番の肉料理","categoryId":"31","categoryUrl":"https://recipe.rakuten.co.jp/category/31/"},{"categoryName":"定番の魚料理","categoryId":"32","categoryUrl":"https://recipe.rakuten.co.jp/category/32/"},{"categoryName":"卵料理","categoryId":"33","categoryUrl":"https://recipe.rakuten.co.jp/category/33/"},{"categoryName":"ご飯もの","categoryId":"14","categoryUrl":"https://recipe.rakuten.co.jp/category/14/"},{"categoryName":"パスタ","categoryId":"15","categoryUrl":"https://recipe.rakuten.co.jp/category/15/"},{"categoryName":"麺・粉物料理","categoryId":"16","categoryUrl":"https://recipe.rakuten.co.jp/category/16/"},{"categoryName":"汁物・スープ","categoryId":"17","categoryUrl":"https://recipe.rakuten.co.jp/category/17/"},{"categoryName":"鍋料理","categoryId":"23","categoryUrl":"https://recipe.rakuten.co.jp/category/23/"},{"categoryName":"サラダ","categoryId":"18","categoryUrl":"https://recipe.rakuten.co.jp/category/18/"},{"categoryName":"パン","categoryId":"22","categoryUrl":"https://recipe.rakuten.co.jp/category/22/"},{"categoryName":"お菓子","categoryId":"21","categoryUrl":"https://recipe.rakuten.co.jp/category/21/"},{"categoryName":"肉","categoryId":"10","categoryUrl":"https://recipe.rakuten.co.jp/category/10/"},{"categoryName":"魚","categoryId":"11","categoryUrl":"https://recipe.rakuten.co.jp/category/11/"},{"categoryName":"野菜","categoryId":"12","categoryUrl":"https://recipe.rakuten.co.jp/category/12/"},{"categoryName":"果物","categoryId":"34","categoryUrl":"https://recipe.rakuten.co.jp/category/34/"},{"categoryName":"ソース・調味料・ドレッシング","categoryId":"19","categoryUrl":"https://recipe.rakuten.co.jp/category/19/"},{"categoryName":"飲みもの","categoryId":"27","categoryUrl":"https://recipe.rakuten.co.jp/category/27/"},{"categoryName":"大豆・豆腐","categoryId":"35","categoryUrl":"https://recipe.rakuten.co.jp/category/35/"},{"categoryName":"その他の食材","categoryId":"13","categoryUrl":"https://recipe.rakuten.co.jp/category/13/"},{"categoryName":"お弁当","categoryId":"20","categoryUrl":"https://recipe.rakuten.co.jp/category/20/"},{"categoryName":"簡単料理・時短","categoryId":"36","categoryUrl":"https://recipe.rakuten.co.jp/category/36/"},{"categoryName":"節約料理","categoryId":"37","categoryUrl":"https://recipe.rakuten.co.jp/category/37/"},{"categoryName":"今日の献立","categoryId":"38","categoryUrl":"https://recipe.rakuten.co.jp/category/38/"},{"categoryName":"健康料理","categoryId":"39","categoryUrl":"https://recipe.rakuten.co.jp/category/39/"},{"categoryName":"調理器具","categoryId":"40","categoryUrl":"https://recipe.rakuten.co.jp/category/40/"},{"categoryName":"その他の目的・シーン","categoryId":"26","categoryUrl":"https://recipe.rakuten.co.jp/category/26/"},{"categoryName":"中華料理","categoryId":"41","categoryUrl":"https://recipe.rakuten.co.jp/category/41/"},{"categoryName":"韓国料理","categoryId":"42","categoryUrl":"https://recipe.rakuten.co.jp/category/42/"},{"categoryName":"イタリア料理","categoryId":"43","categoryUrl":"https://recipe.rakuten.co.jp/category/43/"},{"categoryName":"フランス料理","categoryId":"44","categoryUrl":"https://recipe.rakuten.co.jp/category/44/"},{"categoryName":"西洋料理","categoryId":"25","categoryUrl":"https://recipe.rakuten.co.jp/category/25/"},{"categoryName":"エスニック料理・中南米","categoryId":"46","categoryUrl":"https://recipe.rakuten.co.jp/category/46/"},{"categoryName":"沖縄料理","categoryId":"47","categoryUrl":"https://recipe.rakuten.co.jp/category/47/"},{"categoryName":"日本各地の郷土料理","categoryId":"48","categoryUrl":"https://recipe.rakuten.co.jp/category/48/"},{"categoryName":"行事・イベント","categoryId":"24","categoryUrl":"https://recipe.rakuten.co.jp/category/24/"},{"categoryName":"おせち料理","categoryId":"49","categoryUrl":"https://recipe.rakuten.co.jp/category/49/"},{"categoryName":"クリスマス","categoryId":"50","categoryUrl":"https://recipe.rakuten.co.jp/category/50/"},{"categoryName":"ひな祭り","categoryId":"51","categoryUrl":"https://recipe.rakuten.co.jp/category/51/"},{"categoryName":"春（3月～5月）","categoryId":"52","categoryUrl":"https://recipe.rakuten.co.jp/category/52/"},{"categoryName":"夏（6月～8月）","categoryId":"53","categoryUrl":"https://recipe.rakuten.co.jp/category/53/"},{"categoryName":"秋（9月～11月）","categoryId":"54","categoryUrl":"https://recipe.rakuten.co.jp/category/54/"},{"categoryName":"冬（12月～2月）","categoryId":"55","categoryUrl":"https://recipe.rakuten.co.jp/category/55/"}]}}'

  responses = requests.get(url, params=params)
  print(responses)
  responses = json.load(responses)
  print(responses['result']['rank'])
  
  
    #   for response in responses:
 
  


    
 

    
    #   for data in responses[response][category]:

    # print(response)
  return responses
 

get_datas()