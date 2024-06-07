from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

image_list = ['Cactus.png', 'cherry.png', 'coin.png', 'lime.png', 'apple.png', 'Seven.png']

def calculate_points(images):
    points = 0
    if images.count('coin.png') == 3:
        points = 1000
    elif images.count('coin.png') == 2:
        points = 500
    elif images.count('Cactus.png') == 3:
        points = 1000
    elif images.count('Cactus.png') == 2:
        points = -500
    elif len(set(images)) == 1 and images[0] not in ['coin.png', 'Cactus.png']:
        points = 500
    elif len(set(images)) == 2 and 'coin.png' not in images and 'Cactus.png' not in images:
        points = 200

    # Дополнительные бонусы и штрафы
    if images.count('Seven.png') == 3:
        points += 2000
    if images.count('cherry.png') == 3:
        points += 300
    if images.count('lime.png') == 3:
        points += 150
    if images.count('apple.png') == 3:
        points += 100
    if images.count('Cactus.png') == 1 and images.count('coin.png') == 2:
        points -= 700

    return points

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    images = [random.choice(image_list) for _ in range(3)]
    points = calculate_points(images)
    return jsonify(images=images, points=points)

if __name__ == '__main__':
    app.run(debug=True)