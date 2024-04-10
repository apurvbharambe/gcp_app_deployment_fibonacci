from flask import Flask, request, render_template

app = Flask(__name__)

def fibonacci_series(n):
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        number = int(request.form.get('number', 5))  # Default to 5 if 'number' parameter is not provided
        fib_series = fibonacci_series(number)
        return render_template('fibonacci_combined.html', number=number, fib_series=fib_series)
    else:
        return render_template('fibonacci_combined.html')

if __name__ == '__main__':
    app.run(debug=True)

