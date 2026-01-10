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
search_all_files = [
    'dalshe.html', 'home.html', 'support_author.html', 'Политика_Конфиденциальности.html',
    'all_schools.html', 'Информация_о_сайте.html', 'support.html'
]

search_nsk_files = [
    'Asch_nskob.html', 'Asch_nskob_nsk.html', 'Asch_nskob_nsk_cent.html', 
    'Asch_nskob_nsk_cent_gim1.html', 'Asch_nskob_nsk_cent_lic22.html', 
    'Asch_nskob_nsk_cent_sch29.html', 'Asch_nskob_nsk_cent_sch54.html',
    'Asch_nskob_nsk_cent_sch4.html', 'Asch_nskob_nsk_cent_sch156.html', 'Asch_nskob_nsk_dzer.html', 
    'Asch_nskob_nsk_dzer_sch1.html', 'Asch_nskob_nsk_dzer_sch2.html', 'Asch_nskob_nsk_cent_sch156.html'
]

# Маппинг шаблонов → маршруты (ИСПРАВЛЕНО и дополнено)
def get_route_for_template(template_name):
    mapping = {
        'dalshe.html': url_for('dalshe'),
        'home.html': url_for('home'),
        'support_author.html': url_for('support_author'),
        'Политика_Конфиденциальности.html': url_for('Политика_Конфиденциальности'),
        'all_schools.html': url_for('all_schools'),
        'Информация_о_сайте.html': url_for('Информация_о_сайте'),
        'support.html': url_for('support'),
        'Asch_nskob_nsk.html': url_for('Novosibirsk'),
        'Asch_nskob_nsk_cent.html': url_for('sch_nskob_nsk_cent'),
        'Asch_nskob_nsk_cent_gim1.html': url_for('gimn1nsk'),
        'Asch_nskob_nsk_cent_lic22.html': url_for('Asch_nskob_nsk_cent_lic12'),
        'Asch_nskob_nsk_cent_sch29.html': url_for('Asch_nskob_nsk_cent_sch29'),
        'Asch_nskob_nsk_cent_sch54.html': url_for('Asch_nskob_nsk_cent_sch54'),
        'Asch_nskob_nsk_cent_sch4.html': url_for('Asch_nskob_nsk_cent_sch4'),
        '196_mbou_sosh_nsk.html': url_for('Asch_nskob_nsk_cent_sch156'),
        'Asch_nskob_nsk_dzer.html': url_for('sch_nskob_nsk_dzer'),
        'Asch_nskob_nsk_dzer_sch1.html': url_for('sch_nskob_nsk_dzer_sch1'),
        'Asch_nskob_nsk_dzer_sch2.html': url_for('sch_nskob_nsk_dzer_sch2'),
        'Asch_nskob.html': url_for('sch_nskob')
    }
    return mapping.get(template_name, '#')

# API для динамического поиска
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
                    results.append({
                        'title': os.path.splitext(filename)[0].replace('_', ' ').title(),
                        'url': get_route_for_template(filename)
                    })
        except FileNotFoundError:
            pass
    
    return jsonify(results[:10])  # максимум 10 результатов

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8800, ssl_context='adhoc', debug=True)
