from flask import Flask, request, render_template
from web3 import Web3

app = Flask(__name__)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ae825c6d81834439aa98bb6ed7d29147"))

@app.route('/')
def home():
    return render_template('index.html')  #This loads your form

@app.route('/check', methods=['POST'])
def check_balance():
    address = request.form['ethAddress']
    print("Address received:", address)

    if not web3.is_address(address):
        return render_template('index.html', balance=None, error=f"Invalid Ethereum address: {address}")


    try:
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.from_wei(balance_wei, 'ether')
        return f"<h3>Balance for {address}: {balance_eth} ETH</h3>"
    except Exception as e:
        return f"<h3>Error fetching balance: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
