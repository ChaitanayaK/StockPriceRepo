from flask import Flask, jsonify, request
import yfinance as yf

app = Flask(__name__)

@app.route('/api/stockprice', methods=['GET'])
def get_data():
    try:
        symbol = request.args.get('name', None)  
        stock_symbol = f"{symbol}.NS"  
        stock = yf.Ticker(stock_symbol)
        last_price = stock.info["regularMarketPrice"]
        return jsonify({"stock": stock_symbol, "last_price": last_price}), 200
    except:
        return ({"error": "Invalid Stock Symbol/Unable to fetch data"}), 400
