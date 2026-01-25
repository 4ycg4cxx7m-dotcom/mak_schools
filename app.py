from flask import Flask, render_template, request, url_for, jsonify
import os

app = Flask(__name__)

# Исправленные маршруты (убрал .html из пути)
@app.route('/')
def dalshe():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/support_author')
def support_author():
    return render_template('support_author.html')

@app.route('/Политика_Конфиденциальности')
def Политика_Конфиденциальности():
    return render_template('Политика_Конфиденциальности.html')


@app.route('/all_schools')
def all_schools():
    return render_template('all_schools.html')

@app.route('/1sch_nskob')
def Asch_nskob():
    return render_template('Asch_nskob.html')

@app.route('/Информация_о_сайте')
def Информация_о_сайте():
    return render_template('Информация_о_сайте.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/Novosibirsk')
def Novosibirsk():
    return render_template('Asch_nskob_nsk.html')

@app.route('/sch_nskob_nsk_cent')
def sch_nskob_nsk_cent():
    return render_template('Asch_nskob_nsk_cent.html')

@app.route('/gimn1nsk')
def gimn1nsk():
    return render_template('Asch_nskob_nsk_cent_gim1.html')


@app.route('/nslic220nsk')
def nslic220nsk():
    return render_template('Asch_nskob_nsk_cent_lic22.html')

@app.route('/Asch_nskob_nsk_cent_sch29')
def Asch_nskob_nsk_cent_sch29():  # ИСПРАВЛЕНО: убрал .html
    return render_template('Asch_nskob_nsk_cent_sch29.html')

@app.route('/Asch_nskob_nsk_cent_sch54')
def Asch_nskob_nsk_cent_sch54():
    return render_template('Asch_nskob_nsk_cent_sch54.html')

@app.route('/Asch_nskob_nsk_cent_sch4')
def Asch_nskob_nsk_cent_sch4():
    return render_template('Asch_nskob_nsk_cent_sch4.html')

@app.route('/Asch_nskob_nsk_cent_sch156')
def Asch_nskob_nsk_cent_sch156():
    return render_template('Asch_nskob_nsk_cent_sch156.html')

@app.route('/Asch_nskob_nsk_cent_lic12')
def Asch_nskob_nsk_cent_lic12():
    return render_template('Asch_nskob_nsk_cent_lic12.html')


@app.route('/Asch_nskob_nsk_cent_gim13')
def Asch_nskob_nsk_cent_gim13():
    return render_template('Asch_nskob_nsk_cent_gim13.html')

@app.route('/Asch_nskob_nsk_cent_licEkl')
def Asch_nskob_nsk_cent_licEkl():
    return render_template('Asch_nskob_nsk_cent_licEkl.html')

@app.route('/sch_nskob_nsk_dzer')
def sch_nskob_nsk_dzer():
    return render_template('Asch_nskob_nsk_dzer.html')

@app.route('/sch_nskob_nsk_dzer_sch2')
def sch_nskob_nsk_dzer_sch2():
    return render_template('Asch_nskob_nsk_dzer_sch2.html')

@app.route('/sch_nskob_nsk_dzer_sch1')
def sch_nskob_nsk_dzer_sch1():
    return render_template('Asch_nskob_nsk_dzer_sch1.html')

@app.route('/domoi')
def domoi():
    return render_template('home.html')

@app.route('/sch_nskob')
def sch_nskob():
    return render_template('Asch_nskob.html')

# Списки файлов поиска (ИСПРАВЛЕНО)
# Списки файлов поиска (ИСПРАВЛЕНО)
search_all_files = [
    'dalshe.html', 'home.html', 'support_author.html', 'Политика_Конфиденциальности.html',
    'all_schools.html', 'Информация_о_сайте.html', 'support.html'
]

search_nsk_files = [
    'Asch_nskob_nsk_cent.html', 
    'Asch_nskob_nsk_cent_gim1.html', 'Asch_nskob_nsk_cent_lic22.html', 
    'Asch_nskob_nsk_cent_gim13.html','Asch_nskob_nsk_cent_licEkl.html', 'Asch_nskob_nsk_cent_lic12.html',
    'Asch_nskob_nsk_cent_sch29.html', 'Asch_nskob_nsk_cent_sch54.html',
    'Asch_nskob_nsk_cent_sch4.html', 'Asch_nskob_nsk_cent_sch156.html',  
    
]
# 'Asch_nskob_nsk_dzer_sch1.html', 'Asch_nskob_nsk_dzer_sch2.html', 
# Маппинг: filename → (публичное название, маршрут)
# Маппинг: filename → (публичное название, маршрут)
def get_search_result_info(filename):
    mapping = {
        # Общие страницы
        'home.html': ('Главная', url_for('home')),
        'support_author.html': ('Поддержка автора', url_for('support_author')),
        'Политика_Конфиденциальности.html': ('Политика конфиденциальности', url_for('Политика_Конфиденциальности')),
        'all_schools.html': ('Все школы', url_for('all_schools')),
        'Информация_о_сайте.html': ('Информация о сайте', url_for('Информация_о_сайте')),
        'support.html': ('Поддержка', url_for('support')),
        ### ШКОЛЫ НОВОСИБИРСКА
        'Asch_nskob_nsk_cent_gim1.html': ('Гимназия №1', url_for('gimn1nsk')),
        'Asch_nskob_nsk_cent_lic22.html': ('Лицей №22 «Надежда Сибири»', url_for('nslic220nsk')),
        'Asch_nskob_nsk_cent_gim13.html': ('Гимназия №13 им. Э.А. Быкова', url_for('Asch_nskob_nsk_cent_gim13')),
        'Asch_nskob_nsk_cent_licEkl.html': ('Экономический лицей', url_for('Asch_nskob_nsk_cent_licEkl')),
        'Asch_nskob_nsk_cent_lic12.html': ('Лицей №12', url_for('Asch_nskob_nsk_cent_lic12')),
        'Asch_nskob_nsk_cent_sch29.html': ('Школа №29', url_for('Asch_nskob_nsk_cent_sch29')),
        'Asch_nskob_nsk_cent_sch54.html': ('Школа №54', url_for('Asch_nskob_nsk_cent_sch54')),
        'Asch_nskob_nsk_cent_sch4.html': ('Школа №4', url_for('Asch_nskob_nsk_cent_sch4')),
        'Asch_nskob_nsk_cent_sch156.html': ('Школа №156', url_for('Asch_nskob_nsk_cent_sch156')),
        

    }
    return mapping.get(filename, (os.path.splitext(filename)[0].replace('_', ' ').title(), '#'))

# API для динамического поиска (ИСПРАВЛЕНО)
@app.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('q', '').lower().strip()
    scope = request.args.get('scope', 'all')
    
    if len(query) < 1 and not any(c.isdigit() for c in query):
        return jsonify([])
    
    if len(query) < 3 and not query.isdigit():
        return jsonify([])
    
    if scope == 'nsk':
        files_to_search = search_nsk_files
    else:
        files_to_search = search_all_files + search_nsk_files
    
    results = []
    for filename in files_to_search:
        try:
            with open(f'templates/{filename}', 'r', encoding='utf-8') as f:
                content = f.read().lower()
                if query in content:
                    title, url = get_search_result_info(filename)
                    results.append({
                        'title': title,
                        'url': url
                    })
        except FileNotFoundError:
            pass
    
    return jsonify(results[:1000000])  # максимум 10 результатов

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8800, ssl_context='adhoc', debug=True)
